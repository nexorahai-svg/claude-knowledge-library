#!/usr/bin/env python3
"""Build dashboard/index.html (the radar page) from catalog/index.json and dashboard/template.html.

Usage:  python3 scripts/build_dashboard.py      (run scripts/build_llms.py first, or use build_all.py)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    data = json.load(open(os.path.join(ROOT, "catalog", "index.json"), encoding="utf-8"))
    template = open(os.path.join(ROOT, "dashboard", "template.html"), encoding="utf-8").read()
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("__DATA__", payload)
    with open(os.path.join(ROOT, "dashboard", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"dashboard/index.html built ({len(data['cards'])} cards, {len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
