---
name: pyHanko
slug: pyhanko
category: data-documents
domains: [apps]
verdict: adopt
status: researched
summary: کتابخانه‌ی پایتون برای امضا و اعتبارسنجی امضای دیجیتال PDF؛ ما فقط برای آزمون درستی امضاها به کار بردیم
use_when: "verifying PDF signature behavior, signing order or detecting later edits in a desktop-app signing test"
how: "pip install pyHanko pyhanko-cli (latest 0.38.0 and 0.6.0, MIT; our test used 0.29.1) and use it as a tester with a self-signed certificate; not used for real signing and not checked against Adobe Reader"
url: https://github.com/MatthiasValvekens/pyHanko
repo: "https://github.com/MatthiasValvekens/pyHanko"
license: "MIT"
pricing: free
risk: low
sources: [S146]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-25"
---

# pyHanko

## چیست
✅ آخرین نسخه‌ها در PyPI (۲۰۲۶-۱۰-۲۷): pyHanko 0.38.0 و pyhanko-cli 0.6.0؛ آزمون ما با 0.29.1 بود و با نسخه‌ی جدید تکرار نشده است ❓.
✅ کتابخانه و ابزار خط فرمان پایتون برای امضا و اعتبارسنجی امضای PDF؛ مخزن با مجوز MIT ([S146](../sources/README.md#s146)).
✅ نصب و اجرا (https://github.com/MatthiasValvekens/pyHanko، ۲۰۲۶-۱۰-۲۷): pip install 'pyHanko[pkcs11,image-support,opentype,qr]' pyhanko-cli

## کی استفاده کنیم
🔬 فقط به‌عنوان آزمونگر: نسخه‌ی 0.29.1 با گواهی خودامضا، ترتیب امضای دو طرف و تشخیص ویرایش بعدی را بررسی کرد ([روش](../domains/apps/desktop-apps.md)). برای امضای واقعی به کار نرفته است.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
- ❓ نتیجه‌ی آن با Adobe Acrobat/Reader آزموده نشده است.

## مرتبط
[اپ دسکتاپ: PDF امضاپذیر](../domains/apps/desktop-apps.md)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
