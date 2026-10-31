---
name: Mediabunny
slug: mediabunny
category: video
domains: [social-media]
verdict: trial
status: researched
summary: خواندن، نوشتن و تبدیل ویدیو و صدا در مرورگر با TypeScript خالص
use_when: "a website must trim or convert video in the user's browser ; building a render page that encodes frames to MP4 with WebCodecs ; reading or writing MP4/WebM/MP3/HLS in the browser"
how: "Trial first on a small task: use mediabunny (MPL-2.0, successor of the deprecated mp4-muxer) with WebCodecs; if you modify the library files themselves you must publish those changes; not yet tested in our projects"
url: https://mediabunny.dev
repo: "https://github.com/Vanilagy/mediabunny"
license: "MPL-2.0"
pricing: free
risk: low
sources: [S30, S58]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Mediabunny

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v1.65.0 (۲۰۲۶-۱۰-۳۰)؛ MPL-2.0 بی‌تغییر: https://github.com/Vanilagy/mediabunny/releases
✅ ابزار بدون وابستگی برای MP4، WebM، MP3 و HLS در مرورگر («FFmpeg برای وب»). نسخه‌ی 1.61.6 (۲۰۲۶-۱۰-۱۶)؛ Remotion اسپانسرش است.

## کی استفاده کنیم
🧭 اگر سایت باید ویدیو را در مرورگر کاربر برش دهد یا تبدیل کند. ✅ جانشین رسمی mp4-muxer (منسوخ) است؛ پس برای «صفحه‌ی رندر» که فریم‌ها را با WebCodecs روی کارت گرافیک خود کاربر MP4 می‌کند هم همین را بردار ([ویدیو با کد](../domains/social-media/code-to-video.md#ویدیوی-توضیحی-سهبعدی-با-صدای-فارسی)). 🧪 هنوز در پروژه‌ی خودمان امتحان نشده.

## قیمت و مجوز
✅ MPL-2.0 (کپی‌لفت در سطح فایل: اگر خود فایل‌های کتابخانه را تغییر دهی و منتشر کنی، باید کدشان را منتشر کنی).

## ریسک و هشدار
کم.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S30](../sources/README.md#s30)

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v1.64.0 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
