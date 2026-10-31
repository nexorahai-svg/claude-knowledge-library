---
name: FFmpeg
slug: ffmpeg
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: ابزار خط فرمان استاندارد برای ساخت و تبدیل ویدیو؛ فریم‌های PNG را به MP4 تبدیل می‌کند
use_when: "turning rendered PNG frames into an MP4 ; converting video or making contact sheets for review"
how: "ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -pix_fmt yuv420p out.mp4 (yuv420p is needed for all players; default is 25 fps); running the CLI is not distribution, but libx264 is GPL"
url: https://ffmpeg.org
repo: "https://github.com/FFmpeg/FFmpeg"
license: "LGPL-2.1+ (بخش‌هایی GPL)"
pricing: free
risk: low
sources: [S31, S151]
found_in: [batch-01/P04, batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# FFmpeg

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) هشدار «سایت جواب نداد» خطای بررسی‌کننده بود؛ https://ffmpeg.org/download.html پاسخ ۲۰۰ می‌دهد و 9.0.2 و 8.1.3 و 8.0.3 همان نسخه‌های این کارت‌اند. 🧭 برچسب‌های GitHub معیار نیستند، سایت معیار است.
✅ ابزار استاندارد ویدیو. دستور پایه از ویکی رسمی:
```bash
ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -pix_fmt yuv420p out.mp4
```
✅ `-pix_fmt yuv420p` برای پخش در همه‌ی پخش‌کننده‌ها لازم است؛ بدون `-framerate` پیش‌فرض ۲۵ فریم است. ✅ اصلاح: صفحه‌ی ویکی https://trac.ffmpeg.org/wiki/Slideshow در همین مثال‌ها `-c:v libx264` را صریح آورده است.

## دستور سریع

**نصب** (✅ [ffmpeg.org/download](https://ffmpeg.org/download.html): انتشارهای فعلی `9.0.2`، `8.1.3`، `8.0.3`؛ 🧭 بسته‌ی دیسترو معمولاً قدیمی‌تر است، نسخه را با `ffmpeg -version` ببین):
```bash
sudo apt install ffmpeg      # Debian/Ubuntu
ffmpeg -version | head -1
```
**حداقل اجرا** (✅ ویکی رسمی [H.264](https://trac.ffmpeg.org/wiki/Encode/H.264)): فریم‌های PNG به MP4 سازگار با وب.
```bash
ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -movflags +faststart out.mp4
```
**تنظیم‌های مهم**
- ✅ `-crf`: بازه ۰ تا ۵۱، پیش‌فرض ۲۳، بازه‌ی معقول ۱۷ تا ۲۸؛ هر ۶ واحد بالاتر حدود نصف حجم. 🔬 نسخه‌ی سبک برای فرستادن: `crf 25` تا `28`.
- ✅ `-preset` از `ultrafast` تا `veryslow` (پیش‌فرض `medium`)؛ `slow` فشرده‌تر ولی کندتر. `-movflags +faststart` برای پخش در مرورگر.
- ✅ `loudnorm` سیگنال را برای تشخیص peak به `192 kHz` می‌برد؛ پس `-ar 48000` بگذار. 🔬 هدف: `loudnorm=I=-14:TP=-1.5`.

**خطاهای رایج**
- ✅ بدون `-pix_fmt yuv420p` برخی پخش‌کننده‌ها (QuickTime) فایل را باز نمی‌کنند؛ بدون `-framerate` پیش‌فرض ورودی تصویر ۲۵ فریم است.
- 🔬 خروجی JSON حالت `print_format=json` در `loudnorm` در stderr است و متن اضافه دارد؛ تا آخرین `}` ببُر. صدای محیط کلیپ‌های تولید‌شده را با `-an` بردار.
- 🔬 آلفا: `alphamerge` به VP9 `yuva420p` با `-auto-alt-ref 0` ([روش](../domains/social-media/motion-design-styles.md)). ✅ `libx264` GPL است؛ اجرای CLI توزیع نیست ولی همراه محصول منتشر نکن.

## کی استفاده کنیم
🧭 قدم آخر هر ویدیوی ساخته‌شده با کد؛ ساخت برگه‌ی فریم (contact sheet) برای بازبینی.

## قیمت و مجوز
✅ (https://ffmpeg.org/legal.html) FFmpeg تحت LGPL 2.1 یا بالاتر؛ بخش‌های اختیاری مثل libx264 GPL هستند. 🧭 الزامات مجوز درباره‌ی **توزیع** نرم‌افزار است؛ اجرای CLI روی ویدیوی خودت توزیع نیست. اگر روزی اپی ساختی که FFmpeg را همراهش منتشر می‌کند، مجوز مهم می‌شود.

## ریسک و هشدار
کم.

## یافته‌های ویدیوی خانوادگی ۲۰۲۶-۱۰-۲۴ 🔬
- 🔬 بالاکشی 720p به 1080p وقتی دانلود Upscaled نبود: `scale=1920:1080:flags=lanczos,unsharp=5:5:0.4` (قابل‌قبول).
- 🔬 صدای محیط کلیپ‌های Flow را با `-an` بردار.
- 🔬 میکس: موسیقی −۹ تا −۱۳ دسی‌بل، `sidechaincompress` زیر صدا (threshold 0.02، ratio 3 تا 4، attack 60 تا 80 ms، release 600 تا 900 ms)، و `loudnorm` روی −14 LUFS و −1.5 dBTP.
- 🔬 نسخه‌ی سبک برای فرستادن: crf 25 تا 28 و maxrate 1.5 تا 2.6M. [S151](../sources/README.md#s151)

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S31](../sources/README.md#s31)

🔬 (۲۰۲۶-۱۰-۳۱) نشانی نسخه‌ی تاریخ‌دار BtbN پاک می‌شود و یکی ۴۰۴ داد. در نصب‌کننده‌ی محصول، کپی خودت را روی میزبان خودت نگه دار.
