---
name: YouTube AI Motion Graphics (بوردهای موشن‌گرافیک)
slug: youtube-ai-motion-graphics
category: video
domains: [social-media]
verdict: assess
status: researched
summary: مخزن MIT با ۷۴ بورد موشن‌گرافیک HTML و GSAP برای ویدیوی توضیحی یوتیوب، سه skill برای Claude Code و همگام‌سازی کلمه‌به‌کلمه با صدا از راه Whisper
use_when: "explainer video with charts, diagrams or counters synced to a voice-over ; studying a board-plus-voice-sync method next to HyperFrames"
how: "Do not install without the user's yes. Read only, do not run setup.sh blindly: it may pipe the uv installer from the web, pip-installs faster-whisper, playwright and static-ffmpeg, and the first run downloads a 1.6 GB Whisper model; copy the method, never the board designs; compare with HyperFrames first"
url: https://github.com/sirioberati/YouTube-AI-Motion-Graphics
repo: "https://github.com/sirioberati/YouTube-AI-Motion-Graphics"
license: "MIT"
pricing: free
risk: medium
sources: [S198]
found_in: [watch-2026-10-28-2]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# YouTube AI Motion Graphics (بوردهای موشن‌گرافیک)

## چیست
✅ (GitHub API و فایل‌های مخزن، ۲۰۲۶-۱۰-۲۸) مجوز MIT، ساخته‌شده در ۲۰۲۶-۱۰-۲۷، حدود ۵۶ ستاره. محتوای مخزن:
- ۷۴ بورد موشن‌گرافیک در اندازه‌ی ۱۹۲۰×۱۰۸۰ با HTML و GSAP: نمودار، دیاگرام، شمارنده و گراف گره‌ای.
- سه skill: `explainer-board-brief`، `explainer-board-system` و `board-sync`.
- همگام‌سازی کلمه‌به‌کلمه با faster-whisper.
- خروجی MP4 فریم‌دقیق با Chrome و FFmpeg.
- فایل `checks.md` که هر اصلاح را به یک قانون «بکن / نکن» تبدیل می‌کند.

- ⚠️ آخرین push مخزن ۲۰۲۶-۱۰-۲۷؛ مخزن یک روزه است و هنوز release یا سابقه‌ی نگهداری ندارد (❓ پایداری).

README فهرست انتظار محصول tein.ai و یک جامعه‌ی Skool را هم تبلیغ می‌کند.

## کی استفاده کنیم
👀 فعلاً فقط برای یادگرفتن روش: بورد جدا برای هر جمله، همگام با زمان کلمه‌ها، و فایل چک‌ها برای قانون‌های طراحی. ساخت ویدیو را با [HyperFrames](hyperframes.md) انجام بده که داریم. این مخزن را کنار آن بسنج ([ویدیو از کد](../domains/social-media/code-to-video.md)).

## قیمت و مجوز
✅ کد MIT. فایل `gsap.min.js` همراه مخزن است و مجوز خود GSAP را دارد.

## ریسک و هشدار
✅ این‌ها را خواندم: `setup.sh`، `requirements.txt`، `tools/setup-check.sh`، `tools/export.py` و `board_sync.py` و اسکریپت‌هایش.
- **دانلودها:** اگر uv نصب نباشد، `setup.sh` نصب‌کننده‌ی آن را با `curl | sh` می‌گیرد. پکیج‌های faster-whisper، playwright و static-ffmpeg را نصب می‌کند. اگر ffmpeg نباشد آن را دانلود می‌کند، و اگر مرورگری نباشد Chromium Playwright را (حدود ۱۵۰ مگابایت). اولین اجرای Whisper حدود ۱٫۶ گیگابایت مدل دانلود می‌کند.
- **تله‌متری:** در اسکریپت‌هایی که خواندم تله‌متری یا ارسال داده دیده نشد.
- **✅ خوانده شد (۲۰۲۶-۱۰-۲۸):** `skills/board-sync/assets/kit.js` (حدود ۱۳ کیلوبایت) و `player.html` (۷۶۲ بایت): هیچ fetch، XHR، WebSocket، sendBeacon، eval یا آدرس خارجی نداشتند. `tools/make_gifs.py` فقط ffmpeg محلی را صدا می‌زند.
- **❓ هنوز:** بقیه‌ی ۷۴ بورد و `docs/` را نخواندم؛ هر بورد را پیش از باز کردن در مرورگر ببین.
- **کپی نکن:** طرح بوردها را کپی نکن. فقط روش را بردار.

## مرتبط
[S198](../sources/README.md#s198) · [HyperFrames](hyperframes.md) · [Remotion](remotion.md) · [ویدیو از کد](../domains/social-media/code-to-video.md)
