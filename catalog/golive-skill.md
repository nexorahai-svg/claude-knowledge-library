---
name: golive-skill
slug: golive-skill
category: hosting-deploy
domains: [website, apps, security]
verdict: hold
status: researched
summary: مهارت بردن اپ به production با حساب‌های خود کاربر؛ توکن‌ها plaintext ذخیره می‌شوند
use_when: "(hold) agent-driven deploy to Vercel/Netlify/Supabase ; reference for deploy checklist ideas"
how: "do not install; read docs/TRUST.md only as a design reference"
url: https://github.com/mikehasa/golive-skill
repo: "https://github.com/mikehasa/golive-skill"
license: "MIT"
pricing: free
risk: high
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# golive-skill

## چیست
✅ Agent Skill برای بردن اپ به production (هاست، دیتابیس، دامنه، ایمیل، پرداخت) با حساب‌های خود کاربر؛ هر نوشتن نیاز به تأیید طرح دارد. ✅ نسخه 0.1.0-alpha؛ README خودش می‌گوید توکن‌ها در فایل plaintext با mode 0600 ذخیره می‌شوند و ایجنتی که لاگین باشد می‌تواند بدون golive هم بنویسد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: (hold) agent-driven deploy to Vercel/Netlify/Supabase؛ reference for deploy checklist ideas. وضعیت: ⛔ فعلاً استفاده نکنید.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۱,۳۲۶ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: high.
- ⚠ اعتبارنامه‌ها به‌صورت متن ساده در ~/.config/golive/credentials با mode 0600 ذخیره می‌شوند.
- نسخه 0.1.0-alpha.9.
- یک مشارکت‌کننده، سه هفته سن، ۱۳۲۶ ستاره (مشکوک به رشد سریع) و دسترسی به توکن‌های production و DNS. هولد تا بلوغ بیشتر.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/mikehasa/golive-skill
