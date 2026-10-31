---
name: open-edit
slug: veed-open-edit
category: video
domains: [social-media, claude-code]
verdict: assess
status: researched
summary: CLI و مهارت ایجنت برای ساخت و ویرایش ویدیو روی VEED
use_when: "agent-driven video edit pipeline with captions"
how: "npx @veedstudio/openedit-cli --help (cloud login needed; read before running)."
url: https://github.com/veedstudio/open-edit
repo: "https://github.com/veedstudio/open-edit"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# open-edit

## چیست
✅ ابزار خط فرمان و مهارت agent برای ساخت و ویرایش ویدیو (زیرنویس، موشن، اسلاید) روی VEED؛ Apache-2.0. ⚠ ورود با OAuth در VEED لازم است، پس بخشی ابری است.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: agent-driven video edit pipeline with captions. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۱,۷۵۴ در تاریخ بررسی).
- قیمت: بخش رایگان و بخش پولی یا اعتباری.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ رونویسی میزبانی‌شده‌ی VEED حساب veed.io می‌خواهد و فایل شما را آپلود می‌کند (رایگان حدود ۱۰ دقیقه در ماه)؛ WhisperX محلی از این آپلود جلوگیری می‌کند.
- وابسته به حساب و سرویس ابری VEED؛ چه داده‌ای آپلود می‌شود را نخواندیم.
- ❓ محدودیت‌های رایگان، زبان فارسی، مسیر دادهٔ ابری.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/veedstudio/open-edit
