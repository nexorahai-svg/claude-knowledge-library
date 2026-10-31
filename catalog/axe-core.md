---
name: axe-core (و @axe-core/playwright)
slug: axe-core
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: بررسی خودکار قواعد دسترسی‌پذیری WCAG داخل تست Playwright
use_when: "adding accessibility checks to Playwright tests ; verifying WCAG compliance of a web app before release"
how: "npm i -D @axe-core/playwright; in tests run `new AxeBuilder({ page }).analyze()` and assert `violations` is empty on every main page and also on open dialogs/forms and the cart; automation finds only about 57% of issues so still check keyboard and screen reader"
url: https://github.com/dequelabs/axe-core
repo: "https://github.com/dequelabs/axe-core"
license: "MPL-2.0"
pricing: free
risk: low
sources: [S34]
found_in: [batch-01/P17]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# axe-core (و @axe-core/playwright)

## چیست
✅ قواعد خودکار WCAG 2.0، 2.1 و 2.2. مواردی که مطمئن نیست را «incomplete» برمی‌گرداند تا دستی بررسی شود. نسخه‌ی 4.14.0 (۲۰۲۶-۱۰). در Playwright: `new AxeBuilder({ page }).analyze()` و بررسی خالی بودن `violations`.

## دستور سریع
✅ ([README رسمی](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright)، @axe-core/playwright 4.14.0 که نسخه‌ی axe-core 4.14.x را همراه دارد):
```bash
npm i -D @axe-core/playwright
```
```ts
import { AxeBuilder } from '@axe-core/playwright';
const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa']).analyze();
expect(results.violations).toEqual([]);
```
✅ تنظیم‌های مهم: `withTags([...])` سطح قواعد؛ `.include('.panel')` و `.exclude('.ad')` محدوده؛ `.disableRules('color-contrast')` فقط برای خطای کاذب ثابت‌شده؛ `analyze()` را پس از باز شدن پنجره، فرم، سبد و در تم تیره و صفحه‌ی واردشده هم اجرا کن.
خطاهای رایج (🔬 [بررسی خودکار](../domains/claude-code/verification.md)): بدون `reducedMotion: "reduce"` عناصر وسط fade-in کنتراست پایین می‌گیرند و ده‌ها خطای کاذب می‌آید؛ هدر چسبان و منوی ثابت پایین `target-size` کاذب می‌دهند؛ جدول و `pre` اسکرولی `scrollable-region-focusable` می‌گیرند. ✅ فقط حدود ۵۷٪ مشکل WCAG خودکار پیدا می‌شود؛ کیبورد و صفحه‌خوان را دستی بررسی کن.

## کی استفاده کنیم
🧭 روی هر صفحه‌ی اصلی، در هر بار اجرای تست.

🔬 یک پروژه‌ی سفارش با QR (۲۰۲۶-۱۰-۱۷، نسخه‌ی 4.14.0 با @axe-core/playwright): در اپی که تمام به نظر می‌رسید ده‌ها مورد کنتراست و نام دکمه پیدا کرد؛ پنجره‌ی باز (فرم) و صفحه‌ی سبد را هم جدا بررسی کن، چون در بار اول صفحه دیده نمی‌شوند.

## قیمت و مجوز
✅ MPL-2.0، رایگان.

## ریسک و هشدار
✅ README خودش: «به‌طور میانگین **۵۷٪** مشکلات WCAG را خودکار پیدا می‌کند». یعنی قبولی در axe به معنی «دسترسی‌پذیر» نیست؛ بررسی دستی با کیبورد و صفحه‌خوان لازم است.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
