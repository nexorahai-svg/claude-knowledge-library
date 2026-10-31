---
name: NeMo-Speech.cpp
slug: nemo-speech-cpp
category: audio-voice
domains: [social-media]
verdict: assess
status: researched
summary: اجرای رسمی انویدیا برای مدل‌های Nemotron Speech و Parakeet به‌صورت C++/ggml
use_when: "official NVIDIA local ASR runtime ; Arabic ASR/TTS ; streaming transcription"
how: "Check each model card for Arabic/fa support and licence (NVIDIA Open Model License may apply) before use."
url: https://github.com/NVIDIA/NeMo-Speech.cpp
repo: "https://github.com/NVIDIA/NeMo-Speech.cpp"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# NeMo-Speech.cpp

## چیست
✅ اجرای رسمی انویدیا (C++/ggml) برای مدل‌های Nemotron Speech و Parakeet؛ کد Apache-2.0. ✅ عربی فقط برای TTS مدل MagpieTTS در docs/tts/configuration.md آمده؛ ❓ ASR عربی تأیید نشد و فارسی پیدا نشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: official NVIDIA local ASR runtime؛ Arabic ASR/TTS؛ streaming transcription. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۲۱۸ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ❓ مجوز وزن‌ها و VRAM ذکر نشده است.
- منبع رسمی و امن؛ مجوز مدل‌ها (احتمالاً NVIDIA Open Model License) خوانده نشد.
- ❓ پشتیبانی فارسی، مجوز وزن‌ها، VRAM.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/NVIDIA/NeMo-Speech.cpp
