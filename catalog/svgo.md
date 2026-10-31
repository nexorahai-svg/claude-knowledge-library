---
name: SVGO
slug: svgo
category: assets-media
domains: [website]
verdict: adopt
status: researched
summary: بهینه‌سازی و کوچک کردن فایل‌های SVG
use_when: "optimizing SVG icons and illustrations before publishing"
how: "npx svgo <file> (4.1.0, MIT); default settings may remove viewBox or ids that animations need, so check output visually"
url: https://github.com/svg/svgo
repo: "https://github.com/svg/svgo"
license: "MIT"
pricing: free
risk: low
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# SVGO

## چیست
✅ ابزار Node برای بهینه‌سازی SVG. حدود ۲۳ هزار ستاره؛ نسخه‌ی 4.1.0 (۲۰۲۶-۰۸-۲۴).

## کی استفاده کنیم
🧭 روی آیکون‌ها و تصویرسازی‌ها قبل از انتشار.

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
⚠️ تنظیمات پیش‌فرض ممکن است `viewBox` یا شناسه‌هایی را که انیمیشن به آن‌ها وابسته است حذف کند؛ خروجی را چشمی چک کن.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)
