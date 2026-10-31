---
name: Zibal (زیبال)
slug: zibal
category: database-backend
domains: [apps, website]
verdict: trial
status: researched
summary: درگاه پرداخت ایرانی با مرچنت آزمایشی سلف‌سرویس؛ از بیرون ایران وصل نشد
use_when: "an Iranian store payment, if that work ever returns"
how: "Not researched further; the gateway was unreachable from outside Iran"
url: https://zibal.ir/
repo: ""
license: "شرایط سرویس"
pricing: paid
risk: medium
sources: [S138]
found_in: [project/client]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Zibal (زیبال)

## چیست
❓ (گزارش پژوهش، صفحه‌ی اصلی دوباره خوانده نشد) جریان: `gateway.zibal.ir/v1/request` ← `trackId` ← `/start/{trackId}` ← `/v1/verify`؛ مرچنت آزمایشی با نام `zibal` بدون ثبت‌نام. IDPay و Pay.ir طبق گفته‌ی یک نویسنده‌ی کتابخانه از خارج در دسترس نیستند ❓؛ سندباکس Vandar سلف‌سرویس نیست ❓.
🔬 (یک پروژه‌ی واقعی، دفتر پروژه‌ها) آزمون ۲۰۲۶-۱۰-۲۲: `gateway.zibal.ir` از خارج ایران اتصال نداد؛ همان نتیجه‌ی [ZarinPal](zarinpal.md) ❓.

## کی استفاده کنیم
🧭 جایگزین ZarinPal و برای آزمون جریان با مرچنت آزمایشی.

## قیمت و مجوز
❓ خوانده نشد.

## ریسک و هشدار
callback قابل جعل؛ همیشه verify سرور به سرور.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

🧭 (۲۰۲۶-۱۰-۳۱: 👀 به 🧪) تصمیم مالک: کار ایران متوقف است و این کارت دیگر پیگیری نمی‌شود.
