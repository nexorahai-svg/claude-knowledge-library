---
name: ElevenLabs Scribe
slug: elevenlabs-scribe
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: سرویس ابری تبدیل گفتار به متن با رده‌ی دقت اعلام‌شده برای فارسی
use_when: "transcribing Persian audio when faster-whisper is not accurate enough ; speech-to-text with word timestamps and speakers"
how: "Trial first on a small task: use ElevenLabs Scribe v2 API ($0.22 per hour, Persian high-accuracy tier, word timestamps, up to 32 speakers, 3 GB files); audio goes to an external service so never send sensitive recordings"
url: https://elevenlabs.io/docs/overview/capabilities/speech-to-text
repo: ""
license: "سرویس تجاری"
pricing: paid
risk: medium
sources: [S45, S155]
found_in: []
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# ElevenLabs Scribe

## چیست
✅ «Persian (fas)» در رده‌ی دقت بالا (خطا بین ۵ تا ۱۰٪)؛ Scribe v2 با برچسب زمانی کلمه.

## کی استفاده کنیم
🧭 اگر faster-whisper برای فارسی کافی نبود.

## قیمت و مجوز
✅ قیمت API (https://elevenlabs.io/pricing/api، ۲۰۲۶-۱۰-۳۰): Scribe v2 ‏۰٫۲۲ دلار در ساعت (بیش از ۹۰ زبان)؛ Scribe v2 Realtime ‏۰٫۳۹ دلار در ساعت. «Zero Retention Mode» در همان صفحه فقط کنار مدل بالینی (HIPAA) آمده؛ برای Scribe v2 عمومی صریح نیست ❓.

## ریسک و هشدار
⚠️ صدا به سرویس بیرونی می‌رود.


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ Scribe v2: ‏۰٫۲۲ دلار در ساعت؛ فارسی «دقت بالا» (۵ تا ۱۰٪ خطا)، عربی «خوب» (۱۰ تا ۲۰٪)؛ تا ۳۲ گوینده؛ فایل تا ۳ گیگ.

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [S45](../sources/README.md#s45)
