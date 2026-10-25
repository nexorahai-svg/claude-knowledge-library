# ساخت کلیپ با Claude: مسیر کامل

> **نوع سند:** راهنمای قدم‌به‌قدم
> **هدف این سند:** ساختن کلیپ کوتاه شبکه‌های اجتماعی (۹:۱۶، ۱۵ تا ۶۰ ثانیه، متن و زیرنویس فارسی) با Claude Code، با ساده‌ترین و ارزان‌ترین ترکیب ابزارهای بررسی‌شده، از ایده تا فایل آماده‌ی انتشار.
> **موضوع تحقیق:** ابزارهای پرطرفدار ساخت ویدیو با Claude در مهر ۱۴۰۵ (HyperFrames، Remotion، Claude Motion، OpenMontage و مهارت‌های دیگر) و ساختن ویدیو با مدل‌های تولیدی از داخل Claude (fal، Google Veo، Runway، Higgsfield، HeyGen).
> **منابع:** [S83 ابزارهای پرطرفدار ویدیو با Claude](../../sources/README.md#s83) · [S84 کد HyperFrames](../../sources/README.md#s84) · [S85 Remotion، Claude Motion و موتورهای دیگر](../../sources/README.md#s85) · [S86 ویدیوی تولیدی از داخل Claude](../../sources/README.md#s86)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۸
> **دفعه‌ی بعد چک شود:** هر ماه؛ نسخه و تله‌متری HyperFrames؛ Remotion 5.0 (شمردن پیمانکارها)؛ قیمت Veo در Google و fal؛ شرایط fal برای انتشار عمومی؛ در دسترس بودن Claude Motion برای طرح‌های دیگر.

قانون‌های فنی ساخت ویدیو با کد (فریم تابع خالص زمان، بدون تصادف، بازبینی با برگه‌ی فریم) در [ویدیو با کد](code-to-video.md) است و این‌جا تکرار نمی‌شود. این سند **مسیر کار** را می‌گوید.

---

## اول: «nfp» چیست؟

✅ ابزاری به این نام پیدا نشد (جستجو در npm، گیت‌هاب، فهرست ۳۱۵ مخزن ویدیو با Claude، Hacker News و وب). 🧭 محتمل‌ترین منظور **HyperFrames** است که با `npx hyperframes` اجرا می‌شود و در پست‌های پرطرفدار «Claude این ویدیو را ساخت» بیشتر از همه آمده. دستور نصب رایج پست‌ها هم `npx skills add …` است.

## دو حقیقت که پست‌ها نمی‌گویند

1. ✅ **Claude ویدیو نمی‌سازد، برنامه می‌سازد.** موج پست‌های مهر و آبان «Claude Opus 5.5 این ویدیو را کاملاً با کد ساخت» است: HTML، CSS و انیمیشن که مرورگر بدون رابط فریم‌به‌فریم عکس می‌گیرد و FFmpeg به MP4 تبدیل می‌کند. مدل تولید ویدیو در پست‌های پرطرفدار کم است.
2. ✅ **ابزار تفاوت بزرگی نمی‌سازد.** فهرست awesome-claude-video-skills در ۲۰۲۶-۱۰-۱۱ از ۱۶ مهارت خواست یک تبلیغ ۱۵ ثانیه‌ای یکسان بسازند. همه از چهار آزمونش گذشتند، و Claude Code **بدون هیچ مهارتی** هم گذشت (۴.۴ دقیقه). ❓ این آزمون را سازنده‌ی همان فهرست انجام داده که سایت تبلیغی خودش را هم دارد. 🧭 پس کیفیت از بریف، دارایی واقعی و بازبینی می‌آید، نه از نصب مهارت بیشتر.

---

## ترکیب پیشنهادی (ساده‌ترین و ارزان‌ترین)

| بخش | انتخاب | هزینه | چرا |
|---|---|---|---|
| موتور ویدیو | **HyperFrames** 🧪 🔬 | رایگان (Apache-2.0)، بدون سقف شرکت | HTML که Claude بهتر از همه می‌نویسد؛ شکل‌دهی واقعی فارسی در Chrome؛ از ۲۰۲۶-۱۰-۱۷ آزمون رندر راست‌به‌چپ دارد |
| جایگزین موتور | **Remotion** ✅ | رایگان برای فرد و شرکت تا ۳ نفر؛ بعد از آن ۲۵ دلار برای هر نفر در ماه | بهترین ابزار رسمی Claude و زیرنویس آماده؛ برای قالب تکراری با داده |
| بی‌وابستگی | HTML + [Playwright](../../catalog/playwright.md) + [FFmpeg](../../catalog/ffmpeg.md) ✅ | رایگان | وقتی نمی‌خواهی هیچ ابزار تازه‌ای نصب کنی |
| صدای گوینده | [ElevenLabs](../../catalog/elevenlabs-tts.md) v3 یا v4 | طرح ElevenLabs | فارسی فقط در این دو مدل ([صداگذاری](ai-voice.md#elevenlabs)) |
| زیرنویس | [faster-whisper](../../catalog/faster-whisper.md) محلی، هم‌تراز با متن خودمان | رایگان | داده بیرون نمی‌رود ([زیرنویس و متن](captions-and-copy.md)) |
| موسیقی و افکت | [Openverse](../../catalog/openverse.md) با فیلتر CC0 | رایگان | [کتابخانه‌ی صدا](sound-library.md) |
| تصویر واقعی‌نما (اختیاری) | **Veo 3.1 Lite**، ۷۲۰p، ۴ تا ۸ ثانیه، بدون متن | ۸ ثانیه: ۰.۴۰ دلار در Google؛ ۰.۲۴ دلار بی‌صدا در fal | [مدل‌های ویدیو](ai-video-models.md) |
| فونت فارسی | Vazirmatn (رایگان، OFL) از [Google Fonts](../../catalog/google-fonts.md)، فایل محلی | رایگان | [یکان‌بخ](../../catalog/yekan-bakh.md) پولی است |

**هزینه‌ی یک کلیپ ۳۰ ثانیه‌ای** 🧭: صفر دلار اگر فقط کد باشد؛ حدود ۱ تا ۲ دلار اگر سه تکه‌ی ۸ ثانیه‌ای Veo Lite داشته باشد؛ به‌اضافه‌ی مصرف Claude و طرح ElevenLabs.

---

## قدم ۱: آماده‌سازی (یک بار)

1. **Node ۲۲ به بالا و FFmpeg** نصب باشد.
2. **پوشه‌ی پروژه** با این ساختار: `assets/` (لوگو، عکس محصول، فونت)، `audio/` (صدای گوینده، موسیقی)، `brief.md`، `style-guide.md`.
3. **نصب HyperFrames** (فقط بعد از خواندن فایل‌ها، طبق قانون ۴ [CLAUDE.md](../../CLAUDE.md)). 🔬 در آزمون کلیپ فارسی این ترتیب جواب داد: CLI با نسخه‌ی ثابت داخل پوشه‌ی پروژه، افزونه فقط برای همان پروژه:
   ```bash
   npm install --save-exact hyperframes@0.8.171 gsap
   ```
   ```bash
   claude plugin marketplace add heygen-com/hyperframes
   ```
   ```bash
   claude plugin install hyperframes@hyperframes --scope project
   ```
   🔬 `--scope project` افزونه را فقط در `.claude/settings.json` همان پوشه روشن می‌کند؛ خود فهرست (marketplace) ولی در تنظیمات کاربر ثبت می‌شود. ⚠️ npm 11 اسکریپت نصب esbuild را بدون اجازه اجرا نمی‌کند؛ رندر بدون آن هم کار کرد.
4. **خاموش کردن تله‌متری** ✅ (پیش‌فرض روشن است و به PostHog می‌فرستد):
   ```bash
   npx hyperframes telemetry disable
   ```
   یا متغیر `HYPERFRAMES_NO_TELEMETRY=1` در محیط. ✅ (کد خوانده شد) دو متغیر دیگر هم بگذار: `HYPERFRAMES_NO_UPDATE_CHECK=1` (بدون پرس‌وجو از npm) و `HYPERFRAMES_NO_AUTO_INSTALL=1` (CLI نصب‌شده‌ی سراسری در پس‌زمینه خودش را با `npm install -g` به‌روز نمی‌کند). 🔬 هر چهار متغیر را در یک فایل `.env` پروژه گذاشتیم و قبل از هر دستور بار کردیم؛ `telemetry status` گفت: disabled.
5. ⚠️ **قدم «usage» را خاموش کن.** ✅ مهارت اصلی HyperFrames به Claude می‌گوید در شروع هر کار `npx hyperframes usage --json` را اجرا کند. این دستور توکن ورود Claude Code را از keychain یا `~/.claude/.credentials.json` می‌خواند و به سرور Anthropic می‌فرستد تا سقف باقی‌مانده را بخواند (`packages/cli/src/utils/harnessUsage.ts`). مقصد خود Anthropic است، نه HeyGen، ولی یک ابزار شخص ثالث اعتبارنامه‌ی تو را می‌خواند. در `CLAUDE.md` پروژه بنویس:
   ```text
   Do not run `hyperframes usage`. Never read Claude credentials. Report usage as unknown.
   ```
   ⚠️ ✅ `hyperframes snapshot` گزینه‌ی `--describe` دارد که اگر `GEMINI_API_KEY` در محیط باشد، **خودکار** فریم‌ها را برای توصیف به Gemini می‌فرستد. همیشه `--describe false` بده.
6. **نسخه را ثابت کن.** ✅ HyperFrames پیش از ۱.۰ است و روزی چند نسخه می‌دهد (0.8.171 در ۲۰۲۶-۱۰-۱۸). مهارت‌ها نسخه را در هر پروژه ثابت می‌کنند؛ به‌روزرسانی فقط آگاهانه.

## قدم ۲: بریف و راهنمای سبک

- **بریف** ([روش کار در ویدیو با کد](code-to-video.md#روش-کار-از-مقالههای-p04-p09-p12-بازنویسی-ما)): هدف، مخاطب، طول، نسبت ۹:۱۶، پیام‌ها، دارایی واقعی، صدا، حس، و یک مرجع **برای سبک، نه کپی**.
- **راهنمای سبک** یک بار برای برند نوشته و ذخیره شود: رنگ‌ها و معنایشان، فونت، اندازه‌ی متن، سرعت، نوع گذار. هر کلیپ بعدی در گفت‌وگوی تازه از همین شروع می‌شود ([ویدیوی توضیحی سه‌بعدی](code-to-video.md#ویدیوی-توضیحی-سهبعدی-با-صدای-فارسی)).
- **صدا اول، تصویر بعد:** متن روایت تأیید شود، صدا ساخته شود، بعد هر ضرب تصویر روی زمان واقعی صدا قفل شود.

## قدم ۳: ساختن ترکیب (composition)

✅ در HyperFrames هر کلیپ یک فایل HTML ساده است، بدون مرحله‌ی build:
- یک `div` ریشه با `data-composition-id`، `data-width="1080"`، `data-height="1920"` و `data-fps`
- هر عنصر زمان‌دار کلاس `clip` و `data-start`، `data-duration`، `data-track-index` دارد
- صدا با `<audio>` و `data-volume`
- انیمیشن باید **قابل جابه‌جایی در زمان** باشد: یک timeline متوقف (GSAP، CSS، WAAPI، Lottie، Three.js و…) در `window.__timelines[id]`

✅ هر نام فونت در `font-family` باید `@font-face` با فایل محلی داشته باشد، وگرنه بررسی خطا می‌دهد. ⚠️ ابزار دانلود فونت از سایت، زیرمجموعه‌ی لاتین را ترجیح می‌دهد؛ **فونت فارسی را خودت بگذار**.
✅ همه‌ی دارایی‌ها محلی؛ خواندن از اینترنت وسط رندر قانون «قطعی بودن» را می‌شکند (مثال README، GSAP را از CDN می‌خواند؛ آن را محلی کن).

## قدم ۴: پیش‌نمایش، بازبینی، رندر

```bash
npx hyperframes preview
```
```bash
npx hyperframes render
```
- ✅ خروجی: mp4، webm و mov با کانال شفاف، gif، دنباله‌ی png؛ کیفیت draft، standard یا high.
- ✅ گزینه‌ی `--docker` نسخه‌ی Chrome، فونت‌ها و FFmpeg را ثابت می‌کند تا خروجی روی کامپیوترهای مختلف یکسان باشد.
- ✅ `--workers` از ۱ تا ۲۴؛ هر کارگر یک Chrome حدود ۲۵۶ مگابایت.
- 🔬 **زمان رندر کلیپ ۱۰ ثانیه‌ای ۱۰۸۰×۱۹۲۰، ۳۰ فریم، کیفیت standard** (لینوکس، ۲۴ هسته، RTX 4060):
  - `--docker` بار اول: **۲ دقیقه و ۱۱ ثانیه**، بیشترش ساختن ایمیج `hyperframes-renderer:0.8.171` (۲.۲۹ گیگابایت؛ Debian، Chromium، فونت‌های Noto، FFmpeg 8). خود رندر ۱۰ ثانیه، با کپچر screenshot و GPU نرم‌افزاری.
  - `--docker` بار دوم: **۱۱ ثانیه**.
  - محلی: **۲۰ ثانیه** بار اول، که ⚠️ بی‌اجازه **chrome-headless-shell** (۲۶۴ مگابایت) را در `~/.cache/hyperframes` دانلود کرد؛ خود رندر ۵.۴ ثانیه با beginframe و GPU سخت‌افزاری.
  - شباهت دو خروجی (SSIM) ۰.۹۹۷؛ با فونت محلی، Docker و محلی عملاً یکی‌اند.
  - خروجی: H.264، yuv420p، AAC ۴۸ کیلوهرتز، حدود ۱.۲ مگابایت.
  - ⚠️ بی‌خطر: بعد از رندر Docker هشدار `EROFS … video-state-lock` می‌آید (پوشه‌ی پروژه فقط‌خواندنی سوار شده)؛ رندر سالم است.
- 🔬 `npx hyperframes check` حدود ۵ ثانیه؛ هشدار `nested_structure_needs_subcomposition` برای صحنه‌های یک‌فایلی فقط درباره‌ی نمایش در Studio است و رندر را خراب نمی‌کند.
- ⚠️ مشکل‌های باز مهم: رندر روی WSL2 بدون کارت گرافیک و کند است (#5548)؛ `--docker` با دو ویدیوی هم‌زمان حدود فریم ۲۰۰ گیر می‌کند (#5473).
- 🧭 پیش از رندر کامل: ۳ تا ۶ تصویر ثابت با زیرنویس فارسی، بعد برگه‌ی فریم ([بازبینی](code-to-video.md#پرامپتها)). 🔬 دستور: `npx hyperframes snapshot --at 0,2,5.5,8.8 --no-end --describe false -o stills` (خودش برگه‌ی فریم هم می‌سازد؛ `--zoom "#id"` برای نگاه نزدیک). برگه‌ی فریم ویدیوی نهایی با FFmpeg: `ffmpeg -i out.mp4 -vf "fps=1,scale=270:480,tile=5x2" -frames:v 1 sheet.png`.

## قدم ۵: فارسی

- ✅ متن را Chrome می‌کشد، پس شکل‌دهی حروف فارسی همان شکل‌دهی مرورگر است. ✅ HyperFrames در نسخه‌ی 0.8.168 (۲۰۲۶-۱۰-۱۷) یک خطای غلط درباره‌ی `dir="rtl"` را برداشت و آزمون رندر عربی اضافه کرد (PR #5744).
- 🧭 `dir="rtl"`، فاصله‌ی حروف صفر، **هیچ‌وقت حرف تکی را متحرک نکن** (اتصال حروف می‌شکند)، نیم‌فاصله و رقم فارسی حفظ شود.
- 🔬 **آزمون ۲۰۲۶-۱۰-۱۸ (نسخه‌ی 0.8.171، Vazirmatn 33.003 محلی، هم Docker هم محلی):** اتصال حروف، نیم‌فاصله («می‌سازیم»، «گفت‌وگو»، «خانه‌ی»)، تنوین («لطفاً»)، «؟» و «٪» فارسی، رقم فارسی، و ترتیب متن مخلوط («نسخه‌ی 0.8.171 با رندر Docker») همه درست. بررسی خودکار هیچ خطایی درباره‌ی راست‌به‌چپ نداد. انیمیشن فقط روی کل خط (opacity، y، scale).
- 🔬 **شمارنده‌ی عدد فارسی:** مقدار را از خود timeline بساز (تابع `onUpdate` روی یک شیء GSAP که رقم‌ها را با جدول «۰۱۲۳۴۵۶۷۸۹» عوض می‌کند)، نه از ساعت؛ با جابه‌جایی در زمان درست می‌ماند (فریم میانی «۵۸٪» نشان داد).
- 🔬 **شکستن خط، تنها مشکل واقعی:** پیش‌نمایش اول تاریخ را دو تکه کرد («۲۶» | «مهر ۱۴۰۵») و یک کلمه را تنها در خط دوم گذاشت. `text-wrap: balance` خط‌ها را متعادل کرد ولی بعد «Claude Code» را وسط شکست. راه‌حل: `white-space: nowrap` روی هر نام لاتین و هر تاریخ ([سایت فارسی](../website/02-design/persian-rtl.md)). پس پیش‌نمایش ثابت **قبل** از رندر لازم است.
- 🔬 در Vazirmatn Black با اندازه‌ی خیلی بزرگ، «۰» یک حلقه است و «۱۰۰٪» از دور شبیه «100%» لاتین دیده می‌شود. برای عدد بزرگ تیتر، فونت یا وزن دیگری را هم امتحان کن.
- 🔬 فریم اول: تیتر از فریم ۰ روی صفحه است (بدون fade از سیاهی) تا تصویر کوچک شبکه‌ها خالی نباشد.
- 🔬 ⚠️ روی گرادیان تیره، H.264 با کیفیت standard کمی نوار رنگ (banding) دارد؛ برای انتشار high یا کمی نویز را امتحان کن (هنوز آزموده نشده).

## قدم ۶: صدا و زیرنویس

- صدای گوینده: ElevenLabs v3 یا v4؛ عدد را با حروف بنویس ([صداگذاری](ai-voice.md#elevenlabs)).
- زمان کلمه‌ها: faster-whisper با زبان `fa`، **هم‌تراز با متن خودمان** ([زیرنویس](captions-and-copy.md)). ✅ HyperFrames خودش رونویسی محلی دارد (Parakeet، در غیر این صورت Whisper large-v3 چندزبانه) و Remotion بسته‌ی `@remotion/captions` دارد. ⚠️ مثال‌های Remotion از مدل `medium.en` استفاده می‌کنند که فقط انگلیسی است.
- موسیقی از Openverse با CC0؛ افکت آرام روی ضرب‌ها.

## قدم ۷: تصویر تولیدی (فقط اگر لازم است)

🧭 فقط برای صحنه‌ای که با کد نمی‌شود (منظره، دست، محصول در محیط واقعی). **بدون متن در پرامپت**؛ متن فارسی را موتور کد رویش می‌گذارد.

| راه | اتصال | هزینه‌ی ۸ ثانیه | شرایط |
|---|---|---|---|
| Google Veo 3.1 Lite مستقیم | کلید API در یک اسکریپت کوچک | ۰.۴۰ دلار (با صدا) ✅ | ✅ روشن‌ترین: Google مالکیت ادعا نمی‌کند؛ SynthID |
| fal، همان مدل | `claude mcp add --transport http --scope user fal https://mcp.fal.ai/mcp-relay` (OAuth) | **۰.۲۴ دلار بی‌صدا** ✅ | ⚠️ شرایط fal دسترسی را «برای استفاده‌ی شخصی یا داخلی کسب‌وکار» می‌دهد؛ ❓ برای پست عمومی روشن نیست |
| Replicate، همان مدل | سرور MCP، توکن API | ۰.۴۰ دلار ✅ | مالکیت خروجی با تو، تابع شرایط مدل |
| Runway | `claude plugin install runway-api@runway-dev` | gen4_turbo حدود ۰.۴۰ دلار ✅ | مهارت قدیمی `rw-generate-video` بازنشسته شد |
| Higgsfield | `https://mcp.higgsfield.ai/mcp` | ❓ قیمت خوانده نشد | ⚠️ مالکیت نمی‌خواهد ولی **با خروجی و ورودی تو مدل آموزش می‌دهد** (جز Enterprise) |

✅ Veo 3.1 Lite نسبت ۹:۱۶ و تکه‌های ۴، ۶ یا ۸ ثانیه دارد و طبق مستندات فقط پرامپت انگلیسی کامل پشتیبانی می‌شود. 🧭 پیشنهاد: اول **Google مستقیم** (شرایط روشن)؛ fal فقط بعد از اینکه پاسخ روشن درباره‌ی انتشار عمومی گرفتی.

## قدم ۸: تحویل

- ✅ نسخه‌ی اصلی ۱۰۸۰×۱۹۲۰، H.264، AAC، منطقه‌ی امن متن ([ابعاد شبکه‌ها](platform-specs.md)).
- 🧭 برگه‌ی فریم نهایی: هماهنگی صدا، اتصال حروف، رقم‌ها، فریم اول.
- ✅ رسانه‌ی واقع‌نمای تولیدی برچسب هوش مصنوعی می‌خواهد ([انتشار](publishing.md)).

---

## ابزارهای دیگری که دیده شد

| ابزار | حکم | چرا |
|---|---|---|
| [Remotion](../../catalog/remotion.md) | ✅ | افزونه‌ی رسمی Claude Code: `claude plugin marketplace add remotion-dev/claude-code-plugin` و `claude plugin install remotion@remotion`؛ نسخه‌ی 4.0.536 |
| [Claude Motion](../../catalog/claude-motion.md) | 👀 | ابزار رسمی Anthropic (بتا، ۲۰۲۶-۱۰-۰۸)، فقط Team و Enterprise؛ ۹:۱۶ و فارسی گفته نشده |
| [OpenMontage](../../catalog/openmontage.md) | 👀 | ۱۲ مسیر تولید، ترکیب کد و مدل؛ AGPL؛ رشد ستاره‌ی خیلی سریع |
| [hypit](../../catalog/hypit.md) | ⛔ | «کپی هر ویدیوی وایرال» با تعویض چهره و صدا؛ لینک همکاری در فروش؛ مجوز تغییریافته |
| [onetake](../../catalog/onetake.md) | ⛔ | مجوز PolyForm **غیرتجاری** |
| [fal MCP](../../catalog/fal-mcp.md) | 👀 | ارزان‌ترین Veo Lite بی‌صدا؛ شرایط انتشار نامعلوم |
| [Higgsfield MCP](../../catalog/higgsfield-mcp.md) | 👀 | آموزش مدل با خروجی کاربر؛ قیمت خوانده نشد |
| [HeyGen MCP](../../catalog/heygen-mcp.md) | 👀 | فقط آواتار سخن‌گو؛ رضایت صاحب چهره لازم |
| Motion Canvas | 👀 | تقریباً غیرفعال (آخرین انتشار ۲۰۲۴) |
| Revideo | 👀 | MIT، بدون مهارت عامل؛ تله‌متری پیش‌فرض روشن |

---

## پرامپت‌ها

### شروع کلیپ با HyperFrames
```text
Make a [length]-second 9:16 (1080x1920) clip with HyperFrames about [topic], following
style-guide.md and brief.md. Persian on-screen text, right-to-left, our local Vazirmatn
font via @font-face, Persian digits, no per-letter animation. Keep Latin names and dates
on one line (white-space: nowrap) and use text-wrap: balance. Use only files in assets/
and audio/; load every library locally (no CDN). Do not run `hyperframes usage` and never
read Claude credentials. Before rendering: show me a shot list with a reason for each shot,
then 4 preview stills with the Persian text (snapshot with --describe false). After my approval, render with --docker at
standard quality and build a contact sheet to check text joining, digits, sync and the
first frame.
```

### تکه‌ی تولیدی بدون متن
```text
Write one English Veo 3.1 Lite prompt for an 8-second 9:16 shot of [scene]. No text, no
logos, no UI, no real people. Static or slow camera so we can lay Persian text over it in
code. Tell me the cost before generating and wait for my go.
```

## مرتبط

[ویدیو با کد](code-to-video.md) · [مدل‌های ویدیو](ai-video-models.md) · [زیرنویس و متن](captions-and-copy.md) · [صداگذاری](ai-voice.md) · [ابعاد شبکه‌ها](platform-specs.md) · کارت [HyperFrames](../../catalog/hyperframes.md)
