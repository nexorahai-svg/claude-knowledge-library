#!/usr/bin/env python3
"""Resource guard: measure the machine before heavy work, wait when it is busy, cap what a heavy job may take.

Why: on 2026-10-24 the main Linux machine (24 cores, 30 GB RAM, RTX 4060 8 GB) froze hard and had to be restarted
while Claude sessions, Chrome and other apps were running; work was left half done. No early OOM daemon was active.
The rule (projects/user-profile.md, domains/claude-code/resource-safety.md): measure, then go / reduce / wait — never
refuse ordinary work out of fear, never start heavy work into a red machine.

Usage:
  python3 scripts/resource_guard.py check [--json] [--need-ram 4] [--need-vram 3]   # exit 0 green, 1 yellow, 2 red
  python3 scripts/resource_guard.py wait  [--max 1200] [--need-ram 4] [--need-vram 3] # blocks until not red (exit 0) or timeout (3)
  python3 scripts/resource_guard.py run   [--mem 8G] [--cpu 50] [--max 1200] -- <command …>
      waits until not red, then runs the command capped (systemd-run --user --scope MemoryMax/MemorySwapMax/
      CPUQuota when available, else nice + ionice), so one job can never take the whole machine. MemorySwapMax matters:
      without it a capped job spills into the 22 GB swap and thrashes the disk (tested 2026-10-24: capped job killed
      alone with exit 137, the desktop untouched).
Standard library only; Linux reads /proc and /sys; other systems report "unknown" and never block.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time

# Thresholds. RED = wait; YELLOW = one heavy job at a time, at most 2 subagents, lower parallel flags.
RED = {"mem_avail_pct": 12, "mem_avail_gb": 3.0, "swap_used_pct": 80, "psi_mem_full10": 10, "psi_mem_some10": 30,
       "disk_free_gb": 3.0, "gpu_temp_c": 87, "cpu_temp_c": 95}
# Owner's decision 2026-10-30: swap red line 80%; up to 90% only in an emergency the owner named, with KL_SWAP_EMERGENCY=1.
if os.environ.get("KL_SWAP_EMERGENCY") == "1":
    RED["swap_used_pct"] = 90
YELLOW = {"mem_avail_pct": 25, "swap_used_pct": 25, "psi_mem_some10": 5, "load_per_core": 0.85, "psi_cpu_some10": 50,
          "disk_free_gb": 10.0, "gpu_temp_c": 80, "cpu_temp_c": 85, "vram_used_pct": 85}


def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError:
        return ""


def _meminfo():
    out = {}
    for line in _read("/proc/meminfo").splitlines():
        k, _, v = line.partition(":")
        if v.strip():
            out[k] = int(v.split()[0]) / 1048576   # kB -> GB
    return out


def _psi(kind):
    """{'some': avg10, 'full': avg10} from /proc/pressure/<kind>, or {} when PSI is off."""
    out = {}
    for line in _read(f"/proc/pressure/{kind}").splitlines():
        parts = line.split()
        if parts and parts[0] in ("some", "full"):
            out[parts[0]] = float(dict(p.split("=") for p in parts[1:])["avg10"])
    return out


def _gpu():
    if not shutil.which("nvidia-smi"):
        return None
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=memory.used,memory.total,utilization.gpu,temperature.gpu",
                            "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=3)
        used, total, util, temp = [float(x) for x in r.stdout.strip().splitlines()[0].split(",")]
        return {"vram_used_gb": round(used / 1024, 1), "vram_total_gb": round(total / 1024, 1),
                "vram_free_gb": round((total - used) / 1024, 1), "util_pct": util, "temp_c": temp}
    except (OSError, ValueError, IndexError, subprocess.TimeoutExpired):
        return None


def _cpu_temp():
    best = None
    base = "/sys/class/hwmon"
    for h in (os.listdir(base) if os.path.isdir(base) else []):
        name = _read(os.path.join(base, h, "name")).strip()
        if name not in ("k10temp", "coretemp", "zenpower"):
            continue
        for f in os.listdir(os.path.join(base, h)):
            if f.startswith("temp") and f.endswith("_input"):
                try:
                    t = int(_read(os.path.join(base, h, f))) / 1000
                    best = t if best is None else max(best, t)
                except ValueError:
                    pass
    return best


def measure():
    if not sys.platform.startswith("linux"):
        return {"platform": sys.platform}
    m = _meminfo()
    total, avail = m.get("MemTotal", 0), m.get("MemAvailable", 0)
    swap_t, swap_f = m.get("SwapTotal", 0), m.get("SwapFree", 0)
    home = shutil.disk_usage(os.path.expanduser("~"))   # /tmp is often RAM (tmpfs): RAM is measured above
    load1 = os.getloadavg()[0]
    return {
        "platform": "linux", "cores": os.cpu_count(),
        "mem_total_gb": round(total, 1), "mem_avail_gb": round(avail, 1),
        "mem_avail_pct": round(100 * avail / total, 1) if total else None,
        "swap_used_pct": round(100 * (swap_t - swap_f) / swap_t, 1) if swap_t else 0.0,
        "psi_mem": _psi("memory"), "psi_cpu": _psi("cpu"), "psi_io": _psi("io"),
        "load1": round(load1, 1), "load_per_core": round(load1 / (os.cpu_count() or 1), 2),
        "disk_free_gb": round(home.free / 1e9, 1),
        "cpu_temp_c": _cpu_temp(), "gpu": _gpu(),
    }


def classify(s, need_ram=0.0, need_vram=0.0):
    """-> (level, reasons). level: green / yellow / red / unknown."""
    if s.get("platform") != "linux":
        return "unknown", ["not Linux: no measurement, do not block"]
    red, yellow = [], []
    if s["mem_avail_pct"] is not None and (s["mem_avail_pct"] < RED["mem_avail_pct"] or s["mem_avail_gb"] < RED["mem_avail_gb"]):
        red.append(f"free RAM {s['mem_avail_gb']} GB ({s['mem_avail_pct']}%)")
    elif s["mem_avail_pct"] is not None and s["mem_avail_pct"] < YELLOW["mem_avail_pct"]:
        yellow.append(f"free RAM {s['mem_avail_pct']}%")
    if need_ram and s["mem_avail_gb"] - need_ram < RED["mem_avail_gb"]:
        red.append(f"job needs {need_ram} GB RAM, {s['mem_avail_gb']} GB free")
    # Dead swap of finished programs stays until swapoff: it blocks nothing while RAM is free and memory pressure is low
    # (owner, 2026-10-31: do not be over-strict).
    if s["swap_used_pct"] > RED["swap_used_pct"] and ((s.get("mem_avail_pct") or 0) < YELLOW["mem_avail_pct"] or ((s.get("psi_mem") or {}).get("some") or 0) >= YELLOW["psi_mem_some10"]):
        red.append(f"swap {s['swap_used_pct']}% used")
    elif s["swap_used_pct"] > YELLOW["swap_used_pct"]:
        yellow.append(f"swap {s['swap_used_pct']}% used")
    pm = s["psi_mem"]
    if pm.get("full", 0) > RED["psi_mem_full10"] or pm.get("some", 0) > RED["psi_mem_some10"]:
        red.append(f"memory pressure some={pm.get('some')} full={pm.get('full')} (thrashing)")
    elif pm.get("some", 0) > YELLOW["psi_mem_some10"]:
        yellow.append(f"memory pressure some={pm.get('some')}")
    if s["load_per_core"] > YELLOW["load_per_core"] or s["psi_cpu"].get("some", 0) > YELLOW["psi_cpu_some10"]:
        yellow.append(f"CPU busy (load {s['load1']} on {s['cores']} cores, pressure {s['psi_cpu'].get('some')})")
    if s["disk_free_gb"] < RED["disk_free_gb"]:
        red.append(f"disk almost full ({s['disk_free_gb']} GB free)")
    elif s["disk_free_gb"] < YELLOW["disk_free_gb"]:
        yellow.append(f"disk low ({s['disk_free_gb']} GB free)")
    t = s.get("cpu_temp_c")
    if t and t > RED["cpu_temp_c"]:
        red.append(f"CPU {t}°C")
    elif t and t > YELLOW["cpu_temp_c"]:
        yellow.append(f"CPU {t}°C")
    g = s.get("gpu")
    if g:
        if g["temp_c"] > RED["gpu_temp_c"]:
            red.append(f"GPU {g['temp_c']}°C")
        elif g["temp_c"] > YELLOW["gpu_temp_c"]:
            yellow.append(f"GPU {g['temp_c']}°C")
        if need_vram and g["vram_free_gb"] < need_vram:
            red.append(f"job needs {need_vram} GB VRAM, {g['vram_free_gb']} GB free")
        elif 100 * g["vram_used_gb"] / max(g["vram_total_gb"], 0.1) > YELLOW["vram_used_pct"]:
            yellow.append(f"VRAM {g['vram_used_gb']}/{g['vram_total_gb']} GB")
    if red:
        return "red", red + yellow
    return ("yellow", yellow) if yellow else ("green", [])


ADVICE = {
    "green": "GO: normal work; heavy jobs one or two at a time.",
    "yellow": "REDUCE: one heavy job at a time, at most 2 subagents, lower parallel flags (-j, workers, threads); "
              "light work (reading, editing, small commands) is fine.",
    "red": "WAIT: do not start heavy work now. Run `resource_guard.py wait`; meanwhile only light work. Never kill the "
           "user's programs; tell the user what is using the machine if the wait is long.",
    "unknown": "GO: no measurement on this system.",
}


def report(level, reasons, s):
    head = {"green": "🟢", "yellow": "🟡", "red": "🔴", "unknown": "⚪"}[level]
    g = s.get("gpu") or {}
    line = (f"{head} {level.upper()} — RAM free {s.get('mem_avail_gb')} GB ({s.get('mem_avail_pct')}%), swap "
            f"{s.get('swap_used_pct')}%, load {s.get('load1')}/{s.get('cores')}, disk {s.get('disk_free_gb')} GB"
            + (f", GPU {g.get('vram_used_gb')}/{g.get('vram_total_gb')} GB {g.get('temp_c')}°C" if g else ""))
    return line + ("\n  " + "; ".join(reasons) if reasons else "") + "\n  " + ADVICE[level]


def wait(max_s, need_ram, need_vram, quiet=False):
    start, last = time.time(), 0
    while True:
        s = measure()
        level, reasons = classify(s, need_ram, need_vram)
        if level != "red":
            if not quiet:
                print(report(level, reasons, s), flush=True)
            return 0
        if time.time() - start > max_s:
            print(report(level, reasons, s) + f"\n  still red after {int(max_s)} s: ask the user before going on.", flush=True)
            return 3
        if time.time() - last > 60:
            print(f"waiting for resources ({int(time.time() - start)} s): " + "; ".join(reasons), flush=True)
            last = time.time()
        time.sleep(15)


def run(args):
    code = wait(args.max, args.need_ram, args.need_vram, quiet=True)
    if code:
        return code
    cmd = args.cmd
    if not cmd:
        sys.exit("run: give a command after --")
    wrap = []
    if shutil.which("systemd-run") and sys.platform.startswith("linux"):
        mem = args.mem
        # --wait --pipe (library S107): prints "Memory peak" and "Finished with result: oom-kill" as evidence
        # systemd-run starts the unit with a clean environment: forward the caller's whole environment, or the job loses
        # variables such as DATABASE_PATH or TEST_SOURCE_DB (found 2026-10-29: 105 false test failures under the guard)
        envs = []
        for k, v in os.environ.items():
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", k) and "\n" not in v and "\0" not in v:
                envs += ["-E", f"{k}={v}"]
        wrap = ["systemd-run", "--user", "--wait", "--pipe", "--same-dir", "--quiet"] + envs + [
                "-p", f"MemoryMax={mem}",
                "-p", f"MemorySwapMax={_scale(mem, 0.25)}",   # no MemoryHigh: with a swap cap it stalled a job for minutes
                "-p", f"CPUQuota={args.cpu * (os.cpu_count() or 1)}%",
                "-p", "IOWeight=50", "--"]
    nice = (["nice", "-n", "10"] if shutil.which("nice") else []) + (["ionice", "-c", "2", "-n", "7"] if shutil.which("ionice") else [])
    r = subprocess.run(wrap + nice + cmd)
    if r.returncode != 0 and wrap:
        # a scope that cannot be created (no user systemd) must not block the job: run with nice/ionice only
        probe = subprocess.run(["systemd-run", "--user", "--wait", "--quiet", "true"], capture_output=True)
        if probe.returncode != 0:
            return subprocess.run(nice + cmd).returncode
    return r.returncode


def _scale(mem, f):
    units = {"K": 1, "M": 1024, "G": 1048576}
    n, u = (mem[:-1], mem[-1].upper()) if mem[-1].upper() in units else (mem, "M")
    return f"{int(float(n) * units[u] * f)}K"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["check", "wait", "run"], nargs="?", default="check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--need-ram", type=float, default=0.0, help="GB the job will need")
    ap.add_argument("--need-vram", type=float, default=0.0, help="GB of GPU memory the job will need")
    ap.add_argument("--max", type=float, default=1200, help="longest wait in seconds (default 20 min)")
    ap.add_argument("--mem", default="8G", help="run: memory cap for the job (default 8G)")
    ap.add_argument("--cpu", type=int, default=60, help="run: CPU cap in percent of all cores (default 60)")
    argv = sys.argv[1:]
    cmd = argv[argv.index("--") + 1:] if "--" in argv else []
    a = ap.parse_args(argv[:argv.index("--")] if "--" in argv else argv)
    a.cmd = cmd
    if a.action == "wait":
        sys.exit(wait(a.max, a.need_ram, a.need_vram))
    if a.action == "run":
        sys.exit(run(a))
    s = measure()
    level, reasons = classify(s, a.need_ram, a.need_vram)
    print(json.dumps({"level": level, "reasons": reasons, "advice": ADVICE[level], **s}, ensure_ascii=False)
          if a.json else report(level, reasons, s))
    sys.exit({"green": 0, "unknown": 0, "yellow": 1, "red": 2}[level])


if __name__ == "__main__":
    main()
