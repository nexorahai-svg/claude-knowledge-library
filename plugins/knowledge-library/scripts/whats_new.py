#!/usr/bin/env python3
"""UserPromptSubmit hook: tell an open session what the library learned since it last looked (2026-10-28).

Sessions stay open for days; before this, a new card, rule or method filed in the library reached them only after a
restart, so they kept working without it. On each user message this compares the library's commit with the one this
session last saw; when new changelog rows (changes/*.txt) arrived, it adds them once to Claude's context, with a
pointer to the changed cards' use_when/how. First message of a session: the last 7 days, capped. Must stay fast.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

LIB = os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library"))
DATA = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
LIMIT = 10


def git(*args):
    return subprocess.run(["git", "-C", LIB, *args], capture_output=True, text=True, timeout=3).stdout.strip()


def row(path):
    """The changelog row as one short line: date and change text."""
    try:
        cells = [c.strip() for c in open(os.path.join(LIB, path), encoding="utf-8").readline().strip().strip("|").split("|")]
    except OSError:
        return ""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", " — ".join(c for c in cells[:2] if c))
    return text[:260]


def main():
    data = json.load(sys.stdin)
    sid = re.sub(r"[^\w-]", "", str(data.get("session_id") or ""))[:80]
    if not sid or not os.path.isdir(os.path.join(LIB, ".git")):
        return
    head = git("rev-parse", "HEAD")
    seen_dir = os.path.join(DATA, "seen")
    os.makedirs(seen_dir, exist_ok=True)
    mark = os.path.join(seen_dir, sid)
    try:
        last = open(mark).read().strip()
    except OSError:
        last = ""
    if last == head:
        return
    if last:
        added = git("diff", "--name-only", "--diff-filter=A", f"{last}..{head}", "--", "changes/").splitlines()
        cards = git("diff", "--name-only", f"{last}..{head}", "--", "catalog/").splitlines()
    else:   # first message in this session: the last week
        since = (dt.date.today() - dt.timedelta(days=7)).isoformat()
        added = git("log", f"--since={since}", "--diff-filter=A", "--name-only", "--format=", "--", "changes/").splitlines()
        cards = []
    open(mark, "w").write(head)
    added = sorted({p for p in added if p.endswith(".txt") and not p.endswith("_header.txt")}, reverse=True)
    rows = [r for r in (row(p) for p in added) if r]
    if not rows:
        return
    slugs = sorted({os.path.basename(c)[:-3] for c in cards if c.endswith(".md") and not os.path.basename(c).startswith(("_", "README"))})
    out = [f"New in the knowledge library ({LIB}) since this session last looked — use it from now on, and say in one "
           "line if it changes the current plan:"]
    out += [f"- {r}" for r in rows[:LIMIT]]
    if len(rows) > LIMIT:
        out.append(f"- …and {len(rows) - LIMIT} more in {LIB}/CHANGELOG.md")
    if slugs:
        out.append("Changed cards (read their use_when/how in catalog/<slug>.md before choosing tools): " + ", ".join(slugs[:25]))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "\n".join(out)}},
                     ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
