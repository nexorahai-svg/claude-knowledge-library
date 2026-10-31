---
name: PayTabs
slug: paytabs
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: درگاه پرداخت منطقه که در امارات مجوز فریلنسر را می‌پذیرد و اعلان سرورش HMAC-SHA256 دارد
url: https://paytabs.com
repo: ""
license: "شرایط PayTabs"
pricing: paid
risk: medium
sources: [S124]
found_in: [gap-playbooks]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# PayTabs

## چیست
- ✅ در امارات **گواهی یا مجوز فریلنسر** پذیرفته می‌شود. مدارک: گواهی فریلنس، پاسپورت، Emirates ID، اقامت (برای غیرامارتی)، صورت‌حساب بانکی با IBAN (https://ai.paytabs.com/en/freelancer-certificate-permit-accepted-get-started-with-paytabs/).
- ✅ **اعلان سرور (callback و IPN):** هدر `Signature` = HMAC-SHA256 کل بدنه‌ی خام با ServerKey پروفایل؛ مقایسه‌ی زمان‌ثابت. برگشت مرورگر هم امضا دارد (فیلدها مرتب و URL-encode، بعد HMAC) (https://support.paytabs.com/en/support/solutions/articles/60000718961).
- ✅ بسته‌ی Flutter `flutter_paytabs_bridge` ۲.۷.۱۵ با Apple Pay؛ ولی در pub.dev «uploader تأییدنشده» است (https://pub.dev/packages/flutter_paytabs_bridge).

## کی استفاده کنیم
🧭 مرکز خدمات کوچک یا فریلنسری که مجوز تجاری ندارد و Stripe هم برایش مناسب نیست. Stripe هم مجوز فریلنسر امارات را می‌پذیرد؛ اول آن را ببین.

## قیمت و مجوز
❓ قیمت امارات خوانده نشد. ❓ محیط آزمایشی و کارت‌های آزمایشی بررسی نشد.

## ریسک و هشدار
⚠️ **چرا assess:** قیمت و sandbox ❓؛ مقاله‌های پشتیبانی قدیمی‌اند؛ بسته‌ی Flutter ناشر تأییدشده ندارد.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [S124](../sources/README.md#s124)
