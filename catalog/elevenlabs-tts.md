---
name: ElevenLabs (متن به صدا)
slug: elevenlabs-tts
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: تبدیل متن به گفتار؛ فارسی فقط در مدل‌های v3 و v4
url: https://elevenlabs.io
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S58, S136, S151, S155]
found_in: [batch-02]
last_checked: 2026-10-25
next_check: "2026-11-24"
---

# ElevenLabs (متن به صدا)

## چیست
✅ فارسی در Eleven v4، v4 Turbo، v3 و v3 Conversational؛ نه در Multilingual v2 و Flash v2.5.

## کی استفاده کنیم
🧭 گویندگی فارسی ویدیو؛ مدل v4 یا v3.

## قیمت و مجوز
❓ قیمت و شرایط تجاری این بار خوانده نشد.

## ریسک و هشدار
⚠️ شبیه‌سازی صدای دیگران فقط با رضایت. متن به سرویس بیرونی می‌رود.

## به‌روزرسانی ۲۰۲۶-۱۰-۲۲
✅ قیمت API: v4 و v3 ۰٫۰۸ دلار برای هر ۱۰۰۰ نویسه، v4 Turbo ۰٫۰۴؛ طرح Starter ۶ دلار در ماه (۷۵ هزار نویسه). خروجی طرح پولی تجاری است، طرح رایگان نه؛ صدا باید مال خودت یا «مجاز به اشتراک» باشد. v4 بیش از ۹۰ زبان؛ v4، v4 Turbo و v3 فارسی و عربی دارند؛ Multilingual v2 فارسی ندارد ولی عربی سعودی و اماراتی دارد. سرعت با `voice_settings.speed`؛ زمان نویسه‌به‌نویسه از `/with-timestamps` و زمان کلمه از سرویس forced-alignment. دوبله: ۰٫۳۳ تا ۲٫۲۰ دلار در دقیقه، برای خط تولید ما گران و درشت. [S136](../sources/README.md#s136)

## تجربه‌ی دست‌اول ۲۰۲۶-۱۰-۲۴ 🔬
- 🔬 مالک صدای محلی MOSS-TTS فارسی را «خیلی مصنوعی» دانست و ElevenLabs v4 را پذیرفت؛ MOSS فقط برای پیش‌نویس می‌ماند.
- 🔬 کتابخانه‌ی صدای اشتراکی: `GET /v1/shared-voices?language=fa` دوازده صدای فارسی داد (عربی و انگلیسی بیش از ۳۰۰). افزودن: `POST /v1/voices/add/{public_owner_id}/{voice_id}`. راویان انتخاب‌شده: فارسی «Roya – Warm Tehrani Narrator»، عربی «Farah – Smooth, Calm and Warm»، انگلیسی «Jade – Elegant, Calm, Emotive». نمونه‌های فارسی (Connery، Aran، Sina، Sara، Roya، Setareh) با faster-whisper حدود ۰ تا ۲٪ خطای نویسه داشتند؛ خطای بیشتر فقط از نوشتن رقم و نام لاتین توسط Whisper بود.
- 🔬 هر متن را **یک‌تکه** (نه خط‌به‌خط) بساز؛ طبیعی‌تر است. از `/v1/text-to-speech/{id}/with-timestamps` استفاده کن و `alignment` را نگه دار (نه `normalized_alignment`) تا زمان نویسه‌ها با متن نوشته‌شده بخواند.
- 🔬 تلفظ برند: «دی اِم اِی آی پرو» و در انگلیسی «D-M-A-I Pro». «ۀ/هٔ» را به «ه‌ی» بده تا اضافه تلفظ شود. تیتر مثل «===== بخش ۱» در متن نگذار؛ مدل بلند می‌خواندش. برای خوانش آرام: speed بین ۰٫۸۵ و ۰٫۹۲ و stability روی Natural.
- 🔬 تگ‌هایی که صدا را آه‌کشیدن، نفس‌نفس یا نفس شنیدنی کرد و مالک ردشان کرد: `[tired]`، `[exhales]`، `[inhales slowly]`، `[sighs]`، `[whispers, …]`، `[a little emotional]`، `[smiling softly]`. تگ‌های فقط‌لحن و بی‌خطر: `[calm]`، `[warm]`، `[softly]`، `[thoughtful]`، `[sincere]`، `[hopeful]`، `[gently]`، `[softly, slow]`، `[firm but gentle]`، `[short pause]`، `[long pause]`، و «...» برای مکث. ✅ `<break>` در v4 پشتیبانی نمی‌شود (راهنمای رسمی: https://elevenlabs.io/docs/best-practices/prompting/eleven-v3).
- 🔬 کلون فوری از یادداشت صوتی حدود ۷۶ ثانیه‌ای تلفن (با رضایت گوینده) کلون قانع‌کننده داد؛ `POST /v1/voices/add` به‌صورت multipart. سقف هم‌زمانی طرح Starter پنج درخواست است (ششمی HTTP 429 با `concurrent_limit_exceeded`).
- 🔬 تله‌های فایل کلید: BOM در فایل کلید هدر را می‌شکند (خطای latin-1)؛ خط جاماندهٔ نمونه به هدر چسبید و کلید در متن خطا چاپ شد ← فقط خطی را بخوان که با `sk_` شروع می‌شود، و کلیدِ چاپ‌شده را بچرخان.
- 🔬 محیط Claude Code تولید گفتار با صدای کلون‌شده‌ی شخص واقعی را حتی با رضایت مسدود کرد؛ مالک خودش در برنامه‌ی وب ElevenLabs ساخت (متن، صدا، Eleven v4، Generate، دانلود). دور زدنِ این محدودیت با مرورگر ممنوع است.
- 🔬 هزینه: کل کار ریل‌های فارسی، عربی و انگلیسی کمتر از ۰٫۵ دلار روی Starter. [S151](../sources/README.md#s151) · دفتر پروژه‌ها (یک پروژه‌ی مشتری / Nexorah AI social، personal family videos)


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ طرح‌ها (امروز): Free ۰ (۱۰ هزار اعتبار، **بدون حق تجاری**)، Starter ۶ دلار (۳۰ هزار؛ نه ۷۵ هزار که پیش‌تر ثبت شده بود)، **Creator ۲۲** (۱۲۱ هزار، کلون حرفه‌ای ۱)، Pro ۹۹ (۶۰۰ هزار)، Scale ۲۹۹. API: v4 و v3 ‏۰٫۰۸ دلار برای هر ۱۰۰۰ نویسه، Turbo و Flash ‏۰٫۰۴. ضریب اعتبار به نویسه‌ی v4 ❓. فارسی فقط در v4 و v3؛ Voice Changer و forced alignment فارسی ندارند؛ برای زمان کلمه در فارسی `with-timestamps`. Voice Design (صدا از توصیف). ⚠️ صاحب صدای کتابخانه (مثل «رویا») می‌تواند صدا را بردارد؛ `disable_at_unix` را بخوان. 🧭 برای ۳۰ ریلز در ماه: Creator. راهنمای نوشتن متن: [ابزارهای پولی](../domains/social-media/paid-ai-tools.md).

## مرتبط
[صداگذاری](../domains/social-media/ai-voice.md#elevenlabs) · [S58](../sources/README.md#s58)
