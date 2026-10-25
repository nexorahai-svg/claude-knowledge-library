#!/usr/bin/env python3
"""Keep the two shared registries conflict-free: sources and the changelog.

Two machines adding to the same spot of one big file made git stop for a manual merge
(2026-10-21: sources S129 and S131 were taken twice). Now each item lives in its own file
and the big files are generated from them:

  sources/S12.md       one source: first line `<!-- row: summary | type | status | date -->`,
                       then `## S12 — title` and its bullets          (hand-written)
  sources/_intro.md    text above the summary table                    (hand-written)
  sources/README.md    intro + summary table with anchors `#s12`      (generated)
  changes/*.txt        one CHANGELOG row each                          (hand-written)
  changes/_header.txt  text above the changelog table                  (hand-written)
  CHANGELOG.md         header + rows, newest first                     (generated)
  .registry-state.json what was generated last time                    (generated)

Old habits still work: a row or `## S12 —` section added straight into sources/README.md,
or a row added to the top of CHANGELOG.md, is moved into its own file on the next build;
a hand edit of a generated source row is kept. Changelog fragments are never deleted by the
build: to change or remove a row, edit or delete its file in changes/. In the middle of a
merge or rebase only additions are taken (one side's generated file is always missing the
other side's rows, so "missing" means nothing there; 2026-10-21 this deleted a row). Usage: python3 scripts/build_registry.py
       --absorb  take every row/section in the two big files as content to keep (used by sync.py
                 on the other side of a merge conflict); never removes anything, state untouched.
"""
import datetime
import hashlib
import json
import os
import re
import socket

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sources")
CHG = os.path.join(ROOT, "changes")
STATE = os.path.join(ROOT, ".registry-state.json")

ROW_RE = re.compile(r'^\| (?:<a id="(s\d+)"></a>)?\[(S\d+)\]\([^)]*\) \| (.*) \|\s*$')
TABLE_HEAD = "| شماره | منبع | نوع | وضعیت | آخرین بررسی |\n|---|---|---|---|---|\n"
NOTE = ("\n> این فایل **خودکار ساخته می‌شود** (`scripts/build_registry.py`). هر منبع فایل خودش را دارد: "
        "`sources/S12.md`. منبع تازه: فایل `sources/S<شماره>.md` بساز (شماره‌ی آزاد بعدی را "
        "`python3 scripts/build_all.py` چاپ می‌کند)؛ اگر ردیف یا بخش را این‌جا اضافه کنی، ساخت بعدی خودش جابه‌جایش می‌کند.\n")


def merging():
    git = os.path.join(ROOT, ".git")
    return any(os.path.exists(os.path.join(git, x)) for x in ("rebase-merge", "rebase-apply", "MERGE_HEAD"))


def sha(text):
    return hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:16]


def num(sid):
    return int(sid[1:])


def read(path, default=""):
    return open(path, encoding="utf-8").read() if os.path.exists(path) else default


def write(path, text):
    if read(path, None) != text:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)


# ---------------------------------------------------------------- sources

def load_entries():
    entries = {}
    for f in os.listdir(SRC):
        m = re.fullmatch(r"(S\d+)\.md", f)
        if not m:
            continue
        text = read(os.path.join(SRC, f))
        row = re.match(r"<!-- row: (.*?) -->\n", text)
        body = text[row.end():] if row else text
        entries[m.group(1)] = {"row": row.group(1) if row else "", "body": body.strip() + "\n"}
    return entries


def save_entry(sid, row, body):
    write(os.path.join(SRC, f"{sid}.md"), f"<!-- row: {row} -->\n{body.strip()}\n")


def localize(body):
    """A section moved out of README.md: same folder, but `#s12` must point back to the table."""
    return re.sub(r"\]\(#(s\d+)\)", r"](README.md#\1)", body)


def parse_readme(text):
    rows, sections = {}, {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(2)] = (line.strip(), m.group(3).strip())
    # hand-added detail sections (old layout): `<a id="s12"></a>` then `## S12 — …`
    parts = re.split(r'(?m)^<a id="(s\d+)"></a>\s*\n', text)
    for i in range(1, len(parts), 2):
        sid = parts[i].upper()
        chunk = parts[i + 1].strip()
        chunk = re.sub(r"\n-{3,}\s*$", "", chunk).strip()   # a trailing `---` separator is not content
        if re.match(r"## S\d+", chunk):
            sections[sid] = localize(chunk) + "\n"
    return rows, sections


def intro_from(text):
    m = re.search(r"(?m)^## جدول خلاصه\s*$", text)
    return (text[:m.start()] if m else text).rstrip() + "\n"


def build_sources(state, absorb=False):
    readme_path = os.path.join(SRC, "README.md")
    readme = read(readme_path)
    intro_path = os.path.join(SRC, "_intro.md")
    if not os.path.exists(intro_path):
        write(intro_path, intro_from(readme))
    entries = load_entries()
    rows, sections = parse_readme(readme)
    last = {} if absorb else state.get("sources", {})
    moved = edited = 0
    for sid, (line, cells) in rows.items():
        if sid not in entries and last.get(sid) == sha(line) and sid not in sections:
            continue   # we generated this row and its file was renamed or removed since: do not bring it back
        if sid not in entries:
            body = sections.get(sid, f"## {sid} — (شرح نوشته نشده)\n")
            save_entry(sid, cells, body)
            entries[sid] = {"row": cells, "body": body}
            moved += 1
        elif not absorb and last.get(sid) and sha(line) != last[sid] and cells != entries[sid]["row"]:
            save_entry(sid, cells, entries[sid]["body"])    # hand edit of a generated row wins
            entries[sid]["row"] = cells
            edited += 1
    for sid, body in sections.items():
        if not absorb and sid in entries and body.strip() != entries[sid]["body"].strip():
            save_entry(sid, entries[sid]["row"], body)       # section pasted into README by hand
            entries[sid]["body"] = body
            edited += 1
    lines, new_state = [], {}
    for sid in sorted(entries, key=num):
        line = f'| <a id="{sid.lower()}"></a>[{sid}]({sid}.md) | {entries[sid]["row"]} |'
        lines.append(line)
        new_state[sid] = sha(line)
    intro = read(intro_path).rstrip() + "\n"
    write(readme_path, intro + "\n## جدول خلاصه\n" + NOTE + "\n" + TABLE_HEAD + "\n".join(lines) + "\n")
    state["sources"] = new_state
    return len(entries), moved, edited


# ---------------------------------------------------------------- changelog

def build_changelog(state, absorb=False):
    os.makedirs(CHG, exist_ok=True)
    path = os.path.join(ROOT, "CHANGELOG.md")
    text = read(path)
    head_path = os.path.join(CHG, "_header.txt")
    m = re.search(r"(?m)^\|[^\n]*\|\n\|[-| ]+\|\n", text)
    if not os.path.exists(head_path):
        write(head_path, text[:m.end()] if m else "# گزارش تغییرات\n\n| تاریخ | تغییر | سندها | منابع |\n|---|---|---|---|\n")
    current = [l for l in (text[m.end():] if m else "").splitlines() if l.startswith("| ")]
    frags = {}
    for f in os.listdir(CHG):
        if f.endswith(".txt") and not f.startswith("_"):
            frags[f] = read(os.path.join(CHG, f)).strip()
    known = {sha(r) for r in frags.values()}
    last = set() if absorb else set(state.get("changelog", []))
    cur_sha = {sha(r) for r in current}
    first_run = not frags
    removed = 0
    added = 0
    stamp = datetime.datetime.now().strftime("%H%M%S")
    host = re.sub(r"[^a-zA-Z0-9]", "", socket.gethostname())[:12] or "host"
    # a row we generated last time whose fragment was since edited or renumbered is not a new row
    new_rows = [r for r in current if sha(r) not in known and sha(r) not in last]
    for i, row in enumerate(new_rows):
        dm = re.match(r"\| ([۰-۹\d-]+) \|", row)
        date = dm.group(1) if dm else "unknown"
        date = date.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
        key = f"{len(new_rows) - i:08d}" if first_run else f"{stamp}{99 - min(i, 99):02d}"
        name = f"{date}-{key}-{'m' if first_run else host}.txt"
        write(os.path.join(CHG, name), row.strip() + "\n")
        frags[name] = row.strip()
        added += 1

    def order(f):
        parts = f.split("-")
        return ("-".join(parts[:3]), parts[3] if len(parts) > 3 else "")
    rows = [frags[f] for f in sorted(frags, key=order, reverse=True)]
    write(path, read(head_path) + "\n".join(rows) + "\n")
    state["changelog"] = sorted(sha(r) for r in rows)
    return len(rows), added, removed


def main():
    import sys
    cli_absorb = "--absorb" in sys.argv     # sync feeding us the other side's file: change nothing else
    absorb = cli_absorb or merging()         # mid-merge: additions only, but keep the state current
    state = json.loads(read(STATE, "{}") or "{}")
    n, moved, edited = build_sources(dict(state) if cli_absorb else state, absorb)
    c, added, removed = build_changelog(dict(state) if cli_absorb else state, absorb)
    if not cli_absorb:
        write(STATE, json.dumps(state, ensure_ascii=False, indent=0, sort_keys=True) + "\n")
    nxt = max(num(f[:-3]) for f in os.listdir(SRC) if re.fullmatch(r"S\d+\.md", f)) + 1
    print(f"sources: {n} files ({moved} moved in, {edited} hand edits kept) | "
          f"changelog: {c} rows ({added} new, {removed} removed) | next free source ID: S{nxt}")


if __name__ == "__main__":
    main()
