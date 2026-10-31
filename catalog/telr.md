---
name: Telr
slug: telr
category: database-backend
domains: [apps, website]
verdict: trial
status: researched
summary: درگاه پرداخت امارات با قیمت منتشرشده، حالت آزمایشی، اعلان امضاشده و SDK رسمی Flutter با ناشر تأییدشده
use_when: "taking card payments for a UAE business with trade licence under 500k AED/month ; Flutter app payments"
how: "Trial first on a small task: server POSTs secure.telr.com/gateway/order.json with order.test=1, redirects to hosted page; confirm via signed webhook then method check; Flutter telr_mobile_payment_sdk; app holds no key; Startup plan 249 AED/month, no fee"
url: https://telr.com
repo: "https://github.com/Telr-PG"
license: "شرایط Telr"
pricing: paid
risk: medium
sources: [S95, S124, S184]
found_in: []
last_checked: 2026-10-28
next_check: "2026-11-27"
---

# Telr

## چیست
- ✅ نشانی فعلی مستندات `docs.telr.com` است؛ خود telr.com به آن لینک می‌دهد. نشانی قدیمی `telr-api.readme.io` هنوز همان صفحه‌ها را نشان می‌دهد (هر دو یک پروژه‌ی ReadMe‌اند)، ولی در کارت و کد نشانی تازه را بنویس ([S184](../sources/README.md#s184)، ۲۰۲۶-۱۰-۲۸).
- ✅ درگاه پرداخت با صفحه‌ی پرداخت میزبانی‌شده (Hosted Payment Page). کارت فقط در صفحه‌ی Telr وارد می‌شود (https://docs.telr.com/reference/how-the-hosted-payment-page-works).
- ✅ ساخت سفارش: `POST https://secure.telr.com/gateway/order.json` با `store` و `authkey` در بدنه‌ی JSON. سه نشانی برگشت لازم است: `authorised`، `declined`، `cancelled`. گزینه‌ی `framed` صفحه را در iframe نشان می‌دهد (https://docs.telr.com/reference/payment-page).
- ✅ وضعیت سفارش با `method: "check"` روی همان نشانی گرفته می‌شود (https://docs.telr.com/reference/check-status-1). ❓ جدول کد وضعیت «پرداخت‌شده» برای سفارش در آن صفحه نیست؛ پیش از کد زدن از پشتیبانی یا پاسخ واقعی آزمایشی بخوان.
- ✅ **حالت آزمایشی:** فیلد `order.test` (۱ = آزمایشی، ۰ = واقعی). کارت‌های آزمایشی منتشر شده‌اند؛ CVV با کد پاسخ، رد شدن را شبیه‌سازی می‌کند و ۹۹۹ حالت «نگه‌داشته برای ضدتقلب» است (https://docs.telr.com/reference/test-cards).
- ✅ **اعلان سرور (webhook):** POST سرور به سرور به نشانی ثابت؛ باید ۲۰۰ برگرداند؛ ۳ تلاش با فاصله‌ی ۵ ثانیه. امضا: SHA-1 روی `secretkey:tran_store:tran_type:…:tran_authmessage` در فیلد `tran_check` بدنه (HMAC نیست؛ هدر ندارد) (https://docs.telr.com/reference/webhook).
- ✅ Apple Pay و Google Pay روی صفحه‌ی میزبانی‌شده و در SDK؛ Samsung Pay هم هست.
- ✅ پرداخت تکراری (Repeat billing)، کارت ذخیره‌شده، QuickLinks و فاکتور.
- ✅ SDK رسمی Android، iOS، Flutter و React Native (https://docs.telr.com/reference/introduction-to-mobile-sdks). بسته‌ی Flutter `telr_mobile_payment_sdk` نسخه‌ی ۴.۵.۱ (۲۰۲۶-۱۰-۲۳)، ناشر تأییدشده‌ی telr.com در pub.dev، مجوز MIT. اپ کلید ندارد؛ سرور سفارش را می‌سازد و فقط نشانی‌ها را به اپ می‌دهد (https://docs.telr.com/reference/flutter). ✅ مخزن `Telr-PG/mobile-sdks` در ۲۰۲۶-۱۰-۲۶ ۴۰۴ می‌دهد (pubspec هنوز به آن اشاره می‌کند)؛ سازمان https://github.com/Telr-PG فعال است. مخزن‌های Flutter شخصی (غیر Telr) استفاده نشوند.
- ✅ افزونه‌ی WooCommerce و راهنمای Shopify، و Magento، OpenCart، PrestaShop، Zoho، Odoo.
- ✅ Remote API (گرفتن کارت روی سرور خودمان) پیش‌فرض خاموش است و PCI کامل می‌خواهد؛ ولی بازپرداخت و لغو از راه آن PCI نمی‌خواهد (https://docs.telr.com/reference/get-started).

## کی استفاده کنیم
🧭 پیش‌فرض ما برای کسب‌وکار امارات با مجوز تجاری که ماهانه کمتر از ۵۰۰ هزار درهم می‌فروشد، به‌خصوص اپ Flutter. راه: صفحه‌ی میزبانی‌شده، تأیید با اعلان امضاشده و بعد `check` از سرور. روش کامل: [پرداخت در امارات](../domains/website/04-tech/payments-uae.md).

## قیمت و مجوز
✅ از https://telr.com/pricing (امارات، ماهانه، به‌اضافه‌ی ۵٪ VAT):

| طرح | فروش ماهانه (درهم) | هزینه‌ی ماهانه | کارمزد کارت داخلی | کارت خارجی |
|---|---|---|---|---|
| Startup | ۰ تا ۹٬۹۹۹ | ۲۴۹ درهم | ۰ | ۰ |
| Entry | ۱۰٬۰۰۰ تا ۲۴٬۹۹۹ | ۱۹۹ درهم | ۲.۴۵٪ + ۱ درهم | ۰.۵٪ بیشتر |
| Small | ۲۵٬۰۰۰ تا ۴۹٬۹۹۹ | ۹۹ درهم | ۲.۳۵٪ + ۰.۵ درهم | ۰.۵٪ بیشتر |
| Medium | ۵۰٬۰۰۰ به بالا | ۰ | ۲.۲۵٪ + ۰.۵ درهم | ۰.۵٪ بیشتر |

- ✅ «مجوز تجاری معتبر الزامی است.» بالای ۵۰۰ هزار درهم در ماه: قیمت اختصاصی.
- ❓ هزینه‌ی راه‌اندازی، زمان واریز، پذیرش منطقه‌ی آزاد و فریلنسر، مدارک و زمان تأیید در صفحه نیست.

## ریسک و هشدار
- ⚠️ **چرا trial و نه adopt:** هنوز در پروژه‌ی واقعی آزموده نشده. ❓ راه گرفتن `store` و `authkey` آزمایشی بدون حساب فروشنده مستند نیست؛ پس آزمون واقعی بعد از ثبت‌نام مشتری ممکن است. تا آن موقع با اعلان ساختگی روی سرور آزمون کن.
- ⚠️ امضا SHA-1 با کلید پیشوندی است، نه HMAC-SHA256. 🧭 پس به امضا تنها اعتماد نکن: بعد از امضای درست، وضعیت را با `check` از سرور دوباره بپرس، و مبلغ، ارز و شماره‌ی سبد را با سفارش خودت مقایسه کن.
- ⚠️ نمونه‌ی PHP صفحه‌ی webhook متغیر تعریف‌نشده دارد (`$hash_check`)؛ کد را از روی توضیح بنویس، نه از نمونه.
- `authkey` فقط روی سرور. پرداخت خدمت واقعی در اپ با خرید درون‌برنامه ممنوع است؛ همین‌جاست که درگاه لازم می‌شود.

## یافته‌های اتصال (۲۰۲۶-۱۰-۲۱)
- ✅ صفحه‌ی پرداخت: `POST https://secure.telr.com/gateway/order.json` با `method=create` و بعد `check`؛ آزمایشی با `test=1` در هر درخواست (میزبان جدا ندارد). کد وضعیت سفارش: `3` پرداخت‌شده، `2` تأییدشده، `-1/-2/-3` منقضی/لغو/رد؛ تراکنش `A` تأیید، `H` در انتظار بازبینی. شناسه‌ی سبد تکراری خطای E56 می‌دهد ([S131](../sources/README.md#s131)).
- ⚠️ capture، بازپرداخت و آزادسازی فقط با Remote API (XML، `remote.xml`) است که پیش‌فرض خاموش است، کلید جدا دارد و IP ثابت سرور می‌خواهد؛ از پشتیبانی بخواه.
- ⚠️ مستندات JSON کلید زبان صفحه را نمی‌گوید؛ افزونه‌ی رسمی WooCommerce خودشان `ivp_lang` را در نسخه‌ی فرم می‌فرستد. ترتیب فیلدهای امضای `tran_check` (SHA-1) در مستندات متناقض است و نمونه‌ی PHP آن باگ دارد: اعلان را فقط محرک بدان و با `check` تأیید کن. افزونه‌ی رسمی بررسی TLS را خاموش می‌کند؛ کپی نکن.
- 🔬 (یک پروژه‌ی واقعی) provider سفارشی Medusa 2 با ۸ آزمون روی mock، از جمله `tran_check` دست‌خورده.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [بک‌اند اپ](../domains/apps/app-backend.md) · [S95](../sources/README.md#s95) · [S124](../sources/README.md#s124) · پروژه‌ها
