---
name: Checkout.com
slug: checkout-com
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: درگاه پرداخت بزرگ با فروش‌محور بودن قیمت؛ webhook امضاشده و حساب آزمایشی رایگان دارد ولی Flutter و React Native رسمی ندارد
url: https://www.checkout.com
repo: ""
license: "شرایط Checkout.com"
pricing: paid
risk: medium
sources: [S124]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2026-11-18"
---

# Checkout.com

## چیست
- ✅ سه راه پرداخت: Flow (اجزای آماده در صفحه‌ی خودمان)، Hosted Payments Page و Payment Links. خود Checkout.com هر سه را **SAQ-A** می‌داند؛ هر سه Apple Pay و Google Pay دارند (https://www.checkout.com/docs/payments/accept-payments/payments-solution-comparison).
- ✅ **webhook:** هدر `Cko-Signature`؛ هش SHA-256 بدنه‌ی خام با کلید امضا (یعنی HMAC)؛ به‌اضافه‌ی کلید اختیاری در هدر `Authorization`. «دست‌کم یک بار» می‌رسد، ترتیبش ثابت نیست، باید ظرف ۱۰ ثانیه جواب بگیرد (https://www.checkout.com/docs/developer-resources/event-notifications/receive-webhooks/configure-your-webhook-server).
- ✅ حساب آزمایشی رایگان از https://www.checkout.com/get-test-account (❓ صفحه شرط یا تأیید را صریح نمی‌گوید). کارت‌های آزمایشی: https://www.checkout.com/docs/developer-resources/testing/test-cards.
- ✅ موبایل: «Flow for mobile» فقط iOS و Android بومی. در فهرست مستندات (https://www.checkout.com/docs/llms.txt) نامی از Flutter یا React Native نیست.
- ✅ بازپرداخت، Tamara (پرداخت قسطی رایج در امارات)، افزونه‌ی WooCommerce و اپ Shopify.

## کی استفاده کنیم
🧭 فقط وقتی مشتری بزرگ است و خودش قرارداد Checkout.com دارد یا می‌گیرد. برای کسب‌وکار کوچک امارات و اپ Flutter انتخاب اول نیست.

## قیمت و مجوز
❓ قیمت منتشر نشده: «با تیم ما تماس بگیرید». صفحه‌ی https://www.checkout.com/pricing فقط می‌گوید نرخ ثابت یا interchange++، بدون هزینه‌ی راه‌اندازی و نگهداری حساب. شرایط حساب امارات (مجوز، مدارک) بررسی نشد ❓.

## ریسک و هشدار
- ⚠️ **چرا assess:** قیمت و شرایط پذیرش برای کسب‌وکار کوچک امارات ❓، و SDK چندسکویی (Flutter، React Native) ندارد. فنی‌اش (امضا، sandbox، SAQ-A) خوب است.
- مستندات صفحه‌ای درباره‌ی جریمه‌ی عدم انطباق PCI دارد؛ پیش از قرارداد بخوان.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [S124](../sources/README.md#s124)
