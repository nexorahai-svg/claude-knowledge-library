---
name: HyperFrames (HeyGen)
slug: hyperframes
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: تبدیل HTML، CSS و انیمیشن قابل‌جابه‌جایی به MP4 قطعی؛ افزونه‌ی Claude Code دارد
use_when: "making an MP4 video from HTML, CSS and seekable animations without React ; deterministic video render with a Claude Code plugin"
how: "install the Claude plugin from the card, pin the CLI version in the project, set HYPERFRAMES_NO_TELEMETRY=1 (PostHog telemetry is on by default), never run `hyperframes usage`, keep Persian fonts local (Apache-2.0)"
url: https://hyperframes.heygen.com
repo: "https://github.com/heygen-com/hyperframes"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S30, S84, S151, S208]
found_in: [batch-01/P04, batch-01/P12]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# HyperFrames (HeyGen)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی npm latest: 0.8.223 (GitHub ۲۰۲۶-۱۰-۳۱)؛ Apache-2.0 بی‌تغییر: https://github.com/heygen-com/hyperframes/releases
✅ (جاروی ۲۰۲۶-۱۰-۲۸) یادداشت انتشارهای 0.8.205 تا 0.8.209: فرمان `hyperframes check` صدایی را که بی‌صدا رندر می‌شود هشدار می‌دهد؛ رندر می‌تواند فاصله‌ی keyframe و سقف bitrate بگیرد؛ Studio خروجی GIF با تعداد تکرار می‌دهد؛ روی ویندوز CLI پیشنهاد دانلود اپ HyperFrames می‌دهد.
✅ (۲۰۲۶-۱۰-۳۰) نسخه‌ی npm latest: 0.8.221 (۲۰۲۶-۱۰-۳۰؛ همان روز از 0.8.217 تا 0.8.220 هم رد شد؛ [S208](../sources/README.md#s208)). انتشارها تقریباً هر روز می‌آیند؛ Apache-2.0 بی‌تغییر؛ هنوز پیش از ۱.۰، نسخه را در پروژه ثابت کن.
✅ فریم‌ورک متن‌باز HeyGen که صفحه‌ی HTML با انیمیشن‌های قابل جابه‌جایی در زمان را به MP4 قطعی تبدیل می‌کند. CLI و مهارت عامل؛ افزونه‌ی Claude Code: `claude plugin install hyperframes@hyperframes`. حدود ۶۵.۵ هزار ستاره؛ ساخته‌شده ۲۰۲۶-۰۳-۱۰؛ نسخه‌ی 0.8.167 (پیش از ۱.۰، خیلی فعال). Node ۲۲ به بالا.

## دستور سریع

**نصب** (✅ [README](https://github.com/heygen-com/hyperframes) و npm؛ آخرین `0.8.223`، آزمون ما روی `0.8.171` بود؛ پیش از ۱.۰ است، نسخه را در **پروژه** ثابت کن، نه سراسری):
```bash
export HYPERFRAMES_NO_TELEMETRY=1                  # PostHog پیش‌فرض روشن است
npm install --save-dev --save-exact hyperframes@0.8.223
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes --scope project
```
**حداقل اجرا** (✅ مستند CLI؛ Node ۲۲ به بالا و FFmpeg):
```bash
npx hyperframes init my-video && cd my-video
npx hyperframes lint && npx hyperframes check
npx hyperframes render --output out.mp4 --quality draft --workers 2
```
**تنظیم‌های مهم**
- ✅ `--workers` هر کدام یک Chrome جدا و حدود `256 MB` است؛ با ۸ گیگ RAM یا کمتر حالت `--low-memory-mode` خودکار روشن می‌شود. 🔬 روی رایانه‌ی تحت فشار `2` بگذار و با محافظ منابع (`resource_guard.py run --mem 6G --`) اجرا کن.
- ✅ `--quality`: `draft` برای بازبینی، پیش‌فرض `looks` (CRF 16)؛ `--crf` و `--max-bitrate` برای فایل سبک. `--no-browser-gpu` خروجی قطعی‌تر می‌دهد.
- 🔬 رندر بلند (۵ دقیقه، ۴۳ کلیپ): `NODE_OPTIONS=--max-old-space-size=12288` و `--workers 3`؛ `TMPDIR` و `--frames-cache-dir` را روی دیسک بزرگ بگذار اگر `/tmp` فضای رم است.

**خطاهای رایج**
- ⚠️ `hyperframes usage` را هرگز اجرا نکن (توکن ورود Claude Code را می‌خواند)؛ `snapshot --describe` با `GEMINI_API_KEY` فریم‌ها را به Gemini می‌فرستد؛ فونت فارسی را محلی بگذار. جزئیات در بخش «ریسک و هشدار» و «نصب سراسری» همین کارت.
- 🔬 انیمیشن GSAP روی `letterSpacing` خطای lint `gsap_non_transform_motion` می‌دهد → `scaleX`. `--video-frame-format jpg` شکست خورد؛ `png` کار می‌کند (پیش‌فرض `auto`، برای ضبط صفحه‌نمایش `png`).
- 🔬 بعد از OOM حدود ۲۵ پردازش `chrome-headless-shell` یتیم می‌ماند؛ دستی بکش. swap بالا بعد از آزاد شدن RAM رندر را رد می‌کند (خطا از ffmpeg می‌آید).

## کی استفاده کنیم
🧭 ساده‌ترین مسیر برای ویدیو از HTML بدون React؛ مجوز ساده‌تر از Remotion.

## قیمت و مجوز
✅ Apache-2.0، رایگان.

## ریسک و هشدار
✅ کد افزونه در بازبینی‌های ۲۰۲۶-۱۰-۱۸ و ۲۰۲۶-۱۰-۲۱ خوانده شد (پایین). ❓ اینکه در فهرست افزونه‌های Claude «تأییدشده‌ی Anthropic» است، فقط از نتیجه‌ی جستجو آمده.

## بازبینی ۲۰۲۶-۱۰-۱۸
✅ نسخه‌ی 0.8.171 (۲۰۲۶-۱۰-۱۸)، حدود ۶۶.۵ هزار ستاره، ۲.۶۵ میلیون دانلود npm در یک ماه (۱۷ سپتامبر تا ۱۶ اکتبر). مجوز Apache-2.0 (فایل LICENSE خوانده شد)؛ بدون هزینه‌ی هر رندر و بدون سقف تجاری.
✅ (کد خوانده شد) افزونه‌ی Claude hook و MCP ندارد؛ ۲۱ مهارت. ⚠️ **تله‌متری PostHog پیش‌فرض روشن**: `npx hyperframes telemetry disable` یا `HYPERFRAMES_NO_TELEMETRY=1`. ⚠️ مهارت اصلی در شروع هر کار `npx hyperframes usage --json` را می‌خواهد که **توکن ورود Claude Code** را از keychain یا `~/.claude/.credentials.json` می‌خواند و به `api.anthropic.com` می‌فرستد (`packages/cli/src/utils/harnessUsage.ts`). در CLAUDE.md پروژه منعش کن.
✅ راست‌به‌چپ: PR #5744 در 0.8.168 آزمون رندر عربی اضافه کرد. ⚠️ دانلودگر فونت زیرمجموعه‌ی لاتین را ترجیح می‌دهد؛ فونت فارسی را محلی بگذار. ⚠️ پیش از ۱.۰ و چند انتشار در روز؛ نسخه را ثابت کن.

## تجربه‌ی پروژه ۲۰۲۶-۱۰-۱۸ 🔬
🔬 یک کلیپ آزمایشی ۱۰ ثانیه‌ای ۹:۱۶ با متن فارسی ساختیم. CLI 0.8.171 با نسخه‌ی ثابت داخل پروژه، افزونه با `--scope project`، تله‌متری و به‌روزرسانی خودکار خاموش، `hyperframes usage` در CLAUDE.md پروژه ممنوع. اتصال حروف، نیم‌فاصله، رقم فارسی و متن مخلوط درست بود؛ تنها مشکل شکستن خط بود که با CSS حل شد. رندر: Docker بار اول ۲ دقیقه و ۱۱ ثانیه (ساخت ایمیج ۲.۲۹ گیگابایتی)، بعد ۱۱ ثانیه؛ محلی ۵.۴ ثانیه رندر به‌اضافه‌ی دانلود بی‌اجازه‌ی chrome-headless-shell (۲۶۴ مگابایت). ⚠️ `snapshot --describe` اگر `GEMINI_API_KEY` باشد فریم‌ها را خودکار به Gemini می‌فرستد. ⚠️ مثال رسمی «minimal composition» هنوز GSAP را از CDN می‌خواند. جزئیات در [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md). حکم: هنوز trial (طبق قاعده، ✅ بعد از دو پروژه).

## نصب سراسری ۲۰۲۶-۱۰-۲۱
✅ (کد خوانده شد، commit `a8a8032`) نسخه‌ی 0.8.181، مجوز Apache-2.0، ۲۲ پوشه‌ی مهارت؛ MCP و hook ندارد؛ اسکریپت‌های داخل مهارت‌ها (`.mjs`، `.sh`، `.py`) فقط وقتی مهارت اجرا شود کار می‌کنند. ⚠️ اسکریپت‌های `media-use` (رونویسی، برش) خودشان به PostHog (`us.i.posthog.com`) آمار می‌فرستند، جدا از CLI؛ همان خاموش‌کن مشترک (`telemetryEnabled: false` در `~/.hyperframes/config.json` یا `HYPERFRAMES_NO_TELEMETRY=1` یا `DO_NOT_TRACK=1`) هر دو را می‌بندد. ⚠️ `hyperframes usage` هنوز در چهار مهارت خواسته می‌شود و هنوز توکن ورود Claude Code را می‌خواند.
✅ در سطح کاربر نصب شد، با این محافظ‌ها:
```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes --scope user
```
- `~/.hyperframes/config.json`: `"telemetryEnabled": false`
- `~/.claude/settings.json`: `env.HYPERFRAMES_NO_TELEMETRY = "1"` و در `permissions.deny`: `Bash(npx hyperframes usage:*)` و `Bash(hyperframes usage:*)`
- یک بند در `~/.claude/CLAUDE.md` کاربر: `usage` اجرا نشود، نسخه‌ی CLI در هر پروژه ثابت، فونت فارسی محلی، بدون `GEMINI_API_KEY`.
تماس‌های شبکه‌ی دیگر در مهارت‌ها فقط با کلید خودمان: HeyGen API، Gemini، Openverse، نقشه‌ی پایه (Carto، ArcGIS)، و jsDelivr برای کتابخانه‌ها.

## رندر بلند ۹۰ ثانیه تا ۵ دقیقه (نسخه‌ی 0.8.171) 🔬
- 🔬 `/tmp` در رایانه‌ی آزمون tmpfs با ۱۶ گیگ است و استخراج فریم پرش کرد («Video extraction failed … ffmpeg_failed=29») ← `TMPDIR` و `--frames-cache-dir` را روی دیسک بزرگ (`/data`) بگذار.
- 🔬 رندر ۵ دقیقه‌ای با ۴۳ کلیپ: «Reached heap limit» در Node ← `NODE_OPTIONS=--max-old-space-size=12288` و `--workers 3`.
- 🔬 `--video-frame-format jpg` شکست خورد («Invalid JPEG input at frame 0: empty frame»)؛ png کار می‌کند.
- 🔬 پس از OOM حدود ۲۵ پردازش یتیم chrome-headless-shell ماند ← دستی بکُش.
- 🔬 اسکریپت نگهبان RAM با `pgrep -f "hyperframes render"` خودش را هم می‌گرفت و هرگز تمام نمی‌شد ← الگوی براکتی `'[h]yperframes render'`.
- 🔬 کلیپ‌های استوک را پیش از چیدن با ffmpeg برش و کند کن (`scale`+`crop` به 1920×1080 یا 1080×1920، `setpts` ۱٫۲ تا ۱٫۲۵). [S151](../sources/README.md#s151)

## دسته‌ی ۹۳ صفحه‌ی راهنما × ۶ نسخه (0.8.171، ۲۰۲۶-۱۰-۳۰) 🔬
- 🔬 یک محصول وب : هر صفحه ← صدای ElevenLabs (فارسی، عربی، انگلیسی) ← `npx hyperframes render . -o raw.mp4 --workers 2 --no-browser-gpu --quiet` زیر `resource_guard.py run --mem 6G` ← ffmpeg `libx264 crf 27 yuv420p bt709 tv faststart`. خروجی ۵۵۸ mp4 برای ۹۳ شناسه در حدود ۲ روز؛ هر کلیپ زبانی ۳۵ تا ۵۰ ثانیه رندر، هر صفحه (۶ ویدیو) ۷ تا ۸ دقیقه؛ ۰ زیرنویس بریده (بررسی روی ۵۵۸ فایل).
- 🔬 جدا کردن مرحله‌ها (`STAGE=prep/finish`)، انتظار نگهبان منابع در هر گام، نشانگرهای `PAGE_DONE`/`STEP_FAILED` در لاگ و یک ناظر پس‌زمینه جواب داد. **دام:** swap که بعد از آزاد شدن RAM بالای ۶۰٪ می‌ماند (۲۰ دقیقه با ۱۵ گیگ آزاد) کار سنگین را بی‌پایان رد می‌کند؛ رندر رد شد، `raw.mp4` نبود و خطا از ffmpeg (کد ۲۵۴) آمد نه از رندر. صف ادامه‌یافته بعدها ۱۰ گام را بی‌خطا تمام کرد.
- 🔬 **کادر برجسته با تطبیق متن:** پیدا کردن اولین عنصر دیدنی که `innerText`اش واژه‌های راهنما را دارد، در ۱۶ صفحه کادر را روی خط معرفی صفحه (y≈۶۲، h≈۲۱) و در ۱ صفحه روی آیکون منوی کناری گذاشت. اصلاح: فقط عنصرهای با `getBoundingClientRect().top >= 80` و `!closest('nav,aside')`؛ با بازفیلم‌برداری ۲۱ صفحه، ۷۱ از ۱۲۶ نسخه کادر تازه گرفت و ۰ در سربرگ/منو ماند. اسکن خودکار `boxes.json` (y بین ۵۰ و ۷۵، h ≤ ۲۶، w > ۳۰۰) بیش از ۵ فریم کنتاکت‌شیت پیدا کرد.
- 🔬 **بازبینی با کنتاکت‌شیت:** ffmpeg ۵ فریم (۱۰/۳۰/۵۰/۷۰/۹۰٪) × ۳ نسخه (فارسی تیره، عربی روشن، انگلیسی تیره) را در یک jpg ۱۹۲۰×۶۴۸ برای هر شناسه می‌چیند. `ffprobe` و `subcheck` روی ۵۵۸ فایل ۰ مشکل گفتند ولی ۹۳ شیت ۴ ایراد داده‌ی دمو پیدا کرد (کلید ترجمه‌ی خام `b2b.inv_status_issued`، «۲۰۷۳۴ d ago» از ثانیه به‌جای میلی‌ثانیه، وضعیت «legacy mode»، دلیل برگشت خام). بررسی فایل/قالب این‌ها را نمی‌بیند. بازبین زیرعامل و چیدن ffmpeg هنگام swap بالا توسط hook منابع رد شد؛ شیت‌ها یکی‌یکی خوانده شد (حدود ۱۶ خواندن، هر بار ۶ شیت).

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S30](../sources/README.md#s30) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S84](../sources/README.md#s84)

🔬 (۲۰۲۶-۱۰-۳۰، نسخه‌ی 0.8.171) انیمیشن GSAP روی `letterSpacing` خطای lint `gsap_non_transform_motion` می‌دهد؛ `scaleX` جایگزین است. هشدار `nested_structure_needs_subcomposition` بی‌ضرر بود. برای بازبینی `snapshot --at ... --no-end --describe false` کافی است. خروجی JSON در `loudnorm` ffmpeg در stderr است و بعدش متن اضافه دارد؛ تا آخرین `}` ببُر.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.

🔬 (۲۰۲۶-۱۰-۳۱) مقایسه‌ی 0.8.171 و 0.8.221 روی یک آزمون ۶ ثانیه‌ای 1080×1920 با ۲ worker: ۹ در برابر ۵ ثانیه، بیشترین اختلاف پیکسل ۸ از ۲۵۵، قالب خروجی یکسان. فقط یک آزمون کوتاه است و ریل کامل روی 0.8.221 رندر نشد؛ پیش از ارتقای پروژه با نسخه‌ی پین‌شده بیازما.
