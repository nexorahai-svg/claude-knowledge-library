---
name: Higgs Audio v3 TTS (Boson AI)
slug: higgs-audio-v3
category: audio-voice
domains: [social-media, website]
verdict: trial
status: researched
summary: بهترین صدای فارسی محلیِ آزموده (CER ۰ تا ۵٪، دو برابر سریع‌تر از پخش روی RTX 4060)؛ ولی فقط غیرتجاری، کار مشتری مجوز Boson AI می‌خواهد
url: https://www.boson.ai
repo: ""
license: "پژوهشی و غیرتجاری؛ استفاده‌ی تجاری با قرارداد جدا از Boson AI (contact@boson.ai)"
pricing: free
risk: medium
sources: [S136]
found_in: [یک پروژه‌ی مشتری, video-pipeline]
last_checked: 2026-10-22
next_check: "2027-01-21"
---

# Higgs Audio v3 TTS (Boson AI)

## چیست
مدل ۴ میلیاردی تبدیل متن به گفتار با شبیه‌سازی صدا. ما آن را به شکل GGUF (`higgs-audio-v3-tts-4b-q8_0.gguf`) با **audio.cpp** اجرا می‌کنیم؛ همان ابزاری که MOSS-TTS Local را هم می‌خواند (`--family higgs_audio_tts | moss_tts_local`).

## آزمون (۲۰۲۶-۱۰-۲۲، خط تولید ویدیو)
🔬 (پروژه‌ی video-pipeline، دفتر پروژه‌ها) RTX 4060 با ۸ گیگابایت، Vulkan. چهار جمله‌ی فارسی تبلیغی، مرجع بلند ۳۳ ثانیه‌ای، سنجش با faster-whisper و CER:

| موتور | CER فارسی | سرعت | نظر کاربر |
|---|---|---|---|
| MOSS Local (پایتون)، مرجع کوتاه ۷ ثانیه، تنظیم پیش‌فرض | تا ۱۹٪ پیش از تکرار | حدود ۶ تا ۱۰ برابر کندتر از پخش | «فارسی بسیار بد» |
| MOSS Local، مرجع بلند، `temperature 0.8`، `top_k 30` | ۰ تا ۷٪ | همان | — |
| **Higgs v3 q8_0 با audio.cpp** | **۰ تا ۵٪** | حدود ۰٫۵ برابر زمان پخش (پس از بار شدن مدل) | ✅ **انتخاب کاربر** |

- ⚠️ MOSS با audio.cpp روی کارت ۸ گیگ جا نمی‌شود، حتی `q4_k` (بافر ۱ گیگی کدک صدا خطای ErrorOutOfDeviceMemory می‌دهد)؛ MOSS را با نسخه‌ی پایتونی و `OFFLOAD` اجرا کن.
- ⚠️ Higgs روی پردازنده در این ساخت audio.cpp خطای «illegal instruction» داد (یک پروژه‌ی مشتری)؛ فقط کارت گرافیک.
- دستور: `audiocpp_cli --task clon --family higgs_audio_tts --model <gguf> --backend vulkan --device 0 --seed 7 --language fa --voice-ref <ref.wav> --text "…" --out out.wav`

## مجوز
⚠️ فقط پژوهشی و غیرتجاری. برای ویدیوی مشتری یا محصول، پیش از انتشار قرارداد تجاری با Boson AI لازم است؛ جایگزین آزاد: [MOSS-TTS](moss-tts.md) با مرجع بلند، یا موتور میزبانی‌شده ([ElevenLabs](elevenlabs-tts.md)، [Azure Speech](azure-speech.md)).

## مرتبط
[خط تولید ویدیوی چندزبانه](../domains/social-media/multilang-video-pipeline.md) · [MOSS-TTS](moss-tts.md) · [OmniVoice](omnivoice.md)
