---
name: Poppler (pdftoppm، pdftotext، pdfinfo)
slug: poppler
category: data-documents
domains: [website, apps, claude-code]
verdict: adopt
status: researched
summary: ابزارهای خط فرمان PDF: تصویر هر صفحه، متن خام و تعداد صفحه؛ تا Claude خودش PDF را ببیند
use_when: "checking PDF text extraction visually ; converting a PDF page to an image for Claude to Read ; counting PDF pages"
how: "pdftoppm -png -r 60 -f N -l N file.pdf out then Read the image; pdfinfo for page count; install poppler-utils (Debian) or winget install oschwartz10612.Poppler; use as separate tool only (GPL)"
url: https://poppler.freedesktop.org/
repo: "https://gitlab.freedesktop.org/poppler/poppler"
license: "GPL-2.0 یا GPL-3.0"
pricing: free
risk: low
sources: [S116]
found_in: []
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Poppler (pdftoppm، pdftotext، pdfinfo)

## چیست
✅ کتابخانه و ابزارهای خط فرمان PDF. روی Debian 13 بسته‌ی `poppler-utils` نسخه‌ی 25.03 است؛ روی ویندوز با `winget install oschwartz10612.Poppler` ([S116](../sources/README.md#s116)).

## کی استفاده کنیم
🔬 `pdftoppm -png -r 60 -f N -l N file.pdf out` یک صفحه را تصویر می‌کند تا Claude با ابزار Read آن را ببیند و استخراج متن را با چشم کنترل کند؛ `pdfinfo` تعداد صفحه را می‌دهد. در یک پروژه‌ی واقعی برای کنترل استخراج لیست قیمت به کار رفت (دفتر پروژه‌ها).

## قیمت و مجوز
✅ رایگان، GPL. فقط به‌عنوان ابزار جدا اجرا شود؛ اگر همراه برنامه‌ای فرستاده شود، شرط GPL را بخوان.

## ریسک و هشدار
- 🔬 روی ویندوز، شلی که پیش از نصب باز شده آن را در PATH نمی‌بیند؛ با مسیر کامل صدا بزن یا برنامه را دوباره باز کن.
- 🧭 `pdftotext` نسخه‌ی xpdf داخل Git for Windows مختصات نمی‌دهد؛ برای جدول از [pdf.js](pdfjs-dist.md) استفاده کن.

## مرتبط
[pdf.js](pdfjs-dist.md) · [LibreOffice](libreoffice-headless.md)
