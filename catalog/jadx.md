---
name: jadx
slug: jadx
category: reverse-engineering
domains: [apps, security]
verdict: trial
status: researched
summary: دیکامپایلر APK و DEX به کد جاوا برای دیدن اپ Android خودمان
use_when: "inspecting our own APK before release for keys and URLs ; testing how readable our Android build is"
how: "Trial first on a small task: run jadx (Apache-2.0) on OUR OWN APK or DEX inside a VM or container and search for keys and URLs; never on other people's apps"
url: https://github.com/skylot/jadx
repo: "https://github.com/skylot/jadx"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S120]
found_in: [batch-13]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# jadx

## چیست
✅ دیکامپایلر APK و DEX به کد جاوا برای دیدن اپ Android خودمان. مجوز Apache-2.0؛ ~۵۱ هزار ستاره، فعال (۲۰۲۶-۱۰-۱۴).

## کی استفاده کنیم
🧪 باز کردن APK خودمان پیش از انتشار و جستجوی کلید و آدرس. فقط روی خروجی خودمان، داخل ماشین مجازی یا کانتینر ([محافظت از اپ](../domains/apps/app-protection.md)).

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
⚠️ ابزار مهندسی معکوس است: فقط روی نرم‌افزار خودمان. استفاده روی اپ دیگران برای کپی، قانون اول کتابخانه و معمولاً شرایط استفاده و قانون حق نشر را می‌شکند. طبق قانون کتابخانه بدون درخواست کاربر نصب نشود.

## مرتبط
[محافظت از اپ و آزمون خودمان](../domains/apps/app-protection.md) · [S120](../sources/README.md#s120) · غربال دسته‌ی ۱۳
