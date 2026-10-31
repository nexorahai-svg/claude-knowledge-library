---
name: html-validate
slug: html-validate
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: بررسی آفلاین درستی HTML و چند قاعده‌ی دسترسی‌پذیری
use_when: "checking HTML correctness at build time in a Node project ; validating rendered HTML in Playwright tests"
how: "npm i -D html-validate (11.x, MIT); run the CLI in the build, or feed page.content() from Playwright; turn off rules that give false positives (two attribute-style rules did)"
url: https://html-validate.org
repo: "https://github.com/html-validate/html-validate"
license: "MIT"
pricing: free
risk: low
sources: [S34, S103, S108]
found_in: [batch-01/P17]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# html-validate

## چیست
✅ linter آفلاین HTML با CLI و API. نسخه‌ی 11.16.4 (npm، دیده‌شده ۲۰۲۶-۱۰-۱۹؛ 🔬 در یک سایت واقعی).

## دستور سریع
✅ ([html-validate.org](https://html-validate.org/usage/index.html)، 11.17.0):
```bash
npm install --save-dev html-validate
echo '{ "extends": ["html-validate:recommended"] }' > .htmlvalidate.json
npx html-validate "dist/**/*.html" --max-warnings 0     # الگو را در گیومه بنویس
```
✅ تنظیم‌های مهم: هر قاعده در `"rules"` با `"error"`، `"warn"` یا `"off"`؛ `--max-warnings 0` هشدار را هم شکست می‌داند؛ `-f stylish|json|checkstyle` قالب خروجی؛ روی صفحه‌ی رندرشده‌ی Playwright خروجی `page.content()` را به API بده.
خطاهای رایج (🔬 [بررسی خودکار](../domains/claude-code/verification.md) و بخش پایین): روی `page.content()` ویژگی بولی `checked=""` می‌شود و `attribute-boolean-style` و `attribute-empty-style` خطای کاذب می‌دهند؛ قاعده‌های سلیقه‌ای (`doctype-style`، `no-inline-style`، `tel-non-breaking`، `no-trailing-whitespace`) را خاموش کن تا خطای واقعی دیده شود؛ `valid-id` با شناسه‌های `useId()` ری‌اکت به `relaxed` نیاز دارد؛ `text-content` برای دکمه‌ی آیکونی با فقط `title` خطا می‌دهد؛ `aria-label` را فقط به دکمه‌ی بدون متن بده. نسخه‌ی 11.16.2 وابستگی آسیب‌پذیر ajv و fast-uri داشت؛ `overrides` را ببین.

## کی استفاده کنیم
🧭 در مرحله‌ی build پروژه‌های Node.

🔬 یک پروژه‌ی سفارش با QR (۲۰۲۶-۱۰-۱۷): روی HTML زنده‌ی اپ با `page.content()` در Playwright، دو قانون سبک ویژگی خطای کاذب دادند و خاموش شدند؛ جزئیات در [بررسی خودکار](../domains/claude-code/verification.md) ([S103](../sources/README.md#s103)).

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
کم. ✅ مخزن https://github.com/html-validate/html-validate مجوز MIT دارد، بایگانی نشده و آخرین push آن ۲۰۲۶-۱۰-۳۰ است (GitHub API).

## روی فروشگاه و پنل Next.js 16 🔬

(یک فروشگاه و پنل Next.js 16، ۲۰۲۶-۱۰-۲۸، 11.16.2) روی ۶۶ صفحه‌ی فروشگاه و ۱۸ صفحه‌ی پنل که axe همه‌شان سبز بود، اولین اجرا همه را رد کرد. خطاهای واقعی: دو `<nav>` بی‌نام (سرصفحه و منوی موبایل)، شناسه‌ی تکراری کلید زبان در دو منو، `readonly` روی checkbox، `autocomplete="tel-national"` روی `type="tel"` (✅ طبق جدول WHATWG فقط برای گروه Text؛ `type="text"` با `inputMode="numeric"` همان صفحه‌کلید را می‌دهد)، `role="region"` به‌جای `<section>`، `<div>` داخل `<span>`، فرم بی‌دکمه‌ی submit، شناسه‌ی فاصله‌دار. بی‌اثر یا سلیقه‌ای: `valid-id` با شناسه‌های `useId()` ری‌اکت مثل `_R_` (گزینه‌ی `relaxed`)، `no-redundant-for`، و `long-title` (به هشدار؛ متن عنوان مالک پروژه است). نسخه‌ی 11.16.2 ajv و fast-uri آسیب‌پذیر دارد؛ `overrides: { "fast-uri": "3.1.9" }`.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
