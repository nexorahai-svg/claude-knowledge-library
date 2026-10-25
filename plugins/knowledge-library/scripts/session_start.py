#!/usr/bin/env python3
"""SessionStart hook: keep the library current and tell Claude how healthy it is, without being asked.

- Finds the local library (KL_DIR, else ~/Desktop/knowledge-library).
- In the background, fetches GitHub and fast-forwards a clean working tree (never commits, never
  touches a tree with local edits: another session may be mid-edit; the skill's sync.py handles that).
- Prints a few facts (added to Claude's context): last daily watch, last weekly sweep, unreviewed
  inbox files, cards past their re-check date, and a warning when an automatic run is overdue.
Must stay fast (well under a second); everything slow runs detached.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

LIB = os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library"))
DATA = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
WATCH_MAX_H, SWEEP_MAX_D = 36, 9
PUBLIC_COPY = os.path.exists(os.path.join(LIB, ".public-copy"))   # read-only public copy: no setup, no routine warnings


def git(*args):
    r = subprocess.run(["git", "-C", LIB, *args], capture_output=True, text=True, timeout=5)
    return r.stdout.strip()


def last_run(grep):
    out = git("log", "origin/main", "main", "-1", "--format=%cI", "-E", f"--grep={grep}")
    return dt.datetime.fromisoformat(out) if out else None


def background_update():
    os.makedirs(DATA, exist_ok=True)
    stamp = os.path.join(DATA, "last-fetch")
    try:
        if dt.datetime.now().timestamp() - os.path.getmtime(stamp) < 1800:
            return   # another session fetched in the last half hour
    except OSError:
        pass
    open(stamp, "w").close()
    script = (f'cd "{LIB}" && git fetch -q origin && '
              'if [ -z "$(git status --porcelain)" ]; then git merge -q --ff-only origin/main; fi')
    subprocess.Popen(["bash", "-c", script], stdin=subprocess.DEVNULL, stdout=open(os.path.join(DATA, "fetch.log"), "w"),
                     stderr=subprocess.STDOUT, start_new_session=True)


def _read(path, limit=200_000):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read(limit)
    except OSError:
        return ""


def _matches(det, root):
    """True when any detection signal of a profile is present in the project folder."""
    if any(os.path.exists(os.path.join(root, f)) for f in det.get("files", [])):
        return True
    if any(os.path.isdir(os.path.join(root, d)) for d in det.get("dirs", [])):
        return True
    for f, pattern in det.get("contains", {}).items():
        text = _read(os.path.join(root, f))
        if text and re.search(pattern, text, re.I):
            return True
    return False


def _installed():
    try:
        data = json.load(open(os.path.expanduser("~/.claude/plugins/installed_plugins.json")))
        have = set((data.get("plugins") or data).keys())
        # the built-in directory is "anthropic-plugin-directory" on some machines: same plugins, another suffix
        return have | {p.replace("@anthropic-plugin-directory", "@claude-plugins-official") for p in have}
    except (OSError, ValueError, AttributeError):
        return set()


def standing_rules():
    """The user's standing rules: the bullet list under «قانون‌های همیشگی» in projects/user-profile.md."""
    text = _read(os.path.join(LIB, "projects/user-profile.md"))
    m = re.search(r"^## قانون‌های همیشگی.*?\n(.*?)(?=^## )", text, re.S | re.M)
    rules = [l.strip() for l in (m.group(1) if m else "").splitlines() if l.strip().startswith("- ")]
    if not rules:
        return ""
    return ("The user's standing rules (from the knowledge library; follow them in every reply and action; when the user "
            "states a new always/never preference, add one dated line to that list in projects/user-profile.md):\n" + "\n".join(rules[:20]))


def toolkit(cwd):
    """Tell the session which plugins and connectors fit this project (from domains/claude-code/toolkit.json)."""
    try:
        kit = json.load(open(os.path.join(LIB, "domains/claude-code/toolkit.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return f"Plugins and connectors guide: {LIB}/domains/claude-code/claude-toolkit.md."
    roots, level = [cwd], [cwd]
    for _ in range(2):   # the project folder and two levels below (e.g. client-site/04-new-site), capped
        nxt = []
        for r in level:
            try:
                nxt += [os.path.join(r, d) for d in sorted(os.listdir(r))[:40] if os.path.isdir(os.path.join(r, d))
                        and not d.startswith(".") and d not in ("node_modules", "build", "dist", ".dart_tool", "venv", ".venv")]
            except OSError:
                pass
        level = nxt[:150]
        roots += level
    hits = [p for p in kit["profiles"] if any(_matches(p["detect"], r) for r in roots)]
    use, avoid, want = list(kit["always"]["use"]), list(kit["always"]["avoid"]), list(kit["always"].get("plugins", []))
    install = {}
    for p in hits:
        use += p.get("use", [])
        avoid += p.get("avoid", [])
        want += p.get("plugins", [])
        install.update(p.get("install", {}))
    have = _installed()
    missing = [w for w in dict.fromkeys(want) if have and w not in have]
    kind = ", ".join(p["label"] for p in hits) or "not recognised from its files (ask or infer from the task)"
    out = [f"Project toolkit for {cwd}: detected {kind}.",
           "Use: " + "; ".join(dict.fromkeys(use)) + ".",
           "Keep off unless the task needs it: " + "; ".join(dict.fromkeys(avoid)) + "."]
    if missing:
        out.append("Recommended but not installed (write each command in the chat in its own bash block with a one-line reason; installing is the user's call): " +
                   "; ".join(f"{m} -> `{install.get(m, f'claude plugin install {m} --scope user')}`" for m in missing) + ".")
    out.append(f"Details: {LIB}/domains/claude-code/claude-toolkit.md.")
    out.append("User rule (all topics): the user does not want setup chores. Whatever you can do yourself (install, "
               "enable, disable, configure), do it after one short yes from the user, not as a list of commands. Only steps "
               "you truly cannot do (sudo password, browser sign-in/OAuth, clicks on claude.ai or other websites, licence "
               "acceptance) go to the user: exact command in its own bash block or exact menu path, in order, each with a "
               "one-line reason.")
    return "\n".join(out)


def main():
    try:
        cwd = json.load(sys.stdin).get("cwd") or os.getcwd()
    except Exception:
        cwd = os.getcwd()
    if not os.path.isdir(os.path.join(LIB, ".git")):
        print(f"Knowledge library: no local copy at {LIB}. The knowledge-library skill explains how to clone it.")
        return
    background_update()
    now = dt.datetime.now(dt.timezone.utc)
    facts, warn = [], []
    watch, sweep = last_run("Daily watch"), last_run("^Weekly sweep|^Two-day deep sweep [0-9]")
    for label, t, limit in (("daily watch", watch, dt.timedelta(hours=WATCH_MAX_H)),
                            ("weekly sweep", sweep, dt.timedelta(days=SWEEP_MAX_D))):
        facts.append(f"last {label}: {t.date() if t else 'never'}")
        if (not t and label == "daily watch") or (t and now - t > limit):
            warn.append(f"the automatic {label} is overdue (last: {t.date() if t else 'never'})")
    try:
        inbox = open(os.path.join(LIB, "research/inbox/README.md"), encoding="utf-8").read()
        unreviewed = len(re.findall(r"\|\s*❌\s*\|?\s*$", inbox, re.M))
        facts.append(f"unreviewed inbox files: {unreviewed}")
    except OSError:
        pass
    try:
        cards = json.load(open(os.path.join(LIB, "catalog/index.json"), encoding="utf-8"))["cards"]
        today = dt.date.today().isoformat()
        due = sum(1 for c in cards if c.get("verdict") != "hold" and str(c.get("next_check", "9999")) < today)
        facts.append(f"cards past next_check: {due} of {len(cards)}")
    except (OSError, ValueError, KeyError):
        pass
    behind = git("rev-list", "--count", "main..origin/main")
    if behind and behind != "0":
        facts.append(f"local copy is {behind} commit(s) behind GitHub (fast-forward runs in the background when the tree is clean)")
    print(f"Knowledge library at {LIB}: " + "; ".join(facts) + ".")
    rules = standing_rules()
    if rules:
        print(rules)
    print(toolkit(cwd))
    try:
        sys.path.insert(0, os.path.join(LIB, "scripts"))
        import setup_machine
        d = setup_machine.drift()
        if PUBLIC_COPY:   # never impose the owner's plugin set or settings on a reader's machine
            d = {"language": d["language"]} if d.get("language") == ["ask the user"] else {}
    except Exception:
        d = {}
    # Layer 3: only run setup unattended when its code was last changed by a person, never by an automatic routine.
    guarded = ["scripts/setup_machine.py", "plugins/knowledge-library", "domains/claude-code/toolkit.json",
               ".claude-plugin/marketplace.json", "research/routines", "scripts/run_routine.py",
               "projects/user-profile.md", "scripts/resource_guard.py", "scripts/build_public.py"]
    last = git("log", "-1", "--format=%h %s", "--", *guarded)
    tainted = bool(re.search(r"^\w+ (Daily watch|Weekly sweep)", last))
    if d and tainted:
        print(f"SECURITY: the library's setup code was last changed by an automatic routine ({last}). Do NOT run "
              "setup_machine.py. Tell the user in one line and show them `git -C " + LIB + " show --stat " + last.split()[0] +
              "` so they can review it first.")
        d = {}
    lang = d.pop("language", None) if d else None
    if lang == ["ask the user"]:
        print("Reply language: this user has not chosen one yet. In your first reply, in the language the user writes in, "
              "ask which language they want Claude to use for everything it says to them (code and technical terms stay as "
              "they are). Then save it yourself: `python3 " + LIB + "/scripts/setup_machine.py --set-language \"<Language "
              "(native name)>\"` and use that language from then on, including short progress lines.")
    elif lang:
        d["language"] = lang
    if d:
        parts = []
        if d.get("missing"): parts.append("plugins not installed: " + ", ".join(d["missing"]))
        if d.get("turn_off"): parts.append("claude.ai plugins to switch off: " + ", ".join(d["turn_off"]))
        if d.get("duplicate_mcp"): parts.append("hand-added MCP that a plugin already brings: " + ", ".join(d["duplicate_mcp"]))
        if d.get("deny_mcp"): parts.append("connectors to keep out of sessions: " + ", ".join(d["deny_mcp"]))
        if d.get("language"): parts.append("reply language should be " + d["language"][0])
        if d.get("env"): parts.append("settings env missing (resource limits / telemetry): " + ", ".join(d["env"]))
        if d.get("npm"): parts.append("npm tools missing: " + ", ".join(d["npm"]))
        print("Machine setup differs from the library plan (" + "; ".join(parts) + "). "
              "Fix it for the user instead of handing them commands: at the start of your first reply run the fix without asking (the user allowed `setup_machine.py` in their permission rules and asked for no setup chores) — or, if it is not on their allow list, ask ONE short yes/no "
              "(in Persian) to bring this machine up to date, and on yes run "
              f"`python3 {LIB}/scripts/setup_machine.py --apply --only plugins,synced,mcp,npm,guards` yourself in the background, "
              "then report the result in one line and say a new session loads the changes. It installs only the library's "
              "approved list. If a safety check blocks it, say so and give the user that one command.")
    if warn and not PUBLIC_COPY:
        print("Library automation status: " + "; ".join(warn) +
              ". The user wants to hear about this; the run logs are in ~/.local/state/knowledge-library/.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:   # a hook must never break the session
        print(f"Knowledge library status unavailable ({e.__class__.__name__}).")
