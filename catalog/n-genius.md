---
name: N-Genius (Network International)
slug: n-genius
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: درگاه پرداخت Network International با محیط آزمایشی سلف‌سرویس؛ ولی webhook آن امضا ندارد و دوباره فرستاده نمی‌شود
url: https://docs.ngenius-payments.com
repo: "https://github.com/network-international"
license: "شرایط Network International"
pricing: paid
risk: medium
sources: [S95, S124]
found_in: []
last_checked: 2026-10-19
next_check: "2026-11-18"
---

# N-Genius (Network International)

## چیست
- ✅ صفحه‌ی پرداخت میزبانی‌شده: گرفتن توکن، ساخت سفارش، فرستادن مشتری به لینک `payment.href`، برگشت به `redirectUrl` (https://docs.ngenius-payments.com/reference/hosted-payment-page). توکن از `https://api-gateway.sandbox.ngenius-payments.com/identity/auth/access-token` با هدر `Authorization: Basic <api key>` (https://docs.ngenius-payments.com/reference/request-an-access-token-paypage).
- ✅ وضعیت سفارش: `GET …/transactions/outlets/{outlet}/orders/{order}` با توکن Bearer (https://docs.ngenius-payments.com/reference/retrieve-order-status-hpp).
- ✅ **محیط آزمایشی سلف‌سرویس:** فرم https://www.network.ae/en/test-account با نام شرکت، نام، ایمیل و موبایل؛ بدون مدرک (https://docs.ngenius-payments.com/docs/getting-started-create-an-account). پورتال: https://portal.sandbox.ngenius-payments.com. کارت‌های آزمایشی Visa، Mastercard، Jaywan، Amex و سناریوهای 3DS و ضدتقلب منتشر شده‌اند (https://docs.ngenius-payments.com/reference/sandbox-test-environment).
- ✅ **webhook:** صفحه‌ی رسمی می‌گوید «payload امضا نمی‌شود». فقط یک هدر دلخواه (مثل `X-Webhook-Token`) می‌شود گذاشت. دوباره فرستاده **نمی‌شود**؛ باید ظرف ۱۵ ثانیه ۲۰۰ یا ۲۰۱ برگردد (https://docs.ngenius-payments.com/reference/consuming-web-hooks). رمزگذاری اختیاری AES-256-CBC هست، ولی امضا یا HMAC نیست (https://docs.ngenius-payments.com/reference/webhook-encryption-decryption-guide).
- ✅ Apple Pay و Google Pay، توکن کارت و پرداخت تکراری، API بازپرداخت.
- ✅ SDK رسمی iOS، Android و React Native، و Hosted Session SDK برای وب (https://docs.ngenius-payments.com/reference/mobile-sdk). **Flutter رسمی ندارد.**
- ✅ افزونه‌ی WooCommerce و Shopify (https://docs.ngenius-payments.com/docs/plugins).

## کی استفاده کنیم
🧭 وقتی مشتری از قبل با بانک خودش (مثلاً حساب Network International) قرارداد دارد. آن وقت webhook را فقط «زنگ» بدان و وضعیت را همیشه با API سفارش از سرور بخوان. روش: [پرداخت در امارات](../domains/website/04-tech/payments-uae.md).

## قیمت و مجوز
❓ قیمت منتشر نشده («تماس با فروش»). سایت network.ae به ابزار ما ۴۰۳ داد. شرایط حساب واقعی (مجوز، مدارک، زمان) در مستندات نیست.

## ریسک و هشدار
- ⚠️ **چه چیزی جلوی trial را گرفته:** (۱) webhook امضا ندارد و دوباره فرستاده نمی‌شود، پس به تنهایی قابل اعتماد نیست؛ (۲) قیمت و شرایط حساب واقعی ❓؛ (۳) Flutter رسمی ندارد و افزونه‌ی Flutter در pub.dev ناشر تأییدشده ندارد. 🧭 اگر مشتری اصرار دارد: webhook + خواندن وضعیت از API + کار زمان‌بندی‌شده که سفارش‌های «در انتظار» را هر چند دقیقه دوباره چک کند.
- مستندات می‌گوید هر فروشنده‌ی آنلاین سالانه خودارزیابی PCI لازم دارد؛ نوع SAQ را نام نمی‌برد.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [بک‌اند اپ](../domains/apps/app-backend.md) · [S95](../sources/README.md#s95) · [S124](../sources/README.md#s124)
