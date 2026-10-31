---
name: ExcelJS
slug: exceljs
category: data-documents
domains: [website, apps]
verdict: adopt
status: researched
summary: خواندن و ساختن فایل اکسل (xlsx) با Node، با فرمول، قالب‌بندی و چند برگه؛ نگهداری کند شده
use_when: "generating xlsx files (stock list, quote, import file) with Node ; reading Excel files in a script"
how: "npm install exceljs (4.4.0, MIT, slow maintenance); it writes formulas but does not calculate them, so verify with soffice --headless --convert-to xlsx; avoid on servers because of the uuid audit warning; check alternatives if pivot tables are needed"
url: https://github.com/exceljs/exceljs
repo: "https://github.com/exceljs/exceljs"
license: "MIT"
pricing: free
risk: low
sources: [S116]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# ExcelJS

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) همچنان npm 4.4.0 (۲۰۲۳-۱۰-۱۹)، آخرین push ۲۰۲۵-۰۱-۲۱، ۸۲۴ مسئله‌ی باز، بایگانی نشده، بدون هشدار منتشرشده در GitHub. ❓ fork نگهداری‌شده بررسی عمیق نشد: https://github.com/exceljs/exceljs
✅ (جاروی ۲۰۲۶-۱۰-۲۸) ❓ وضعیت: آخرین نسخه‌ی npm 4.4.0 (اکتبر ۲۰۲۳)، آخرین push ۲۰۲۵-۰۱-۲۱، ۸۲۴ issue باز و بدون بیانیه‌ی نگهدارنده؛ بایگانی نشده ولی عملاً راکد. ریسک نگهداری بلندمدت؛ برای وابستگی تازه جایگزین را هم بسنج.
✅ کتابخانه‌ی Node برای خواندن و نوشتن xlsx: برگه، قالب سلول، فرمول، فیلتر و ستون ثابت. آخرین نسخه‌ی npm ‏4.4.0 است و آخرین تغییر مخزن ۲۰۲۵-۰۱؛ مخزن بایگانی نشده ولی تند به‌روز نمی‌شود ([S116](../sources/README.md#s116)).

## کی استفاده کنیم
🔬 فایل‌های عملیاتی کسب‌وکار (لیست انبار، قیمت پیشنهادی، دسته‌بندی سایت، فایل ورود به صندوق) که کارکنان در Excel باز می‌کنند. در یک پروژه‌ی واقعی ده‌ها اکسل چندبرگه با بیش از ۱۰ هزار ردیف ساخت.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
- 🔬 ExcelJS فرمول را محاسبه نمی‌کند؛ فقط می‌نویسد. عدد فرمول وقتی Excel یا LibreOffice فایل را باز کند ساخته می‌شود. برای کنترل، یک نسخه را با `soffice --headless --convert-to xlsx` بازمحاسبه کن و بخوان ([LibreOffice](libreoffice-headless.md)).
- 🔬 `COUNT(A1,B1,C1)` روی سلول خالی تکی در LibreOffice و Excel جواب متفاوت داد؛ جمع `ISNUMBER` در هر دو یکسان است.
- ✅ `npm audit` (۲۰۲۶-۱۰-۱۹): دو هشدار متوسط از `uuid` کهنه داخل ExcelJS 4.4.0 (GHSA-w5hq-g745-h8pq)؛ «رفع» پیشنهادی npm، ExcelJS را به 3.4 برمی‌گرداند. برای اکسل‌سازی محلی پذیرفتنی است؛ در سرور با ورودی کاربر، دوباره بسنج.
- 🧭 چون نگهداری کند است، اگر به ویژگی تازه (مثلاً جدول محوری) نیاز شد، اول جایگزین را بسنج.

- ✅ بازبینی ۲۰۲۶-۱۰-۲۶: npm هنوز 4.4.0 (و prerelease 4.4.1-prerelease.0)؛ مخزن بایگانی نشده، آخرین push ۲۰۲۵-۰۱-۲۱ (https://api.github.com/repos/exceljs/exceljs).

## مرتبط
[pdf.js](pdfjs-dist.md) · [Poppler](poppler.md) · [S116](../sources/README.md#s116)

✅ (بررسی ۲۰۲۶-۱۰-۳۰) مخزن آرشیو نشده ولی آخرین push در ۲۰۲۵-۰۱-۲۱ بوده و آخرین نسخه‌ی npm همان 4.4.0 از ۲۰۲۳-۱۰-۱۹ است؛ ۸۲۴ issue باز دارد. 🧭 هنوز کار می‌کند، ولی برای پروژه‌ی تازه نسخه را پین کن و اگر باگی دیدی منتظر اصلاح نباش.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
