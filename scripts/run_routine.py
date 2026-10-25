#!/usr/bin/env python3
"""Run the library's automatic routines without the Claude desktop app, and watch over them.

The desktop app's scheduled tasks only run while the app is open, and on 2026-10-21 they silently dropped out of
its list (the daily watch stopped after 10-20; the two-day sweep never ran). This runner is driven by systemd
user timers instead: they run whenever the user is logged in, and `Persistent=true` catches up a run missed while
the computer was off. The prompts live in research/routines/*.md (also usable by a claude.ai cloud routine).

Usage:
  python3 scripts/run_routine.py install          # write and start the systemd user timers (daily 10:00, Monday 11:00)
  python3 scripts/run_routine.py uninstall
  python3 scripts/run_routine.py status           # last runs, next runs, failures, inbox, due cards
  python3 scripts/run_routine.py run daily|weekly [--force]

A run is skipped when its heartbeat commit ("Daily watch <date>:" today, or "Weekly sweep" in the last 6 days)
is already on GitHub, so a cloud routine and this timer can both be on without doing the work twice.
On failure (non-zero exit, timeout, or no heartbeat commit) it sends a desktop notification.
"""
import datetime as dt
import fcntl
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_DIR = os.path.expanduser("~/.local/state/knowledge-library")
STATUS = os.path.join(STATE_DIR, "routines.json")
UNIT_DIR = os.path.expanduser("~/.config/systemd/user")
ROUTINES = {
    "daily": {"prompt": "research/routines/daily-watch.md", "grep": "^Daily watch {date}", "minutes": 45,
              "calendar": "*-*-* 10:00:00", "desc": "Knowledge library daily watch"},
    "weekly": {"prompt": "research/routines/weekly-sweep.md", "grep": "^Weekly sweep|^Two-day deep sweep [0-9]", "minutes": 120,
               "calendar": "Mon *-*-* 11:00:00", "desc": "Knowledge library weekly deep sweep"},
}
# Files an unattended run must never change: sessions may run setup_machine.py without asking (user's allow rule).
PROTECTED = ("scripts/setup_machine.py", "scripts/run_routine.py", "plugins/knowledge-library/",
             "domains/claude-code/toolkit.json", ".claude-plugin/marketplace.json", "research/routines/",
             "projects/user-profile.md", "scripts/resource_guard.py", "scripts/build_public.py")
# Layer 2: a git pre-commit hook (written into .git/hooks, which git never syncs) refuses commits that touch PROTECTED
# while KL_ROUTINE=1, the variable this runner sets for the unattended Claude run.
PRE_COMMIT = """#!/bin/sh
# Written by scripts/run_routine.py: unattended library routines may not change setup code (user's allow rule).
[ "$KL_ROUTINE" = "1" ] || exit 0
bad=$(git diff --cached --name-only | grep -E '^(%s)')
if [ -n "$bad" ]; then
  echo "BLOCKED: an automatic routine may not change these protected files:" >&2
  echo "$bad" >&2
  echo "Unstage them (git restore --staged <file> && git checkout -- <file>) and propose the change in research/inbox instead." >&2
  exit 1
fi
""" % "|".join(p.replace(".", "\\.") for p in PROTECTED)


def install_pre_commit():
    path = os.path.join(ROOT, ".git", "hooks", "pre-commit")
    if not os.path.exists(path) or open(path).read() != PRE_COMMIT:
        if os.path.exists(path) and "run_routine.py" not in open(path).read():
            os.replace(path, path + ".before-kl")   # keep any hook the user had
        with open(path, "w") as f:
            f.write(PRE_COMMIT)
        os.chmod(path, 0o755)
TOOLS = "Bash Read Write Edit Glob Grep WebFetch WebSearch Agent TodoWrite Artifact"


def git(*args, check=False):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, check=check).stdout.strip()


def load_status():
    try:
        return json.load(open(STATUS))
    except (OSError, ValueError):
        return {}


def save_status(st):
    os.makedirs(STATE_DIR, exist_ok=True)
    json.dump(st, open(STATUS, "w"), indent=1)


def notify(title, body):
    if shutil.which("notify-send"):
        subprocess.run(["notify-send", "-u", "critical", "-a", "Knowledge library", title, body])


def heartbeat(name, today):
    """The routine's own commit, on GitHub or local main."""
    r = ROUTINES[name]
    if name == "daily":
        out = git("log", "origin/main", "main", "-1", "--format=%cI", "-E", f"--grep={r['grep'].format(date=today)}")
        return bool(out)
    out = git("log", "origin/main", "main", "-1", "--format=%cI", "-E", f"--grep={r['grep']}")
    return bool(out) and dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(out) < dt.timedelta(days=6)


def run(name, force=False):
    r = ROUTINES[name]
    os.makedirs(STATE_DIR, exist_ok=True)
    lock = open(os.path.join(STATE_DIR, f"{name}.lock"), "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print(f"{name}: already running")
        return 0
    today = dt.date.today().isoformat()
    git("fetch", "-q", "origin")
    if not force and heartbeat(name, today):
        print(f"{name}: already done ({today}), skipped")
        return 0
    if not git("status", "--porcelain"):
        git("merge", "-q", "--ff-only", "origin/main")
    claude = shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")
    prompt = (f"Today is {today} ({dt.datetime.now().astimezone().tzname()}). Read {r['prompt']} in this repository and "
              "follow it exactly. You run unattended: there is no user to ask; decide by the rules in that file.")
    install_pre_commit()
    before = git("rev-parse", "origin/main")
    log = os.path.join(STATE_DIR, f"{name}-{today}.log")
    st = load_status()
    st[name] = {"started": dt.datetime.now().isoformat(timespec="seconds"), "log": log, "result": "running"}
    save_status(st)
    try:
        with open(log, "w") as f:
            code = subprocess.run([claude, "-p", prompt, "--model", "sonnet", "--permission-mode", "acceptEdits",
                                   "--allowedTools", TOOLS], cwd=ROOT, stdout=f, stderr=subprocess.STDOUT,
                                  env={**os.environ, "KL_ROUTINE": "1"},
                                  stdin=subprocess.DEVNULL, timeout=r["minutes"] * 60).returncode
    except subprocess.TimeoutExpired:
        code = "timeout"
    git("fetch", "-q", "origin")
    touched = [f for f in git("diff", "--name-only", f"{before}..origin/main").splitlines() if f.startswith(PROTECTED)]
    if touched:
        notify("Library routine changed protected files",
               f"{name} run touched {', '.join(touched)}. Review before any session runs setup_machine.py.")
    ok = code == 0 and heartbeat(name, today) and not touched
    st = load_status()
    st[name].update({"ended": dt.datetime.now().isoformat(timespec="seconds"), "exit": code,
                     "result": "ok" if ok else "failed"})
    save_status(st)
    if not ok:
        why = "timed out" if code == "timeout" else (f"exit {code}" if code else "no heartbeat commit on GitHub")
        notify(f"Library {name} run failed", f"{why}. Log: {log}")
    if ok:   # refresh the public read-only copy; build_public.py refuses to publish if its leak check finds anything
        pub = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_public.py"), "--push"],
                             capture_output=True, text=True, timeout=600)
        with open(log, "a") as f:
            f.write("\n--- public copy ---\n" + pub.stdout[-2000:] + pub.stderr[-1000:])
        if pub.returncode:
            notify("Library public copy not published", "Leak check or push failed; see " + log)
    print(f"{name}: {'ok' if ok else 'FAILED'} ({code})")
    return 0 if ok else 1


def install():
    os.makedirs(UNIT_DIR, exist_ok=True)
    py = sys.executable
    path = os.environ.get("PATH", "") + ":" + os.path.expanduser("~/.local/bin")
    for name, r in ROUTINES.items():
        open(os.path.join(UNIT_DIR, f"kl-{name}.service"), "w").write(
            f"[Unit]\nDescription={r['desc']}\nWants=network-online.target\nAfter=network-online.target\n\n"
            f"[Service]\nType=oneshot\nEnvironment=PATH={path}\nWorkingDirectory={ROOT}\n"
            f"ExecStart={py} {os.path.join(ROOT, 'scripts', 'run_routine.py')} run {name}\n"
            f"TimeoutStartSec={r['minutes'] + 10}min\nNice=10\nMemoryMax=4G\n")
        open(os.path.join(UNIT_DIR, f"kl-{name}.timer"), "w").write(
            f"[Unit]\nDescription={r['desc']} (timer)\n\n[Timer]\nOnCalendar={r['calendar']}\nPersistent=true\n"
            "RandomizedDelaySec=5min\n\n[Install]\nWantedBy=timers.target\n")
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    for name in ROUTINES:
        subprocess.run(["systemctl", "--user", "enable", "--now", f"kl-{name}.timer"], check=True)
    status()


def uninstall():
    for name in ROUTINES:
        subprocess.run(["systemctl", "--user", "disable", "--now", f"kl-{name}.timer"])
        for ext in ("service", "timer"):
            p = os.path.join(UNIT_DIR, f"kl-{name}.{ext}")
            if os.path.exists(p):
                os.remove(p)
    subprocess.run(["systemctl", "--user", "daemon-reload"])


def status():
    st = load_status()
    today = dt.date.today().isoformat()
    git("fetch", "-q", "origin")
    for name, r in ROUTINES.items():
        s = st.get(name, {})
        last = git("log", "origin/main", "main", "-1", "--format=%cs %s", "-E", f"--grep={r['grep'].format(date='')}")
        nxt = subprocess.run(["systemctl", "--user", "show", f"kl-{name}.timer", "-p", "NextElapseUSecRealtime",
                              "--value"], capture_output=True, text=True).stdout.strip() or "timer not installed"
        print(f"{name}: last heartbeat: {last or 'never'} | last local run: {s.get('started', '-')} "
              f"{s.get('result', '')} (exit {s.get('exit', '-')}) | next: {nxt} | done today/this week: "
              f"{heartbeat(name, today)}")
        if s.get("result") == "failed":
            print(f"  log: {s.get('log')}")
    try:
        inbox = open(os.path.join(ROOT, "research/inbox/README.md"), encoding="utf-8").read()
        print("unreviewed inbox files:", sum(1 for l in inbox.splitlines() if l.rstrip().endswith("❌ |")))
        cards = json.load(open(os.path.join(ROOT, "catalog/index.json"), encoding="utf-8"))["cards"]
        print("cards past next_check:", sum(1 for c in cards if c.get("verdict") != "hold" and str(c.get("next_check", "9999")) < today))
    except (OSError, ValueError, KeyError):
        pass


def main():
    a = sys.argv[1:]
    if not a or a[0] == "status":
        status()
    elif a[0] == "install":
        install()
    elif a[0] == "uninstall":
        uninstall()
    elif a[0] == "run" and len(a) > 1 and a[1] in ROUTINES:
        sys.exit(run(a[1], force="--force" in a))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
