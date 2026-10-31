#!/usr/bin/env python3
"""Stop hook: after a session tested, built, rendered, benchmarked or installed something, ask Claude to send an
experience report to the library queue (scripts/report_experience.py), so the user never has to feed the library.

Owner's decision 2026-10-30: project sessions report every new experience; the librarian session analyses and files it.
Detects installs and clones (pip/uv/npm/pnpm/yarn/npx, flutter/dart pub add, cargo, apt, git clone, claude mcp/plugin
add/install, ollama/hf downloads) and tests, builds, renders and benchmarks. Silent when: the stop is already a hook
continuation, the session works inside the library, a report was sent after the last such command, there is nothing
new since the last reminder, or the last reminder was less than 90 minutes ago.
"""
import json
import os
import re
import sys
import time

LIB = os.path.realpath(os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library")))
DATA = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
INSTALL = re.compile(
    r"\b(pip3? install|uv (?:pip install|add|tool install)|npm (?:i|install|add)\b|pnpm add|yarn add|npx -y|"
    r"(?:flutter|dart) pub add|cargo install|apt(?:-get)? install|git clone|claude (?:mcp add|plugin install)|"
    r"ollama pull|huggingface-cli download|hf download|brew install|go install|gem install|"
    r"npm (?:run )?(?:test|check|build)|pnpm (?:run )?(?:test|build)|yarn (?:test|build)|npx (?:playwright|vitest|jest|lighthouse|lhci)|"
    r"pytest|python3? -m (?:pytest|unittest)|flutter (?:test|build|analyze)|dart test|cargo (?:test|build|bench)|go test|"
    r"gradlew? \w*(?:test|assemble|build)|xcodebuild|maestro test|hyperframes (?:render|check)|remotion render|"
    r"npx (?:-y )?(?:hyperframes|remotion) render|ffmpeg|wrangler deploy|vercel deploy|docker (?:build|compose up))\b[^\n;&|]*")
COOLDOWN_S = 90 * 60


def commands(transcript):
    """Yield every Bash command the assistant ran in this session."""
    with open(transcript, encoding="utf-8") as f:
        for line in f:
            try:
                msg = json.loads(line).get("message") or {}
            except ValueError:
                continue
            content = msg.get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    inp = block.get("input") or {}
                    yield block.get("name", ""), json.dumps(inp, ensure_ascii=False) if block.get("name") != "Bash" else inp.get("command", "")


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        return
    cwd = os.path.realpath(data.get("cwd") or ".")
    if cwd.startswith(LIB) or os.path.exists(os.path.join(LIB, ".public-copy")):   # readers cannot file back
        return
    sid = data.get("session_id", "x")
    if not os.path.exists(data.get("transcript_path") or ""):
        return
    state_path = os.path.join(DATA, "reminded", sid)
    try:
        state = json.load(open(state_path))
    except (OSError, ValueError):
        state = {"seen": 0, "at": 0}
    found, since_report = [], []
    for name, text in commands(data["transcript_path"]):
        if "report_experience.py" in text:
            since_report = []   # a report covers everything before it
            continue
        if name == "Bash":
            for m in INSTALL.finditer(text):
                since_report.append(m.group(0).strip()[:120])
    total = len(since_report)
    if not since_report or total <= state.get("seen", 0) or time.time() - state.get("at", 0) < COOLDOWN_S:
        return
    for x in since_report:
        if x not in found:
            found.append(x)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    json.dump({"seen": total, "at": time.time()}, open(state_path, "w"))
    listed = "\n".join(f"- {x}" for x in found[-15:])
    print(json.dumps({"decision": "block", "reason": (
        "Experience report check (owner's rule): since the last report this session ran:\n" + listed + "\n"
        f"If any of it taught something new (a result with numbers, a failure, a version or install trap, a method, a "
        f"library claim that proved wrong), send ONE report now: `python3 {LIB}/scripts/report_experience.py` with JSON "
        "on stdin (fields in its header), then notify the librarian session it names. Do not edit the library yourself. "
        "Never include secrets. If nothing is new, say so in one line in the user's language and stop."
    )}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
