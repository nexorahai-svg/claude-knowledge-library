---
name: tinbase
slug: tinbase
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: بک‌اند سازگار با Supabase در یک پردازش با PGlite بدون Docker (آلفا)
use_when: "Local Supabase-compatible dev without Docker ; offline demos and tests of supabase-js code"
how: "npx tinbase start in a scratch folder (never for production data)"
url: https://github.com/tinbase/tinbase
repo: "https://github.com/tinbase/tinbase"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# tinbase

## چیست
✅ بک‌اند سازگار با Supabase در یک پردازش (PGlite/Postgres WASM) بدون Docker که supabase-js را بدون تغییر می‌پذیرد. ✅ README خودش هشدار Alpha می‌دهد. ❓ سازمان tinbase تازه است (۲ مخزن، ۱۰۰٪ جدید).

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Local Supabase-compatible dev without Docker؛ offline demos and tests of supabase-js code. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۳۵۴ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- Alpha و سازمان تازه؛ فقط برای توسعه محلی. سازگاری کامل با Supabase ادعای خودشان است.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/tinbase/tinbase
