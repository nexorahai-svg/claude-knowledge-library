---
name: antigravity-rtl
slug: antigravity-rtl
category: claude-code-tooling
domains: [claude-code]
verdict: assess
status: researched
summary: پچ راست‌به‌چپ برای برنامه‌ی Antigravity (فارسی، عربی، عبری) با فونت Vazirmatn
use_when: "Persian RTL in Antigravity IDE"
how: "Read bin/payload.js before running; keep the .bak backup."
url: https://github.com/mmnaderi/antigravity-rtl
repo: "https://github.com/mmnaderi/antigravity-rtl"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# antigravity-rtl

## چیست
✅ پچ راست‌به‌چپ برای برنامه‌ی Antigravity: فارسی، عربی و عبری با فونت Vazirmatn تأیید شد؛ MIT. ⚠ app.asar برنامه را بازبسته و در out/main.js تزریق می‌کند؛ فایل .bak و گزینه‌ی --restore وجود دارد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Persian RTL in Antigravity IDE. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲۸۲ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ روی لینوکس sudo npx لازم است، یعنی اجرای کد npm با دسترسی root.
- فایل‌های برنامهٔ دیگر را پچ می‌کند و لاگ می‌نویسد؛ فقط برای Antigravity کاربرد دارد.
- ❓ اجرای واقعی، سازگاری با نسخه‌های جدید.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/mmnaderi/antigravity-rtl
