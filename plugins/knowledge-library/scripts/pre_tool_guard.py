#!/usr/bin/env python3
"""PreToolUse hook: measure the machine before heavy work (resource rule, 2026-10-24).

Only heavy Bash commands (builds, renders, local AI models, test suites, installs, emulators, headless Claude) and
new subagents are checked; reading, editing and small commands pass untouched, so the rule never stops ordinary work.
  red    -> the call is denied with the reason and the exact wait command; Claude waits, then retries.
  yellow -> the call goes ahead with a note: one heavy job at a time, lower parallel flags, at most 2 subagents.
  green  -> nothing is said.
Measurement: <library>/scripts/resource_guard.py (RAM, swap, memory/CPU pressure, disk, CPU/GPU temperature, VRAM).
Must stay fast (about 30 ms) and must never break a session.

Release gate removed (2026-10-29, owner's decision): blocking uploads cost the owner hours and changed no result.
Tests get deeper each round instead (rule in projects/user-profile.md).
"""
import json
import os
import re
import sys

LIB = os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library"))
HEAVY = re.compile(
    r"\b(flutter\s+(build|run|test|drive)|gradlew?\b|\./gradlew|emulator\b|xcodebuild|"
    r"(npm|pnpm|yarn|bun)\s+(run\s+)?(build|test|install|ci|i\b|dev|start|render)|npx\s+(\S*hyperframes|\S*remotion|playwright|lhci|vite|next|astro)|"
    r"next\s+build|astro\s+build|vite\s+build|tsc\b|webpack|turbo\s+run|"
    r"ffmpeg|hyperframes\s+render|remotion\s+render|"
    r"docker\s+(build|run|compose)|podman\s+(build|run)|"
    r"ollama\s+(run|pull|serve)|llama-server|audiocpp_cli|vllm|"
    r"pip3?\s+install|uv\s+(sync|pip\s+install|add)|cargo\s+(build|test|install)|make\s+-j|cmake\s+--build|"
    r"pytest|playwright\s+test|lighthouse|"
    r"claude\s+-p\b|run_routine\.py\s+run|vp\.py|torch|whisper|tts_\w+\.py)", re.I)
# GPU-heavy commands also need VRAM headroom
GPU = re.compile(r"ollama|llama-server|audiocpp|vllm|torch|whisper|tts_|vp\.py|cuda|--backend\s+vulkan", re.I)


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name", "")
    inp = data.get("tool_input") or {}
    if tool == "Bash":
        cmd = inp.get("command", "")
        if "resource_guard.py" in cmd or not HEAVY.search(cmd):
            return
        what = "this heavy command"
    elif tool in ("Agent", "Task"):
        what = "a new subagent"
        cmd = ""
    else:
        return
    sys.path.insert(0, os.path.join(LIB, "scripts"))
    import resource_guard as rg
    s = rg.measure()
    level, reasons = rg.classify(s, need_vram=1.5 if GPU.search(cmd) else 0.0)
    guard = f"python3 {LIB}/scripts/resource_guard.py"
    if level == "red":
        out = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
               "permissionDecisionReason": (
                   f"Resource rule: the machine is under pressure ({'; '.join(reasons)}), so {what} was not started, to "
                   f"avoid freezing the computer. Run `{guard} wait` (it returns as soon as the machine is free, at most "
                   "20 minutes), then retry the same call. Meanwhile only light work. Do not kill the user's programs; if "
                   "the wait times out, tell the user what is using the machine and ask. Only if the owner called this an "
                   f"emergency in this session: `env KL_SWAP_EMERGENCY=1 {guard} run --mem 8G -- <command>` (swap limit 90%; "
                   "`export` in the shell does not reach this hook).")}}
        print(json.dumps(out, ensure_ascii=False))
    elif level == "yellow":
        out = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": (
            f"Resource rule: machine is busy ({'; '.join(reasons)}). Go ahead, but keep it to one heavy job at a time, "
            "lower parallel flags (build workers, render concurrency, test workers, -j), at most 2 subagents, and for a "
            f"long or memory-hungry job use `{guard} run --mem 8G -- <command>` so it cannot take the whole machine.")}}
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
