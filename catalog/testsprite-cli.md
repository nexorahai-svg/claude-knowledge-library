---
name: testsprite-cli
slug: testsprite-cli
category: app-testing
domains: [website, apps]
verdict: assess
status: researched
summary: CLI رسمی TestSprite برای تست ابری برنامه‌ی زنده و گزارش به ایجنت
use_when: "AI-written web app needs automated live-app verification ; E2E test generation for Claude Code"
how: "npx testsprite setup (needs API key and credits); set TESTSPRITE_NO_UPDATE_NOTIFIER=1; do not tunnel private data"
url: https://github.com/TestSprite/testsprite-cli
repo: "https://github.com/TestSprite/testsprite-cli"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# testsprite-cli

## چیست
✅ CLI رسمی TestSprite است و برنامه‌ی زنده را در ابر تست می‌کند و نتیجه را به ایجنت می‌دهد. ✅ نیاز به API key و اعتبار (credit) دارد؛ هر اجرای مجدد فرانت‌اند ۰٫۵ اعتبار؛ قیمت در صفحه‌ی مخزن نیامده. ✅ تونل به برنامه‌های محلی. ❓ تله‌متری: README فقط بررسی روزانه‌ی به‌روزرسانی npm را ذکر می‌کند (خاموش با TESTSPRITE_NO_UPDATE_NOTIFIER=1)؛ وجود تله‌متری تأیید نشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: AI-written web app needs automated live-app verification؛ E2E test generation for Claude Code. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۵,۱۲۵ در تاریخ بررسی).
- قیمت: بخش رایگان و بخش پولی یا اعتباری.

## ریسک و هشدار
- سطح ریسک: medium.
- ۲۴۴ issue باز.
- برنامه را از طریق تونل به سرویس ابری وصل می‌کند؛ داده/آدرس لوکال بیرون می‌رود. کلید API را فقط خود کاربر باید وارد کند. مدل قیمت دقیق را تأیید نکردم.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/TestSprite/testsprite-cli
