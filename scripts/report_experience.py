#!/usr/bin/env python3
"""Project sessions report new experience to the library through one fixed queue (2026-10-30, owner's decision).

Every session that ran a test, build, benchmark, render, install or any work and learned something new (a tool worked or
failed, a number, a version trap, a method, a correction to the library) writes ONE report here instead of editing the
library itself. The librarian session analyses each report, verifies it, files it (cards, documents, projects/README.md
row, changelog) and marks it with scripts/experience_queue.py. Reports live in research/inbox/experience/, which the
public copy never publishes.

Usage (JSON on stdin, or --json FILE):
  python3 ~/Desktop/knowledge-library/scripts/report_experience.py <<'EOF'
  {"project": "...", "session": "<title or local_… id>", "kind": "test", "title": "...", "done": "...",
   "result": "...", "worked": "...", "failed": "...", "tools": "...", "evidence": "...",
   "library_said": "...", "confidence": "🔬"}
  EOF
Fields (all required, plain text, any language):
  project      project name and folder
  session      this session's title or local_… id
  kind         test | build | tool | method | failure | correction | version | cost | other
  title        one line
  done         what was done, exact commands where they matter
  result       the outcome with numbers (counts, times, sizes, errors); "none" is not allowed
  worked       what worked
  failed       what failed or surprised ("nothing" is allowed)
  tools        tools/cards/models with exact versions
  evidence     paths, logs, commands or URLs that prove it
  library_said what the library said before (card/document) and how reality differed, or "not in library"
  confidence   🔬 tested here | 🧭 rule of thumb | ❓ unsure
Optional: "next" (what this suggests for the library), "urgent": true (a safety or licence problem).
The script refuses reports that contain secrets (keys, tokens, passwords) and prints the file path and how to notify.
"""
import datetime as dt
import json
import os
import re
import socket
import subprocess
import sys
import time

LIB = os.path.realpath(os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library")))
QUEUE = os.path.join(LIB, "research", "inbox", "experience")
STATE = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
REQUIRED = ["project", "session", "kind", "title", "done", "result", "worked", "failed", "tools", "evidence",
            "library_said", "confidence"]
KINDS = {"test", "build", "tool", "method", "failure", "correction", "version", "cost", "other"}
SECRET = re.compile(
    r"(sk-(?:ant-)?[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|xox[abpr]-[A-Za-z0-9-]{10,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}|"
    r"(?i:(?:api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+]{12,}))")


def fail(msg):
    print(f"REFUSED: {msg}", file=sys.stderr)
    sys.exit(2)


def librarian():
    try:
        return json.load(open(os.path.join(STATE, "librarian.json"), encoding="utf-8")).get("session_id", "")
    except (OSError, ValueError):
        return ""


def main():
    raw = open(sys.argv[sys.argv.index("--json") + 1], encoding="utf-8").read() if "--json" in sys.argv else sys.stdin.read()
    try:
        rep = json.loads(raw)
    except ValueError as e:
        fail(f"not valid JSON ({e})")
    missing = [k for k in REQUIRED if not str(rep.get(k, "")).strip()]
    if missing:
        fail("missing fields: " + ", ".join(missing))
    if str(rep["kind"]).strip().lower() not in KINDS:
        fail("kind must be one of: " + ", ".join(sorted(KINDS)))
    if str(rep["result"]).strip().lower() in {"none", "-", "n/a", "ok", "done"}:
        fail("result must say what actually happened, with numbers where there are any")
    if str(rep["confidence"]).strip() not in {"🔬", "🧭", "❓"}:
        fail("confidence must be 🔬, 🧭 or ❓")
    hit = SECRET.search(json.dumps(rep, ensure_ascii=False))
    if hit:
        fail("the report contains something that looks like a secret; remove it and send again")
    os.makedirs(QUEUE, exist_ok=True)
    now = dt.datetime.now()
    host = re.sub(r"[^A-Za-z0-9-]", "", socket.gethostname())[:20] or "host"
    slug = re.sub(r"[^a-z0-9]+", "-", str(rep["project"]).lower()).strip("-")[:30] or "project"
    name = f"{now:%Y-%m-%d-%H%M%S}-{host}-{slug}.md"
    path = os.path.join(QUEUE, name)
    n = 1
    while os.path.exists(path):
        n += 1
        path = os.path.join(QUEUE, name[:-3] + f"-{n}.md")
    labels = {"project": "پروژه", "session": "جلسه", "kind": "نوع", "done": "چه شد", "result": "نتیجه (با عدد)",
              "worked": "کار کرد", "failed": "شکست یا غافل‌گیری", "tools": "ابزار و نسخه", "evidence": "مدرک",
              "library_said": "کتابخانه چه می‌گفت", "next": "پیشنهاد برای کتابخانه"}
    body = ["---", "status: new", f"received: {now:%Y-%m-%d %H:%M}", f"host: {host}",
            f"urgent: {'yes' if rep.get('urgent') else 'no'}", f"confidence: {rep['confidence']}", "---", "",
            f"# {str(rep['title']).strip()}", ""]
    for key, label in labels.items():
        if str(rep.get(key, "")).strip():
            body.append(f"**{label}:** {str(rep[key]).strip()}")
            body.append("")
    body += ["## پردازش کتابدار", "(خالی تا وقتی کتابدار پردازش کند)", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(body))
    rel = os.path.relpath(path, LIB)
    for _ in range(5):   # commit only this file; another session may hold the index for a moment
        r = subprocess.run(["git", "-C", LIB, "add", "--", rel], capture_output=True, text=True)
        if r.returncode == 0:
            r = subprocess.run(["git", "-C", LIB, "commit", "-q", "-m", f"Experience report: {slug}", "--", rel],
                               capture_output=True, text=True)
            if r.returncode == 0:
                break
        time.sleep(1.5)
    else:
        print(f"note: saved but not committed ({r.stderr.strip()[:200]}); the librarian's sync will pick it up")
    print(f"QUEUED: {path}")
    sid = librarian()
    if sid:
        print(f"NOW notify the librarian session: send_message to {sid} with one line: "
              f"\"Experience report queued: {rel}\" (if that session is gone, the queue still holds the report).")
    else:
        print("No librarian session is registered; the report waits in the queue for the next library session.")


if __name__ == "__main__":
    main()
