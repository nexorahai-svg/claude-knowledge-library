---
name: Fancy Components
slug: fancy-components
category: ui-components
domains: [website]
verdict: trial
status: researched
summary: کامپوننت‌ها و افکت‌های متحرک خلاقانه برای React (متن، تصویر، فیزیک)
use_when: "need an animated React component for text, images or physics ; one special animated section in a React site"
how: "Trial first on a small task: needs React, Tailwind and motion (pnpm add tailwindcss@latest motion); run pnpm dlx shadcn@latest init, add registry @fancy = https://fancycomponents.dev/r/{name}.json in components.json, then pnpm dlx shadcn add @fancy/component-name; MIT; honour prefers-reduced-motion"
url: https://www.fancycomponents.dev
repo: "https://github.com/danielpetho/fancy"
license: "MIT"
pricing: free
risk: low
sources: [S122]
found_in: [batch-15]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# Fancy Components

## چیست
✅ MIT؛ حدود ۳٫۳ هزار ستاره؛ آخرین تغییر ۲۰۲۶-۰۳-۱۴. React 19، Next 16، Tailwind 4، کتابخانه‌ی `motion` و matter-js برای فیزیک؛ ساختار ثبت کامپوننت بر پایه‌ی shadcn. ✅ مراحل نصب با مستندات رسمی (۲۰۲۶-۱۰-۲۷) تطبیق داده شد: pnpm add tailwindcss@latest motion ؛ pnpm dlx shadcn@latest init ؛ افزودن رجیستری @fancy به components.json.

✅ نصب و اجرا (https://www.fancycomponents.dev/docs/installation، ۲۰۲۶-۱۰-۲۷): pnpm dlx shadcn add @fancy/component-name (پس از افزودن رجیستری @fancy به components.json)

## کی استفاده کنیم
🧪 برای یک بخش متحرک خاص در سایت React، کنار [کتابخانه‌های کامپوننت](../domains/website/04-tech/component-libraries.md). فقط React است؛ برای Flutter نه.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
کم. 🧭 افکت سنگین را با `prefers-reduced-motion` و نسخه‌ی ساده برای دستگاه ضعیف همراه کن.

## مرتبط
[S122](../sources/README.md#s122) · غربال دسته‌ی ۱۵
