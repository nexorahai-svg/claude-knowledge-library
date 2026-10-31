---
name: nono
slug: nono
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: ران‌تایم امنیتی عامل‌ها با sandbox سطح کرنل و تزریق اعتبارنامه بیرون از عامل
use_when: "running Claude Code/agents with restricted file+network access ; keeping API keys out of the agent"
how: "install per README (brew/binary); nono run -- claude with a profile; test on a scratch project first"
url: https://github.com/nolabs-ai/nono
repo: "https://github.com/nolabs-ai/nono"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# nono

## چیست
✅ ران‌تایم امنیتی عامل‌ها با sandbox در سطح کرنل، تزریق اعتبارنامه بیرون از عامل، و ممیزی؛ برای Claude Code، Codex و دیگران؛ باینری تک‌فایل بدون root، Linux/macOS/WSL2. ✅ README سازنده را همان تیم Sigstore معرفی می‌کند.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: running Claude Code/agents with restricted file+network access؛ keeping API keys out of the agent. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۴,۷۶۴ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ اولین روش نصب README دستور curl https://nono.sh/install.sh | sh است؛ فایل را بخوانید.
- ✅ پروژه هنوز پیش از نسخه‌ی ۱.۰ است.
- قبل از ۱.۰ و API ناپایدار؛ ۲۸۲ issue باز؛ ادعای «تیم Sigstore» تأیید مستقل نشد؛ سازمان تازه (۲۰۲۶-۰۶، ۵۲ دنبال‌کننده).
- ❓ هسته و پروفایل‌های sandbox بررسی نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/nolabs-ai/nono
