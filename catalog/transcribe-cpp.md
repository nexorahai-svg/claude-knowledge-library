---
name: transcribe.cpp
slug: transcribe-cpp
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: کتابخانه‌ی C/C++ تشخیص گفتار روی ggml با چندین خانواده مدل و بک‌اند CUDA/Vulkan/Metal
use_when: "local multi-model STT for Persian/Arabic subtitles ; compare ASR models by WER on fa ; GGUF speech models on 8 GB GPU"
how: "Read docs/models/*.md for the model's fa row and its own licence; build with CUDA preset in a separate dir; test fa WER on own clips before trusting."
url: https://github.com/handy-computer/transcribe.cpp
repo: "https://github.com/handy-computer/transcribe.cpp"
license: "MIT"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# transcribe.cpp

## چیست
✅ کتابخانه‌ی C/C++ تشخیص گفتار روی ggml با ۱۶ خانواده مدل و بیش از ۶۰ نوع و بک‌اند CUDA/Vulkan/Metal؛ کد MIT. ✅ WER فارسی فقط در docs/models/*.md آمده: نوع‌های بزرگ Whisper حدود ۳۰ تا ۳۸٪، qwen3-asr-0.6b حدود ۵۰٫۳٪، whisper-small حدود ۵۸٪، whisper-base حدود ۸۸٪. مدل‌های عربی هم هست.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: local multi-model STT for Persian/Arabic subtitles؛ compare ASR models by WER on fa؛ GGUF speech models on 8 GB GPU. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲,۱۱۳ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ❓ مجوز وزن‌ها و مصرف VRAM ذکر نشده است.
- سازمان تازه (ژانویه ۲۰۲۶)؛ کد خوانده شد، چیزی نصب نشد؛ مجوز وزن هر مدل باید جدا چک شود.
- ❓ وزن مدل‌ها و مجوزشان، دقت واقعی فارسی روی ویدیوی خودمان، مصرف VRAM.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/handy-computer/transcribe.cpp

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
