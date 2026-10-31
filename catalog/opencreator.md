---
name: OpenCreator (KrillinAI سابق)
slug: opencreator
category: video
domains: [social-media]
verdict: assess
status: researched
summary: میز کار دسکتاپ/وب متن‌باز (Apache-2.0) برای ترجمه و دوبله‌ی ویدیو، زیرنویس RTL و ابزارهای تولید محتوا روی موتور Codex CLI؛ اعتبار و مدل‌های ابری پولی اختیاری است
use_when: "translating or subtitling an existing video into many languages with an RTL-aware subtitle editor ; downloading a public video and its captions for reference ; studying how a Codex-based creator workspace is built"
how: "Do not install without the user's yes; get releases only from github.com/krillinai/OpenCreator, never connect the main ChatGPT sign-in or a main API key, use a spare key with a spend cap; Persian dubbing quality must be tested by ear"
url: https://github.com/krillinai/OpenCreator
repo: "https://github.com/krillinai/OpenCreator"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S144]
found_in: [x-yarad_ai-2026-10-23]
last_checked: 2026-10-28
next_check: "2026-11-27"
---

# OpenCreator (KrillinAI سابق)

## چیست
- ✅ نام تازه‌ی KrillinAI (README: «formerly known as KrillinAI»). مخزن [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator): Apache-2.0، حدود ۱۴ هزار ستاره، ساخته ۲۰۲۴-۱۲-۱۷، push ۲۰۲۶-۱۰-۲۶. آخرین release: v3.2.9 (۲۰۲۶-۱۰-۲۵)، سه release در ده روز؛ فعال. فایل‌های نصب: macOS (dmg/zip)، Windows (exe)، CLI و Server برای لینوکس. نصب‌کننده‌ی دسکتاپ لینوکس در فهرست فایل‌ها دیده نشد (❓)؛ باید از سورس بسازی یا CLI/Server بگیری.
- ✅ **موتور اجرا Codex CLI شرکت OpenAI** است، نه Claude؛ مدل زبان از فهرست Codex یا هر ارائه‌دهنده‌ی سازگار با OpenAI. تصویر/ویدیو/صدا/رونویسی با سرویس‌هایی که در Settings → AI Services وارد می‌کنی (GPT Image، Seedream، Kling، Nano Banana، Seedance، Veo، Whisper، Edge TTS و ...).
- ✅ ده ابزار: ترجمه و دانلود ویدیو، تولید کاور، تصویر، مقاله، پست Xiaohongshu، فیلم‌نامه‌ی کوتاه، انیمیشن آدمک، صدا (TTS) و ویدیو؛ «Auto Clips» و «Digital Avatar» هنوز در توسعه‌اند.
- ✅ ترجمه‌ی ویدیو: ۱۲۳ زبان مبدأ و ۱۲۴ مقصد؛ README صریح می‌گوید پوشش واقعی رونویسی و دوبله به سرویس انتخاب‌شده بستگی دارد. ویرایشگر زیرنویس با موج صدا، تقسیم/ادغام، جایگزینی؛ فونت پشتیبان برای خط‌های پیچیده و راست‌به‌چپ.
- ✅ رابط ۴۳ زبانه با چیدمان راست‌به‌چپ برای فارسی، عربی، اردو و عبری (ادعای README). ❓ کیفیت دوبله‌ی فارسی و رندر زیرنویس فارسی آزموده نشد.
- ✅ مهارت‌ها (`skills/`) برای Agentهای دارای KrillinAI CLI: زیرنویس، TTS، رندر افقی/عمودی، کاور.

## ریسک و هشدار
- ⚠️ ✅ راه‌اندازی اول **پیکربندی Codex محلی را اسکن می‌کند** و پیشنهاد می‌دهد ورود ChatGPT یا کلید API موجود را بازاستفاده کند. این یعنی دسترسی به اعتبار حساب؛ بپذیر فقط با حساب فرعی یا کلید جدا با سقف هزینه.
- ✅ حساب و اشتراک: ورود از طریق `https://www.open-creator.ai/device`، خرید با Stripe، «اعتبار» برای مدل‌های رسمی؛ `OPENCREATOR_GATEWAY_ORIGIN` پیش‌فرض همان سایت است. پس پرامپت و فایل‌ها ممکن است به سرور آن‌ها بروند اگر از «مدل‌های رسمی» استفاده کنی (❓ مسیر داده روشن نیست). [صفحه‌ی قیمت](https://www.open-creator.ai/pricing) جدول قیمت را بدون جاوااسکریپت نشان نداد (❓ قیمت بسته‌ها نامعلوم).
- ✅ README می‌گوید داده، پیوست و لاگ به‌طور پیش‌فرض محلی است؛ کلیدها در ذخیره‌ی اعتبار سیستم؛ ASAR integrity و رمزنگاری کوکی در بسته‌ی دسکتاپ. تله‌متری در README ذکر نشد (❓ کد خوانده نشد).
- ⚠️ دانلودر ویدیو از YouTube، X، TikTok، Instagram و ... «ممکن است کوکی پلتفرم بخواهد»: کوکی حساب اصلی را وارد نکن؛ دانلود از پلتفرم‌ها شرایط استفاده‌ی آن‌ها را نقض می‌کند (🧭).
- ⚠️ yt-dlp نایتلی هر هفت روز به‌روزرسانی را چک می‌کند (نصب خودکار نیست).

## کی استفاده کنیم
👀 فقط مرجع برای ترجمه و دوبله‌ی ویدیوی موجود و ویرایشگر زیرنویس RTL. خط تولید خودمان روی Claude است و موتور Codex را دو بار هزینه نمی‌کنیم؛ برای زیرنویس و دوبله اول [HyperFrames](hyperframes.md) و Whisper محلی را بسنج. اگر کار ترجمه‌ی انبوه شد، با یک حساب فرعی آزمون کن.

## قیمت و مجوز
✅ نرم‌افزار رایگان و متن‌باز (Apache-2.0)؛ README: با کلید API خودت کار می‌کند. اعتبار/اشتراک پولی برای سرویس‌های رسمی اختیاری است (freemium). هزینه‌ی مدل‌ها (Codex یا سرویس‌های ترجمه و صدا) جدا.

## مرتبط
[S144](../sources/README.md#s144) · [ویدیو از کد](../domains/social-media/code-to-video.md)
