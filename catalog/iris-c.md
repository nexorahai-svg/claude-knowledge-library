---
name: iris.c
slug: iris-c
category: image-generation
domains: [social-media]
verdict: assess
status: researched
summary: تولید تصویر در C خالص با FLUX.2 Klein و Z-Image-Turbo
use_when: "simple dependency-free local image generation ; Z-Image-Turbo test on one GPU"
how: "make cuda; download Z-Image-Turbo or FLUX.2 Klein 4B only; check each licence."
url: https://github.com/antirez/iris.c
repo: "https://github.com/antirez/iris.c"
license: "MIT (کد)؛ وزن‌ها مجوزهای جدا"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# iris.c

## چیست
✅ تولید تصویر با FLUX.2 Klein و Z-Image-Turbo در C خالص بدون وابستگی، با بک‌اند CUDA/Metal/ROCm؛ MIT برای کد. ⚠ مدل 9B غیرتجاری است و FLUX.3 مجوز Kommunity دارد؛ 4B مجوز آزادتری دارد. دانلود مدل ۱۲ تا ۳۰ گیگ.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: simple dependency-free local image generation؛ Z-Image-Turbo test on one GPU. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (کد)؛ وزن‌ها مجوزهای جدا (✅ از LICENSE مخزن؛ ستاره‌ها ۲,۰۶۸ در تاریخ بررسی).
- قیمت: رایگان.
- ✅ مدل‌های 9B غیرتجاری‌اند و FLUX.3 تحت FLUX Kommunity License است؛ ❓ مجوز 4B و Z-Image تأیید نشد.

## ریسک و هشدار
- سطح ریسک: low.
- README مقدار RAM می‌دهد نه VRAM.
- نویسنده معتبر (antirez)؛ مجوز مدل‌ها مختلف و بعضی غیرتجاری.
- ❓ VRAM واقعی روی ۸ گیگ، سرعت.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/antirez/iris.c
