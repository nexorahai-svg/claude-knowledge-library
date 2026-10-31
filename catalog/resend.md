---
name: Resend
slug: resend
category: email-domain
domains: [apps, website]
verdict: trial
status: researched
summary: API ارسال ایمیل با آموزش رسمی برای Cloudflare Workers
use_when: "transactional email from a site or app ; SMTP sender for an auth service"
how: "Use the API key as the SMTP password on smtp.resend.com; verify the sending domain with DNS records first; keep the key on the server only"
url: https://resend.com/
repo: ""
license: "❓"
pricing: freemium
risk: low
sources: [S138]
found_in: [project/client, project/client]
last_checked: 2026-10-31
next_check: "2026-11-29"
---

# Resend

## چیست
✅ (https://resend.com/docs/send-with-cloudflare-workers) آموزش رسمی ارسال از Cloudflare Worker دارد. ✅ صفحه‌ی Resend در ۲۰۲۶-۱۰-۳۰ باز شد (HTTP 200، «Send emails with Cloudflare Workers»). Postmark: آموزش رسمی خود Cloudflare برای ارسال با Postmark از Workers هست (https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/)؛ صفحه‌ای از خود Postmark پیدا نشد.

## کی استفاده کنیم
🧭 ارسال ایمیل کلید مجوز و لینک ورود از زیر‌دامنه‌ی `mail.<دامنه>` با SPF، DKIM و DMARC (از `p=none` شروع، بعد quarantine). کلید را در صفحه‌ی بعد از پرداخت هم نشان بده تا به ایمیل وابسته نباشد.

## SMTP
✅ (https://resend.com/docs/send-with-smtp) `smtp.resend.com`، پورت‌های 465/2465 (SSL) یا 25/587/2587 (STARTTLS)، نام کاربری `resend`، رمز = کلید API. 🔬 به‌عنوان SMTP «Send mail as» در Gmail کار کرد و DKIM دامنه‌ی خودمان را گذاشت ([دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md) بخش ۵).

## قیمت و مجوز
✅ (https://resend.com/pricing، ۲۰۲۶-۱۰-۲۸) طرح رایگان: ۰ دلار، ۳٬۰۰۰ ایمیل در ماه، ۱۰۰ در روز، ۳ دامنه.

## ریسک و هشدار
محتوای ایمیل از سرویس بیرونی رد می‌شود؛ کلید API فقط در Worker secret.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
