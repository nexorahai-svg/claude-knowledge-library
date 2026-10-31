#!/usr/bin/env python3
"""Check every relative link and #anchor between the Markdown files of this library.

Usage:  python3 scripts/check_links.py
Anchors follow GitHub's heading slugs (punctuation and zero-width joiners removed,
spaces turned into hyphens) plus explicit <a id="..."> tags.
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE = re.compile(r"```.*?```", re.S)


def slug(text):
    out = []
    for ch in text.strip().lower():
        cat = unicodedata.category(ch)
        if ch == " ":
            out.append("-")
        elif ch == "-" or cat[0] in "LMN" or cat == "Pc":
            out.append(ch)
    return "".join(out)


def main():
    files, anchors = [], {}
    for d, dirs, fs in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(d, f)
                files.append(p)
                text = open(p, encoding="utf-8").read()
                body = CODE.sub("", text)
                seen, found = {}, set()
                for h in re.findall(r"^#{1,6}\s+(.*)$", body, re.M):
                    s = slug(re.sub(r"<[^>]+>", "", h))
                    n = seen.get(s, 0)
                    seen[s] = n + 1
                    found.add(s if n == 0 else f"{s}-{n}")
                found |= set(re.findall(r'<a id="([^"]+)"', text))
                anchors[p] = found
    bad = 0
    for p in files:
        if p.replace(os.sep, "/").startswith("scripts/public/") or "/scripts/public/" in p.replace(os.sep, "/"):
            continue   # the public repo's landing page: its links are relative to that repo's root, checked there
        body = CODE.sub("", open(p, encoding="utf-8").read())
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        body = re.sub(r"`[^`\n]*`", "", body)   # links inside inline code are examples, not links
        for link in re.findall(r"\]\(([^)\s]+)\)", body):
            if link.startswith(("http", "mailto")):
                continue
            path, _, frag = link.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
            rel = os.path.relpath(p, ROOT)
            if not os.path.exists(target):
                print(f"MISSING FILE   {rel} -> {link}")
                bad += 1
            elif frag and target.endswith(".md") and frag not in anchors.get(target, set()):
                print(f"MISSING ANCHOR {rel} -> {link}")
                bad += 1
    print(f"checked {len(files)} files, problems: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
