---
name: Agent Skills (Addy Osmani)
slug: addy-agent-skills
category: claude-code-tooling
domains: [apps, website]
verdict: assess
status: researched
summary: پلاگین مهارت‌های مهندسی برای عامل‌های کدنویسی؛ چرخه‌ی spec، plan، build، test، review، ship با ۹ فرمان
use_when: "needing a disciplined spec -> plan -> build -> test -> review flow in a code project ; web performance audit of a site"
how: "Trial first on a small task: install the plugin from github.com/addyosmani/agent-skills after reading hooks/; use /spec, /plan, /test, /webperf; call /agent-skills:review (built-in /review clashes); avoid /build auto without approval"
url: https://github.com/addyosmani/agent-skills
repo: https://github.com/addyosmani/agent-skills
license: MIT
pricing: free
risk: medium
sources: [S181, S189]
found_in: [instagram]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Agent Skills (Addy Osmani)

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) نسخه‌ی 0.6.15 (۲۰۲۶-۱۰-۳۱): بررسی کلید مرحله‌شده در skill امنیتی دیگر خود کلید را چاپ نمی‌کند؛ دو اشکال simplify-ignore که می‌توانست کد محافظت‌شده را خراب کند رفع شد؛ آستانه‌ی کنتراست اصلاح شد: https://github.com/addyosmani/agent-skills/releases
✅ (README و GitHub API، ۲۰۲۶-۱۰-۲۷) مجموعه‌ی مهارت (skill) برای عامل‌های کدنویسی که روش کار مهندسان باتجربه را بسته‌بندی می‌کند: تعریف، برنامه، ساخت تکه‌تکه، آزمون، بازبینی و انتشار. ۹ فرمان (`/spec`، `/plan`، `/build`، `/test`، `/constraints`، `/review`، `/webperf`، `/code-simplify`، `/ship`) و ۲۵ مهارت که با موضوع کار خودکار فعال می‌شوند. برای Claude Code، Codex، Gemini و OpenCode. نسخه‌ی 0.6.13 (۲۰۲۶-۱۰-۱۳)، حدود ۱۱۰ هزار ستاره، MIT. سازنده Addy Osmani (مدیر مهندسی پیشین Chrome در گوگل).

✅ یادداشت: استاندارد Agent Skills که این مجموعه بر آن بنا شده از ۲۰۲۶-۱۰-۲۲ مال AAIF (Linux Foundation) است، نه Anthropic ([S189](../sources/README.md#s189)).

## کی استفاده کنیم
🧭 برای پروژه‌های کد (اپ، سایت) وقتی روند منظم spec ← plan ← آزمون می‌خواهیم. با روش‌های خود کتابخانه ([آزمون اپ](../domains/apps/app-testing.md)، [بررسی](../domains/claude-code/verification.md)) هم‌پوشانی دارد؛ اول روی یک کار کوچک امتحان شود.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
متوسط: hook دارد (اسکریپت‌های shell در `hooks/`): شروع جلسه، کش WebFetch با `curl` در `.claude/sdd-cache/` پروژه، و فهرست نادیده‌گیری برای ساده‌سازی؛ پیش از نصب فایل‌ها را بخوان. فرمان `/review` با فرمان داخلی هم‌نام است (شکل کامل: `/agent-skills:review`). `/build auto` همه‌ی کارها را پس از یک تأیید خودکار اجرا می‌کند؛ با قانون «کار بزرگ با تأیید» هم‌خوان نگه دار.

## مرتبط
[S181](../sources/README.md#s181) · [Ponytail](ponytail.md) · [Graphify](graphify.md)
