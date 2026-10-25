---
name: html-validate
slug: html-validate
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: بررسی آفلاین درستی HTML و چند قاعده‌ی دسترسی‌پذیری
url: https://html-validate.org
repo: "https://github.com/html-validate/html-validate"
license: "MIT"
pricing: free
risk: low
sources: [S34, S103, S108]
found_in: [batch-01/P17]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# html-validate

## چیست
✅ linter آفلاین HTML با CLI و API. نسخه‌ی 11.16.4 (npm، دیده‌شده ۲۰۲۶-۱۰-۱۹؛ 🔬 در Sun Shade DXB).

## کی استفاده کنیم
🧭 در مرحله‌ی build پروژه‌های Node.

🔬 QR Order (۲۰۲۶-۱۰-۱۷): روی HTML زنده‌ی اپ با `page.content()` در Playwright، دو قانون سبک ویژگی خطای کاذب دادند و خاموش شدند؛ جزئیات در [بررسی خودکار](../domains/claude-code/verification.md) ([S103](../sources/README.md#s103)).

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
کم. ❓ سایت و مخزن مستقیم خوانده نشدند (فقط ثبت npm).

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
