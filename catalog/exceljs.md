---
name: ExcelJS
slug: exceljs
category: data-documents
domains: [website, apps]
verdict: trial
status: researched
summary: خواندن و ساختن فایل اکسل (xlsx) با Node، با فرمول، قالب‌بندی و چند برگه؛ نگهداری کند شده
url: https://github.com/exceljs/exceljs
repo: "https://github.com/exceljs/exceljs"
license: "MIT"
pricing: free
risk: low
sources: [S116]
found_in: []
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# ExcelJS

## چیست
✅ کتابخانه‌ی Node برای خواندن و نوشتن xlsx: برگه، قالب سلول، فرمول، فیلتر و ستون ثابت. آخرین نسخه‌ی npm ‏4.4.0 است و آخرین تغییر مخزن ۲۰۲۵-۰۱؛ مخزن بایگانی نشده ولی تند به‌روز نمی‌شود ([S116](../sources/README.md#s116)).

## کی استفاده کنیم
🔬 فایل‌های عملیاتی کسب‌وکار (لیست انبار، قیمت پیشنهادی، دسته‌بندی سایت، فایل ورود به صندوق) که کارکنان در Excel باز می‌کنند. در پروژه‌ی یک فروشگاه مشتری ده‌ها اکسل چندبرگه با بیش از ۱۰ هزار ردیف ساخت (دفتر پروژه‌ها).

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
- 🔬 ExcelJS فرمول را محاسبه نمی‌کند؛ فقط می‌نویسد. عدد فرمول وقتی Excel یا LibreOffice فایل را باز کند ساخته می‌شود. برای کنترل، یک نسخه را با `soffice --headless --convert-to xlsx` بازمحاسبه کن و بخوان ([LibreOffice](libreoffice-headless.md)).
- 🔬 `COUNT(A1,B1,C1)` روی سلول خالی تکی در LibreOffice و Excel جواب متفاوت داد؛ جمع `ISNUMBER` در هر دو یکسان است.
- ✅ `npm audit` (۲۰۲۶-۱۰-۱۹): دو هشدار متوسط از `uuid` کهنه داخل ExcelJS 4.4.0 (GHSA-w5hq-g745-h8pq)؛ «رفع» پیشنهادی npm، ExcelJS را به 3.4 برمی‌گرداند. برای اکسل‌سازی محلی پذیرفتنی است؛ در سرور با ورودی کاربر، دوباره بسنج.
- 🧭 چون نگهداری کند است، اگر به ویژگی تازه (مثلاً جدول محوری) نیاز شد، اول جایگزین را بسنج.

## مرتبط
[pdf.js](pdfjs-dist.md) · [Poppler](poppler.md) · [S116](../sources/README.md#s116)
