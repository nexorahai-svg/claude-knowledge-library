---
name: مهارت‌های طراحی به سبک اپل (emilkowalski و dickwu)
slug: apple-design-skills
category: claude-code-tooling
domains: [apps, website]
verdict: trial
status: researched
summary: دو مهارت Claude برای بازبینی رابط و حرکت به سبک اپل؛ یکی MIT، یکی بدون مجوز
use_when: "reviewing UI and motion against Apple HIG principles for web ; needing spring motion, interruptible transitions or reduced-motion guidance"
how: "Trial first on a small task: use only emilkowalski/skills `apple-design` (MIT); treat dickwu/apple-design-skill as read-only learning because it has no licence (do not copy or modify) and its scripts folder is unread"
url: https://github.com/emilkowalski/skills/tree/main/skills/apple-design
repo: "https://github.com/emilkowalski/skills"
license: "MIT (emilkowalski)؛ بدون مجوز (dickwu)"
pricing: free
risk: low
sources: [S78, S77]
found_in: [batch-03]
last_checked: 2026-10-18
next_check: "2027-01-16"
---

# مهارت‌های طراحی به سبک اپل

## چیست
✅ `apple-design` در https://github.com/emilkowalski/skills (MIT، حدود ۴۷ هزار ستاره): اصول طراحی و حرکت اپل برای وب، بر اساس گفتارهای WWDC؛ حرکت فنری، اشاره، گذار قابل‌وقفه، مواد شفاف، تایپوگرافی، کاهش حرکت.
✅ https://github.com/dickwu/apple-design-skill (حدود ۱٬۵۰۰ ستاره): بازبینی رابط بر اساس HIG برای Flutter، Tauri، Electron و React Native؛ پوشه‌های `scripts` و `references` دارد. **فایل مجوز ندارد.**

## کی استفاده کنیم
🧭 مهارت emilkowalski برای حرکت و تعامل در وب و اپ‌های وبی. مهارت dickwu فقط برای خواندن و یاد گرفتن، تا مجوز اضافه شود.

## قیمت و مجوز
✅ هر دو رایگان در گیت‌هاب. ⚠️ بدون مجوز یعنی همه‌ی حقوق برای سازنده است؛ کپی در پروژه یا تغییرش آزاد نیست.

## ریسک و هشدار
⚠️ پوشه‌ی `scripts` در مخزن dickwu پیش از هر استفاده خوانده شود (این بار خوانده نشد ❓).
✅ سایت amirhosseinai.com این دو لینک رایگان را پشت فرم شماره تلفن گذاشته است؛ لینک مستقیم همین‌جاست و فرم لازم نیست.

## مرتبط
[طراحی اپ](../domains/apps/app-design.md#مهارت-آماده-برای-بازبینی-طراحی) · [S78](../sources/README.md#s78)
