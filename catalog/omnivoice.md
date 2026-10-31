---
name: OmniVoice (k2-fsa)
slug: omnivoice
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: تبدیل متن به گفتار و شبیه‌سازی صدا برای ۶۰۰+ زبان، محلی؛ کد Apache-2.0 ولی وزن‌ها غیرتجاری (CC-BY-NC)
use_when: "personal tests, previews or internal samples of Persian voice ; quick voice cloning experiments"
how: "Trial first on a small task: OmniVoice in a separate uv venv; use auto or clone mode for Persian (voice design is unintelligible); weights are CC-BY-NC so NOT for client videos, ads or products; bind demo to 127.0.0.1; clone voices only with owner permission"
url: https://github.com/k2-fsa/OmniVoice
repo: "https://github.com/k2-fsa/OmniVoice"
license: "کد Apache-2.0؛ وزن‌ها CC-BY-NC؛ توکنایزر صدا Boson Higgs Audio 2 Community License"
pricing: free
risk: medium
sources: [S130]
found_in: [batch-16]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# OmniVoice (k2-fsa)

## چیست
✅ مدل تبدیل متن به گفتار از تیم k2-fsa (حدود ۱۵ هزار ستاره، ساخته‌شده ۲۰۲۶-۰۳-۳۱، فعال، مقاله arXiv 2604.00688). سه حالت: شبیه‌سازی صدا با صدای مرجع و متنش، طراحی صدا با ویژگی (جنس، سن، زیر و بمی)، و صدای خودکار. فهرست رسمی زبان‌ها فارسی (`fa`) را با حدود ۳۶۶ ساعت داده‌ی آموزشی دارد. رابط وب محلی با `omnivoice-demo`.

## آزمون روی رایانه‌ی آزمون (۲۰۲۶-۱۰-۲۱)
✅ نصب در venv جدا با uv (PyTorch 2.8.0 + CUDA 12.8، `omnivoice` از PyPI)، روی RTX 4060 با ۸ گیگابایت. بار اول مدل ۷۴ ثانیه (با دانلود)، حدود ۲ گیگابایت حافظه‌ی GPU در fp16. ارزیابی بی‌گوش: صدای ساخته‌شده را با [faster-whisper](faster-whisper.md) large-v3 دوباره به متن برگرداندیم و نرخ خطای حرف (CER) را با متن اصلی سنجیدیم:

| حالت | زمان ساخت | طول صدا | CER | نتیجه |
|---|---|---|---|---|
| خودکار | ۱٫۲ ثانیه | ۶٫۱ ثانیه | ۰٫۰۸ (بیشتر «۲۰» به‌جای «بیست» و فاصله) | ✅ واضح |
| شبیه‌سازی از صدای مصنوعی خودش | ۲٫۵ ثانیه | ۴٫۹ ثانیه | ۰٫۰۵ | ✅ واضح |
| طراحی صدا (`instruct="female, ..."`) | ۰٫۹ ثانیه | ۷٫۹ ثانیه | ۰٫۸۸ | ⛔ نامفهوم |

✅ این با هشدار خود README می‌خواند: طراحی صدا فقط با داده‌ی چینی و انگلیسی آموزش دیده. برای فارسی حالت خودکار یا شبیه‌سازی.

## کی استفاده کنیم
🧭 برای آزمون شخصی، پیش‌نمایش و نمونه‌ی داخلی صدای فارسی. ⛔ برای ویدیوی مشتری، تبلیغ یا محصول، نه: وزن‌ها غیرتجاری‌اند.

## قیمت و مجوز
✅ (README مدل در Hugging Face) کد Apache-2.0؛ «مدل از پیش آموزش‌دیده به‌خاطر داده‌ی آموزشی (مثل Emilia) CC-BY-NC است». توکنایزر صدا جداگانه زیر Boson Higgs Audio 2 Community License (بر پایه‌ی Llama 3). ⚠️ پست معرفی آن را «رایگان و متن‌باز» گفته بود و غیرتجاری بودن را نگفت.

## ریسک و هشدار
⚠️ شبیه‌سازی صدای دیگران فقط با اجازه‌ی صاحب صدا. ⚠️ `omnivoice-demo --ip 0.0.0.0` در README رابط را روی شبکه باز می‌کند؛ `127.0.0.1` بگذار. ⚠️ با `faster-whisper` 1.2 و `av` تازه، دادن مسیر فایل به `transcribe` خطای `metadata_errors` می‌دهد؛ صدا را با soundfile بخوان و آرایه بده.

## مرتبط
[صداگذاری](../domains/social-media/ai-voice.md) · [VoiceStudio](voicestudio.md) · [S130](../sources/README.md#s130) · دسته‌ی ۱۶
