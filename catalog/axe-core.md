---
name: axe-core (و @axe-core/playwright)
slug: axe-core
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: بررسی خودکار قواعد دسترسی‌پذیری WCAG داخل تست Playwright
url: https://github.com/dequelabs/axe-core
repo: "https://github.com/dequelabs/axe-core"
license: "MPL-2.0"
pricing: free
risk: low
sources: [S34]
found_in: [batch-01/P17]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# axe-core (و @axe-core/playwright)

## چیست
✅ قواعد خودکار WCAG 2.0، 2.1 و 2.2. مواردی که مطمئن نیست را «incomplete» برمی‌گرداند تا دستی بررسی شود. نسخه‌ی 4.14.0 (۲۰۲۶-۱۰). در Playwright: `new AxeBuilder({ page }).analyze()` و بررسی خالی بودن `violations`.

## کی استفاده کنیم
🧭 روی هر صفحه‌ی اصلی، در هر بار اجرای تست.

🔬 QR Order (۲۰۲۶-۱۰-۱۷، نسخه‌ی 4.14.0 با @axe-core/playwright): در اپی که تمام به نظر می‌رسید ده‌ها مورد کنتراست و نام دکمه پیدا کرد؛ پنجره‌ی باز (فرم) و صفحه‌ی سبد را هم جدا بررسی کن، چون در بار اول صفحه دیده نمی‌شوند.

## قیمت و مجوز
✅ MPL-2.0، رایگان.

## ریسک و هشدار
✅ README خودش: «به‌طور میانگین **۵۷٪** مشکلات WCAG را خودکار پیدا می‌کند». یعنی قبولی در axe به معنی «دسترسی‌پذیر» نیست؛ بررسی دستی با کیبورد و صفحه‌خوان لازم است.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
