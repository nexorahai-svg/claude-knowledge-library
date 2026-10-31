---
name: Kensaku
slug: kensaku
category: local-ai
domains: [apps, security]
verdict: assess
status: researched
summary: جست‌وجوگر و لانچر فایل رومیزی (Rust) با جست‌وجوی نام، متن کامل، OCR، معنایی و سرور MCP
use_when: "Searching local files by content, OCR text or meaning ; giving an agent read-only search over a documents folder via MCP"
how: "Read-only MCP by default, keep it that way; builds are unsigned so build from source or verify; README no-telemetry claim is unverified"
url: https://github.com/yjid/kensaku
repo: "https://github.com/yjid/kensaku"
license: "MIT"
pricing: free
risk: medium
sources: [S206]
found_in: [batch-25]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Kensaku

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README) لانچر فایل رومیزی به زبان Rust: جست‌وجوی نام، متن کامل (PDF، DOCX، EPUB، کد)، OCR تصویر (Tesseract و اختیاری PP-OCRv6)، جست‌وجوی معنایی، پرسش زمانی به زبان طبیعی، `kensaku-cli` و سرور MCP (پیش‌فرض فقط‌خواندنی). ویندوز، مک، لینوکس. MIT، ۲۱۵ ستاره، ساخته‌شده ۲۰۲۶-۱۰-۲۴.
❓ README ادعا می‌کند بدون حساب، تله‌متری و ابر است؛ در کد راستی‌آزمایی نشد. ❓ OCR فارسی نامعلوم. ✅ بیلدها بی‌امضا هستند.

## کی استفاده کنیم
🧭 آزمایش برای جست‌وجوی فایل‌های شخصی؛ روی داده‌ی مشتری نه، تا کد بررسی شود.

## قیمت و مجوز
MIT، رایگان.

## ریسک و هشدار
به محتوای همه‌ی فایل‌ها ایندکس می‌سازد؛ بیلد بی‌امضا؛ MCP را فقط‌خواندنی نگه دار.

## مرتبط
- https://github.com/yjid/kensaku
