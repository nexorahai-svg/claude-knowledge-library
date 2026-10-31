#!/usr/bin/env python3
"""Hook launcher: run the library's live copy of a hook script, so every session uses today's rules (2026-10-28).

Claude Code runs plugin hooks from a cached copy that only refreshes when Claude starts, so sessions that stay open for
days kept old hooks (the "nothing half-done" guard and new rules never reached them). This launcher runs
<library>/plugins/knowledge-library/scripts/<name> when the library is on the machine, else the bundled copy.
Safety: when the plugin code was last changed by an automatic routine (daily watch / sweep), the bundled copy runs.
Usage in hooks.json: python3 ${CLAUDE_PLUGIN_ROOT}/scripts/run.py <script.py>
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library"))


def pick(name):
    bundled = os.path.join(HERE, name)
    live = os.path.join(LIB, "plugins/knowledge-library/scripts", name)
    if not os.path.isfile(live) or os.path.realpath(live) == os.path.realpath(bundled):
        return bundled
    try:
        last = subprocess.run(["git", "-C", LIB, "log", "-1", "--format=%s", "--", "plugins/knowledge-library"],
                              capture_output=True, text=True, timeout=3).stdout
    except Exception:
        return bundled
    if re.match(r"(Daily watch|Weekly sweep|Two-day deep sweep)", last):
        return bundled
    return live


def main():
    if len(sys.argv) < 2 or not re.fullmatch(r"[a-z_]+\.py", sys.argv[1]):
        return
    script = pick(sys.argv[1])
    if os.path.isfile(script):
        os.execv(sys.executable, [sys.executable, script, *sys.argv[2:]])   # stdin passes through


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
