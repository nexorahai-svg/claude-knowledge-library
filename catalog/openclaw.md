---
name: OpenClaw
slug: openclaw
category: agents-memory
domains: [claude-code, security]
verdict: assess
status: researched
summary: عامل شخصی خودمیزبان که از پیام‌رسان‌ها فرمان می‌گیرد؛ دسترسی پوسته و حساب‌ها، هشدارهای امنیتی زیاد
url: https://github.com/openclaw/openclaw
repo: "https://github.com/openclaw/openclaw"
license: "MIT"
pricing: free
risk: high
sources: [S158, S198]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# OpenClaw

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) برچسب v2026.10.8 (آخرین push ۲۰۲۶-۱۰-۲۷؛ تاریخ انتشار برچسب ۲۰۲۶-۱۰-۲۷ طبق https://api.github.com/repos/openclaw/openclaw/releases/tags/v2026.10.8)؛ MIT بی‌تغییر.
✅ عامل شخصی (MIT، حدود ۳۹۳ هزار ستاره، به‌روزرسانی روزانه) که واتس‌اپ، تلگرام و اسلک را به مدل و ابزار با دسترسی پوسته و فایل وصل می‌کند. ۷۳ اطلاعیه‌ی امنیتی در مخزن؛ CVE-2026-100567 (SSRF در gateway، رفع در 2026.8.1) 🧭.

## هشدار امنیتی
✅ (NVD، ۲۰۲۶-۱۰-۲۸) CVE-2026-53831: دور زدن allowlist در `system.run` با گسترش shell، پیش از 2026.5.18. CVE-2026-41396 و CVE-2026-41336: فایل `.env` فضای کار مسیر پلاگین‌ها و hookهای همراه را عوض می‌کرد، پیش از 2026.3.31. فقط نسخه‌ی تازه ([S198](../sources/README.md#s198)).

## کی استفاده کنیم
🧭 کار ما را Claude Code می‌کند. اگر روزی امتحان شد: فقط روی ماشین جدا، gateway هرگز روی اینترنت، skill ناخوانده از ClawHub نصب نکن، نصب `curl | bash` نه.

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v2026.10.9 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
