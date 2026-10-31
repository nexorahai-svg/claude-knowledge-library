---
name: LTX-2.5 (Lightricks)
slug: ltx-2-5
category: video
domains: [social-media]
verdict: assess
status: researched
summary: مدل ۲۲ میلیاردی Lightricks برای ویدیو و صدای ۴۸ کیلوهرتز هم‌زمان؛ مجوز Community رایگان زیر ۱۰ میلیون دلار درآمد سالانه، با بند تحریم و واترمارک؛ روی ۸ گیگ شدنی نیست
use_when: "a multi-shot scene (wide, medium, close-up) with the same character, light and voice in one generation ; a clip with synchronized audio on a rented GPU where Wan or MiniMax have no sound ; image-to-video-and-audio from a product still ; dubbing or audio-to-video experiments"
how: "Do not install without the user's yes; easiest local route is the LTX Desktop app (Apache-2.0) but it needs 24 GB VRAM (floor 9 GB fp8 on Windows, 15 GB Linux) or a 48 GB Mac on macOS 26, so on the 8 GB RTX 4060 use a cloud GPU (22B transformer plus Gemma 4 encoder, 42 GB bf16 or 18.7 GB nvfp4); read the LTX-2.x Community License sections 2, 6 and 7 first; gated on Hugging Face, accept terms there"
url: https://huggingface.co/Lightricks/LTX-2.5-Diffusers
repo: "https://github.com/Lightricks/LTX-2"
license: "LTX-2.x Community License (تاریخ ۲۰۲۶-۰۸-۱۱؛ رایگان زیر ۱۰ میلیون دلار درآمد سالانه)"
pricing: free
risk: medium
sources: [S191, S203]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# LTX-2.5 (Lightricks)

## چیست
- ✅ مدل پایه‌ی ویدیو و صدا از Lightricks. منابع: مخزن [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) (آخرین release در GitHub: v1.5.0 در ۲۰۲۶-۱۰-۱۸، حدود ۹٫۹ هزار ستاره)، مخزن وزن [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) (ساخته ۲۰۲۶-۰۷-۲۳، حدود ۲٫۲ میلیون دانلود، ۹٫۷ هزار لایک) و نسخه‌ی [Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers) (به‌روزرسانی ۲۰۲۶-۱۰-۲۲).
- ✅ ترنسفورمر ۲۲B؛ حالت‌ها: متن/تصویر/صدا به ویدیو-صدا، ویدیو به صدا، کلیدفریم، DFR برای کیفیت تولیدی، DubIt. زبان‌های برچسب کارت: en, de, es, fr, ja, ko, zh, it, pt؛ فارسی نیست (❓ گفتار فارسی احتمالاً بد).
- ✅ حجم و VRAM (فهرست فایل‌ها): ترنسفورمر bf16 حدود ۴۲ گیگ، نسخه‌ی int8 حدود ۲۱٫۵ گیگ، nvfp4 حدود ۱۸٫۷ گیگ؛ کدگذار متن Gemma 4 دوازده‌میلیاردی حدود ۲۶٫۳ گیگ (int8 حدود ۱۵٫۴). README برای کمبود حافظه `--quantization fp8-cast --offload cpu|disk` پیشنهاد می‌کند. حداقل VRAM رسماً گفته نشده (❓)؛ روی RTX 4060 با ۸ گیگ عملاً شدنی نیست (🧭).
- ❓ کیفیت نسبت به Wan و Kandinsky آزموده نشد.

## ریسک و هشدار
متن کامل [LICENSE-2_x](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x) را خواندم. نکته‌های مهم:
- ✅ **سقف درآمد (بند ۲٫۱):** استفاده‌ی تجاری رایگان است مگر «موجودیتی» با درآمد سالانه ≥ ۱۰ میلیون دلار؛ آن‌ها مجوز پولی می‌خواهند (licensing@ltx.io). درآمد شرکت‌های وابسته و هم‌گروه جمع می‌شود. برای مشتری بزرگ، خروجی گرفتن از طرف او همچنان باید بررسی شود (🧭).
- ✅ **بند تحریم (بند ۷):** باید مقیم یا ثبت‌شده در کشور تحت تحریم جامع نباشی. ❓ اگر کاربر یا مشتری در چنین کشوری است، این مجوز شاید اجازه ندهد؛ پیش از هر کار مشتری موقعیت حقوقی را روشن کن.
- ✅ **واترمارک و شفافیت (بند ۶):** حذف یا دور زدن واترمارک، متادیتا یا افشای نهفته ممنوع است و می‌تواند مجوز را فوراً لغو کند؛ مسئولیت برچسب «هوش مصنوعی» با کاربر است. باید آخرین نسخه را به‌کار ببری.
- ✅ مشتقات (fine-tune، LoRA، تقطیر با خروجی مدل) تحت همین مجوز می‌مانند و به شرکت بزرگ منتقل‌شده مجوز پولی لازم دارد. داوری ICC در نیویورک. خروجی را Lightricks مالک نیست (بند ۵) ولی مسئولیتش با توست و سیاست استفاده‌ی مجاز ([AUP](https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf)) اعمال می‌شود (AUP خوانده شد؛ بخش «بررسی دوباره» پایین).
- ✅ مخزن وزن «gated: auto» است؛ دانلود یعنی پذیرش مجوز. ✅ کدگذار Gemma 4 زیر Apache-2.0 است (بخش بررسی دوباره در پایین).
- ⚠️ سنگین: ده‌ها گیگ؛ هرگز روی رایانه‌ی آزمون؛ قانون منابع.

## کی استفاده کنیم
👀 فعلاً هیچ. در صورت نیاز به صدای هم‌زمان، فقط روی GPU ابری ([molab](molab.md)) و پس از مقایسه با [Kandinsky 6](kandinsky-6.md) که MIT است و بند تحریم ندارد، و با [Wan 2.2](wan-2-2.md) و [MiniMax H3](minimax-h3.md) ([مدل‌های ویدیو](../domains/social-media/ai-video-models.md)).

## قیمت و مجوز
✅ رایگان با شرط بالا؛ مجوز پولی برای درآمد ≥ ۱۰ میلیون دلار (قیمت منتشر نشده). مجوز همه‌ی نسخه‌های LTX-2.5 از ۲۰۲۶-۰۸-۱۱ به بعد را شامل می‌شود؛ مخزن GitHub در API مجوز را NOASSERTION نشان می‌دهد.

## مرتبط
[S191](../sources/README.md#s191) · [S203](../sources/README.md#s203) · [مدل‌های ویدیوی هوش مصنوعی](../domains/social-media/ai-video-models.md)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ AUP لایتریکس (به‌روز ۲۰۲۶-۰۳-۳۰، https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf): ممنوعیت دیپ‌فیک، جعل هویت یا شخصیت ساختگی بی‌رضایت، محتوای گمراه‌کننده، اسپم و تعامل ساختگی. برای کار تجاری باید مطمئن شوی خروجی چهره، برند یا مکان واقعی را بی‌مجوز تقلید نمی‌کند. استفاده از خروجی برای آموزش مدل رقیب ممنوع است. دسترسی دادن به کاربران «مکان‌های پشتیبانی‌نشده» هم ممنوع است.
- ❓ اینکه قید «افشای هوش مصنوعی» در AUP برای پست ساده‌ی شبکه‌ی اجتماعی هم لازم باشد روشن نیست؛ متن بیشتر به محصول API و چت‌بات می‌خورد. 🧭 برچسب AI را به‌هرحال بزن.
- ✅ کدگذار Gemma 4 زیر Apache-2.0 است (https://huggingface.co/google/gemma-4-12b) و شرایط قدیمی Gemma شامل آن نمی‌شود (https://ai.google.dev/gemma/terms). پس هشدار قبلی درباره‌ی مجوز جدای Gemma برطرف شد.

## اپ LTX Desktop و ادعاهای ریل (۲۰۲۶-۱۰-۳۰)
- ✅ اپ رومیزی رسمی [LTX-Desktop](https://github.com/Lightricks/LTX-Desktop): مجوز Apache-2.0، حدود ۲٫۲ هزار ستاره، نسخه‌ی v1.3.1 در ۲۰۲۶-۱۰-۱۹، هنوز بتا. برای ویندوز x64، مک Apple Silicon و لینوکس. تولید روی سخت‌افزار خود کاربر است. پیش‌فرضش LTX 2.5 Fast است و 2.5 Pro فقط از راه API در دسترس است.
- ✅ سخت‌افزار لازم: ویندوز و لینوکس ۲۴ گیگ VRAM یا بیشتر (۳۲ پیشنهادی) و ۳۲ گیگ RAM می‌خواهند. مک باید ۴۸ گیگ حافظه و macOS 26 داشته باشد؛ با ۳۲ گیگ فقط 540p و ۵ ثانیه. حداقلی که اپ می‌پذیرد: ۹ GiB روی ویندوز با کارت fp8، ۱۵ GiB روی لینوکس. دیسک ۱۰۰ گیگ یا بیشتر لازم است. حالت stream ویندوز ۴۰ GiB RAM می‌خواهد ([جدول سازگاری](https://github.com/Lightricks/LTX-Desktop/blob/main/docs/local-compat-matrix.md)).
- 🧭 رایانه‌ی آزمون (RTX 4060 با ۸۱۸۸ MiB، حدود ۳۰ گیگ RAM، لینوکس) زیر هر دو حداقل است. اپ به‌جای ابزار تولید پیام «Coming soon to your device» نشان می‌دهد. پس نصبش روی این رایانه فایده ندارد.
- ✅ چندشاتی بومی ([ltx.io/model](https://ltx.io/model)): شخصیت، محیط، نور و صدا را در نماهای باز، متوسط و نزدیک داخل **یک** تولید ثابت نگه می‌دارد. اینکه «حافظه بین رندرها» حفظ شود در منبع رسمی نیست (❓).
- ✅ آمار دانلود کل در HF (۲۰۲۶-۱۰-۳۰): LTX-2 حدود ۸٫۹۵ میلیون، LTX-Video حدود ۹٫۵۶ میلیون، LTX-2.5 حدود ۵٫۰۹ میلیون. «۱۸ میلیون» ریل فقط با جمع دو نسل قبلی درست درمی‌آید.
- ارزیابی همان assess می‌ماند؛ آزموده نشد.
