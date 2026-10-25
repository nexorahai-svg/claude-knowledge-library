---
name: pdf.js (pdfjs-dist)
slug: pdfjs-dist
category: data-documents
domains: [website, apps]
verdict: adopt
status: researched
summary: کتابخانه‌ی Mozilla برای خواندن PDF؛ در Node متن را با مختصات و خط‌های جدول می‌دهد
url: https://github.com/mozilla/pdf.js
repo: "https://github.com/mozilla/pdf.js"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S116]
found_in: []
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# pdf.js (pdfjs-dist)

## چیست
✅ موتور PDF مرورگر Firefox، به‌صورت بسته‌ی npm ‏`pdfjs-dist`. نسخه‌ی پایدار ۲۰۲۶-۱۰ ‏6.4.299 است؛ مخزن فعال ([S116](../sources/README.md#s116)).

## کی استفاده کنیم
🔬 استخراج جدول از لیست قیمت تأمین‌کننده (PDF): متن هر تکه با x و y، و ستون‌ها از خط‌های جدول (عملگرهای مسیر). در یک فروشگاه مشتری از ۲۲ فایل «New Arrival» با SKU، EAN و قیمت، ۱۰۷ نوع کالا بی‌خطا درآمد و با تصویر صفحه کنترل شد (دفتر پروژه‌ها).

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
- 🔬 رندر صفحه به تصویر در Node با `@napi-rs/canvas` روی ویندوز segfault داد؛ برای تصویر صفحه از [Poppler](poppler.md) (`pdftoppm`) استفاده کن.
- 🔬 **ارتقا از 4.x به 5 یا 6 کد خواندن خط جدول را می‌شکند:** در 4.x آرگومان `constructPath` به شکل `[ops, args]` بود (با عملگر جدای rectangle)؛ از 5 به بعد `[paintOp, [path], minMax]` است و path یک Float32Array با کدهای ۰ moveTo، ۱ lineTo، ۲ curveTo، ۳ quadraticCurveTo، ۴ closePath، و مستطیل به شکل moveTo + سه lineTo + closePath می‌آید. خطای دیده‌شده: `ops is not iterable`. در یک فروشگاه مشتری اسکریپت هر دو قالب را خواند و خروجی 6.4.299 با 4.10 بایت‌به‌بایت برابر شد (۲۰۲۶-۱۰-۱۹). روش امن: خروجی نسخه‌ی فعلی را نگه دار، در کپی جدا ارتقا بده، مقایسه کن.
- 🧭 pdfjs-dist 6 روی Node 24 آزموده شد؛ نسخه‌ی کمینه‌ی Node را پیش از ارتقا در package.json آن ببین.
- 🧭 PDF اسکن‌شده متن ندارد؛ آنجا OCR لازم است.

## مرتبط
[ExcelJS](exceljs.md) · [Poppler](poppler.md)
