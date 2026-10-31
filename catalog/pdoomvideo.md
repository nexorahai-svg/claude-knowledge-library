---
name: PDoomVideo
slug: pdoomvideo
category: video
domains: [social-media]
verdict: assess
status: researched
summary: موزیک‌ویدیوی ساخته‌شده با Opus و زیرعامل‌های موازی؛ بدون مجوز — فقط برای مطالعه
url: https://github.com/JohnHeibel/PDoomVideo
repo: "https://github.com/JohnHeibel/PDoomVideo"
license: "بدون مجوز (همه‌ی حقوق محفوظ)"
pricing: free
risk: medium
sources: [S31]
found_in: [batch-01/P04]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# PDoomVideo

## چیست
✅ ۲٬۱۶۶ ستاره (پست گفته بود حدود ۱.۱ هزار). شامل ANIMATION_GUIDE.md و STORYBOARD.md که خود Opus برای هدایت زیرعامل‌های موازی نوشته؛ ۹ فصل که هر کدام مال یک زیرعامل است. قواعد راهنما: هر نما تابع خالص زمان؛ فریم‌ها موازی و بی‌ترتیب رندر می‌شوند؛ عدد تصادفی ممنوع (به‌جایش hash).

## کی استفاده کنیم
🧭 **فقط برای یاد گرفتن روش** (به‌خصوص تقسیم کار بین زیرعامل‌ها). کد را استفاده نکن.

## قیمت و مجوز
✅ فایل مجوز ندارد → از نظر قانونی همه‌ی حقوق محفوظ است.

## ریسک و هشدار
اسکریپت render.mjs با puppeteer-core مرورگر Chrome و ffmpeg را اجرا می‌کند؛ پرچم `--allow-file-access-from-files` دارد. قبل از اجرا کامل بخوان.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S31](../sources/README.md#s31)
