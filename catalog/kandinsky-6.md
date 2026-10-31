---
name: Kandinsky 6.0 Video
slug: kandinsky-6
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مدل متن‌باز MIT ویدیوی ۵ ثانیه‌ای با صدای هم‌زمان و لب‌همخوانی؛ Lite ۳ میلیاردی و Pro ۲۹ میلیاردی؛ کمینه‌ی آزموده‌شده کارت ۱۶ گیگ
use_when: "short 5-second clips with synchronized audio and lip-sync on a rented GPU ; comparing open video-audio models against LTX and Wan ; image-to-video-and-audio from a product frame"
how: "Trial first on a small task: check the CC BY-NC-SA header in the vendored mmaudio edm2_utils.py before commercial use; cloud GPU first (README benchmarks start at 16 GB; 8 GB untested); use just setup then just download lite-distill; weights come only from the kandinskylab Hugging Face org"
url: https://github.com/kandinskylab/kandinsky-6
repo: "https://github.com/kandinskylab/kandinsky-6"
license: "MIT (کد و وزن‌های Diffusers)"
pricing: free
risk: low
sources: [S178]
found_in: [sweep-2026-10-26]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# Kandinsky 6.0 Video

## چیست
- ✅ مخزن رسمی [kandinskylab/kandinsky-6](https://github.com/kandinskylab/kandinsky-6): خانواده‌ی مدل‌های انتشار برای ساخت هم‌زمان ویدیو و صدا. Lite (۳ میلیارد پارامتر) و Pro (۲۹ میلیارد). هر دو کلیپ ۵ ثانیه‌ای با صدای ۴۴ کیلوهرتز و لب‌همخوانی می‌سازند؛ حالت‌های متن به ویدیو-صدا و تصویر به ویدیو-صدا. مدل [super-resolution](https://github.com/kandinskylab/kandinsky-6-sr) جداگانه تا ۱۹۲۰×۱۰۸۰ بالا می‌برد. مقاله: [arXiv 2610.05608](https://arxiv.org/abs/2610.05608).
- ✅ مجوز MIT (متن LICENSE خوانده شد). کارت وزن‌های Diffusers در Hugging Face هم `license: mit` دارد (مثلاً [Lite-distill](https://huggingface.co/kandinskylab/Kandinsky-6.0-Lite-distill-5s-Diffusers)). پس ابهام «مجوز جدای وزن‌ها» برطرف شد.
- ✅ فعالیت: ساخته‌شده ۲۰۲۶-۱۰-۰۵، آخرین push ۲۰۲۶-۱۰-۲۵ (حالت‌های اول/آخر فریم، ورودی صدا و ویدیو)، ۳۳۹ ستاره، بایگانی نشده، بدون release برچسب‌خورده.
- ✅ سخت‌افزار (جدول benchmark در README): کارت‌های آزموده RTX 4090 (۲۴ گیگ) و RTX 5060 Ti (۱۶ گیگ) تا H100. نمونه: Lite Distill با کیفیت SD روی 4090 حدود ۶۸ ثانیه، روی 5060 Ti حدود ۱۷۴ ثانیه؛ Pro روی 5060 Ti حدود یک ساعت برای Full HD. برای Lite آفلود ماژولی/بلوکی هست. وزن Lite حدود ۲۸ گیگ. RTX 4060 با ۸ گیگ ❓ آزموده نشده و محتملاً بسیار کند یا ناممکن است (🧭).
- ✅ پایتون ۳٫۱۳ یا ۳٫۱۴، uv، just، و برای SageAttention باید `nvcc` باشد. تقویت پرامپت با Qwen2.5 انجام می‌شود (دانلود اضافه).
- ❓ زبان: پرامپت‌ها انگلیسی‌اند؛ گفتار فارسی گفته نشده و محتملاً پشتیبانی نمی‌شود.
- ❓ کیفیت نسبت به Wan 3.0 و LTX آزموده نشد؛ فقط ادعاهای گزارش سازنده.

## ریسک و هشدار
- ✅ ریسک امنیتی پایین: MIT، بدون `trust_remote_code` در نمونه‌ی Diffusers (Kandinsky6TI2VAPipeline در خود diffusers است)، بدون تله‌متری در README (❓ کد خوانده نشد).
- ⚠️ `just setup` بسته‌های CUDA 13 و SageAttention را می‌سازد و حجم دانلود زیاد است. روی رایانه‌ی آزمون نصب نکن؛ قانون منابع.
- ⚠️ خروجی صدای انسان و لب‌همخوانی: برچسب «ساخته‌شده با هوش مصنوعی» را در انتشار رعایت کن (🧭).

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: a rented cloud GPU only. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
👀 فعلاً هیچ؛ با ۸ گیگ VRAM فقط روی GPU ابری ([molab](molab.md)) و پس از مقایسه با [LTX-2.5](ltx-2-5.md)، [Wan 3.0](wan-3.md) و [MiniMax H3](minimax-h3.md) ([مدل‌های ویدیو](../domains/social-media/ai-video-models.md)). مزیت: MIT بدون سقف درآمد، بر خلاف LTX.

## قیمت و مجوز
✅ رایگان؛ MIT برای کد و وزن‌ها، بدون سقف درآمد و بدون بند تحریم (برخلاف [LTX-2.5](ltx-2-5.md)).

## مرتبط
[S178](../sources/README.md#s178) · [مدل‌های ویدیوی هوش مصنوعی](../domains/social-media/ai-video-models.md)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ README و کارت Diffusers هیچ بیانیه‌ی زبانی ندارند؛ کدگذار متن Qwen2.5-VL است. ❓ فارسی ادعا نشده و آزموده نشد. پرامپت را انگلیسی بنویس.

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد گشته شد (SHA `7ceeefa`). تله‌متری دیده نشد. دانلود مدل فقط صریح و فقط از huggingface.co است. `setup-gpu.sh` کتابخانه‌ی SageAttention را از GitHub بیلد می‌کند.
- ⚠️ **مجوز:** فایل vendored `kandinsky/core/components/mmaudio/ext/autoencoder/edm2_utils.py` (کد NVIDIA) سرتیتر **CC BY-NC-SA 4.0 (غیرتجاری)** دارد، در حالی که مخزن MIT است. این فایل جزء بخش صدای mmaudio است. ❓ پیش از کار تجاری روشن کن که مسیر ویدیوی تو این فایل را بارگذاری می‌کند یا نه.
- 🧭 آزمون ۲۰۲۶-۱۰-۲۹ اجرا نشد: GPU اجاره‌ای و تأیید هزینه از سوی کاربر لازم است. نکته‌ی مجوز edm2_utils.py برای آزمون بعدی یادداشت شد.
