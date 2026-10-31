---
name: OpenFile
slug: openfile
category: assets-media
domains: [website, security]
verdict: hold
status: researched
summary: ابزارهای فایل در مرورگر با WebAssembly؛ پروژه‌ی تک‌نفره‌ی دوروزه با ادعای بازاریابی، نگه‌داشته شد
use_when: "Evaluating browser-only file converters ; deciding whether an unknown web file tool is safe for client files"
how: "Do not use with client files; prefer established tools such as ffmpeg.wasm; the zero-upload claim is unverified"
url: https://openfile-studio.vercel.app
repo: "https://github.com/aniruddhaadak80/OpenFile"
license: "MIT"
pricing: free
risk: medium
sources: [S206]
found_in: [batch-25]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# OpenFile

## چیست
✅ (۲۰۲۶-۱۰-۳۰) ابزارهای فایل در مرورگر با WebAssembly، PWA، MIT، ۱ ستاره، ساخته‌شده ۲۰۲۶-۱۰-۲۸. توضیح مخزن «۳۰۰+ ابزار» و نشان README «۴۲۷ ابزار در ۲۳ استودیو» می‌گوید (ناهمخوان).
❓ ادعای «بدون آپلود» راستی‌آزمایی نشد.

## کی استفاده کنیم
⛔ فعلاً نه؛ به‌جای آن از ابزارهای جاافتاده مثل ffmpeg.wasm استفاده کن.

## قیمت و مجوز
MIT، رایگان.

## ریسک و هشدار
پروژه‌ی یک‌نفره‌ی دوروزه با ادعاهای بازاریابی؛ هرگز با فایل مشتری.

## مرتبط
- https://github.com/aniruddhaadak80/OpenFile
- https://openfile-studio.vercel.app
