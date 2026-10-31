---
name: ACE-Step 1.5
slug: ace-step
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: مدل محلی ساخت موسیقی از پرامپت (بی‌کلام یا با شعر، تا ۱۰ دقیقه)، MIT؛ روی کارت ۸ گیگ اجرا می‌شود؛ برای موسیقی پس‌زمینه‌ی ویدیو
use_when: "background music for reels, ads or explainer videos without licensing worries ; instrumental loop or a short song with lyrics from a text prompt ; style LoRA from a few own songs"
how: "Trial first on a small task: needs NVIDIA driver 570+ on Linux (torch cu128 pin), check nvidia-smi first; set GRADIO_ANALYTICS_ENABLED=False; from the repo README use uv, models auto-download on first run (Gradio UI); on 8 GB VRAM pick the 2B turbo DiT with the 0.6B LM; listen for artifacts before any client use"
url: https://github.com/ace-step/ACE-Step-1.5
repo: "https://github.com/ace-step/ACE-Step-1.5"
license: "MIT (کد و وزن‌ها)"
pricing: free
risk: medium
sources: [S144]
found_in: [x-yarad_ai-2026-10-23]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# ACE-Step 1.5

## چیست
- ✅ مدل متن‌باز ساخت موسیقی از متن: بی‌کلام یا با شعر، ۱۰ ثانیه تا ۱۰ دقیقه، کنترل BPM و کلید، بازسازی بخشی از قطعه (repaint)، cover و آموزش LoRA از چند آهنگ. منبع: [README](https://github.com/ace-step/ACE-Step-1.5) (۲۰۲۶-۱۰-۲۸).
- ✅ مخزن: MIT، بایگانی نشده، ۱۴٫۱ هزار ستاره. آخرین نسخه‌ی برچسب‌خورده v0.1.8 (۲۰۲۶-۰۵-۱۸). نسخه‌ی XL (DiT چهار میلیاردی) از ۲۰۲۶-۰۴-۰۲ هست.
- ✅ کارت [Hugging Face](https://huggingface.co/ACE-Step/Ace-Step1.5) (مجوز MIT، به‌روزرسانی ۲۰۲۶-۰۲-۰۳، حدود ۸۸ هزار دانلود): می‌گوید داده‌ی آموزش «مجوزدار، بدون حق نشر و ساختگی (MIDI)» است و استفاده‌ی تجاری از خروجی را مجاز می‌داند.
- ✅ سخت‌افزار (جدول README): ≤۶ گیگ VRAM فقط DiT دوبلیونی turbo؛ ۶ تا ۸ گیگ همان به‌علاوه‌ی LM کوچک ۰٫۶B؛ مدل XL دست‌کم ۱۲ گیگ. پس RTX 4060 با ۸ گیگ در محدوده‌ی پشتیبانی‌شده است، ولی سرعت و کیفیت واقعی آزموده نشده (❓).
- ✅ روی لینوکس x86_64، `pyproject.toml` نسخه‌ی torch 2.10.0+cu128 را قفل کرده است (https://github.com/ace-step/ACE-Step-1.5/blob/main/pyproject.toml). CUDA 12.8 درایور NVIDIA ≥ 570 می‌خواهد (https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/). پس با درایور 550 (CUDA 12.4) نصب نمی‌شود. پیش از آزمون، `nvidia-smi` را ببین. روی یک رایانه با درایور 550 نصب مسدود شد.
- ✅ زبان شعر: ادعای «بیش از ۵۰ زبان»؛ کد فارسی `fa` در فهرست زبان‌های معتبر کد هست. ❓ کیفیت خواندن فارسی آزموده نشده.
- ⚠️ پست معرفی به مخزن قدیمی `ace-step/ACE-Step` لینک داده بود؛ نسخه‌ی ۱٫۵ مخزن جدای `ACE-Step-1.5` است.
- ⚠️ ادعای README که کیفیت «بین Suno v4.5 و v5» است، ادعای خود سازنده است (🧭)، نه آزمون مستقل.

## ریسک و هشدار
- ✅ ریسک نصب پایین: کد باز، وزن‌ها از Hugging Face رسمی. بدون تله‌متری دیده‌شده در README (❓ کد خوانده نشد).
- 🧭 ریسک حقوقی خروجی: README خودش هشدار شباهت سبکی و ادعای حق نشر را می‌دهد. ❓ اینکه Content ID یوتیوب یا اینستاگرام برای موسیقی تولیدشده ادعا ثبت نکند، بررسی نشده؛ پیش از انتشار تبلیغی روی یک پست آزمایشی بیازما.
- ⚠️ مدل‌ها در اجرای اول خودکار دانلود می‌شوند؛ حجم را پیش از اجرا بپرس.

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: one background track, listen before use. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
🧭 موسیقی پس‌زمینه‌ی ریلز، تبلیغ و ویدیوی توضیحی، جایگزین کتابخانه‌ی موسیقی. 👀 ارتقا به trial پیشنهاد می‌شود: مجوز MIT (کد و وزن) روشن، سخت‌افزار ما در جدول پشتیبانی‌شده، و ریسک پایین؛ فقط یک آزمون کوچک (۳ قطعه‌ی ۳۰ ثانیه‌ای) لازم است.

## قیمت و مجوز
✅ رایگان؛ MIT برای کد و وزن‌ها ([LICENSE](https://github.com/ace-step/ACE-Step-1.5/blob/main/LICENSE)).

## مرتبط
[S144](../sources/README.md#s144) · [Hugging Face](https://huggingface.co/ACE-Step/Ace-Step1.5)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ❓ هیچ بیانیه‌ی رسمی YouTube یا Meta درباره‌ی Content ID برای موسیقی هوش مصنوعی پیدا نشد.
- ✅ YouTube افشای «موسیقی ساخته‌شده با هوش مصنوعی» را وقتی محور ویدیوست می‌خواهد (https://support.google.com/youtube/answer/14328491). Meta برای صدای واقع‌نما برچسب می‌خواهد (https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/).
- ✅ README مالکیت خروجی را نمی‌گوید و مسئولیت اصالت را به کاربر می‌دهد. 🧭 پیش از کار مشتری، با یک پست آزمایشی خصوصی بسنج.

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد خوانده شد (SHA `ca1e85f`). تله‌متری اختصاصی ندارد. ⚠️ ولی به `gradio==6.2.0` وابسته است و Gradio طبق مستند رسمی analytics را پیش‌فرض روشن دارد (https://www.gradio.app/guides/environment-variables). پس `GRADIO_ANALYTICS_ENABLED=False` بگذار.
- ⚠️ مدل LM با `trust_remote_code=True` بارگذاری می‌شود. پس وزن را فقط از سازمان رسمی Hugging Face بگیر. اگر uv نصب نباشد، `start_gradio_ui.sh` آن را با `curl … | sh` از astral.sh نصب می‌کند. `git pull` خودکار هم دارد که با `CHECK_UPDATE=false` خاموش می‌شود. به همین دلیل ریسک از low به medium رفت.
- 🧭 آزمون ۲۰۲۶-۱۰-۲۹ اجرا نشد: درایور 550 کمتر از ۵۷۰ است. ارتقای درایور یا اجاره‌ی GPU تصمیم کاربر است.
