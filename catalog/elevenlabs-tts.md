---
name: ElevenLabs (متن به صدا)
slug: elevenlabs-tts
category: audio-voice
domains: [social-media]
verdict: adopt
status: researched
summary: تبدیل متن به گفتار؛ فارسی فقط در مدل‌های v3 و v4
use_when: "Persian voice-over for videos ; natural cloud TTS where local voices sound artificial"
how: "use model Eleven v4 or v3 for Persian (not Multilingual v2 or Flash v2.5); paid plan needed for commercial output; clone a voice only with consent; text leaves our machine"
url: https://elevenlabs.io
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S58, S136, S151, S155, S192]
found_in: [batch-02]
last_checked: 2026-10-31
next_check: "2026-11-29"
---

# ElevenLabs (متن به صدا)

## چیست
✅ فارسی در Eleven v4، v4 Turbo، v3 و v3 Conversational؛ نه در Multilingual v2 و Flash v2.5.

## دستور سریع

**نصب** (✅ [مستند API](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)؛ SDK پایتون `elevenlabs 2.75.0` اختیاری است، REST کافی است). کلید را در متغیر محیطی بگذار و **چاپ نکن**:
```bash
read -rs ELEVENLABS_API_KEY && export ELEVENLABS_API_KEY    # 🔬 اگر از فایل می‌خوانی: BOM و خط اضافه هدر را می‌شکند؛ فقط خطی که با sk_ شروع می‌شود
```
**حداقل اجرا** (✅ نمونه‌ی رسمی curl؛ شناسه‌ی مدل از [صفحه‌ی مدل‌ها](https://elevenlabs.io/docs/overview/models)):
```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID?output_format=mp3_44100_128" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"text":"سلام، این یک آزمون است.","model_id":"eleven_v4","voice_settings":{"speed":0.9}}' -o out.mp3
```
**تنظیم‌های مهم**
- ✅ `eleven_v4` (حداکثر `10,000` نویسه در هر درخواست) و `eleven_v3` (`5,000`) فارسی دارند؛ `eleven_multilingual_v2` ندارد. `eleven_v4_turbo` ارزان‌تر است.
- 🔬 برای خوانش آرام: `speed` بین `0.85` و `0.92` و stability روی Natural؛ هر متن را **یک‌تکه** بساز.
- 🔬 زمان نویسه‌به‌نویسه: `POST /v1/text-to-speech/{id}/with-timestamps` و `alignment` (نه `normalized_alignment`) را نگه دار. سقف هم‌زمانی طرح Starter پنج درخواست است (ششمی 429).

**خطاهای رایج**
- ✅ `<break>` در v4 پشتیبانی نمی‌شود؛ مکث را با «...» یا `[short pause]` بده. 🔬 تگ‌های `[sighs]`، `[exhales]`، `[whispers]` برای ریل مناسب نبود؛ تگ‌های لحنی مثل `[calm]` و `[warm]` بی‌خطرند.
- 🔬 «ۀ/هٔ» را «ه‌ی» بنویس؛ تیتر مثل «===== بخش ۱» را در متن نگذار (می‌خواندش)؛ نام برند را حرف‌به‌حرف بنویس.
- ⚠️ کلید چاپ‌شده در خطا را بچرخان. صدای دیگران فقط با رضایت؛ صدای کتابخانه ممکن است صاحبش بردارد (`disable_at_unix`).

**هزینه** (✅ [elevenlabs.io/pricing/api](https://elevenlabs.io/pricing/api)، ۲۰۲۶-۱۰-۳۱): v4 و v3 ‏`$0.08` و v4 Turbo/Flash ‏`$0.04` برای هر ۱۰۰۰ نویسه. 🔬 کل ریل‌های سه‌زبانه کمتر از `$0.5` شد. محافظ: نویسه‌ها را پیش از ارسال بشمار و فقط متن نهایی را بفرست.

## کی استفاده کنیم
🧭 گویندگی فارسی ویدیو؛ مدل v4 یا v3.

## قیمت و مجوز
✅ قیمت API (https://elevenlabs.io/pricing/api): v3 ‏۰٫۰۸ دلار و Flash/Turbo ‏۰٫۰۴ دلار برای هر ۱۰۰۰ نویسه. ❓ متن کامل شرایط استفاده‌ی تجاری خوانده نشد.

## ریسک و هشدار
⚠️ شبیه‌سازی صدای دیگران فقط با رضایت. متن به سرویس بیرونی می‌رود.

## به‌روزرسانی ۲۰۲۶-۱۰-۲۲
✅ قیمت API: v4 و v3 ۰٫۰۸ دلار برای هر ۱۰۰۰ نویسه، v4 Turbo ۰٫۰۴؛ طرح Starter ۶ دلار در ماه (۷۵ هزار نویسه). خروجی طرح پولی تجاری است، طرح رایگان نه؛ صدا باید مال خودت یا «مجاز به اشتراک» باشد. v4 بیش از ۹۰ زبان؛ v4، v4 Turbo و v3 فارسی و عربی دارند؛ Multilingual v2 فارسی ندارد ولی عربی سعودی و اماراتی دارد. سرعت با `voice_settings.speed`؛ زمان نویسه‌به‌نویسه از `/with-timestamps` و زمان کلمه از سرویس forced-alignment. دوبله: ۰٫۳۳ تا ۲٫۲۰ دلار در دقیقه، برای یک خط تولید کوچک گران و درشت. [S136](../sources/README.md#s136)

## تجربه‌ی دست‌اول ۲۰۲۶-۱۰-۲۴ 🔬
- 🔬 صدای محلی MOSS-TTS فارسی «خیلی مصنوعی» بود و ElevenLabs v4 پذیرفته شد؛ MOSS فقط برای پیش‌نویس می‌ماند.
- 🔬 کتابخانه‌ی صدای اشتراکی: `GET /v1/shared-voices?language=fa` دوازده صدای فارسی داد (عربی و انگلیسی بیش از ۳۰۰). افزودن: `POST /v1/voices/add/{public_owner_id}/{voice_id}`. راویان آزموده‌شده: فارسی «Roya – Warm Tehrani Narrator»، عربی «Farah – Smooth, Calm and Warm»، انگلیسی «Jade – Elegant, Calm, Emotive». نمونه‌های فارسی (Connery، Aran، Sina، Sara، Roya، Setareh) با faster-whisper حدود ۰ تا ۲٪ خطای نویسه داشتند؛ خطای بیشتر فقط از نوشتن رقم و نام لاتین توسط Whisper بود.
- 🔬 هر متن را **یک‌تکه** (نه خط‌به‌خط) بساز؛ طبیعی‌تر است. از `/v1/text-to-speech/{id}/with-timestamps` استفاده کن و `alignment` را نگه دار (نه `normalized_alignment`) تا زمان نویسه‌ها با متن نوشته‌شده بخواند.
- 🔬 تلفظ برند: نام برند را حرف‌به‌حرف و آوایی بنویس.«ۀ/هٔ» را به «ه‌ی» بده تا اضافه تلفظ شود. تیتر مثل «===== بخش ۱» در متن نگذار؛ مدل بلند می‌خواندش. برای خوانش آرام: speed بین ۰٫۸۵ و ۰٫۹۲ و stability روی Natural.
- 🔬 تگ‌هایی که صدا را آه‌کشیدن، نفس‌نفس یا نفس شنیدنی کرد و برای ریل‌ها نامناسب بود: `[tired]`، `[exhales]`، `[inhales slowly]`، `[sighs]`، `[whispers, …]`، `[a little emotional]`، `[smiling softly]`. تگ‌های فقط‌لحن و بی‌خطر: `[calm]`، `[warm]`، `[softly]`، `[thoughtful]`، `[sincere]`، `[hopeful]`، `[gently]`، `[softly, slow]`، `[firm but gentle]`، `[short pause]`، `[long pause]`، و «...» برای مکث. ✅ `<break>` در v4 پشتیبانی نمی‌شود (راهنمای رسمی: https://elevenlabs.io/docs/best-practices/prompting/eleven-v3).
- 🔬 کلون فوری از یادداشت صوتی حدود ۷۶ ثانیه‌ای تلفن (با رضایت گوینده) کلون قانع‌کننده داد؛ `POST /v1/voices/add` به‌صورت multipart. سقف هم‌زمانی طرح Starter پنج درخواست است (ششمی HTTP 429 با `concurrent_limit_exceeded`).
- 🔬 تله‌های فایل کلید: BOM در فایل کلید هدر را می‌شکند (خطای latin-1)؛ خط جاماندهٔ نمونه به هدر چسبید و کلید در متن خطا چاپ شد ← فقط خطی را بخوان که با `sk_` شروع می‌شود، و کلیدِ چاپ‌شده را بچرخان.
- 🔬 محیط Claude Code تولید گفتار با صدای کلون‌شده‌ی شخص واقعی را حتی با رضایت مسدود کرد؛ تولید دستی در برنامه‌ی وب ElevenLabs انجام شد (متن، صدا، Eleven v4، Generate، دانلود). دور زدنِ این محدودیت با مرورگر ممنوع است.
- 🔬 هزینه: کل کار ریل‌های فارسی، عربی و انگلیسی کمتر از ۰٫۵ دلار روی Starter. [S151](../sources/README.md#s151)


## تجربه‌ی دست‌اول ۲۰۲۶-۱۰-۲۸ 🔬
- 🔬 کلون فوری از ۹۱ ثانیه ویس واتساپ به‌هم‌چسبیده (Opus ۴۸ کیلوهرتز، تمیز با ffmpeg: highpass، afftdn، silenceremove، loudnorm) کلون قابل‌قبول و عالی از آب درآمد. تنظیم: Eleven v4، stability ۰٫۵، similarity ۰٫۸، speed ۰٫۹، `with-timestamps`؛ ۷۴۱ نویسه‌ی فارسی ← ۵۵ ثانیه.
- 🔬 این بار محیط Claude Code فراخوانی API را **مسدود نکرد** (برخلاف تجربه‌ی ۲۰۲۶-۱۰-۲۴ بالا که مسدود شد)؛ هر دو تجربه ثبت شد، پس مسدود شدن ثابت نیست و نباید روی آن حساب کرد. رضایت صاحب صدا همچنان لازم است. [S192](../sources/README.md#s192)

## بازخوانی Whisper (۲۰۲۶-۱۰-۳۰) 🔬
🔬 مقایسه‌ی بازخوانی Whisper با متن برای تأیید صدا، پاسخ فارسی درست با عدد و نام لاتین را رد می‌کند؛ راه‌حل و اعداد در [صداگذاری](../domains/social-media/ai-voice.md).

## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ طرح‌ها (امروز): Free ۰ (۱۰ هزار اعتبار، **بدون حق تجاری**)، Starter ۶ دلار (۳۰ هزار؛ نه ۷۵ هزار که پیش‌تر ثبت شده بود)، **Creator ۲۲** (۱۲۱ هزار، کلون حرفه‌ای ۱)، Pro ۹۹ (۶۰۰ هزار)، Scale ۲۹۹. API: v4 و v3 ‏۰٫۰۸ دلار برای هر ۱۰۰۰ نویسه، Turbo و Flash ‏۰٫۰۴. ✅ صفحه‌ی https://elevenlabs.io/pricing/api برای «مدل‌های با بالاترین کیفیت» هر نویسه ۱ اعتبار و برای Flash/Turbo هر نویسه ۰٫۵ اعتبار می‌نویسد (نام v4 در همان جمله نیست). فارسی فقط در v4 و v3؛ Voice Changer و forced alignment فارسی ندارند؛ برای زمان کلمه در فارسی `with-timestamps`. Voice Design (صدا از توصیف). ⚠️ صاحب صدای کتابخانه (مثل «رویا») می‌تواند صدا را بردارد؛ `disable_at_unix` را بخوان. 🧭 برای ۳۰ ریلز در ماه: Creator. راهنمای نوشتن متن: [ابزارهای پولی](../domains/social-media/paid-ai-tools.md).

## مرتبط
[صداگذاری](../domains/social-media/ai-voice.md#elevenlabs) · [S58](../sources/README.md#s58)
