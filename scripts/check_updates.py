#!/usr/bin/env python3
"""Mechanical update check for every catalog card (part A of the two-day deep sweep).

Usage:  python3 scripts/check_updates.py              # check, write the report, update the state file
        python3 scripts/check_updates.py --dry-run    # check and print, change nothing

For every card except hold cards (⛔, "red": we do not follow them) and the template:
  - GitHub repo (from `repo:`): archived, license, last push, newest release, stars
  - website (`url:`): does it still answer (HTTP status)
  - package registry, from `package: npm:<name>` / `pub:<name>` / `pypi:<name>` or a pub.dev,
    npmjs.com or pypi.org `url:`: newest version, discontinued or deprecated
Then a promotion list (no network needed; alone with `--promotions`): how many real projects in
projects/README.md used each card. Trial cards used in 2+ projects with no problem -> review for
adopt; adopt cards with a problem -> review for demotion; assess cards already used -> consider trial.
Compares with research/sweep-state.json from the previous run and writes
research/inbox/<date>-updates.md listing only what changed or looks wrong:
new release, license differs from the card, archived, no push for 12 months, dead site.
The sweep agents then verify each item against the primary source and update the cards.

Uses the GitHub CLI (`gh api`) when it is logged in (5000 requests/hour), otherwise the
public API (60 requests/hour, enough for a partial run; the rest is reported as skipped).
"""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "research", "sweep-state.json")
TODAY = datetime.date.today()
STALE_DAYS = 365
UA = {"User-Agent": "knowledge-library-sweep"}


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    fields = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"')
    return fields


@lru_cache(maxsize=1)
def gh_ready():
    return bool(shutil.which("gh")) and subprocess.run(["gh", "auth", "status"], capture_output=True).returncode == 0


def gh_json(endpoint):
    if gh_ready():
        for _ in range(3):  # retry short network hiccups
            r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True)
            if r.returncode == 0 or "404" in r.stderr:
                break
        if r.returncode != 0:
            return None if "404" in r.stderr else {"_error": r.stderr.strip()[:120]}
        return json.loads(r.stdout)
    try:
        with urllib.request.urlopen(urllib.request.Request("https://api.github.com/" + endpoint, headers=UA), timeout=10) as f:
            return json.load(f)
    except urllib.error.HTTPError as e:
        return None if e.code == 404 else {"_error": f"HTTP {e.code}"}
    except Exception as e:  # network problems are reported, not fatal
        return {"_error": str(e)[:120]}


def site_status(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=10) as f:
                return f.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405):
                return e.code
        except Exception:
            if method == "GET":
                return 0
    return 0


def check_repo(repo_url):
    m = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", repo_url)
    if not m:
        return None
    full = f"{m.group(1)}/{m.group(2).removesuffix('.git')}"
    info = gh_json(f"repos/{full}")
    if info is None:
        return {"repo": full, "missing": True}
    if "_error" in info:
        return {"repo": full, "error": info["_error"]}
    rel = gh_json(f"repos/{full}/releases/latest")
    return {
        "repo": full,
        "archived": info.get("archived", False),
        "license": (info.get("license") or {}).get("spdx_id") or "",
        "pushed": (info.get("pushed_at") or "")[:10],
        "stars": info.get("stargazers_count", 0),
        "release": (rel or {}).get("tag_name", "") if rel and "_error" not in rel else "",
        "release_date": ((rel or {}).get("published_at") or "")[:10] if rel and "_error" not in rel else "",
    }


def package_of(fm):
    pkg = fm.get("package", "")
    if ":" in pkg:
        return tuple(pkg.split(":", 1))
    for pat, kind in ((r"pub\.dev/packages/([A-Za-z0-9_]+)", "pub"), (r"npmjs\.com/package/((?:@[^/]+/)?[^/?#]+)", "npm"),
                      (r"pypi\.org/project/([^/?#]+)", "pypi")):
        m = re.search(pat, fm.get("url", ""))
        if m:
            return kind, m.group(1)
    return None


def check_package(kind, name):
    try:
        if kind == "pub":
            d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://pub.dev/api/packages/{name}", headers=UA), timeout=15))
            return {"version": d["latest"]["version"], "published": d["latest"].get("published", "")[:10],
                    "discontinued": bool(d.get("isDiscontinued"))}
        if kind == "npm":
            d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://registry.npmjs.org/{name}/latest", headers=UA), timeout=15))
            return {"version": d.get("version", ""), "discontinued": bool(d.get("deprecated"))}
        if kind == "pypi":
            d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://pypi.org/pypi/{name}/json", headers=UA), timeout=15))
            return {"version": d["info"]["version"], "discontinued": bool(d["info"].get("yanked"))}
    except Exception as e:
        return {"error": str(e)[:100]}
    return None


def project_uses():
    """How many rows of the project log link to each card (one row = one real project)."""
    log = open(os.path.join(ROOT, "projects", "README.md"), encoding="utf-8").read()
    uses = {}
    for row in (l for l in log.splitlines() if re.match(r"\| [۰-۹\d]{4}-", l)):
        for slug in set(re.findall(r"catalog/([a-z0-9._-]+)\.md", row)):
            uses[slug] = uses.get(slug, 0) + 1
    return uses


def promotions(results):
    uses = project_uses()
    up, down, try_ = [], [], []
    for slug, entry, notes, fm in results:
        n, v = uses.get(slug, 0), fm.get("verdict")
        if v == "trial" and n >= 2 and not notes:
            up.append(f"| [{slug}](../../catalog/{slug}.md) | 🧪 | {n} پروژه | برای ✅ بازبینی شود |")
        elif v == "adopt" and notes:
            down.append(f"| [{slug}](../../catalog/{slug}.md) | ✅ | {n} پروژه | {'؛ '.join(notes)} |")
        elif v == "assess" and n >= 1:
            try_.append(f"| [{slug}](../../catalog/{slug}.md) | 👀 | {n} پروژه | در پروژه استفاده شده؛ برای 🧪 بازبینی شود |")
    out = "", "## فهرست ارتقا و تنزل", "",
           "> از [دفتر پروژه‌ها: هر ردیف یک پروژه‌ی واقعی است. حکم را فقط بعد از خواندن تجربه‌ها و منبع اصلی عوض کن.", ""]
    rows = up + down + try_
    if rows:
        out += ["| کارت | حکم فعلی | استفاده | پیشنهاد |", "|---|---|---|---|"] + rows
    else:
        out.append("موردی نیست.")
    return out


def check_card(name, old):
    fm = front_matter(os.path.join(ROOT, "catalog", name))
    slug = fm.get("slug") or name[:-3]
    if fm.get("verdict") == "hold":
        return slug, None, None, fm
    entry, notes = {}, []
    if fm.get("repo", "").startswith("https://github.com/"):
        r = check_repo(fm["repo"])
        if r and r.get("error"):
            notes.append(f"گیت‌هاب جواب نداد ({r['error']})")
        elif r and r.get("missing"):
            notes.append(f"مخزن `{r['repo']}` دیگر وجود ندارد یا خصوصی شد")
        elif r:
            entry.update(r)
            prev = old.get(slug, {})
            if r["archived"]:
                notes.append("مخزن بایگانی (archived) شده")
            if r["release"] and prev.get("release") and r["release"] != prev["release"]:
                notes.append(f"نسخه‌ی تازه: {prev['release']} ← {r['release']} ({r['release_date']})")
            elif r["release"] and not prev:
                entry["first_seen"] = True
            card_lic = re.sub(r"[\s\-_.]", "", fm.get("license", "").lower())
            if r["license"] and r["license"] != "NOASSERTION" and re.sub(r"[\s\-_.]", "", r["license"].lower()) not in card_lic:
                notes.append(f"مجوز گیت‌هاب `{r['license']}` با کارت («{fm.get('license', '')}») نمی‌خواند")
            if prev.get("license") and r["license"] != prev["license"]:
                notes.append(f"مجوز عوض شد: {prev['license']} ← {r['license']}")
            if r["pushed"] and (TODAY - datetime.date.fromisoformat(r["pushed"])).days > STALE_DAYS:
                notes.append(f"بیش از ۱۲ ماه بدون تغییر (آخرین: {r['pushed']})")
    pkg = package_of(fm)
    if pkg:
        r = check_package(*pkg)
        if r and r.get("error"):
            notes.append(f"مخزن بسته‌ی {pkg[0]} جواب نداد ({r['error']})")
        elif r:
            entry["package"] = f"{pkg[0]}:{pkg[1]}"
            entry["package_version"] = r["version"]
            prev = old.get(slug, {}).get("package_version")
            if prev and prev != r["version"]:
                notes.append(f"نسخه‌ی تازه‌ی {pkg[0]} `{pkg[1]}`: {prev} ← {r['version']}")
            if r.get("discontinued"):
                notes.append(f"بسته‌ی {pkg[0]} `{pkg[1]}` کنار گذاشته (discontinued/deprecated) شده")
    url = fm.get("url", "")
    if url.startswith("http"):
        code = site_status(url)
        entry["site"] = code
        if code == 0 or code >= 400 and code not in (401, 403, 429):
            notes.append(f"سایت جواب نداد ({code or 'بدون پاسخ'}): {url}")

    return slug, entry, notes, fm


def main():
    dry = "--dry-run" in sys.argv
    if "--promotions" in sys.argv:   # offline: only the promotion list, from the project log
        cards = sorted(f for f in os.listdir(os.path.join(ROOT, "catalog")) if f.endswith(".md") and not f.startswith(("_", "README")))
        res = []
        for n in cards:
            fm = front_matter(os.path.join(ROOT, "catalog", n))
            res.append((fm.get("slug") or n[:-3], {}, [], fm))
        print("\n".join(promotions(res)))
        return
    old = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}
    new, findings, skipped = {}, [], []
    cards = sorted(f for f in os.listdir(os.path.join(ROOT, "catalog")) if f.endswith(".md") and not f.startswith(("_", "README")))
    gh_ready()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda n: check_card(n, old), cards))
    for slug, entry, notes, fm in results:
        if entry is None:
            skipped.append(slug)
            continue
        new[slug] = entry
        if notes:
            findings.append((slug, fm.get("verdict", ""), notes))

    lines = [f"# بررسی خودکار کارت‌ها — {TODAY}", "",
             f"> ساخته‌ی `scripts/check_updates.py` (بخش الف جاروی دو‌روزه). {len(cards) - len(skipped)} کارت بررسی شد؛ "
             f"{len(skipped)} کارت ⛔ عمداً بررسی نشد. هر مورد باید با منبع اصلی تأیید و بعد در کارت ثبت شود.", ""]
    if findings:
        lines += ["| کارت | حکم | چه چیزی عوض شده یا مشکوک است |", "|---|---|---|"]
        lines += [f"| [{s}](../../catalog/{s}.md) | {v} | {'؛ '.join(n)} |" for s, v, n in findings]
    else:
        lines.append("چیزی عوض نشده.")
    lines += promotions(results)
    report = "\n".join(lines) + "\n"
    if dry:
        print(report)
        return
    out = os.path.join(ROOT, "research", "inbox", f"{TODAY}-updates.md")
    open(out, "w", encoding="utf-8").write(report)
    json.dump(new, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"{len(findings)} cards with changes or problems -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
