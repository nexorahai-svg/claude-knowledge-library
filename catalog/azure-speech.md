---
name: Azure AI Speech (صدای عصبی)
slug: azure-speech
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: صدای ابری با فارسی (fa-IR) و عربی امارات (ar-AE)؛ تنها موتوری که طول دقیق صدا را می‌گیرد، با زمان هر کلمه
url: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/
repo: ""
license: "سرویس تجاری Microsoft"
pricing: freemium
risk: low
sources: [S136, S155]
found_in: []
last_checked: 2026-10-25
next_check: "2026-11-24"
---

# Azure AI Speech

## چیست
✅ (Microsoft Learn، ۲۰۲۶-۱۰-۲۲) صداهای عصبی استاندارد: فارسی `fa-IR` (Dilara، Farid)، عربی امارات `ar-AE` (Fatima، Hamdan)، عربی سعودی `ar-SA` (Zariyah، Hamed) و ۱۷ گونه‌ی عربی. **`mstts:audioduration` طول دقیق صدا را تعیین می‌کند** (بین ۰٫۵ تا ۲ برابر طول طبیعی، حداکثر ۳۰۰ ثانیه)؛ `prosody rate` بین ۰٫۵ تا ۲؛ رویداد `WordBoundary` زمان و طول هر کلمه را می‌دهد.

## قیمت و مجوز
✅ نیم میلیون نویسه در ماه رایگان. ❓ قیمت هر میلیون نویسه در صفحه خوانده نشد.

## کی استفاده کنیم
🧪 عربی خلیجی و هر جا صدا باید دقیقاً به طول یک کلیپ ثابت (مثلاً تصویر هوش مصنوعی) برسد. صداها HD نیستند؛ برای طبیعی‌ترین گفتار [ElevenLabs](elevenlabs-tts.md).


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
🧭 قیمت حدود ۱۵ دلار برای هر میلیون نویسه؛ ✅ ۵۰۰ هزار نویسه در ماه رایگان. صداهای fa-IR (دلارا، فرید) و ar-AE (فاطمه، حمدان) همه Standard‌اند، نه HD. پانویس ۳ صداهای فارسی بریده خوانده شد ❓ (اگر خبر بازنشستگی باشد مهم است).

## مرتبط
[ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [صداگذاری](../domains/social-media/ai-voice.md) · [S136](../sources/README.md#s136)
