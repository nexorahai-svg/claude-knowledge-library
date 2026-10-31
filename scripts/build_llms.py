#!/usr/bin/env python3
"""Build llms.txt (a short index Claude reads first) and catalog/index.json (machine-readable catalog).

Usage:  python3 scripts/build_llms.py
Reads the tool cards (via build_catalog.load) and the header of every domain document.
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_catalog import CATEGORIES, ROOT, VERDICTS, load  # noqa: E402

DOMAIN_TITLES = {
    "website": "وبسایت",
    "apps": "اپلیکیشن (موبایل و دسکتاپ، چندسکویی)",
    "social-media": "شبکه‌های اجتماعی (ویدیو، عکس، پست، صدا)",
    "claude-code": "Claude Code (هزینه، امنیت، کار موازی، بررسی، دستیار)",
    "security": "امنیت (هشدارهای ماه، به‌روزرسانی، زنجیره‌ی تأمین، عامل‌ها)",
}


def header_field(text, label):
    m = re.search(r"^> \*\*" + re.escape(label) + r":\*\*\s*(.+)$", text, re.M)
    if not m:
        return ""
    # generated data must not carry private text: drop private blocks, keep the public wording
    val = re.sub(r"", "", m.group(1), flags=re.S)
    val = re.sub(r"(.*?)", r"\1", val, flags=re.S)
    return re.sub(r"<!--.*?-->", "", val, flags=re.S).strip()


def domain_docs():
    docs = []
    base = os.path.join(ROOT, "domains")
    for d, _, fs in os.walk(base):
        for f in sorted(fs):
            if not f.endswith(".md") or f == "README.md":
                continue
            p = os.path.join(d, f)
            text = open(p, encoding="utf-8").read()
            title = re.search(r"^# (.+)$", text, re.M)
            rel = os.path.relpath(p, ROOT)
            docs.append({
                "path": rel,
                "domain": rel.split(os.sep)[1],
                "title": title.group(1).strip() if title else f,
                "type": header_field(text, "نوع سند"),
                "purpose": header_field(text, "هدف این سند"),
                "last_checked": header_field(text, "آخرین بررسی"),
            })
    return sorted(docs, key=lambda x: x["path"])


def playbooks():
    base = os.path.join(ROOT, "playbooks")
    out = []
    for f in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        if f.endswith(".md") and f not in ("README.md", "_template.md"):
            text = open(os.path.join(base, f), encoding="utf-8").read()
            title = re.search(r"^# (.+)$", text, re.M)
            out.append({"path": f"playbooks/{f}", "title": title.group(1).strip() if title else f,
                        "purpose": header_field(text, "هدف این سند")})
    return out


def main():
    today = datetime.date.today().isoformat()
    cards = load()
    docs = domain_docs()

    index = {
        "built": today,
        "verdicts": {k: v[1] for k, v in VERDICTS.items()},
        "categories": CATEGORIES,
        "cards": [
            {k: c.get(k) for k in ("name", "slug", "category", "domains", "verdict", "status", "summary",
                                   "use_when", "how", "url", "repo", "license", "pricing", "risk", "sources",
                                   "last_checked", "next_check")}
            | {"file": "catalog/" + c["_file"]}
            for c in cards
        ],
        "documents": docs,
        "playbooks": playbooks(),
    }
    with open(os.path.join(ROOT, "catalog", "index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)

    out = [
        "# Knowledge library (کتابخانه‌ی دانش)",
        "",
        "> Verified tools, methods and sources for cross-platform apps (mobile and desktop), websites",
        "> and social media content, plus Claude Code know-how. Documents are in Persian; prompts are in English.",
        f"> Built {today} by scripts/build_llms.py. Read this first, then open only what you need.",
        "",
        "Rules: never copy others' designs, prompts or code; use only clearly licensed assets;",
        "verdicts are adopt (use) / trial (small test first) / assess (not yet recommended) /",
        "hold (do not use). Cards with status queued are not recommendations. Every project must",
        "use the newest verified option and file new findings back (see CLAUDE.md, projects/README.md).",
        "",
        "## Start here: project playbooks (the teacher)",
        "",
        "Classify the project, open its playbook and follow it phase by phase: questions to ask,",
        "default stack with verdicts, and a runnable 'done' gate for every phase. Router: playbooks/README.md",
        "",
    ] + [f"- [{p['title']}]({p['path']}): {p['purpose']}" for p in playbooks()] + [
        "",
        "## Documents",
        "",
    ]
    for dom, title in DOMAIN_TITLES.items():
        group = [d for d in docs if d["domain"] == dom]
        if not group:
            continue
        out.append(f"### {title}")
        for d in group:
            kind = f" [{d['type']}]" if d["type"] else ""
            out.append(f"- [{d['title']}]({d['path']}){kind}: {d['purpose']}")
        out.append("")

    order = ["adopt", "trial", "hold"]
    labels = {"adopt": "Adopt (✅ use)", "trial": "Trial (🧪 small test first)", "hold": "Hold (⛔ do not use)"}
    out += ["## Tools by verdict", "", "Assess (👀) items are omitted here; see catalog/README.md.", ""]
    for v in order:
        group = sorted((c for c in cards if c.get("verdict") == v and c.get("status") == "researched"),
                       key=lambda c: (c.get("category", ""), c["name"].lower()))
        out.append(f"### {labels[v]}")
        for c in group:
            out.append(f"- [{c['name']}](catalog/{c['_file']}) ({c.get('category')}, {c.get('license') or '?'}): {c.get('summary')}")
        out.append("")
    out += [
        "## Other entry points",
        "",
        "- [Full catalog with all verdicts](catalog/README.md) and [machine-readable index](catalog/index.json)",
        "- [Sources registry](sources/README.md) (permanent IDs S01…, next checks)",
        "- [Watchlist of official sources](research/watchlist.md) and [X accounts with trust ratings](research/x-accounts.md)",
        "- Project experience log and changelog",
        "",
    ]
    with open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # catalog/use-when.md: situation -> tool -> exact action, from each usable card's use_when/how.
    # The session-start hook shows the lines for the detected project kind; sessions open this file
    # when they are about to do one of these jobs.
    uw = [
        "# When to use what (generated)",
        "",
        f"> Built {today} by scripts/build_llms.py from the `use_when` and `how` fields of adopt and trial cards.",
        "> Never edit by hand: change the card and run scripts/build_all.py. Trial = small test first.",
        "",
    ]
    for dom, title in DOMAIN_TITLES.items():
        group = sorted((c for c in cards if c.get("verdict") in ("adopt", "trial") and c.get("use_when")
                        and dom in (c.get("domains") or [])),
                       key=lambda c: (c.get("verdict") != "adopt", c["name"].lower()))
        if not group:
            continue
        uw += [f"## {title}", "", "| When | Tool | How |", "|---|---|---|"]
        for c in group:
            mark = "✅" if c.get("verdict") == "adopt" else "🧪"
            cell = lambda s: str(s or "").replace("|", "/")
            uw.append(f"| {cell(c.get('use_when'))} | {mark} [{c['name']}]({c['_file']}) | {cell(c.get('how'))} |")
        uw.append("")
    with open(os.path.join(ROOT, "catalog", "use-when.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(uw))

    # llms.txt is read at the start of every session: keep it a short router (a few KB, not 60),
    # and send Claude to the full list only when it needs it.
    short = [
        "# Knowledge library (کتابخانه‌ی دانش) — start here",
        "",
        f"> Built {today} by scripts/build_llms.py. Short router; the full list of every document and",
        "> every tool by verdict is llms-full.txt (open it only when you need to search the whole library).",
        "",
        "1. Read projects/user-profile.md (standing rules, budget rules, guards) before choosing anything.",
        "2. Classify the task with the routes below, open that one file, follow it.",
        "3. Verdicts: adopt ✅ use · trial 🧪 small test first · assess 👀 not yet · hold ⛔ never. Never copy",
        "   others' designs, prompts or code; only clearly licensed assets. File new findings back (CLAUDE.md).",
        "",
        "## Routes",
        "",
        "| Task | Open |",
        "|---|---|",
        "| Any project: which playbook | playbooks/README.md |",
        "| Design an app (any kind, Android + iOS) | domains/apps/app-design-system.md, then app-styles.md and app-screen-patterns.md |",
        "| Start the code of a Flutter app | starters/flutter-app/README.md |",
        "| A link, post, reel or tool to check | research/x-research-plan.md (+ scripts/fetch_post.py) |",
        "| Is a tool still current / ready for a better verdict | scripts/check_updates.py and its report in research/inbox/ |",
        "| Claude Code cost, safety, plugins, MCP, parallel work | domains/claude-code/README.md |",
        "| Security: this month's advisories, patching, supply chain, plugins/MCP risk | domains/security/README.md |",
        "| Set up a new machine like the main one | projects/new-machine.md (+ scripts/setup_machine.py) |",
        "| Which tool and exact step for the job at hand (situation -> tool -> how) | catalog/use-when.md |",
        "| Find a tool by name or category | catalog/README.md or catalog/index.json |",
        "| A source ID (S12) | sources/S12.md |",
        "",
        "## Playbooks",
        "",
    ] + [f"- {p['title']}: {p['path']}" for p in playbooks()] + [
        "",
        "## Domains",
        "",
    ] + [f"- {title}: domains/{dom}/README.md" for dom, title in DOMAIN_TITLES.items()] + [
        "",
        f"Counts: {len(cards)} tool cards, {len(docs)} documents. Sync: python3 scripts/sync.py at start and end.",
        "",
    ]
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(short))
    print(f"llms.txt (short), llms-full.txt and catalog/index.json built: {len(cards)} cards, {len(docs)} documents")


if __name__ == "__main__":
    main()
