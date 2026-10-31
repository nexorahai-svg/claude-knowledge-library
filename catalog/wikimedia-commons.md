---
name: Wikimedia Commons (تصویر تاریخی)
slug: wikimedia-commons
category: assets-media
domains: [social-media, website]
verdict: adopt
status: researched
summary: تصویر دامنه‌ی عمومی و CC0 از API ویکی‌مدیا برای ویدیوهای تاریخی
use_when: "need historical or era images for a historical video"
how: "Query the Wikimedia API with a descriptive User-Agent, backoff and pauses (generic UA gives HTTP 429); keep only LicenseShortName Public domain or CC0; show small 300-600px images as framed prints; check each file licence"
url: https://commons.wikimedia.org
repo: ""
license: "هر فایل مجوز خودش را دارد"
pricing: free
risk: low
sources: [S151]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Wikimedia Commons

## چیست
🔬 API ویکی‌مدیا با User-Agent عمومی HTTP 429 داد؛ با User-Agent توصیفی، backoff و مکث بین درخواست‌ها کار کرد. با `LicenseShortName` فقط Public domain و CC0 را نگه دار. بسیاری از تصویرهای تاریخی کوچک‌اند (۳۰۰ تا ۶۰۰ پیکسل) ← آن‌ها را به‌شکل «چاپ» قاب‌دار روی نسخه‌ی تار همان تصویر نشان بده، با حرکت Ken-Burns.

## کی استفاده کنیم
🔬 ویدیوی خانوادگی/تاریخی که تصویر دوران لازم دارد.

## قیمت و مجوز
رایگان؛ مجوز را برای هر فایل بخوان. ✅ راهنمای رسمی (https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia): اگر مجوز فایل ذکر منبع می‌خواهد باید بدهی و به شیوه‌ای که دارنده گفته؛ برای دامنه‌ی عمومی در بعضی کشورها الزام قانونی نیست ولی ذکر منبع توصیه می‌شود. شرط هر مجوز (مثل CC BY-SA) را از صفحه‌ی همان فایل بخوان.

## ریسک و هشدار
درخواست پرشتاب = مسدود شدن؛ فایل‌های «دامنه‌ی عمومی» گاهی در کشور دیگر محدودیت دارند ❓.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [Openverse](openverse.md) · [S151](../sources/README.md#s151)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
