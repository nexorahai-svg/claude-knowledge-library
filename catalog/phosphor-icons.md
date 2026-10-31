---
name: Phosphor Icons
slug: phosphor-icons
category: icons-logos
domains: [website, apps]
verdict: adopt
status: researched
summary: مجموعه‌ی آیکون متن‌باز MIT با شش وزن، از جمله duotone، برای React و وب
use_when: "need UI icons or category icons in a React/Next.js site"
how: "npm install @phosphor-icons/react (2.1.10, MIT, 6 weights); in long lists use one SVG sprite with <use>; with Next.js/Turbopack import each icon as its own module, not an all-icons barrel"
url: https://phosphoricons.com/
repo: "https://github.com/phosphor-icons/homepage"
license: "MIT"
pricing: free
risk: low
sources: [S66, S105]
found_in: []
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Phosphor Icons

## چیست
✅ مجموعه‌ی آیکون با بیش از ۱٬۲۰۰ آیکون در شش وزن: Thin، Light، Regular، Bold، Fill و Duotone (طبق README مخزن). ✅ بسته‌ی `@phosphor-icons/react` نسخه‌ی 2.1.10 (ثبت npm، ۲۰۲۶-۱۰-۱۷).

## کی استفاده کنیم
آیکون رابط کاربری و آیکون دسته‌ها. 🔬 در یک فروشگاه واقعی وزن duotone داخل کاشی‌های نئونی استفاده شد و در صفحه‌ی فهرست خدمات همه‌ی آیکون‌ها یک بار در یک اسپرایت SVG فرستاده می‌شوند ([کامپوننت‌ها](../domains/website/04-tech/component-libraries.md)، دفتر پروژه‌ها).

## قیمت و مجوز
✅ رایگان، MIT («MIT © Phosphor Icons»).

## ریسک و هشدار
کم. 🔬 در فهرست بلند، آیکون کامپوننتی را در هر کارت تکرار نکن؛ یک اسپرایت با `<use>` بساز. 🔬 با Next.js و Turbopack همه‌ی آیکون‌ها را در یک فایل جمع نکن: هر صفحه همه را می‌گیرد؛ هر آیکون یک ماژول ([کامپوننت‌ها](../domains/website/04-tech/component-libraries.md)، [S105](../sources/README.md#s105)). ✅ بسته `sideEffects: false` دارد، پس وارد کردن نام‌دار از `@phosphor-icons/react/dist/ssr` فقط همان آیکون را می‌آورد.

## مرتبط
[منابع طراحی](../domains/website/06-resources/design-resources.md) · [S66](../sources/README.md#s66)
