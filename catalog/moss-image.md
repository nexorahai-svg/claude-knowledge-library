---
name: MOSS-Image (OpenMOSS)
slug: moss-image
category: image-generation
domains: [social-media]
verdict: assess
status: researched
summary: مدل متن‌به‌تصویر Apache-2.0 از OpenMOSS با کنترل چیدمان JSON و جای متن؛ انگلیسی و چینی خوب، فارسی ناشناخته؛ حدود ۲۷ گیگ وزن و نیاز CUDA
use_when: "poster or infographic images where text placement matters, English or Chinese text ; an Apache-licensed local image model next to FLUX and Qwen-Image ; layout-controlled product visuals"
how: "Do not install without the user's yes; the quick start uses trust_remote_code=True so read pipeline_moss_image first; rented GPU first (about 27 GB of weights); test Persian text by eye, expect failure"
url: https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT
repo: "https://github.com/OpenMOSS/MOSS-Image"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# MOSS-Image (OpenMOSS)

## چیست
- ✅ مدل متن‌به‌تصویر از تیم OpenMOSS، در دو نسخه: [Base](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base) و [SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT) (ساخته ۲۰۲۶-۱۰-۱۱؛ به‌روزرسانی ۲۰۲۶-۱۰-۲۱؛ حدود ۱۴ هزار دانلود، ۸۰۰ لایک). مقاله: [arXiv 2610.23374](https://arxiv.org/abs/2610.23374). کد: [OpenMOSS/MOSS-Image](https://github.com/OpenMOSS/MOSS-Image) (Apache-2.0، ۲٫۲ هزار ستاره، push ۲۰۲۶-۱۰-۲۷، بدون release برچسب‌خورده).
- ✅ ورودی: جمله‌ی طبیعی، فهرست تگ، یا چیدمان JSON با مختصات پیکسلی مطلق برای جای متن و اشیا. توصیه‌ی [راهنما](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md): ۱ تا ۲ مگاپیکسل؛ بین ۰٫۲۵ تا ۴ مگاپیکسل هم می‌رود؛ هر نسبت ابعاد به‌شرط مضرب ۱۶.
- ✅ زبان: کارت فقط en و zh را فهرست می‌کند؛ راهنما می‌گوید انگلیسی بهترین است و «زبان‌های دیگر هم پشتیبانی می‌شوند». ❓ فارسی/عربی بررسی نشده و به‌احتمال زیاد حروف را می‌شکند (🧭).
- ✅ سخت‌افزار: مجموع فایل‌های SFT حدود ۲۷ گیگ؛ نیازمند پایتون ۳٫۱۰+، PyTorch ۲٫۹+، CUDA و diffusers ≥ ۰٫۳۸. حداقل VRAM رسمی گفته نشده (❓). ابزار آموزش جامعه (KohakuMossTrainer) می‌گوید آموزش آداپتر با ۶ گیگ شدنی است؛ استنتاج روی ۸ گیگ آزموده نشده.
- ❓ کیفیت نسبت به FLUX و Qwen-Image آزموده نشد.

## ریسک و هشدار
- ⚠️ نمونه‌ی کد `trust_remote_code=True` و `custom_pipeline="pipeline_moss_image"` دارد؛ یعنی کد پایتون از مخزن هنگام اجرا بارگیری می‌شود. پیش از اجرا فایل پایپلاین را بخوان و نسخه را پین کن (✅ واقعیت؛ ریسک 🧭).
- ✅ مجوز Apache-2.0 برای وزن‌ها و کد (کارت و README). بدون محدودیت تجاری دیده‌شده. ❓ داده‌ی آموزش و مالکیت خروجی توضیح داده نشده.
- ⚠️ سکوی API تجاری MOSI هم تبلیغ می‌شود؛ ارسال پرامپت به آن ارسال داده به سرویس چینی است، استفاده نکن مگر با اجازه‌ی کاربر.

## کی استفاده کنیم
👀 فعلاً هیچ. نامزد مدل تصویر محلی با مجوز باز کنار [FLUX](flux-api.md) و [Qwen-Image 2.1](qwen-image-2-1.md) ([تصویر و گرافیک](../domains/social-media/images-and-graphics.md)). مزیت واقعی: کنترل چیدمان JSON برای جای متن. برای متن فارسی روی تصویر مناسب نیست مگر آزمون خلافش را نشان دهد.

## قیمت و مجوز
✅ Apache-2.0، رایگان.

## مرتبط
[S191](../sources/README.md#s191) · [MOSS-TTS](moss-tts.md) · [تصویر و گرافیک](../domains/social-media/images-and-graphics.md)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ USERGUIDE فقط en و zh را نام می‌برد و می‌گوید «زبان‌های دیگر هم پشتیبانی می‌شوند»؛ نامی از فارسی نیست (https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md). ❓ رفتار واقعی با فارسی آزموده نشد. پرامپت را انگلیسی بنویس.
