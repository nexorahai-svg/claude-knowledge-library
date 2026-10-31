---
name: Tamara
slug: tamara
category: database-backend
domains: [website, apps]
verdict: trial
status: researched
use_when: "UAE or Saudi online shop that needs buy-now-pay-later next to Tabby"
how: "Trial first on a small task: custom Medusa 2 payment provider (medusa-payment-tamara is Medusa 1 only); verify tamaraToken JWT with a fixed HS256, then fetch the order from the API and process idempotently; sandbox first"
summary: قسطی «الان بخر، بعداً بپرداز» در عربستان و امارات؛ webhook با توکن JWT امضاشده (HS256)
url: https://tamara.co
license: proprietary
pricing: paid
risk: medium
sources: [S131]
found_in: []
last_checked: 2026-10-28
next_check: 2026-12-21
---

# Tamara

## چیست
- ✅ پرداخت قسطی برای فروشگاه‌های عربستان و امارات؛ مشتری به صفحه‌ی خود Tamara می‌رود ([S131](../sources/README.md#s131)).
- ✅ webhook از Partner Portal ثبت می‌شود (Settings، General Settings، Webhooks)، نوع Order، HTTPS، نشانی حداکثر ۲۵۵ نویسه؛ رویداد Approved لازم است. هر اعلان یک توکن JWT با HS256 در پارامتر `tamaraToken` و در سرآیند `Authorization: Bearer` دارد که با Notification Token خودمان بررسی می‌شود ([S131](../sources/README.md#s131)).

## کی استفاده کنیم
کنار Tabby برای مشتریانی که Tamara دارند؛ در امارات هر دو رایج‌اند.

## قیمت و مجوز
❓ کارمزد فروشنده در منابع خوانده‌شده نیامده؛ از Partner Portal یا مدیر حساب.

## ریسک و هشدار
- 🧭 توکن JWT را با کتابخانه‌ی معتبر و الگوریتم ثابت HS256 بررسی کن (نه الگوریتمی که خود توکن می‌گوید)، بعد سفارش را از API بگیر و پردازش را تکرارپذیر بساز.
- ⚠️ افزونه‌ی `medusa-payment-tamara` (۱.۱.۲، مارس ۲۰۲۴) برای Medusa 1 است (`@medusajs/medusa >= 1.20.2`)؛ برای Medusa 2 provider سفارشی لازم است ([S131](../sources/README.md#s131)).

- ✅ جریان: `POST /checkout` ← صفحه‌ی Tamara ← وضعیت `approved` ← **ما باید `POST /orders/{id}/authorise` را بزنیم** (حداکثر ۷۲ ساعت، وگرنه منقضی) ← capture هنگام ارسال با `shipping_info` (بعد از ۲۱ روز خود Tamara capture می‌کند) ← بازپرداخت با `POST /payments/simplified-refund/{id}` ([S131](../sources/README.md#s131): docs.tamara.co/docs/direct-online-checkout).
- ✅ sandbox: `https://api-sandbox.tamara.co`؛ امارات: شماره‌ی ۹ رقمی تصادفی که با ۵ شروع شود (رقم دوم ۰، ۲، ۳، ۴، ۵، ۶ یا ۸) موفق، `526422337` رد، رمز 3DS `Checkout1!`.
- ❓ مقدار `payment_type` و `instalments` برای امارات، قالب تلفن، و `/orders` یا `/merchants/orders` در مستندات یکدست نیست؛ از Tamara بپرس.
- 🔬 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۱) provider سفارشی Medusa 2 با ۸ آزمون روی mock؛ توکن جعلی، `alg: none` و نبود توکن رد شد. Medusa رشته‌ی query را به provider نمی‌دهد، پس توکن را از سرآیند `Authorization` بخوان. بسته‌ی npm `tamara-sdk` از ۲۰۲۳ به‌روز نشده.

## مرتبط
[پرداخت امارات](../domains/website/04-tech/payments-uae.md) · [Medusa](medusa.md) · [Stripe](stripe.md) · [Telr](telr.md) · پروژه‌ها
