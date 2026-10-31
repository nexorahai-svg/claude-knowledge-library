---
name: openasr
slug: openasr
category: audio-voice
domains: [social-media]
verdict: assess
status: researched
summary: ASR محلی با هسته‌ی Rust و خروجی SRT/VTT/JSON با زمان کلمات
use_when: "local subtitle generation SRT/VTT ; offline transcription CLI"
how: "Prefer building from source over install.sh (curl | sh in README); verify no network calls."
url: https://github.com/QuintinShaw/openasr
repo: "https://github.com/QuintinShaw/openasr"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# openasr

## چیست
✅ ASR محلی با هستهٔ Rust و موتور ggml، خروجی SRT/VTT/JSON با زمان کلمات، زیرنویس زنده و API محلی؛ Apache-2.0. ادعا می‌کند بدون تماس شبکه است. نسخهٔ لینوکس دسکتاپ هنوز نیامده. ❓ پشتیبانی فارسی بررسی نشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: local subtitle generation SRT/VTT؛ offline transcription CLI. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۲۹۱ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ نصب README با curl|sh از https://dl.openasr.org/install.sh است (یا build/Homebrew).
- ❓ «بدون تله‌متری» ادعای README است. مدل‌ها مجوز خودشان را دارند. نسخه‌ی دسکتاپ لینوکس هنوز نیامده (CLI کار می‌کند).
- ❓ پشتیبانی فارسی تأیید نشد.
- README دستور curl | sh دارد؛ پیش‌انتشار (pre-v1)؛ ادعای بدون تلمتری فقط از README.
- ❓ زبان‌های فارسی، install.sh، مجوز بسته‌های مدل.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/QuintinShaw/openasr
