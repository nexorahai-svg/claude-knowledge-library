---
name: flutter_animate
slug: flutter-animate
category: app-frameworks
domains: [apps]
verdict: trial
status: researched
summary: بسته‌ی Flutter برای انیمیشن زنجیره‌ای کوتاه (fadeIn، slide، scale، تأخیر پلکانی) با یک خط
url: https://pub.dev/packages/flutter_animate
repo: "https://github.com/gskinner/flutter_animate"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S132]
found_in: [batch-17]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# flutter_animate

## چیست
✅ (pub.dev، ۲۰۲۶-۱۰-۲۱) نسخه‌ی 4.5.2، BSD-3، حدود ۴٫۳ هزار لایک، ۱۵۰ امتیاز. نوشتن انیمیشن به‌صورت زنجیره: `widget.animate().fadeIn(delay: 90.ms).slideX(begin: 0.12)`؛ `animate(target:)` برای حالت روشن/خاموش. ⚠️ آخرین انتشار ۲۰۲۴-۱۱-۲۵.

## کی استفاده کنیم
🧪 ورود پلکانی کارت‌ها، دکمه‌ی پسند، نوار بالا. برای حرکت پیچیده (کشیدن خط لوگو) `CustomPainter` با `AnimationController` خودمان بهتر است.

## تجربه ✅
✅ در design-lab ورود پلکانی کارت‌ها و پرش قلب کار کرد. ⚠️ اگر کارت با تأخیر وارد شود و `AnimatedSwitcher` جای اسکلت را زودتر خالی کند، چند فریم سفید دیده می‌شود؛ مدت `AnimatedSwitcher` را از بیشترین تأخیر بیشتر بگذار.

## قیمت و مجوز
✅ رایگان، BSD-3.

## مرتبط
[طراحی رابط اپ](../domains/apps/app-design.md) · [Flutter](flutter.md) · [S132](../sources/README.md#s132)
