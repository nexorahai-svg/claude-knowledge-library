#!/usr/bin/env python3
"""Build dashboard/index.html (the radar page) from catalog/index.json and dashboard/template.html.

The page is bilingual (English default, Persian). English card summaries, document titles and licence notes come
from dashboard/i18n-en.json (slug/path -> text); anything missing there falls back to Persian and is counted below,
so whoever adds a card or document also adds its English line.

Usage:  python3 scripts/build_dashboard.py      (run scripts/build_llms.py first, or use build_all.py)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    data = json.load(open(os.path.join(ROOT, "catalog", "index.json"), encoding="utf-8"))
    template = open(os.path.join(ROOT, "dashboard", "template.html"), encoding="utf-8").read()
    en_path = os.path.join(ROOT, "dashboard", "i18n-en.json")
    en = json.load(open(en_path, encoding="utf-8")) if os.path.exists(en_path) else {}
    data["en"] = en
    missing = [c["slug"] for c in data["cards"] if c["slug"] not in en.get("cards", {})]
    missing += [d["path"] for d in data["documents"] if d["path"] not in en.get("docs", {})]
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("__DATA__", payload)
    with open(os.path.join(ROOT, "dashboard", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"dashboard/index.html built ({len(data['cards'])} cards, {len(html) // 1024} KB)"
          + (f"; no English text yet for {len(missing)}: {', '.join(missing[:8])}" if missing else ""))


if __name__ == "__main__":
    main()
