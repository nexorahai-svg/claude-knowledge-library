---
name: EmailJS
slug: emailjs
category: email-domain
domains: [website]
verdict: trial
status: researched
summary: فرستادن ایمیل فرم سایت مستقیم از مرورگر، بدون سرور؛ محدودیت دامنه فقط در طرح پولی
url: https://www.emailjs.com/
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S54]
found_in: [project/client]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# EmailJS

## چیست
✅ سرویسی که فرم سایت ایستا را بدون سرور به ایمیل تبدیل می‌کند؛ قالب و گیرنده در داشبورد EmailJS تنظیم می‌شوند.

## کی استفاده کنیم
🔬 در یک سایت مشتری فقط برای **اعلان** فرم (فرم اصلی در پایگاه داده ذخیره می‌شود). 🧭 اگر سرور (Function) داری، ارسال از سرور امن‌تر است؛ برای همین 🧪 نه ✅.

## قیمت و مجوز
✅ (https://www.emailjs.com/pricing/) رایگان: ۲۰۰ درخواست در ماه، ۲ قالب. Personal: ماهی ۹ دلار، ۲٬۰۰۰ درخواست، **فهرست دامنه‌های مجاز**.

## ریسک و هشدار
⚠️ در طرح رایگان کلید عمومی از هر سایتی قابل استفاده است (سوءاستفاده و تمام شدن سهمیه). ✅ (https://www.emailjs.com/docs/sdk/init/) `blockHeadless` و `limitRate` را روشن کن. ⚠️ 🔬 گیرنده در داشبورد است، نه در کد: بعد از عوض شدن ایمیل شرکت، قالب را هم عوض کن.

## مرتبط
[دامنه و ایمیل شرکتی](../domains/website/04-tech/domain-and-email.md) · [S54](../sources/README.md#s54)
