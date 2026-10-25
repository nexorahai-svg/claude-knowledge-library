---
name: Cloudflare Email Service
slug: cloudflare-email-service
category: email-domain
domains: [apps, website]
verdict: assess
status: researched
summary: ارسال ایمیل از Workers؛ هنوز بتا و فقط با طرح پولی Workers
url: https://developers.cloudflare.com/email-service/
repo: ""
license: "سرویس تجاری"
pricing: paid
risk: medium
sources: [S138]
found_in: [project/client]
last_checked: 2026-10-22
next_check: "2026-11-21"
---

# Cloudflare Email Service

## چیست
✅ (https://developers.cloudflare.com/email-service/ و صفحه‌ی قیمت آن) ارسال **بتا** است؛ نیاز به Workers Paid؛ ۳٬۰۰۰ ایمیل در ماه شامل طرح؛ بعدش ۰٫۳۵ دلار برای هر هزار؛ فرستنده را می‌شود متوقف کرد.
✅ جایگزین قدیمی، **ادغام رایگان MailChannels با Workers، از ۲۰۲۴-۰۸-۳۱ تمام شد** (اعلامیه‌ی پایان خدمت MailChannels)؛ آموزش‌های قدیمی که آن را پیشنهاد می‌کنند منسوخ‌اند.

## کی استفاده کنیم
🧭 وقتی همه‌چیز روی Cloudflare است و بتا بودن قابل قبول است. برای ایمیل کلید مجوز (حیاتی) فعلاً [Resend](resend.md) یا Postmark امن‌تر است ❓ (بتا).

## قیمت و مجوز
✅ بالا.

## ریسک و هشدار
بتا: ممکن است رفتار یا قیمت عوض شود. دامنه‌ی فرستنده: SPF، DKIM، DMARC را تنظیم کن.

## مرتبط
[مجوزدهی و فروش اپ دسکتاپ](../domains/apps/licensing-and-sales.md) · [S138](../sources/README.md#s138)

