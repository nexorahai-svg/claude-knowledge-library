---
name: Keygen
slug: keygen
category: database-backend
domains: [apps]
verdict: assess
status: researched
summary: سرویس و API مجوزدهی نرم‌افزار؛ برای ما نمونه‌ی طراحی است، نه ابزار مصرفی
url: https://keygen.sh/
repo: ""
license: "Fair Core License (FCL-1.0-ALv2)"
pricing: unknown
risk: low
sources: [S138]
found_in: [project/client]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Keygen

## چیست
✅ (مستندات رسمی) موجودیت‌ها: Policy، License، Machine، Key. راهبرد انقضا: RESTRICT، REVOKE، MAINTAIN («پرداخت‌شده تا تاریخ انقضا، برای نسخه‌هایی که پیش از آن منتشر شده‌اند همیشه معتبر») و ALLOW. تمدید با `renewalBasis` (از تاریخ انقضا، از حالا، یا از حالا اگر منقضی شده) روی همان مجوز و همان کلید. فایل مجوز آفلاین امضاشده با `issued`، `ttl` و `expiry`؛ مجوز «issued در آینده» رد می‌شود؛ ttl خالی یعنی غیرقابل‌ابطال (توصیه نمی‌شود). کلیدِ امضاشده تغییرناپذیر است، پس تمدید = کلید تازه و خودشان فایل مجوز را ترجیح می‌دهند.
✅ heartbeat ده‌دقیقه‌ای برای ماشین مجازی است و برای دسکتاپ نادرست؛ «بررسی هر N روز» می‌خواهد.

## کی استفاده کنیم
🧭 **مرجع طراحی** برای مدل مجوز خودمان ([سند](../domains/apps/licensing-and-sales.md))؛ برای استفاده هنوز ارزیابی نشده: قیمت و قابلیت خودمیزبان خوانده نشد ❓. ❓ مستندات از طرف ایران بودن یا نبودن مشتری چیزی نگفتند؛ پیش از خرید باید جداگانه پرسید.

## قیمت و مجوز
✅ مخزن https://github.com/keygen-sh/keygen-api زیر Fair Core License 1.0 با «ALv2 Future License» (فایل LICENSE.md)؛ این مجوز متن‌باز استاندارد OSI نیست و محدودیت رقابتی دارد. قیمت ابری خوانده نشد ❓.

## ریسک و هشدار
داده‌ی مشتری و کلید فروش بیرون از سرور خودمان می‌رود؛ وابستگی به یک سرویس برای ابطال.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

