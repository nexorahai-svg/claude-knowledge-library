# راهنمای پروژه: محتوای شبکه‌های اجتماعی

> **نوع سند:** راهنمای قدم‌به‌قدم
> **هدف این سند:** Claude در یک پروژه‌ی محتوای شبکه‌های اجتماعی (ریل و ویدیوی کوتاه ۹:۱۶ با زیرنویس فارسی، ویدیوی لانچ با کد، تصویر پست و کاروسل، صدا، موسیقی، کپشن و انتشار) از اولین پیام تا تحویل و نگهداری، قدم‌به‌قدم بداند چه بپرسد، چه بسازد، با کدام ابزار، و هر مرحله کی «تمام» است.
> **موضوع تحقیق:** جمع‌بندی سندها و کارت‌های کتابخانه و تجربه‌ی پروژه‌های واقعی برای این نوع پروژه (این راهنما ادعای تازه نمی‌سازد؛ هر واقعیت به سند منبعش لینک دارد).
> **منابع:** سندهای لینک‌شده در متن · دفتر پروژه‌ها
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۹
> **دفعه‌ی بعد چک شود:** وقتی حکم یکی از کارت‌های جدول پشته عوض شد (lint آن را می‌گیرد) یا پروژه‌ی تازه‌ای از این نوع تمام شد.

---

## این راهنما برای کدام پروژه است

- ریل، Shorts یا کلیپ TikTok با متن یا زیرنویس فارسی.
- ویدیوی لانچ، دموی محصول یا انیمیشن ورود لوگو که با کد ساخته می‌شود.
- تصویر پست، کاور یا کاروسل با برند ثابت و متن فارسی.
- صدای گوینده، موسیقی و افکت برای همین محتوا.
- کپشن، نسخه‌ی هر شبکه، و زمان‌بندی انتشار با تأیید انسان.

اگر کار ساختن خود لوگو و هویت برند است: [برند و لوگو](brand-identity.md). بقیه: [فهرست راهنماها](README.md).

## پیش از شروع: پرسش‌ها از کاربر

فقط آن‌هایی را بپرس که جوابشان در پیام یا پوشه‌ی پروژه نیست.

1. **چه چیزی می‌سازیم؟** اگر ویدیو ← مرحله‌های ۱ تا ۵. اگر فقط تصویر و کاروسل ← مرحله‌ی ۱، ۲ و ۶. اگر هر دو ← همه. پیش‌فرض: یک نسخه‌ی اصلی ۹:۱۶ و یک تصویر ۴:۵ ([ابعاد شبکه‌ها](../domains/social-media/platform-specs.md)).
2. **گوینده دارد؟** اگر بله ← اول متن روایت، بعد صدا، بعد تصویر (مرحله‌ی ۳). اگر نه ← متن روی صفحه و موسیقی CC0. پیش‌فرض: بدون گوینده.
3. **صحنه‌ی واقع‌نما لازم است (منظره، دست، محصول در محیط)؟** اگر نه ← فقط کد، هزینه‌ی ابزار صفر. اگر بله ← تکه‌ی تولیدی بدون متن، با گفتن هزینه پیش از ساخت. پیش‌فرض: نه ([ساخت کلیپ با Claude، قدم ۷](../domains/social-media/claude-clip-pipeline.md#قدم-۷-تصویر-تولیدی-فقط-اگر-لازم-است)).
4. **یک کلیپ است یا قالب تکراری با داده‌ی متغیر؟** اگر یکی ← HyperFrames. اگر قالب تکراری ← Remotion؛ اگر تیم بیش از ۳ نفر است، مجوز پولی Remotion را بگو ([ویدیو با کد، مجوزها](../domains/social-media/code-to-video.md#مجوزها-در-یک-نگاه)). پیش‌فرض: HyperFrames.
5. **زبان‌ها؟** اگر فقط فارسی ← یک لایه‌ی متن. اگر فارسی و زبان دیگر ← نسخه‌ی بدون متن نگه دار و لایه‌ی متن را جدا بساز. پیش‌فرض: فقط فارسی، زیرنویس سوخته در ویدیو.
6. **انتشار با کیست؟** اگر کاربر خودش ← فایل‌ها و جدول کپشن. اگر ابزار زمان‌بندی ← فقط پیش‌نویس، بعد تأیید ([انتشار](../domains/social-media/publishing.md)). پیش‌فرض: فایل و جدول، بدون اتصال به هیچ حساب.

## پشته‌ی پیش‌فرض

| نیاز | انتخاب پیش‌فرض | کی چیز دیگر | جزئیات |
|---|---|---|---|
| موتور ویدیو | [HyperFrames](../catalog/hyperframes.md) 🧪 با نسخه‌ی ثابت | قالب تکراری با داده ← [Remotion](../catalog/remotion.md) ✅؛ بدون نصب ابزار تازه ← [Playwright](../catalog/playwright.md) ✅ + [FFmpeg](../catalog/ffmpeg.md) ✅ | [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) |
| کدگذاری و ترکیب نهایی | [FFmpeg](../catalog/ffmpeg.md) ✅ | — | [ابعاد شبکه‌ها](../domains/social-media/platform-specs.md#دستور-ffmpeg-برای-نسخهی-اصلی-) |
| صحنه‌ی سه‌بعدی و رندر GPU | [Three.js](../catalog/threejs.md) ✅ | رمزگذاری در مرورگر ← [Mediabunny](../catalog/mediabunny.md) 🧪 | [ویدیو با کد](../domains/social-media/code-to-video.md#ویدیوی-توضیحی-سهبعدی-با-صدای-فارسی) |
| فونت فارسی | Vazirmatn از [Google Fonts](../catalog/google-fonts.md) ✅، فایل محلی | فونت پولی ← [یکان‌بخ](../catalog/yekan-bakh.md) 🧪 (خرید، ویدیو را پوشش می‌دهد) | [فارسی و RTL](../domains/website/02-design/persian-rtl.md) |
| صدای گوینده | [ElevenLabs](../catalog/elevenlabs-tts.md) 🧪 فقط مدل v3 یا v4 | — | [صداگذاری](../domains/social-media/ai-voice.md#elevenlabs) |
| زمان کلمه‌ها و زیرنویس | [faster-whisper](../catalog/faster-whisper.md) ✅ محلی | زمان دقیق‌تر ← [WhisperX](../catalog/whisperx.md) 🧪؛ کیفیت کم ← [ElevenLabs Scribe](../catalog/elevenlabs-scribe.md) 🧪 | [زیرنویس و متن](../domains/social-media/captions-and-copy.md) |
| موسیقی و افکت | [Openverse](../catalog/openverse.md) ✅ با `license_type=commercial,modification` | — | [کتابخانه‌ی صدا](../domains/social-media/sound-library.md) |
| تکه‌ی تولیدی بدون متن | [Google Veo](../catalog/google-veo.md) 🧪 (3.1 Lite) | [Runway](../catalog/runway.md) 🧪؛ [Luma Ray](../catalog/luma-ray.md) 🧪 فقط با اشتراک پولی | [مدل‌های ویدیو](../domains/social-media/ai-video-models.md) |
| تصویر پست و کاروسل | قالب HTML + [Playwright](../catalog/playwright.md) ✅ | کارت ساده ← [Satori](../catalog/satori.md) ✅ پس از تست متن مخلوط | [تصویر و گرافیک](../domains/social-media/images-and-graphics.md) |
| پس‌زمینه‌ی تولیدی | [Nano Banana](../catalog/nano-banana.md) 🧪 | [Recraft](../catalog/recraft.md) 🧪 فقط طرح پولی | [تصویر و گرافیک، راه ۳](../domains/social-media/images-and-graphics.md#راه-۳-مدل-تولید-تصویر-فقط-پسزمینه) |
| فشرده‌سازی تصویر | [Squoosh](../catalog/squoosh.md) ✅ | — | [تصویر و گرافیک](../domains/social-media/images-and-graphics.md#فشردهسازی-پیش-از-انتشار) |
| کمک در کپشن | Claude، با تأیید انسان | ساختار کار ← [Instagram Agent Skill](../catalog/instagram-agent-skill.md) 🧪 (نه `ig-human` روی فارسی) | [زیرنویس و متن](../domains/social-media/captions-and-copy.md#کپشن-و-هشتگ) |
| زمان‌بندی | هیچ (فایل و جدول) | [Metricool](../catalog/metricool.md) 🧪 یا [Buffer](../catalog/buffer.md) 🧪، فقط پیش‌نویس | [انتشار](../domains/social-media/publishing.md) |

قانون: نشان حکم بلافاصله بعد از لینک کارت می‌آید و باید با کارت یکی باشد. HyperFrames 🧪 است، ولی آزمون کوچکش در clip-test گذشت (دفتر پروژه‌ها) 🔬؛ پس نسخه را ثابت کن و هر نسخه‌ی تازه را دوباره با همان آزمون فارسی بسنج.

**زیر نظر:** [Pika](../catalog/pika.md) 👀 (حالا مرکز چند مدل، بدون واترمارک، تجاری از ۱۰ دلار). جدول کامل ابزارهای پولی: [ابزارهای پولی](../domains/social-media/paid-ai-tools.md).

**استفاده نکن:** [Sora](../catalog/sora.md) ⛔ (حذف شد)، [Midjourney](../catalog/midjourney.md) ⛔ برای کار خودکار، [hypit](../catalog/hypit.md) ⛔، [onetake](../catalog/onetake.md) ⛔، [Later و Hootsuite](../catalog/later-hootsuite.md) ⛔. کارت‌های 👀 مثل [fal MCP](../catalog/fal-mcp.md) 👀 و [Claude Motion](../catalog/claude-motion.md) 👀 پیش‌فرض نیستند.

## مراحل

### مرحله‌ی ۱: آماده‌سازی امن
- **هدف:** پوشه و ابزارها طوری آماده شوند که هیچ چیزی بی‌اجازه داده نفرستد یا دانلود نکند.
- **کارها:** Node ۲۲ به بالا و FFmpeg. پوشه‌های `assets/`، `audio/`، `brief.md`، `style-guide.md`. فایل‌های HyperFrames را پیش از نصب بخوان (قانون ۴ [CLAUDE.md](../CLAUDE.md))، CLI را با `--save-exact` داخل پروژه نصب کن و افزونه را با `--scope project`. چهار متغیر خاموش‌کردن را در `.env` بگذار. در `CLAUDE.md` پروژه اجرای `hyperframes usage` را ممنوع کن.
- **تمام یعنی:** `npx hyperframes telemetry status` می‌گوید disabled؛ `ffmpeg -hide_banner -buildconf | grep enable-libass` یک خط برمی‌گرداند (زیرنویس فارسی بدون libass خراب می‌شود)؛ خط ممنوعیت `usage` در `CLAUDE.md` پروژه هست.
- **بخوان:** [ساخت کلیپ با Claude، قدم ۱](../domains/social-media/claude-clip-pipeline.md#قدم-۱-آمادهسازی-یک-بار) · [زیرنویس، فارسی درست در FFmpeg](../domains/social-media/captions-and-copy.md#فارسی-درست-در-ffmpeg)

### مرحله‌ی ۲: بریف، راهنمای سبک و فهرست نما
- **هدف:** Claude جای خالی را با پیش‌فرض امن پر نکند.
- **کارها:** بریف تولید (هدف، مخاطب، طول، نسبت، پیام‌ها، دارایی واقعی، صدا، حس، مرجع فقط برای سبک). راهنمای سبک یک بار برای برند ذخیره شود. فهرست نما: هر نما ورود، خروج و دلیل. تایم‌لاین با شماره‌ی فریم.
- **تمام یعنی:** `brief.md` و `style-guide.md` در پوشه هستند؛ هر ردیف فهرست نما سه ستون ورود، خروج و دلیل دارد؛ کاربر فهرست را صریح تأیید کرده؛ هر دارایی نام‌برده در `assets/` واقعاً هست (`ls`). دارایی گم‌شده یعنی توقف و سؤال، نه اختراع.
- **بخوان:** [ویدیو با کد، روش کار](../domains/social-media/code-to-video.md#روش-کار-از-مقالههای-p04-p09-p12-بازنویسی-ما)

### مرحله‌ی ۳: متن روایت، صدا و زمان‌بندی (اگر گوینده دارد)
- **هدف:** صدا اول، تصویر بعد؛ هر ضرب روی زمان واقعی صدا قفل شود.
- **کارها:** متن فارسی محاوره‌ای، عدد با حروف، نام برند لاتین. صدا با ElevenLabs v3 یا v4. زمان کلمه‌ها با faster-whisper (`fa`)، ولی متن زیرنویس همیشه متن تأییدشده‌ی خودمان. نیم‌فاصله حفظ، «ی» و «ک» فارسی.
- **تمام یعنی:** شمار کلمه تقسیم بر مدت صدا (از `ffprobe -show_entries format=duration`) نزدیک ۲٫۳ تا ۲٫۶ کلمه در ثانیه است 🧭؛ یک اسکریپت کوتاه روی SRT نشان می‌دهد هر خط پایانش بعد از شروعش است، دو خط روی هم نمی‌افتند، آخرین خط از مدت صدا جلو نمی‌زند، و هیچ «ي» یا «ك» عربی نیست؛ کاربر فهرست کلمه‌های نامطمئن را دیده.
- **بخوان:** [ویدیوی توضیحی سه‌بعدی](../domains/social-media/code-to-video.md#ویدیوی-توضیحی-سهبعدی-با-صدای-فارسی) · [زیرنویس، روش کار](../domains/social-media/captions-and-copy.md#روش-کار-خط-لوله-)

### مرحله‌ی ۴: ساختن ترکیب و پیش‌نمایش ثابت
- **هدف:** متن فارسی پیش از رندر کامل درست دیده شود.
- **کارها:** HTML با ۱۰۸۰×۱۹۲۰، timeline متوقف، همه‌ی کتابخانه‌ها و فونت‌ها محلی. `dir="rtl"`، فاصله‌ی حروف صفر، هیچ حرف تکی متحرک نشود، `white-space: nowrap` روی هر نام لاتین و تاریخ. فریم اول همان صحنه است، نه سیاهی. متن و لوگو در منطقه‌ی امن (۱۴٪ بالا، ۳۵٪ پایین، ۶٪ هر طرف).
- **تمام یعنی:** `npx hyperframes check` بدون خطا؛ `npx hyperframes snapshot --at … --describe false` چهار تصویر ثابت داده و Claude آن‌ها را دیده: اتصال حروف، نیم‌فاصله، رقم فارسی، هیچ تاریخ یا نام لاتین دوتکه؛ کاربر تصویرها را تأیید کرده.
- **بخوان:** [ساخت کلیپ، قدم ۳ تا ۵](../domains/social-media/claude-clip-pipeline.md#قدم-۵-فارسی) · [ابعاد شبکه‌ها، پنج قانون](../domains/social-media/platform-specs.md#پنج-قانون-مشترک-)

### مرحله‌ی ۵: رندر و بازبینی با برگه‌ی فریم
- **هدف:** فایل نهایی هم از نظر فنی و هم از نظر دیداری قبول شود.
- **کارها:** رندر `--docker` با کیفیت standard (یا high اگر گرادیان تیره نوار رنگ داد). برگه‌ی فریم با FFmpeg. Claude ویدیو را نمره می‌دهد و فقط سه ایراد بدتر را درست می‌کند. برای تکه‌ی تولیدی: بدون متن، و برچسب هوش مصنوعی اگر واقع‌نماست.
- **تمام یعنی:** `ffprobe` نشان می‌دهد: ۱۰۸۰×۱۹۲۰، `h264`، `yuv420p`، ۳۰ فریم، صدای `aac` با ۴۸۰۰۰ هرتز (اگر صدا دارد). `ffmpeg -i out.mp4 -vf "fps=1,scale=270:480,tile=5x2" -frames:v 1 sheet.png` ساخته و دیده شده: هماهنگی صدا، اتصال حروف، رقم‌ها، فریم اول. هر شبکه‌ی مقصد حد طول و حجمش را دارد.
- **بخوان:** [ساخت کلیپ، قدم ۴ و ۸](../domains/social-media/claude-clip-pipeline.md#قدم-۴-پیشنمایش-بازبینی-رندر) · [ویدیو با کد، پرامپت بازبینی](../domains/social-media/code-to-video.md#بازبینی) · [ابعاد شبکه‌ها](../domains/social-media/platform-specs.md)

### مرحله‌ی ۶: تصویر پست و کاروسل
- **هدف:** همه‌ی پست‌ها یک قالب، املای دقیق و رنگ برند داشته باشند.
- **کارها:** قالب HTML با اندازه‌ی دقیق (مثلاً ۱۰۸۰×۱۳۵۰)، داده از `posts.json`، یک PNG برای هر پست با Playwright. مدل تصویر فقط پس‌زمینه‌ی بدون متن. کاروسل Instagram تا ۱۰ مورد. پیش از انتشار فشرده‌سازی محلی.
- **تمام یعنی:** پست اول پیش از بقیه به کاربر نشان داده و تأیید شده؛ `ffprobe` یا `file` ابعاد هر فایل را درست نشان می‌دهد؛ تصویر فید JPEG با sRGB و زیر ۵ مگابایت؛ [axe-core](../catalog/axe-core.md) ✅ روی صفحه‌ی قالب خطای کنتراست ندارد (متن ۴٫۵ به ۱، متن بزرگ ۳ به ۱؛ [رنگ و کنتراست](../domains/website/02-design/color-and-texture.md#کنتراست)).
- **بخوان:** [تصویر و گرافیک](../domains/social-media/images-and-graphics.md) · [ابعاد شبکه‌ها، Instagram](../domains/social-media/platform-specs.md#instagram-)

### مرحله‌ی ۷: کپشن، اعتبار و نسخه‌ی هر شبکه
- **هدف:** متن هر شبکه در حد مجاز، و هیچ مجوزی جا نماند.
- **کارها:** کپشن فارسی با قلاب در جمله‌ی اول، هشتگ کم. فایل اعتبار صدا (عنوان، سازنده، مجوز، `foreign_landing_url`). برچسب هوش مصنوعی برای هر رسانه‌ی واقع‌نمای تولیدی. SRT جدا برای YouTube.
- **تمام یعنی:** یک شمارش نویسه نشان می‌دهد هر کپشن Instagram زیر ۲٬۲۰۰ نویسه و ۳۰ هشتگ است و هر عنوان Shorts زیر ۱۰۰؛ برای هر فایل CC BY متن `attribution` در توضیحات هست؛ ستون «برچسب هوش مصنوعی بله/نه» برای هر پست پر شده.
- **بخوان:** [زیرنویس و متن، کپشن](../domains/social-media/captions-and-copy.md#کپشن-و-هشتگ) · [کتابخانه‌ی صدا](../domains/social-media/sound-library.md) · [انتشار، قانون شبکه‌ها](../domains/social-media/publishing.md#قانون-شبکهها)

### مرحله‌ی ۸: انتشار با تأیید انسان
- **هدف:** Claude پیش‌نویس می‌سازد؛ انسان تأیید می‌کند؛ ابزار منتشر می‌کند.
- **کارها:** پیش از وصل کردن هر MCP زمان‌بندی، [امنیت MCP](../domains/claude-code/mcp-safety.md). پست‌ها فقط «پیش‌نویس». پست تقریباً یکسان انبوه نساز.
- **تمام یعنی:** جدول (تاریخ، شبکه، فایل، کپشن، برچسب) به کاربر نشان داده شده و کاربر در گفتگو صریح «بله» گفته؛ پیش از آن هیچ پستی زمان‌بندی یا منتشر نشده؛ پس از انتشار یک آپلود واقعی هر شبکه بدون رد یا برش دیده شده.
- **بخوان:** [انتشار و زمان‌بندی](../domains/social-media/publishing.md)

## چرا این ترتیب (برای Claude)

Claude ویدیو نمی‌سازد، برنامه می‌سازد؛ پس کیفیت از بریف، دارایی واقعی و بازبینی می‌آید، نه از ابزار بیشتر ([ساخت کلیپ](../domains/social-media/claude-clip-pipeline.md#دو-حقیقت-که-پستها-نمیگویند)). هر مرحله ارزان‌تر از مرحله‌ی بعد است: اصلاح فهرست نما چند ثانیه، اصلاح تصویر ثابت یک دقیقه، و اصلاح رندر کامل یا تکه‌ی تولیدی پولی گران؛ پس هر خطا را در ارزان‌ترین جا بگیر. صدا پیش از تصویر می‌آید چون زمان واقعی صدا ضرب تصویر را تعیین می‌کند. Claude از تصویر متحرک فقط فریم اول را می‌بیند، پس همیشه تصویر ثابت و برگه‌ی فریم بده. هر جا متن فارسی هست، شکل‌دهی را به مرورگر بسپار، نه به مدل تولیدی. هر کاری که به نام کاربر بیرون می‌رود (انتشار، هزینه، اتصال حساب) بدون «بله»‌ی صریح در گفتگو انجام نمی‌شود.

## خطاهایی که در پروژه‌های خودمان دیدیم 🔬

از دفتر پروژه‌ها:
- **clip-test (HyperFrames):** تاریخ دوتکه شد و بعد از `text-wrap: balance`، «Claude Code» داخل `<bdi>` وسط خط شکست؛ `white-space: nowrap` حل کرد. پس پیش‌نمایش ثابت پیش از رندر لازم است.
- **clip-test:** رندر محلی بی‌اجازه chrome-headless-shell (۲۶۴ مگابایت) دانلود کرد؛ `--docker` بار اول ۲ دقیقه و ۱۱ ثانیه و بعد ۱۱ ثانیه طول کشید. هشدار `EROFS` بعد از رندر Docker بی‌خطر است.
- **clip-test:** روی گرادیان تیره کمی نوار رنگ دیده شد؛ «۱۰۰٪» درشت با Vazirmatn Black از دور شبیه «100%» لاتین بود.
- **Sun Shade DXB، انیمیشن ورود لوگو:** برگه‌ی فریم پیش از تحویل چهار ایراد واقعی نشان داد (دایره‌ی تیره‌ی خورشید پیش از طلوع، دو جرقه‌ی هم‌زمان، هم‌پوشانی نام با لوگو، بیرون زدن خورشید از کنار بادبان) ([ویدیو با کد](../domains/social-media/code-to-video.md#قانونهای-فنی)).
- **Sun Shade DXB:** علامت `&` در عنوان SVG فایل را خراب کرد؛ متن را escape کن ([لوگو و برند](../domains/website/02-design/logo-and-brand.md)).

## شکاف‌های کتابخانه

- ❓ کتابخانه هنوز ندارد: منطقه‌ی امن رسمی TikTok و Shorts (فقط عدد Meta برای Reels تبلیغاتی هست).
- ❓ کتابخانه هنوز ندارد: راه آپلود SRT در Instagram و TikTok، و فارسی در زیرنویس خودکار TikTok؛ پس زیرنویس را بسوزان.
- ❓ کتابخانه هنوز ندارد: نرخ خطای Whisper و Scribe روی صدای فارسی خودمان.
- ❓ کتابخانه هنوز ندارد: هدف بلندی صدا (LUFS) رسمی هیچ شبکه‌ای؛ −۱۴ رایج است ولی رسمی نیست.
- ❓ کتابخانه هنوز ندارد: مجوز موسیقی تجاری داخل Reels و TikTok، آمار شخصی حساب خودمان. الگوریتم، طول، قلاب و بهترین زمان (بدون زمان ثابت): [راهبرد ریلز](../domains/social-media/reels-strategy.md).
- ❓ کتابخانه هنوز ندارد: راه آزموده‌ی رفع نوار رنگ (کیفیت high یا نویز هنوز آزموده نشده).
- ❓ کتابخانه هنوز ندارد: شرایط fal برای پست عمومی، و کیفیت فارسی Fish Audio.

## پرامپت شروع (English)

```text
This is a social media content project. Follow playbooks/social-content.md in my knowledge
library phase by phase. First ask me only the "before you start" questions you cannot
answer from my message or this folder, then show me the default stack with each card's
verdict and wait for my OK. Use only real assets from assets/ and audio/; if something is
missing, stop and ask. Persian text right-to-left in our local font, no per-letter
animation, Latin names and dates kept on one line. Do not run `hyperframes usage`, never
read Claude credentials, and pass --describe false to snapshot. Before each phase, open
its "read" links; a phase is done only when its "done means" check has been run and its
output shown here. Never publish, schedule, connect an account or spend money without my
explicit yes in this chat. At the end, file anything genuinely new back into the library.
```

## پایان کار: چه چیزی به کتابخانه برگردد

- یک ردیف در دفتر پروژه‌ها: کارت‌ها، زمان رندر، چه شکست و چه درست شد.
- نسخه‌ی تازه‌ی HyperFrames یا Remotion که آزموده شد، در کارتش.
- هر عدد تازه از آپلود واقعی (حد طول، حجم، رد شدن فایل) در [ابعاد شبکه‌ها](../domains/social-media/platform-specs.md).
- هر جواب به یکی از شکاف‌های بالا، با منبع اصلی، طبق [CLAUDE.md](../CLAUDE.md).

## مرتبط

[برند و لوگو](brand-identity.md) · [هوش مصنوعی در محصول و عامل](ai-feature-agent.md) (عامل زمان‌بندی‌شده) · [حوزه‌ی شبکه‌های اجتماعی](../domains/social-media/README.md) · [بررسی خودکار](../domains/claude-code/verification.md) · [هزینه و کارایی](../domains/claude-code/cost-efficiency.md)
