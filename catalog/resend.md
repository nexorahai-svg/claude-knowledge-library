---
name: Resend
slug: resend
category: email-domain
domains: [apps, website]
verdict: assess
status: researched
summary: API ارسال ایمیل با آموزش رسمی برای Cloudflare Workers
url: https://resend.com/
repo: ""
license: "❓"
pricing: freemium
risk: low
sources: [S138]
found_in: [project/client]
last_checked: 2026-10-22
next_check: "2026-11-21"
---

# Resend

## چیست
✅ (https://resend.com/docs/send-with-cloudflare-workers) آموزش رسمی ارسال از Cloudflare Worker دارد. Postmark هم آموزش رسمی Workers دارد (از گزارش پژوهش؛ صفحه دوباره خوانده نشد ❓).

## کی استفاده کنیم
🧭 ارسال ایمیل کلید مجوز و لینک ورود از زیر‌دامنه‌ی `mail.<دامنه>` با SPF، DKIM و DMARC (از `p=none` شروع، بعد quarantine). کلید را در صفحه‌ی بعد از پرداخت هم نشان بده تا به ایمیل وابسته نباشد.

## قیمت و مجوز
❓ طرح رایگان و قیمت خوانده نشد.

## ریسک و هشدار
محتوای ایمیل از سرویس بیرونی رد می‌شود؛ کلید API فقط در Worker secret.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

