#!/usr/bin/env python3
"""Stop hook: when a session installed or cloned something new and never touched the library,
ask Claude once (per session) to file the findings back, so the user does not have to feed it.

Detects installs and clones in the session's Bash commands (pip/uv/npm/pnpm/yarn/npx, flutter/dart
pub add, cargo, apt, git clone, claude mcp/plugin add/install, ollama/hf downloads). Silent when:
the stop is already a hook continuation, the session works inside the library, the library was
already edited or synced in this session, or this session was reminded before.
"""
import json
import os
import re
import sys

LIB = os.path.realpath(os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library")))
DATA = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
INSTALL = re.compile(
    r"\b(pip3? install|uv (?:pip install|add|tool install)|npm (?:i|install|add)\b|pnpm add|yarn add|npx -y|"
    r"(?:flutter|dart) pub add|cargo install|apt(?:-get)? install|git clone|claude (?:mcp add|plugin install)|"
    r"ollama pull|huggingface-cli download|hf download|brew install|go install|gem install)\b[^\n;&|]*")


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
    marker = os.path.join(DATA, "reminded", sid)
    if os.path.exists(marker) or not os.path.exists(data.get("transcript_path") or ""):
        return
    found, touched = [], False
    for name, text in commands(data["transcript_path"]):
        if LIB in text or "Desktop/knowledge-library" in text:
            touched = True
        if name == "Bash":
            for m in INSTALL.finditer(text):
                item = m.group(0).strip()[:120]
                if item not in found:
                    found.append(item)
    if touched or not found:
        return
    os.makedirs(os.path.dirname(marker), exist_ok=True)
    open(marker, "w").close()
    listed = "\n".join(f"- {x}" for x in found[:15])
    print(json.dumps({"decision": "block", "reason": (
        "Knowledge library check (once per session): this session installed or fetched these, and the library "
        f"was not updated in it:\n{listed}\n"
        "Per the knowledge-library skill section 3: compare them with the library (llms-full.txt / catalog); file anything "
        "genuinely new or any correction (new tool, version, failure, method), add a projects/README.md row if a real "
        "project used them, run scripts/build_all.py and scripts/sync.py. If nothing is new, say so in one line and stop."
    )}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
