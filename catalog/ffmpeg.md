---
name: FFmpeg
slug: ffmpeg
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: ابزار خط فرمان استاندارد برای ساخت و تبدیل ویدیو؛ فریم‌های PNG را به MP4 تبدیل می‌کند
url: https://ffmpeg.org
repo: "https://github.com/FFmpeg/FFmpeg"
license: "LGPL-2.1+ (بخش‌هایی GPL)"
pricing: free
risk: low
sources: [S31, S151]
found_in: [batch-01/P04, batch-01/P24]
last_checked: 2026-10-24
next_check: "2027-01-15"
---

# FFmpeg

## چیست
✅ ابزار استاندارد ویدیو. دستور پایه از ویکی رسمی:
```bash
ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -pix_fmt yuv420p out.mp4
```
✅ `-pix_fmt yuv420p` برای پخش در همه‌ی پخش‌کننده‌ها لازم است؛ بدون `-framerate` پیش‌فرض ۲۵ فریم است. ❓ بخش `-c:v libx264` در همان صفحه‌ی ویکی صریح نبود (استاندارد است).

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
- 🔬 نسخه‌ی سبک برای فرستادن: crf 25 تا 28 و maxrate 1.5 تا 2.6M. [S151](../sources/README.md#s151) · دفتر پروژه‌ها (یک پروژه‌ی مشتری / Nexorah AI social، personal family videos)

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S31](../sources/README.md#s31)
