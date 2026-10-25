---
name: Tabby
slug: tabby
category: database-backend
domains: [website, apps]
verdict: assess
status: researched
summary: قسطی «الان بخر، بعداً بپرداز» در امارات و عربستان؛ تأیید پرداخت با گرفتن پرداخت از API، webhook فقط خبر است
url: https://tabby.ai
license: proprietary
pricing: paid
risk: medium
sources: [S131]
found_in: []
last_checked: 2026-10-21
next_check: 2026-12-21
---

# Tabby

## چیست
- ✅ پرداخت قسطی (Pay in 4 و طرح‌های بلندتر) برای فروشگاه‌های امارات؛ مشتری به صفحه‌ی خود Tabby می‌رود ([S131](../sources/README.md#s131)).
- ✅ وضعیت پرداخت در API: CREATED، AUTHORIZED، CLOSED، REJECTED، EXPIRED. فقط AUTHORIZED را می‌شود capture کرد؛ تا ۲۱ روز پس از تأیید capture یا لغو دست ماست و بعد از آن ممکن است Tabby خودش capture کند. نشست پرداخت پیش‌فرض ۲۰ دقیقه است ([S131](../sources/README.md#s131)).
- ✅ webhook با IP مجاز یا یک سرآیند ثابت که خودمان هنگام ثبت می‌گذاریم محافظت می‌شود و امضای HMAC ندارد؛ مستندات می‌گویند webhook را فقط خبر بدان، با `payment_id` پرداخت را از API بگیر، و اگر webhook نرسید هر چند دقیقه وضعیت را بپرس ([S131](../sources/README.md#s131)).

## کی استفاده کنیم
فروشگاه امارات که خرید قسطی می‌خواهد (لوازم الکترونیکی گران‌تر). کنار درگاه کارت، نه به‌جای آن.

## قیمت و مجوز
❓ کارمزد فروشنده منتشر نمی‌شود: نرخ متغیر بر اساس صنعت و نوع کسب‌وکار به‌اضافه‌ی یک مبلغ ثابت برای هر سفارش، در قرارداد ([S131](../sources/README.md#s131)). برای مشتری Pay in 4 بدون سود در موعد.

## ریسک و هشدار
- 🧭 webhook امضا ندارد: مثل N-Genius، هیچ تصمیمی را روی بدنه‌ی webhook نگیر؛ همیشه پرداخت را از API بگیر، و پردازش را تکرارپذیر (idempotent) بساز چون webhook ممکن است تکراری برسد.
- ✅ حالت آزمایشی میزبان جدا ندارد: کلید تعیین می‌کند (`sk_test_`/`pk_test_` در برابر `sk_`/`pk_`، همان `https://api.tabby.ai`). داده‌ی آزمایشی امارات: OTP همیشه `8888`؛ موفق `otp.success@tabby.ai` و `+971500000001`؛ رد پیش‌امتیازدهی `+971500000002`؛ رد در صفحه `otp.rejected@tabby.ai` ([S131](../sources/README.md#s131): docs.tabby.ai/testing-guidelines/testing-credentials).
- ✅ capture با `reference_id` ثابت (مثل `capture-<سفارش>`) تکرارپذیر است؛ تکرار همان نتیجه را برمی‌گرداند. ثبت webhook با `POST /api/v1/webhooks` (نسخه‌ی ۱) و سرآیند ثابت خودمان؛ حداکثر ۴ تا؛ ۴ بار تلاش دوباره با فاصله‌ی ۱ تا ۴ دقیقه؛ IPهای فرستنده در مستندات آمده.
- ✅ برای قبول در QA: اسم روش دقیقاً «Pay later with Tabby» / «ادفع لاحقًا مع تابي»، snippet در همه‌ی محصول‌ها و سبد، و `tabby-card.js` زیر گزینه. id نگهدارنده را `TabbyPromo` یا `TabbyCard` نگذار (سازنده را روی `window` می‌پوشاند).
- 🔬 (یک فروشگاه مشتری، ۲۰۲۶-۱۰-۲۱) provider سفارشی Medusa 2 نوشته شد و با mock ساخته‌شده از مستندات ۹ آزمون گذراند؛ با خاموش کردن عمدی بررسی سرآیند، آزمون شکست خورد. هنوز روی sandbox واقعی آزموده نشده. SDK رسمی Node ندارد.

## مرتبط
[پرداخت امارات](../domains/website/04-tech/payments-uae.md) · [Medusa](medusa.md) · [Stripe](stripe.md) · [Telr](telr.md) · پروژه‌ها
