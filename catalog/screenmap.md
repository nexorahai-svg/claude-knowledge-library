---
name: screenmap
slug: screenmap
category: app-testing
domains: [apps]
verdict: assess
status: researched
summary: گرفتن اسکرین‌شات از صفحه‌های تغییرکرده‌ی اپ Expo در GitHub Actions و قراردادن در PR
use_when: "Expo/React Native pull requests need visual review ; screen map of an app for design review"
how: "add the GitHub Action per README on a test repo first"
url: https://github.com/aleqsio/screenmap
repo: "https://github.com/aleqsio/screenmap"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# screenmap

## چیست
✅ در GitHub Actions اپ Expo/React Native را اجرا می‌کند، از صفحه‌های تغییرکرده اسکرین‌شات می‌گیرد و در PR می‌گذارد؛ تصاویر در branch خود مخزن می‌مانند. ✅ ۴ مشارکت‌کننده.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Expo/React Native pull requests need visual review؛ screen map of an app for design review. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲۵۲ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- اکشن شخص ثالث با دسترسی نوشتن به مخزن؛ نسخه را با SHA پین کن. فایل action/cli/screenmap-ci.mjs را کامل نخواندم.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/aleqsio/screenmap
