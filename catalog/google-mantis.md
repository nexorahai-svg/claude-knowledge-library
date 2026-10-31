---
name: mantis
slug: google-mantis
category: claude-code-tooling
domains: [claude-code, security]
verdict: hold
status: researched
summary: مهارت‌ها و هارنس برای مدل‌سازی تهدید و پژوهش آسیب‌پذیری؛ کد تولیدشده را اجرا می‌کند
use_when: "studying a secure-development skill method (read only)"
how: "read skills/ only; do not run the harness outside a sandbox"
url: https://github.com/google/mantis
repo: "https://github.com/google/mantis"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# mantis

## چیست
✅ مهارت‌ها و هارنس ADK برای مدل‌سازی تهدید، پژوهش آسیب‌پذیری، بازتولید و وصله. ✅ README هشدار می‌دهد که کد تولیدشده را اجرا می‌کند و فقط در محیط ایزوله باشد؛ اسکن PR هنوز تست‌نشده است.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: studying a secure-development skill method (read only). وضعیت: ⛔ فعلاً استفاده نکنید.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۲,۶۷۵ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: high.
- ⚠ README: کد تولیدشده را اجرا می‌کند؛ فقط در محیط ایزوله. اکشن را برای مسدودکردن merge به کار نبرید.
- ❓ هارنس و اکشن اجرا یا خوانده نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/google/mantis
