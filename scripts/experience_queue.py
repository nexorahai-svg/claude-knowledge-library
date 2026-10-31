#!/usr/bin/env python3
"""The librarian's side of the experience queue (2026-10-30). See scripts/report_experience.py for the sender's side.

  python3 scripts/experience_queue.py list              # reports not yet processed (status: new), oldest first
  python3 scripts/experience_queue.py count             # just the number (used by the session-start hook)
  python3 scripts/experience_queue.py mark FILE STATUS --note "what was filed where" [--links "catalog/x.md, ..."]
      STATUS: filed | duplicate | rejected | needs-info
  python3 scripts/experience_queue.py register SESSION_ID   # make this session the librarian that senders notify

Processing rule (librarian): for each new report, verify the claims (primary source for facts; the report's own evidence
for 🔬 results), compare with the library, then file per CLAUDE.md "Adding a finding" and "Projects contribute back"
(card or document, projects/README.md row, changelog fragment), run build_all.py, mark the report, and sync. A report
is never deleted; "rejected" and "duplicate" need a note with the reason. Urgent reports (safety, licence) go first.
"""
import datetime as dt
import json
import os
import re
import sys

LIB = os.path.realpath(os.path.expanduser(os.environ.get("KL_DIR", "~/Desktop/knowledge-library")))
QUEUE = os.path.join(LIB, "research", "inbox", "experience")
STATE = os.environ.get("CLAUDE_PLUGIN_DATA") or os.path.expanduser("~/.local/state/knowledge-library")
STATUSES = {"filed", "duplicate", "rejected", "needs-info"}


def reports():
    if not os.path.isdir(QUEUE):
        return []
    out = []
    for name in sorted(os.listdir(QUEUE)):
        if not name.endswith(".md") or name.startswith(("_", "README")):
            continue
        text = open(os.path.join(QUEUE, name), encoding="utf-8").read()
        status = (re.search(r"^status: *(\S+)", text, re.M) or [None, "new"])[1]
        urgent = bool(re.search(r"^urgent: *yes", text, re.M))
        title = (re.search(r"^# (.+)$", text, re.M) or [None, name])[1]
        out.append({"file": name, "status": status, "urgent": urgent, "title": title})
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "count":
        print(sum(1 for r in reports() if r["status"] in ("new", "needs-info")))
    elif cmd == "list":
        new = [r for r in reports() if r["status"] in ("new", "needs-info")]
        new.sort(key=lambda r: (not r["urgent"], r["file"]))
        for r in new:
            print(f"{'URGENT ' if r['urgent'] else ''}{r['status']:10} research/inbox/experience/{r['file']}  {r['title']}")
        print(f"{len(new)} report(s) waiting")
    elif cmd == "mark":
        if len(sys.argv) < 4 or sys.argv[3] not in STATUSES or "--note" not in sys.argv:
            sys.exit("usage: mark FILE filed|duplicate|rejected|needs-info --note \"...\" [--links \"...\"]")
        path = os.path.join(QUEUE, os.path.basename(sys.argv[2]))
        note = sys.argv[sys.argv.index("--note") + 1]
        links = sys.argv[sys.argv.index("--links") + 1] if "--links" in sys.argv else ""
        text = open(path, encoding="utf-8").read()
        text = re.sub(r"^status: *\S+", f"status: {sys.argv[3]}", text, count=1, flags=re.M)
        stamp = dt.date.today().isoformat()
        entry = f"- {stamp}: **{sys.argv[3]}** — {note}" + (f" ({links})" if links else "")
        text = text.replace("(خالی تا وقتی کتابدار پردازش کند)", entry) if "(خالی تا" in text else text.rstrip() + "\n" + entry + "\n"
        open(path, "w", encoding="utf-8").write(text)
        print(f"marked {os.path.basename(path)}: {sys.argv[3]}")
    elif cmd == "register":
        os.makedirs(STATE, exist_ok=True)
        json.dump({"session_id": sys.argv[2], "since": dt.datetime.now().isoformat(timespec="seconds")},
                  open(os.path.join(STATE, "librarian.json"), "w"))
        print(f"librarian session: {sys.argv[2]}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
