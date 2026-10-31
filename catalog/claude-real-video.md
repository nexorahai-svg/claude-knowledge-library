---
name: claude-real-video
slug: claude-real-video
category: video
domains: [social-media, claude-code]
verdict: assess
status: researched
summary: بسته‌ی پایتون که از ویدیو فریم و رونوشت Whisper می‌سازد تا Claude آن را «ببیند»
use_when: "let Claude review a rendered reel (frames + transcript)"
how: "pip install in a venv after reading the package; pick --whisper-model turbo/medium for Persian."
url: https://github.com/HUANGCHIHHUNGLeo/claude-real-video
repo: "https://github.com/HUANGCHIHHUNGLeo/claude-real-video"
license: "MIT"
pricing: freemium
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# claude-real-video

## چیست
✅ بسته‌ی پایتون (PyPI) که از ویدیو فریم‌های بدون تکرار به‌همراه رونوشت Whisper می‌سازد تا Claude «ببیند»؛ MIT. می‌تواند برای بازبینی ریلز تولیدشده مفید باشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: let Claude review a rendered reel (frames + transcript). وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲,۲۷۴ در تاریخ بررسی).
- قیمت: بخش رایگان و بخش پولی یا اعتباری.
- ✅ افزونه‌ی پولی crv Pro (۲۹ دلار) هم وجود دارد.

## ریسک و هشدار
- سطح ریسک: low.
- ⚠ ورودی URL با yt-dlp است و گزینه‌ی --cookies-from-browser دارد (در معرض قرار گرفتن اعتبارنامه).
- Whisper turbo حدود ۶ گیگ و ۱٫۶ گیگ دانلود دارد.
- ❓ install-skill.sh خوانده نشد.
- نصب از PyPI و اسکریپت install-skill.sh (نخوانده کامل).
- ❓ کیفیت Whisper فارسی، رفتار شبکه.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/HUANGCHIHHUNGLeo/claude-real-video
