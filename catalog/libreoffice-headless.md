---
name: LibreOffice (حالت headless)
slug: libreoffice-headless
category: data-documents
domains: [website, apps, claude-code]
verdict: adopt
status: researched
summary: تبدیل و بازمحاسبه‌ی فایل اکسل و ورد از خط فرمان، بدون پنجره؛ برای کنترل خروجی اسکریپت
url: https://www.libreoffice.org/
repo: "https://git.libreoffice.org/core"
license: "MPL-2.0"
pricing: free
risk: low
sources: [S116]
found_in: []
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# LibreOffice (حالت headless)

## چیست
✅ مجموعه‌ی اداری آزاد. `soffice --headless --convert-to <قالب> <فایل>` بدون پنجره تبدیل می‌کند. روی این رایانه‌ی لینوکس نسخه‌ی 25.2.3 ([S116](../sources/README.md#s116)).

## کی استفاده کنیم
🔬 بعد از ساختن اکسل با [ExcelJS](exceljs.md)، یک نسخه را با `--convert-to xlsx` بازمحاسبه کن تا عدد فرمول‌ها را بخوانی و با انتظار مقایسه کنی؛ این اوراکل خودکار اکسل است ([بررسی خودکار](../domains/claude-code/verification.md))؛ در یک فروشگاه مشتری به کار رفت (دفتر پروژه‌ها). همچنین وقتی Excel نصب نیست، کارکنان با آن فایل را باز می‌کنند.

## قیمت و مجوز
✅ رایگان، MPL-2.0.

## ریسک و هشدار
- 🔬 رفتار چند تابع با Excel یکی نیست (`COUNT` روی سلول خالی تکی)؛ فرمولی بنویس که در هر دو یکسان است.
- 🧭 `--convert-to png` فقط صفحه‌ی اول را می‌دهد؛ برای PDF چندصفحه‌ای از [Poppler](poppler.md) استفاده کن.

## مرتبط
[ExcelJS](exceljs.md) · [Poppler](poppler.md)
