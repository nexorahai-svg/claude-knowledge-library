---
name: ZarinPal (زرین‌پال)
slug: zarinpal
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: درگاه پرداخت ایرانی؛ API نسخه‌ی ۴ ساده است، ولی از بیرون ایران وصل نشد
url: https://www.zarinpal.com/
repo: ""
license: "شرایط سرویس"
pricing: paid
risk: medium
sources: [S138]
found_in: [project/client]
last_checked: 2026-10-22
next_check: "2026-11-21"
---

# ZarinPal (زرین‌پال)

## چیست
✅ (https://www.zarinpal.com/docs/paymentGateway/connectToGateway) جریان v4: `POST payment.zarinpal.com/pg/v4/payment/request.json` با merchant_id، amount، callback_url، description ← `authority` ← انتقال مرورگر مشتری به `/pg/StartPay/{authority}` ← بازگشت با `?Authority&Status` ← `POST verify.json` با merchant_id، amount، authority: کد ۱۰۰ موفق، ۱۰۱ قبلاً تأیید شده.
❓ سندباکس در گزارش‌ها «در دسترس نیست»؛ ❓ مدارک ثبت‌نام (کد ملی، شبای هم‌نام، نماد اعتماد) تأییدنشده. ❓ پرداخت تکرارشونده با کارت ذخیره‌شده نیست؛ تمدید = لینک پرداخت.
🔬 (یک پروژه‌ی مشتری، دفتر پروژه‌ها) **آزمون ۲۰۲۶-۱۰-۲۲ از این رایانه (خارج از ایران):** `payment.zarinpal.com` و `www.zarinpal.com` اتصال نداد. ❓ نتیجه: تماس سرور به سرور (request و verify) احتمالاً به رله‌ی میزبانی‌شده در ایران نیاز دارد؛ ریدایرکت مرورگر مشتری تأثیری نمی‌گیرد.

## کی استفاده کنیم
🧭 فروش به مشتری ایرانی. callback قابل جعل است: مبلغ را در سرور نگه دار و فقط با verify سرور به سرور مجوز بده ([سند](../domains/apps/licensing-and-sales.md)).

## قیمت و مجوز
❓ کارمزد خوانده نشد.

## ریسک و هشدار
رله‌ی ایرانی یعنی نقطه‌ی خرابی و اعتماد اضافه؛ بسته‌ی `zarinpal-checkout-v4@1.3.0` در npm فقط خوانده شد، نصب نشد.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

