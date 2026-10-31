#!/usr/bin/env python3
"""Stop hook: nothing half-done or forgotten (2026-10-28).

A session ran the release gate while items its subagents had reported as "not done" were still open, and only named
them after the gate passed, so the user had to test again. The rule: every turn that did work ends with a "remaining
work" list (or an explicit "none"), and the human decides what happens next. This hook reads the turn from the
transcript; when Claude edited files or ran commands in it and the final answer has no such section, the turn is sent
back once. Pure question-and-answer turns are never checked.
"""
import json
import os
import re
import sys

WORK_TOOLS = {"Edit", "Write", "NotebookEdit", "Bash", "Agent", "Task", "Workflow"}
# a "remaining work" section in Persian, Arabic or English
LEFTOVER = re.compile(r"باقی[‌ ]?مانده|باقیمانده|کار(?:های)? باقی|کار(?:ی)? (?:باز|نمانده)|موارد باز|هیچ کاری (?:باقی )?نمانده|"
                      r"مانده(?:‌اند| است)?\s*[:：]|المتبقي|المهام المتبقية|"
                      r"\bremaining\b|\bleft to do\b|\bstill open\b|\bnothing (?:is )?left\b|\bopen items\b|\bleftovers?\b", re.I)


def turn(transcript):
    """Tool names used and Claude's text blocks since the user's last real message."""
    tools, texts = set(), []
    with open(transcript, encoding="utf-8") as f:
        for line in f:
            try:
                msg = json.loads(line).get("message") or {}
            except ValueError:
                continue
            role, content = msg.get("role"), msg.get("content")
            if role == "user":
                if isinstance(content, str) or (isinstance(content, list) and any(
                        isinstance(b, dict) and b.get("type") == "text" for b in content)):
                    tools, texts = set(), []   # a new user turn starts
            elif role == "assistant" and isinstance(content, list):
                for b in content:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_use":
                        tools.add(b.get("name", ""))
                    elif b.get("type") == "text":
                        texts.append(b.get("text", ""))
    return tools, texts


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active") or not os.path.exists(data.get("transcript_path") or ""):
        return
    tools, texts = turn(data["transcript_path"])
    if not tools & WORK_TOOLS:
        return
    last = data.get("last_assistant_message")
    final = last if isinstance(last, str) and last else (texts[-1] if texts else "")
    if LEFTOVER.search(final):
        return
    print(json.dumps({"decision": "block", "reason": (
        "Nothing-half-done rule: this turn did work, but the final answer has no \"remaining work\" section. Rewrite the "
        "final answer in the user's language and end it with that section: every open item (unfinished steps, known "
        "defects, items a subagent reported as not done, decisions the user must make, anything not tested), or an "
        "explicit \"none\" when nothing is left. Do not drop or defer anything on your own; the user decides what is "
        "done next.")}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
