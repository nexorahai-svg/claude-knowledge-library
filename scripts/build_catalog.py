#!/usr/bin/env python3
"""Build catalog/README.md from the tool cards and report cards that are due for a re-check.

Usage:  python3 scripts/build_catalog.py          # rebuild the index
        python3 scripts/build_catalog.py --due    # only list overdue / incomplete cards
No third-party packages needed.
"""
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "catalog")

VERDICTS = {
    "adopt": ("✅", "استفاده کن"),
    "trial": ("🧪", "آزمایش کن"),
    "assess": ("👀", "زیر نظر"),
    "hold": ("⛔", "استفاده نکن"),
}
CATEGORIES = {
    "animation": "انیمیشن و حرکت",
    "3d": "سه‌بعدی و WebGL",
    "ui-components": "کامپوننت‌های رابط کاربری",
    "design-inspiration": "الهام طراحی",
    "fonts": "فونت",
    "icons-logos": "آیکون و لوگو",
    "templates": "قالب و کتابخانه‌ی پرامپت",
    "assets-media": "دارایی‌های رسانه (تکسچر، تصویر)",
    "audio-voice": "صدا و گفتار",
    "video": "ویدیو و موشن با کد",
    "image-generation": "تولید تصویر و قالب پست",
    "social-publishing": "انتشار و زمان‌بندی شبکه‌ها",
    "app-frameworks": "فریم‌ورک اپ (موبایل و دسکتاپ)",
    "app-testing": "تست اپ و اتصال به شبیه‌ساز",
    "app-publishing": "امضا و انتشار اپ",
    "hosting-deploy": "میزبانی و انتشار",
    "database-backend": "پایگاه داده و بک‌اند",
    "local-ai": "هوش مصنوعی محلی (موتور و مدل)",
    "site-generators": "سازنده‌ی سایت (فریم‌ورک)",
    "seo-search": "سئو، جستجو و کسب‌وکار محلی",
    "email-domain": "ایمیل، دامنه و DNS",
    "claude-code-tooling": "ابزارهای Claude Code",
    "cost-tokens": "هزینه و مصرف توکن",
    "browser-testing": "مرورگر و تست",
    "agents-memory": "عامل‌ها و حافظه",
    "research-tools": "ابزار تحقیق",
    "data-documents": "داده، اکسل و PDF",
    "reverse-engineering": "مهندسی معکوس",
    "experimental": "آزمایشی و پژوهشی",
}
STATUS = {"researched": "تحقیق کامل", "queued": "در صف تحقیق"}
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, _, val = line.partition(":")
        val = val.strip().strip('"')
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        meta[key.strip()] = val
    meta["_file"] = os.path.basename(path)
    return meta


def load():
    cards = []
    for f in sorted(os.listdir(CATALOG)):
        if f.endswith(".md") and not f.startswith(("_", "README")):
            meta = parse(os.path.join(CATALOG, f))
            if meta:
                cards.append(meta)
    return cards


def problems(card, today):
    out = []
    for key in ("name", "category", "verdict", "status", "summary", "url", "last_checked"):
        if not card.get(key):
            out.append(f"فیلد خالی: {key}")
    if card.get("verdict") not in VERDICTS:
        out.append(f"حکم نامعتبر: {card.get('verdict')}")
    if card.get("category") not in CATEGORIES:
        out.append(f"دسته‌ی نامعتبر: {card.get('category')}")
    if card.get("status") == "researched":
        due = card.get("next_check")
        if not due:
            out.append("next_check ندارد")
        elif datetime.date.fromisoformat(due) <= today:
            out.append(f"زمان بررسی دوباره رسیده ({due})")
    return out


def main():
    today = datetime.date.today()
    cards = load()
    if "--due" in sys.argv:
        found = False
        for c in cards:
            p = problems(c, today)
            if p:
                found = True
                print(f"{c['_file']}: " + "؛ ".join(p))
        if not found:
            print("همه‌ی کارت‌ها به‌روزند.")
        return

    lines = [
        "# فهرست ابزارها (کاتالوگ)",
        "",
        "> **این فایل خودکار ساخته می‌شود. دستی ویرایش نکن.** برای به‌روزرسانی: `python3 scripts/build_catalog.py`",
        f"> **آخرین ساخت:** {today.isoformat().translate(FA_DIGITS)} · **تعداد کارت‌ها:** {str(len(cards)).translate(FA_DIGITS)}",
        ">",
        "> حکم‌ها: " + " · ".join(f"{e} {fa}" for e, fa in VERDICTS.values()),
        "> وضعیت «در صف تحقیق» یعنی فقط مجوز و فعالیت مخزن چک شده و هنوز تحقیق کامل نشده؛ به حکمش تکیه نکن.",
        "> قالب کارت جدید: [_template.md](_template.md)",
        "",
    ]
    counts = {v: sum(1 for c in cards if c.get("verdict") == v) for v in VERDICTS}
    lines.append("| " + " | ".join(f"{VERDICTS[v][0]} {VERDICTS[v][1]}" for v in VERDICTS) + " |")
    lines.append("|" + "---|" * len(VERDICTS))
    lines.append("| " + " | ".join(str(counts[v]).translate(FA_DIGITS) for v in VERDICTS) + " |")
    lines.append("")
    order = list(VERDICTS)
    for cat, title in CATEGORIES.items():
        group = [c for c in cards if c.get("category") == cat]
        if not group:
            continue
        group.sort(key=lambda c: (order.index(c.get("verdict", "assess")) if c.get("verdict") in order else 9, c["name"].lower()))
        lines += [f"## {title}", "", "| ابزار | حکم | وضعیت | قیمت | مجوز | ریسک | خلاصه |", "|---|---|---|---|---|---|---|"]
        for c in group:
            e, fa = VERDICTS.get(c.get("verdict"), ("❓", "؟"))
            lines.append(
                f"| [{c['name']}]({c['_file']}) | {e} {fa} | {STATUS.get(c.get('status'), c.get('status', ''))} | "
                f"{c.get('pricing', '')} | {c.get('license', '') or '❓'} | {c.get('risk', '')} | {c.get('summary', '')} |"
            )
        lines.append("")
    issues = [(c["_file"], problems(c, today)) for c in cards]
    issues = [(f, p) for f, p in issues if p]
    if issues:
        lines += ["## نیازمند توجه", ""]
        lines += [f"- [{f}]({f}): " + "؛ ".join(p) for f, p in issues]
        lines.append("")
    open(os.path.join(CATALOG, "README.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"catalog/README.md ساخته شد: {len(cards)} کارت، {len(issues)} مورد نیازمند توجه")


if __name__ == "__main__":
    main()
