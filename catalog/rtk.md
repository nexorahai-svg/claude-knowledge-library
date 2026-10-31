---
name: rtk
slug: rtk
category: cost-tokens
domains: [claude-code]
verdict: assess
status: researched
summary: فشرده‌سازی خروجی دستورات شل پیش از رسیدن به مدل برای کم‌کردن توکن
use_when: "reducing token use of noisy command output (git, tests, logs) in Claude Code"
how: "brew install rtk or install.sh (read first); rtk init for the Claude hook; rtk gain shows savings; leave rtk-proxy off"
url: https://github.com/rtk-ai/rtk
repo: "https://github.com/rtk-ai/rtk"
license: "Apache-2.0 (CLI)؛ rtk-engine و rtk-proxy تحت BUSL-1.1"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# rtk

## چیست
✅ ابزار CLI تک‌فایل که خروجی دستورات شل را پیش از رسیدن به مدل فشرده می‌کند (ادعای ۶۰ تا ۹۰ درصد)، با هوک PreToolUse برای Claude Code و عامل‌های دیگر؛ نسخهٔ جدید یک rtk-proxy اختیاری برای ترافیک API دارد. ✅ telemetry به‌صورت پیش‌فرض خاموش و با rtk telemetry enable فعال می‌شود.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: reducing token use of noisy command output (git, tests, logs) in Claude Code. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (CLI)؛ rtk-engine و rtk-proxy تحت BUSL-1.1 (✅ از LICENSE مخزن؛ ستاره‌ها ۸۵,۰۵۵ در تاریخ بررسی).
- قیمت: رایگان.
- ✅ طبق بررسی: CLI زیر Apache-2.0 است ولی بخش‌های rtk-engine و rtk-proxy تحت BUSL-1.1 هستند (مجوز محدود)؛ پیش از استفاده‌ی تجاری متن را بخوانید.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ نصب README با curl|sh هم ممکن است؛ فایل را بخوانید.
- ❓ درصد صرفه‌جویی ۶۰ تا ۹۰ را تأیید نکردیم.
- هوک روی تمام فرمان‌های شل می‌نشیند؛ ۱۶۳۶ issue باز؛ مجوز دوگانه (BUSL برای بخشی)؛ ادعای درصد صرفه‌جویی تأییدنشده؛ سازمان تازه (۲۰۲۶-۰۱).
- ❓ درصد صرفه‌جویی تست نشد؛ کد proxy و engine و جزئیات BUSL خوانده نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/rtk-ai/rtk
