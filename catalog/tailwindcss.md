---
name: Tailwind CSS
slug: tailwindcss
category: ui-components
domains: [website, apps]
verdict: adopt
status: researched
summary: CSS با کلاس‌های کوچک کاربردی؛ نسخه‌ی ۴ با پیکربندی در خود CSS، کلاس‌های منطقی برای RTL و نوع rtl:
use_when: "styling a React/Next.js/Astro/Vite site or dashboard ; RTL Arabic or Persian layouts"
how: "npm install tailwindcss (4.3.3): use @import tailwindcss and @theme in CSS; upgrade with npx @tailwindcss/upgrade; use logical classes ms-/me-/ps-/pe- for RTL and put dir on html; stay on 3.4 for old browsers; keep own CSS inside @layer"
url: https://tailwindcss.com
repo: "https://github.com/tailwindlabs/tailwindcss"
license: "MIT"
pricing: free
risk: low
sources: [S123]
found_in: [gap-playbooks]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Tailwind CSS

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) ✅ Tailwind Labs به Shopify پیوست (پست رسمی ۲۰۲۶-۰۹-۰۹): Tailwind CSS و پروژه‌های متن‌باز دیگرش MIT می‌مانند؛ ثبت‌نام مشتری تازه برای محصول‌های تجاری Tailwind Labs بسته می‌شود و مشتری‌های فعلی Tailwind Plus و ui.sh را نگه می‌دارند؛ تغییر قیمتی اعلام نشده. آخرین نسخه 4.3.3 (۲۰۲۶-۰۷-۱۶). https://tailwindcss.com/blog/tailwind-is-joining-shopify
✅ چارچوب CSS با کلاس‌های کاربردی کوچک (`p-4`، `flex`، `text-lg`). مالک: Tailwind Labs, Inc. حدود ۹۸ هزار ستاره، فعال.
✅ نسخه‌ی پایدار (npm): **4.3.3** (۲۰۲۶-۰۷-۱۶). نسخه‌ی ۴٫۰٫۰ در ۲۰۲۵-۰۱-۲۱ آمد. نسخه‌ی ۳ هنوز با برچسب `v3-lts` (3.4.19) نگهداری می‌شود.

✅ تغییرهای شکننده‌ی نسخه‌ی ۴ (https://tailwindcss.com/docs/upgrade-guide):
- مرورگر حداقل: Safari 16.4، Chrome 111، Firefox 128. برای مرورگر قدیمی‌تر روی 3.4 بمان.
- پیکربندی در خود CSS: `@import "tailwindcss";` و `@theme { ... }`. فایل `tailwind.config.js` دیگر خودکار خوانده نمی‌شود (با `@config` بارش کن).
- تغییر نام: `shadow-sm` → `shadow-xs`، `shadow` → `shadow-sm`، `outline-none` → `outline-hidden`، `ring` حالا ۱ پیکسل است (`ring-3` برای قبلی). `bg-opacity-*` حذف شد (`bg-black/50`).
- رنگ پیش‌فرض `border` حالا `currentColor` است، نه خاکستری.
- `!` برای important در آخر کلاس می‌آید (`bg-red-500!`).
- ابزار ارتقا: `npx @tailwindcss/upgrade` (Node 20 به بالا).
- 🔬 کلاس‌ها در `@layer utilities` هستند و CSS بیرون از لایه‌ی خودت بر آن‌ها پیروز می‌شود (پنل معامله‌گر کریپتو؛ [تکنولوژی، Tailwind 4](../domains/website/04-tech/tech-stack.md)).

## کی استفاده کنیم
✅ 🔬 داشبورد و نرم‌افزار وب با [Next.js](nextjs.md) و [shadcn/ui](shadcn-ui.md)؛ سایت [Astro](astro.md) یا [Vite](vite.md). 🧭 برای سایت محتوایی [Eleventy](eleventy.md) CSS ساده کافی است.

✅ RTL (عربی و فارسی):
- کلاس‌های منطقی (https://tailwindcss.com/docs/margin): `ms-*` و `me-*` یعنی `margin-inline-start/end`؛ همین‌طور `ps-*`/`pe-*` برای padding، و `mbs-*`/`mbe-*` برای بالا و پایین. سند با مثال `dir="ltr"` و `dir="rtl"` نشان می‌دهد که خودشان جهت را برمی‌گردانند. 🧭 پیش‌فرض ما: همیشه کلاس منطقی، نه `ml-`/`mr-` ([فارسی و RTL](../domains/website/02-design/persian-rtl.md)).
- نوع `rtl:` و `ltr:` (https://tailwindcss.com/docs/hover-focus-and-other-states): با انتخابگر `:dir(rtl)` یا `[dir="rtl"]` روی خود عنصر یا والدش کار می‌کند؛ پس `dir` را روی `<html>` بگذار. فقط برای چیزهایی که کلاس منطقی ندارند (مثل چرخاندن آیکون فلش).

## قیمت و مجوز
✅ رایگان، MIT. 🧭 کامپوننت‌ها و قالب‌های پولی Tailwind Plus محصول جدا و با مجوز خودشان هستند؛ این کارت فقط درباره‌ی خود چارچوب است.

## ریسک و هشدار
کم. ✅ در ۱۲ ماه گذشته هیچ هشدار امنیتی منتشرشده‌ای در مخزن tailwindlabs/tailwindcss نیست (GitHub Security Advisories، ۲۰۲۶-۱۰-۱۹). ❓ صفحه‌ای درباره‌ی تله‌متری در مستندات پیدا نشد. ⚠️ 🔬 تله‌ی لایه‌ها در نسخه‌ی ۴ (بالا).

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md) · دفتر پروژه‌ها · [S123](../sources/README.md#s123)
