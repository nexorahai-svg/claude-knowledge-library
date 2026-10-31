---
name: VoxCPM2 (OpenBMB)
slug: voxcpm2
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: مدل TTS دو میلیاردی Apache-2.0 با ۳۰ زبان (عربی دارد، فارسی ندارد)، خروجی ۴۸ کیلوهرتز، طراحی و شبیه‌سازی صدا؛ حدود ۸ گیگ VRAM
use_when: "Arabic voice-over for Dubai store or site videos where Persian is not needed ; voice design from a text description ; cloning a licensed own voice from a short clip"
how: "Trial first on a small task: pip install voxcpm in a venv, model downloads from Hugging Face; about 8 GB VRAM so use a rented GPU first; clone only voices you have written consent for; use MOSS-TTS for Persian"
url: https://huggingface.co/openbmb/VoxCPM2
repo: "https://github.com/OpenBMB/VoxCPM"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# VoxCPM2 (OpenBMB)

## چیست
- ✅ مدل TTS بدون tokenizer (انتشار-خودبازگشتی)، ۲ میلیارد پارامتر، آموزش‌دیده روی بیش از ۲ میلیون ساعت گفتار، خروجی ۴۸ کیلوهرتز. منبع: [کارت Hugging Face](https://huggingface.co/openbmb/VoxCPM2) (به‌روزرسانی ۲۰۲۶-۰۸-۱۸، حدود ۹۹۷ هزار دانلود، ۱٫۷ هزار لایک) و مخزن [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) (Apache-2.0، ۴۰٫۸ هزار ستاره، push ۲۰۲۶-۱۰-۰۸).
- ✅ آخرین release مخزن: 2.0.3 (۲۰۲۶-۰۵-۱۱).
- ✅ ۳۰ زبان بدون نیاز به برچسب زبان: عربی، عبری، هندی و ترکی هست؛ فارسی و اردو **نیست**. (فهرست کارت: Arabic, Burmese, Chinese, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Khmer, Korean, Lao, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swahili, Swedish, Tagalog, Thai, Turkish, Vietnamese + لهجه‌های چینی.)
- ✅ ویژگی‌ها: طراحی صدا از توصیف متنی (توصیف داخل پرانتز اول متن)، شبیه‌سازی صدا از کلیپ کوتاه با کنترل سبک، شبیه‌سازی دقیق با متن مرجع، آموزش SFT/LoRA با ۵ تا ۱۰ دقیقه صدا، جریان زنده (RTF حدود ۰٫۳ روی RTX 4090).
- ✅ سخت‌افزار (جدول README): حدود ۸ گیگ VRAM، CUDA ≥ ۱۲٫۰، PyTorch ≥ ۲٫۵. پس RTX 4060 با ۸ گیگ مرزی است (🧭)؛ ❓ آزموده نشد.
- ❓ کیفیت عربی، به‌ویژه لهجه‌ی خلیجی، آزموده نشد.
- ✅ فارسی: پشتیبانی نمی‌شود. فارسی می‌شود با LoRA ✅ (README می‌گوید fine-tune برای زبان تازه ممکن است) ولی این کار آزموده نشده (❓).

## ریسک و هشدار
- ✅ ریسک نصب پایین: بسته‌ی `voxcpm` در PyPI با همان مخزن رسمی OpenBMB؛ پیش از نصب نام ناشر را در PyPI تطبیق بده (✅ نویسنده‌ی `voxcpm` در PyPI: OpenBMB، نسخه‌ی ۲٫۰٫۳). وزن‌ها از Hugging Face رسمی.
- ⚠️ شبیه‌سازی صدا: فقط صدای خود فرد یا با رضایت کتبی؛ تقلید صدای دیگران ریسک حقوقی و اعتباری دارد (🧭).
- ⚠️ بخش «Limitations» کارت را پیش از کار مشتری بخوان (✅ وجود دارد؛ متنش را کامل نخواندم).

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: Arabic voice-over only, on a rented GPU first. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
👀 نامزد گفتار عربی برای ویدیوهای فروشگاه و سایت‌های دبی؛ مقایسه با [OmniVoice](omnivoice.md) و [Higgs Audio v3](higgs-audio-v3.md) ([صدا با هوش مصنوعی](../domains/social-media/ai-voice.md)). برای فارسی [MOSS-TTS](moss-tts.md). ابتدا روی GPU ابری ([molab](molab.md)) بیازما.

## قیمت و مجوز
✅ رایگان؛ Apache-2.0 برای کد و وزن‌ها، «آماده‌ی استفاده‌ی تجاری» طبق کارت.

## مرتبط
[S191](../sources/README.md#s191) · [صدا با هوش مصنوعی](../domains/social-media/ai-voice.md)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ بسته‌ی `voxcpm` در PyPI (نسخه‌ی ۲٫۰٫۳) نویسنده‌اش OpenBMB است و همه‌ی لینک‌ها به https://github.com/OpenBMB/VoxCPM می‌رود (https://pypi.org/pypi/voxcpm/json). فیلد maintainer در PyPI خالی است؛ فقط author_email ‏you@example.com ثبت شده (https://pypi.org/pypi/voxcpm/json) ✅.
- ✅ CUDA ≥ ۱۲٫۰ می‌خواهد، پس برخلاف ace-step با درایور ۵۵۰ مشکلی ندارد.
- 🧭 آزمون ۲۰۲۶-۱۰-۲۹ اجرا نشد. روی کارت ۸ گیگی با درایور قدیمی که سابقه‌ی یخ‌زدن زیر بار GPU دارد، اجرا نشد؛ اول GPU اجاره‌ای.
