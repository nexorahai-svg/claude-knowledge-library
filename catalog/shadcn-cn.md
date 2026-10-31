---
name: cn
slug: shadcn-cn
category: ui-components
domains: [website, apps]
verdict: trial
status: researched
summary: جایگزین بدون وابستگی برای clsx و tailwind-merge با همان API
use_when: "Tailwind project using cn()/twMerge in hot paths ; edge runtime bundle size"
how: "npm i cn then import { cn } from 'cn'; run existing tests before swapping"
url: https://github.com/shadcn-ui/cn
repo: "https://github.com/shadcn-ui/cn"
license: "MIT"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# cn

## چیست
✅ جایگزین بدون وابستگی (تأیید شد) برای tailwind-merge و clsx با همان API. ❓ ادعای «۳۰ برابر سریع‌تر» عدد خود نویسندگان است: در یک سناریوی مصنوعی نسبت به clsx + tailwind-merge، بازه‌ی ۱٫۹ تا ۱۷۲ برابر و میانگین هندسی ۳۷ برابر روی ۵۸ مخزن؛ مستقل اندازه‌گیری نشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Tailwind project using cn()/twMerge in hot paths؛ edge runtime bundle size. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۱,۷۱۹ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ریسک زنجیره تأمین عادی یک بسته npm؛ سازمان رسمی. برابری کامل با tailwind-merge ادعای خودشان است.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/shadcn-ui/cn

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
