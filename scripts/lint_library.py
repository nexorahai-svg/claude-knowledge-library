#!/usr/bin/env python3
"""Quality checks for the knowledge library.

Usage:  python3 scripts/lint_library.py
Checks: standard header in every domain document, valid document type, every source ID
used by a card or document exists in sources/README.md, duplicate tool cards (same URL or
repo), and confidence labels present in documents. Exits 1 if any error is found.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_catalog import ROOT, load  # noqa: E402

HEADER_FIELDS = ["نوع سند", "هدف این سند", "موضوع تحقیق", "منابع", "آخرین بررسی", "دفعه‌ی بعد چک شود"]
DOC_TYPES = {"راهنمای قدم‌به‌قدم", "دستورالعمل", "مرجع", "توضیح"}
LABELS = ("✅", "🧭", "❓", "🔬")
# 🔬 means "worked in a real project": the file must link projects/README.md or name a logged
# project. Add a keyword here when a new row is added to the projects log.
PROJECT_KEYS = ("projects/README", "یک سایت مشتری", "یک سایت مشتری", "MARIO", "QR Order", "سفارش با کد QR",
                "پنل قرارداد", "a-project", "Crypto AI", "معامله‌گر")


def main():
    errors, warnings = [], []
    # sources: one file per source (sources/S12.md); sources/README.md is generated from them
    sdir = os.path.join(ROOT, "sources")
    known = set()
    for f in sorted(os.listdir(sdir)):
        m = re.fullmatch(r"(S\d+)\.md", f)
        if not m:
            continue
        sid = m.group(1)
        known.add(sid.lower())
        text = open(os.path.join(sdir, f), encoding="utf-8").read()
        row = re.match(r"<!-- row: (.+?) -->\n", text)
        if not row or row.group(1).count("|") != 3:
            errors.append(f"sources/{f}: first line must be <!-- row: summary | type | status | date -->")
        if not re.search(rf"(?m)^## {sid} —", text):
            errors.append(f"sources/{f}: heading '## {sid} — …' missing or numbered differently")
    registry = open(os.path.join(sdir, "README.md"), encoding="utf-8").read()
    in_table = {i.lower() for i in re.findall(r'<a id="(s\d+)"></a>\[S\d+\]', registry)}
    for sid in sorted(known - in_table):
        errors.append(f"sources/README.md: S{sid[1:]} has a file but no table row (run build_all.py)")
    nums = [int(i[1:]) for i in known]

    # leftover merge markers must never be committed (2026-10-21 one reached CHANGELOG.md)
    for d, dirs, fs in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", ".dart_tool", "build", "node_modules")]
        for f in fs:
            if f.endswith((".md", ".txt", ".py", ".json", ".yaml", ".yml", ".dart", ".html")):
                p = os.path.join(d, f)
                try:
                    body = open(p, encoding="utf-8").read()
                except UnicodeDecodeError:
                    continue
                if re.search(r"(?m)^(<{7} |>{7} )", body):
                    errors.append(f"{os.path.relpath(p, ROOT)}: merge conflict markers left in the file")
    print(f"next free source ID: S{max(nums) + 1}")

    for d, _, fs in os.walk(os.path.join(ROOT, "domains")):
        for f in fs:
            if not f.endswith(".md") or f == "README.md":
                continue
            p = os.path.join(d, f)
            rel = os.path.relpath(p, ROOT)
            text = open(p, encoding="utf-8").read()
            head = text[:3000]
            for field in HEADER_FIELDS:
                if f"**{field}:**" not in head:
                    errors.append(f"{rel}: header field missing: {field}")
            m = re.search(r"\*\*نوع سند:\*\*\s*(.+)", head)
            if m and m.group(1).strip() not in DOC_TYPES:
                errors.append(f"{rel}: unknown document type: {m.group(1).strip()}")
            if "🔬" in text and not any(k in text for k in PROJECT_KEYS):
                warnings.append(f"{rel}: 🔬 used but no project named and no link to projects/README.md")
            if not any(lbl in text for lbl in LABELS):
                warnings.append(f"{rel}: no confidence labels (✅ 🧭 ❓)")
            for sid in set(re.findall(r"README\.md#(s\d+)", text)):
                if sid not in known:
                    errors.append(f"{rel}: unknown source {sid.upper()}")

    cards = load()
    verdict_of = {c["_file"]: c.get("verdict") for c in cards}
    emoji = {"✅": "adopt", "🧪": "trial", "👀": "assess", "⛔": "hold"}

    def check_verdicts(rel, text, as_error):
        """A card link followed by a verdict emoji must match the card, so teaching documents
        never recommend a tool whose verdict has changed since they were written."""
        for f, mark in re.findall(r"\]\((?:\.\./)+catalog/([a-z0-9._-]+\.md)\)\s*\**\s*(✅|🧪|👀|⛔)", text):
            if f in verdict_of and verdict_of[f] != emoji[mark]:
                msg = f"{rel}: {mark} next to catalog/{f} but the card says {verdict_of[f]}"
                (errors if as_error else warnings).append(msg)

    # playbooks: the teacher layer; same header rules as documents, verdict marks must match cards
    pdir = os.path.join(ROOT, "playbooks")
    for f in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if not f.endswith(".md") or f in ("README.md", "_template.md"):
            continue
        rel = f"playbooks/{f}"
        text = open(os.path.join(pdir, f), encoding="utf-8").read()
        for field in HEADER_FIELDS:
            if f"**{field}:**" not in text[:3000]:
                errors.append(f"{rel}: header field missing: {field}")
        for sid in set(re.findall(r"README\.md#(s\d+)", text)):
            if sid not in known:
                errors.append(f"{rel}: unknown source {sid.upper()}")
        if "🔬" in text and not any(k in text for k in PROJECT_KEYS):
            warnings.append(f"{rel}: 🔬 used but no project named and no link to projects/README.md")
        check_verdicts(rel, text, as_error=True)
    for d, _, fs in os.walk(os.path.join(ROOT, "domains")):
        for f in fs:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(d, f), ROOT)
                check_verdicts(rel, open(os.path.join(d, f), encoding="utf-8").read(), as_error=False)

    seen = {}
    for c in cards:
        ctext = open(os.path.join(ROOT, "catalog", c["_file"]), encoding="utf-8").read()
        if "🔬" in ctext and not any(k in ctext for k in PROJECT_KEYS):
            warnings.append(f"catalog/{c['_file']}: 🔬 used but no project named and no link to projects/README.md")
        for sid in c.get("sources") or []:
            if isinstance(sid, str) and sid.lower() not in known:
                errors.append(f"catalog/{c['_file']}: unknown source {sid}")
        for key in ("repo", "url"):
            val = (c.get(key) or "").rstrip("/").lower()
            if val.startswith("http"):
                if val in seen and seen[val] != c["_file"]:
                    warnings.append(f"catalog/{c['_file']}: same {key} as catalog/{seen[val]} ({val})")
                seen.setdefault(val, c["_file"])

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"lint: {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
