---
name: Mixkit (ویدیو و صدای رایگان)
slug: mixkit
category: assets-media
domains: [social-media]
verdict: adopt
status: researched
summary: کلیپ ویدیوی استوک رایگان با مجوز Mixkit، قابل‌خواندن با اسکریپت
use_when: "need free stock video for backgrounds or cover scenes in a clip"
how: "Open mixkit.co video pages (JSON-LD VideoObject contentUrl assets.mixkit.co/videos/{id}/{id}-1080.mp4) and download under the Mixkit Video License; avoid culturally wrong stock; adjust crop x for vertical frame; trim and slow with ffmpeg"
url: https://mixkit.co
repo: ""
license: "Mixkit Video License (https://mixkit.co/license/#videoFree)"
pricing: free
risk: low
sources: [S151]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-22"
---

# Mixkit

## چیست
🔬 صفحه‌ها با اسکریپت قابل‌خواندن‌اند؛ داده‌ی ویدیو در JSON-LD از نوع VideoObject است و `contentUrl` به شکل `assets.mixkit.co/videos/{id}/{id}-1080.mp4` است. در مقابل صفحه‌های Pexels به اسکریپت ۴۰۳ می‌دهند.

## کی استفاده کنیم
🔬 پوشش و صحنه‌های پس‌زمینه. از استوک نامناسب فرهنگی (مثلاً شام کریسمس) برای داستان خانواده‌ی ایرانی دوری کن. کلیپ افقی را در قاب عمودی ببین: دست و چهره از قاب افتاد ← مقدار برش x را تنظیم کن.

## قیمت و مجوز
رایگان؛ مجوز در https://mixkit.co/license/#videoFree. ❓ شرط دقیق استفاده‌ی تجاری و ذکر منبع در این بار کامل خوانده نشد.

## ریسک و هشدار
پیش‌برش و کندکردن با ffmpeg لازم می‌شود ([HyperFrames](hyperframes.md)).

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [کتابخانه‌ی صدا](../domains/social-media/sound-library.md) · [Openverse](openverse.md) · [S151](../sources/README.md#s151)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
