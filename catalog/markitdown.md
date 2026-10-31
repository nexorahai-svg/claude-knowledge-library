---
name: MarkItDown (Microsoft)
slug: markitdown
category: data-documents
domains: [claude-code]
verdict: adopt
status: researched
summary: تبدیل PDF، Word، اکسل، پاورپوینت و تصویر به Markdown برای مدل
use_when: "feeding a customer document (PDF, Office) to a model with fewer tokens ; converting documents to Markdown"
how: "in a virtual env run pip install markitdown with the all extra (Python 3.10-3.14), then markitdown file.pdf -o document.md; MIT; check Persian output manually (unverified)"
url: https://github.com/microsoft/markitdown
repo: "https://github.com/microsoft/markitdown"
license: "MIT"
pricing: free
risk: low
sources: [S159]
last_checked: 2026-10-31
next_check: "2027-01-25"
---

# MarkItDown (Microsoft)

## چیست
✅ ابزار Microsoft (MIT، حدود ۱۹۲ هزار ستاره؛ آخرین نسخه v0.1.9 در ۲۰۲۶-۱۰-۲۱). ✅ README: Python 3.10 تا 3.14؛ هشدار رسمی: ابزار با دسترسی‌های همان پردازش فایل/آدرس می‌خواند، ورودی ناامن را پاک‌سازی کن.

✅ نصب و اجرا (https://github.com/microsoft/markitdown، ۲۰۲۶-۱۰-۲۷): pip install 'markitdown[all]' ؛ markitdown path-to-file.pdf -o document.md

## کی استفاده کنیم
🧭 برای دادن سند مشتری به مدل با توکن کمتر؛ برای فارسی خروجی را چک کن ❓.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
