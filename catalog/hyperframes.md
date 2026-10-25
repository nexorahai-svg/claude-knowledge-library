---
name: HyperFrames (HeyGen)
slug: hyperframes
category: video
domains: [social-media]
verdict: trial
status: researched
summary: تبدیل HTML، CSS و انیمیشن قابل‌جابه‌جایی به MP4 قطعی؛ افزونه‌ی Claude Code دارد
url: https://hyperframes.heygen.com
repo: "https://github.com/heygen-com/hyperframes"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S30, S84, S151]
found_in: [batch-01/P04, batch-01/P12]
last_checked: 2026-10-24
next_check: "2027-01-15"
---

# HyperFrames (HeyGen)

## چیست
✅ فریم‌ورک متن‌باز HeyGen که صفحه‌ی HTML با انیمیشن‌های قابل جابه‌جایی در زمان را به MP4 قطعی تبدیل می‌کند. CLI و مهارت عامل؛ افزونه‌ی Claude Code: `claude plugin install hyperframes@hyperframes`. حدود ۶۵.۵ هزار ستاره؛ ساخته‌شده ۲۰۲۶-۰۳-۱۰؛ نسخه‌ی 0.8.167 (پیش از ۱.۰، خیلی فعال). Node ۲۲ به بالا.

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
🔬 یک کلیپ آزمایشی ۱۰ ثانیه‌ای ۹:۱۶ با متن فارسی در `~/Desktop/clip-test` ساختیم (ردیف دفتر پروژه‌ها). CLI 0.8.171 با نسخه‌ی ثابت داخل پروژه، افزونه با `--scope project`، تله‌متری و به‌روزرسانی خودکار خاموش، `hyperframes usage` در CLAUDE.md پروژه ممنوع. اتصال حروف، نیم‌فاصله، رقم فارسی و متن مخلوط درست بود؛ تنها مشکل شکستن خط بود که با CSS حل شد. رندر: Docker بار اول ۲ دقیقه و ۱۱ ثانیه (ساخت ایمیج ۲.۲۹ گیگابایتی)، بعد ۱۱ ثانیه؛ محلی ۵.۴ ثانیه رندر به‌اضافه‌ی دانلود بی‌اجازه‌ی chrome-headless-shell (۲۶۴ مگابایت). ⚠️ `snapshot --describe` اگر `GEMINI_API_KEY` باشد فریم‌ها را خودکار به Gemini می‌فرستد. ⚠️ مثال رسمی «minimal composition» هنوز GSAP را از CDN می‌خواند. جزئیات در [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md). حکم: هنوز trial (طبق قاعده، ✅ بعد از دو پروژه).

## نصب سراسری ۲۰۲۶-۱۰-۲۱
✅ (کد خوانده شد، commit `a8a8032`) نسخه‌ی 0.8.181، مجوز Apache-2.0، ۲۲ پوشه‌ی مهارت؛ MCP و hook ندارد؛ اسکریپت‌های داخل مهارت‌ها (`.mjs`، `.sh`، `.py`) فقط وقتی مهارت اجرا شود کار می‌کنند. ⚠️ اسکریپت‌های `media-use` (رونویسی، برش) خودشان به PostHog (`us.i.posthog.com`) آمار می‌فرستند، جدا از CLI؛ همان خاموش‌کن مشترک (`telemetryEnabled: false` در `~/.hyperframes/config.json` یا `HYPERFRAMES_NO_TELEMETRY=1` یا `DO_NOT_TRACK=1`) هر دو را می‌بندد. ⚠️ `hyperframes usage` هنوز در چهار مهارت خواسته می‌شود و هنوز توکن ورود Claude Code را می‌خواند.
✅ روی رایانه‌ی اصلی در سطح کاربر نصب شد، با این محافظ‌ها:
```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes --scope user
```
- `~/.hyperframes/config.json`: `"telemetryEnabled": false`
- `~/.claude/settings.json`: `env.HYPERFRAMES_NO_TELEMETRY = "1"` و در `permissions.deny`: `Bash(npx hyperframes usage:*)` و `Bash(hyperframes usage:*)`
- یک بند در `~/.claude/CLAUDE.md` کاربر: `usage` اجرا نشود، نسخه‌ی CLI در هر پروژه ثابت، فونت فارسی محلی، بدون `GEMINI_API_KEY`.
تماس‌های شبکه‌ی دیگر در مهارت‌ها فقط با کلید خودمان: HeyGen API، Gemini، Openverse، نقشه‌ی پایه (Carto، ArcGIS)، و jsDelivr برای کتابخانه‌ها.

## رندر بلند ۹۰ ثانیه تا ۵ دقیقه (نسخه‌ی 0.8.171) 🔬
- 🔬 `/tmp` در این رایانه tmpfs با ۱۶ گیگ است و استخراج فریم پرش کرد («Video extraction failed … ffmpeg_failed=29») ← `TMPDIR` و `--frames-cache-dir` را روی دیسک بزرگ (`/data`) بگذار.
- 🔬 رندر ۵ دقیقه‌ای با ۴۳ کلیپ: «Reached heap limit» در Node ← `NODE_OPTIONS=--max-old-space-size=12288` و `--workers 3`.
- 🔬 `--video-frame-format jpg` شکست خورد («Invalid JPEG input at frame 0: empty frame»)؛ png کار می‌کند.
- 🔬 پس از OOM حدود ۲۵ پردازش یتیم chrome-headless-shell ماند ← دستی بکُش.
- 🔬 اسکریپت نگهبان RAM با `pgrep -f "hyperframes render"` خودش را هم می‌گرفت و هرگز تمام نمی‌شد ← الگوی براکتی `'[h]yperframes render'`.
- 🔬 کلیپ‌های استوک را پیش از چیدن با ffmpeg برش و کند کن (`scale`+`crop` به 1920×1080 یا 1080×1920، `setpts` ۱٫۲ تا ۱٫۲۵). [S151](../sources/README.md#s151) · دفتر پروژه‌ها (یک پروژه‌ی مشتری / Nexorah AI social، personal family videos)

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S30](../sources/README.md#s30) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S84](../sources/README.md#s84)
