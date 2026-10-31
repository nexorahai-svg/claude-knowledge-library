---
name: speech.cpp
slug: speech-cpp
category: audio-voice
domains: [social-media]
verdict: assess
status: researched
summary: دستور و کتابخانه‌ی C++ برای TTS، ASR و VAD روی ggml بدون CUDA
use_when: "small local ASR with Persian (fa) ; local OpenAI-compatible speech server ; CPU/Vulkan speech without CUDA"
how: "Use qwen3-asr-0.6b (Apache-2.0 weights) via the speech CLI; avoid Drama-3 TTS for commercial work."
url: https://github.com/nyosegawa/speech.cpp
repo: "https://github.com/nyosegawa/speech.cpp"
license: "MIT"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# speech.cpp

## چیست
✅ دستور و کتابخانه‌ی C++ برای TTS، ASR، VAD و جداسازی گوینده روی ggml؛ کد MIT. README زبان فارسی/عربی را فهرست نمی‌کند؛ ✅ کارت HF مدل Qwen3-ASR-0.6B (Apache-2.0) فارسی و عربی را فهرست کرده است. ✅ بک‌اندها فقط Metal، Vulkan و CPU هستند (CUDA ندارد).

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: small local ASR with Persian (fa)؛ local OpenAI-compatible speech server؛ CPU/Vulkan speech without CUDA. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲۱۹ در تاریخ بررسی).
- قیمت: رایگان.
- ✅ Drama-3: Fish Audio Community License 1.0 (تجاری زیر ۵۰۰ هزار دلار در سال؛ سرویس کلون صدا مجوز جدا می‌خواهد). Irodori v4.1-Small: MIT با محدودیت‌های اخلاقی؛ v4-Large: Gemma Terms.

## ریسک و هشدار
- سطح ریسک: low.
- ⚠ سرور محلی روی 127.0.0.1 احراز هویت ندارد.
- یک نگه‌دارنده؛ وزن‌های مختلف مجوز متفاوت دارند و Drama-3 غیرتجاری است.
- ❓ کیفیت فارسی در عمل، نسخه‌های Linux/CUDA، فایل‌های دانلودشدهٔ مدل.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/nyosegawa/speech.cpp
