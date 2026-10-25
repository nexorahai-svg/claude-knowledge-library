---
name: Vite
slug: vite
category: site-generators
domains: [website, apps]
verdict: adopt
status: researched
summary: ابزار توسعه و build برای وب؛ پایه‌ی Astro و vinext؛ برای داشبورد تک‌منظوره با TypeScript ساده
url: https://vite.dev
repo: "https://github.com/vitejs/vite"
license: "MIT"
pricing: free
risk: low
sources: [S123]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Vite

## چیست
✅ سرور توسعه با بارگذاری فوری و ابزار build برای JavaScript و TypeScript، با یا بدون فریم‌ورک (React، Vue، Svelte یا هیچ). حدود ۸۳ هزار ستاره، فعال. پایه‌ی [Astro](astro.md) و vinext (اجرای Next.js روی Cloudflare) هم هست.
✅ نسخه‌ی پایدار (npm): **8.3.4** (۲۰۲۶-۱۰-۰۸). Node: `^20.19.0 || >=22.12.0`.
✅ نگهدارنده (https://vite.dev/blog/announcing-vite8): تیم Vite؛ پروژه را شرکت VoidZero با همکاری Bolt و NuxtLabs پشتیبانی می‌کند. متن مجوز: «VoidZero Inc. and Vite contributors».

✅ نسخه‌ی ۸ (۲۰۲۶-۰۳-۱۲): Rolldown (باندلر Rust) جای esbuild و Rollup را گرفت و Oxc کامپایلر شد؛ ادعای خود تیم: build تا ۱۰ تا ۳۰ برابر سریع‌تر ❓ (روی پروژه‌ی ما سنجیده نشده). یک لایه‌ی سازگاری تنظیم‌های `esbuild` و `rollupOptions` قدیمی را ترجمه می‌کند، پس بیشتر پروژه‌ها بی‌تغییر ارتقا می‌یابند. برای پروژه‌ی پیچیده: اول روی Vite 7 بسته‌ی `rolldown-vite` را امتحان کن، بعد Vite 8. حجم نصب حدود ۱۵ مگابایت بیشتر از ۷. راهنمای کامل: https://vite.dev/guide/migration

## کی استفاده کنیم
🧭 داشبورد یا صفحه‌ی تک‌منظوره‌ی متحرک با TypeScript ساده، بدون فریم‌ورک (مثل [دستور شیشه‌ای](../domains/website/02-design/design-styles.md))؛ اپ تک‌صفحه‌ای React بدون نیاز به رندر سرور؛ و رابط [Tauri](tauri.md) یا [Electron](electron.md). خروجی `vite build` فایل ایستاست و روی [Cloudflare Pages](cloudflare-pages.md) رایگان می‌نشیند. ❓ هنوز به‌تنهایی در پروژه‌ی خودمان آزموده نشده.
🧭 چندزبانه و RTL مسئله‌ی خود Vite نیست؛ با کد خودت یا فریم‌ورک بالای آن حل می‌شود.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
کم. ✅ هشدارهای ۱۲ ماه گذشته (https://github.com/vitejs/vite/security/advisories) همه مربوط به **سرور توسعه** هستند، نه سایت منتشرشده:
- ۲۰۲۶-۰۴-۰۶ · GHSA-p9ff-h696-f583 (CVE-2026-39363) بالا: خواندن هر فایل از طریق WebSocket سرور توسعه؛ رفع 8.0.5 (و 7.3.2، 6.4.2). در همان روز دو هشدار متوسط دیگر (`server.fs.deny` و `.map`).
- ۲۰۲۶-۰۶-۰۱ · GHSA-fx2h-pf6j-xcff متوسط: دور زدن `server.fs.deny` در ویندوز؛ رفع 8.0.16.
- ۲۰۲۶-۱۰-۰۶ · GHSA-rq7h-c2jc-7f22 و GHSA-vfpm-58rq-9qcg متوسط، GHSA-9jrq-w75r-8gcw کم: فایل بیرون از `server.fs.allow`؛ رفع **8.3.3**.

🧭 قاعده‌ی ما: حداقل 8.3.3؛ سرور توسعه را با `--host` روی شبکه‌ی عمومی باز نکن.
❓ صفحه‌ای درباره‌ی تله‌متری در مستندات Vite پیدا نشد.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [Astro](astro.md) · [Next.js](nextjs.md) · [S123](../sources/README.md#s123)
