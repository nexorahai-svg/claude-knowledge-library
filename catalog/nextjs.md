---
name: Next.js
slug: nextjs
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: فریم‌ورک React از Vercel برای سایت و نرم‌افزار وب با رندر سرور، ساخت ایستا و API؛ باید همیشه به‌روز بماند
url: https://nextjs.org
repo: "https://github.com/vercel/next.js"
license: "MIT"
pricing: free
risk: medium
sources: [S123]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Next.js

## چیست
✅ فریم‌ورک React با App Router، Server Components، Server Actions، رندر سرور، ساخت ایستا و ISR. مالک و نگهدارنده: Vercel (متن مجوز: «Copyright (c) 2025 Vercel, Inc.»). حدود ۱۴۳ هزار ستاره، فعال.
✅ نسخه‌ی پایدار (npm، `latest`): **16.4.2** (۲۰۲۶-۱۰-۱۵). نسخه‌ی ۱۶٫۰٫۰ در ۲۰۲۵-۱۰-۲۲ آمد. شاخه‌ی ۱۵ فقط وصله‌ی امنیتی می‌گیرد (`backport`: 15.5.28). Node حداقل 20.9.

✅ تغییرهای شکننده‌ی نسخه‌ی ۱۶ (https://nextjs.org/docs/app/guides/upgrading/version-16):
- Turbopack پیش‌فرض `next dev` و `next build` است؛ پیکربندی `webpack` سفارشی build را می‌شکند مگر با `--webpack`.
- `cookies()`، `headers()`، `draftMode()`، `params` و `searchParams` فقط async؛ دسترسی همگام کاملاً حذف شد.
- `middleware.ts` منسوخ و `proxy.ts` جایش آمد؛ `proxy` فقط روی Node اجرا می‌شود، نه edge.
- پیش‌فرض‌های `next/image` سخت‌تر: `qualities` فقط `[75]`، `minimumCacheTTL` چهار ساعت، IP محلی بسته، حداکثر ۳ redirect.
- حذف شد: AMP، دستور `next lint`، `serverRuntimeConfig` و `publicRuntimeConfig`. همه‌ی اسلات‌های parallel route فایل `default.js` لازم دارند.
- ابزار ارتقا: `npx @next/codemod@canary upgrade latest`.

## کی استفاده کنیم
✅ 🔬 نرم‌افزار وب و داشبورد با ورود کاربر، داده‌ی حساس، Server Actions و کامپوننت‌های زیاد React (با [shadcn/ui](shadcn-ui.md)). در MARIO E.G.S.H روی سرور خودمان پشت [Caddy](caddy.md) و در پنل معامله‌گر کریپتو به کار رفت (دفتر پروژه‌ها).
🧭 برای سایت معرفی که فقط محتواست، [Eleventy](eleventy.md) یا [Astro](astro.md) سبک‌ترند.

✅ چندزبانه و RTL (https://nextjs.org/docs/app/guides/internationalization): App Router مسیریابی زبان آماده ندارد. خودت پوشه‌ی `app/[lang]` می‌سازی، در `proxy.ts` زبان را از `Accept-Language` پیدا و redirect می‌کنی، و با `generateStaticParams` صفحه‌ی هر زبان را ایستا می‌سازی. ❓ سند رسمی درباره‌ی `dir="rtl"` چیزی نمی‌گوید؛ `lang` و `dir` را خودت در `app/[lang]/layout` بگذار ([فارسی و RTL](../domains/website/02-design/persian-rtl.md)). کتابخانه‌هایی مثل `next-intl` فقط در فهرست منابع سند آمده‌اند، نه به‌عنوان توصیه.

## میزبانی
| میزبان | واقعیت | منبع |
|---|---|---|
| خروجی ایستا (`output: 'export'`) | ✅ هر میزبان فایل ایستا، از جمله Cloudflare Pages. ولی این‌ها کار نمی‌کنند: cookies، rewrites، redirects، headers، `proxy`، ISR، بهینه‌سازی تصویر با loader پیش‌فرض، Draft Mode، Server Actions، مسیر پویا بدون `generateStaticParams` | https://nextjs.org/docs/app/guides/static-exports |
| Cloudflare (سرور) | ✅ Cloudflare حالا **vinext** را پیش‌فرض می‌داند: افزونه‌ی Vite که API نکست را دوباره پیاده می‌کند، روی Workers، و خودش می‌گوید «در بتا است». OpenNext فقط برای اپ‌های موجود OpenNext. Pages فقط برای خروجی ایستا | https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/ |
| OpenNext روی Cloudflare | ✅ `@opennextjs/cloudflare` 1.20.12 (۲۰۲۶-۱۰-۱۵)، MIT، نگهداری جامعه‌ی OpenNext؛ روی Workers با Node. پشتیبانی: Next 16 و آخرین نسخه‌های ۱۴ و ۱۵، App Router، SSR، ISR، `use cache`. پشتیبانی نمی‌شود: «Node Middleware» (از ۱۵٫۲). ❓ پس `proxy.ts` نسخه‌ی ۱۶ (که همیشه Node است) احتمالاً کار نمی‌کند؛ صفحه صریح نگفته. بهینه‌سازی تصویر فقط با Cloudflare Images. سقف حجم Worker: ۳ مبی‌بایت رایگان، ۱۰ مبی‌بایت پولی (فشرده) | https://opennext.js.org/cloudflare |
| Netlify | ✅ از ۱۳٫۵ به بعد با آداپتور OpenNext: App Router، ISR، middleware، تصویر کامل. محدودیت: headers و redirects بعد از middleware اجرا می‌شوند؛ middleware روی Node به `fs` دسترسی ندارد | https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/overview/ |
| Vercel | ✅ بهترین سازگاری. ولی Hobby «فقط شخصی و غیرتجاری» است؛ حتی اگر فقط برنامه‌نویس پول گرفته باشد تجاری حساب می‌شود ([کارت Vercel](vercel.md)) | https://vercel.com/docs/limits/fair-use-guidelines |
| سرور خودمان | ✅ 🔬 `next start` پشت Caddy ([سرور خودمان](../domains/website/04-tech/self-hosted-server.md)) | |

🧭 نتیجه: اگر nonce در `proxy.ts` یا Server Actions لازم است، سرور خودمان یا Vercel Pro. روی Cloudflare رایگان یا خروجی ایستا، یا vinext پس از آزمون سازگاری.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
⚠️ ✅ **هشدارهای امنیتی زیاد** (GitHub Security Advisories، https://github.com/vercel/next.js/security/advisories): در ۱۲ ماه گذشته ۴۸ هشدار منتشر شد، از جمله چند «بحرانی» با اجرای کد از راه دور. مهم‌ترین‌ها:
- ۲۰۲۵-۱۲-۰۳ · GHSA-9qr9-h5gf-34mp (CVE-2025-55182) بحرانی: اجرای کد در React Server Components؛ رفع در 16.0.7 و 15.5.7.
- ۲۰۲۶-۰۵-۰۶ · GHSA-492v-c6pp-mqqv، GHSA-36qx-fr4f-26g5 (i18n در Pages Router) و GHSA-267c-6grr-h53f بالا: **دور زدن احراز هویت در Middleware/Proxy**؛ رفع در 16.2.5 و 15.5.16؛ رفع ناقص با GHSA-26hh-7cqf-hhc6 در 16.2.6 و 15.5.18 تکمیل شد.
- ۲۰۲۶-۰۷-۲۱ · GHSA-6gpp-xcg3-4w24 بالا: دور زدن Proxy با Turbopack و فقط یک زبان در `i18n.locales`؛ رفع 16.2.11.
- ۲۰۲۶-۰۸-۲۵ · GHSA-2xp9-vwfh-vxw4 (تصویر AVIF) و GHSA-p293-qw3h-jr36 (سرور ویندوز) بحرانی: اجرای کد بدون احراز هویت؛ رفع 16.3.3 و 15.5.24.
- ۲۰۲۶-۰۹-۲۲ · GHSA-vcvr-r3jv-pc5j بحرانی: اجرای کد در `next/og`؛ رفع 16.3.6. ۲۰۲۶-۰۹-۳۰: چند هشدار SSRF و آلودگی کش؛ رفع 16.3.8.
- ۲۰۲۶-۱۰-۱۴ · GHSA-2464-fhr4-w9xw (تصویر SVG، از طریق `sharp`) و GHSA-673q-mjm6-r5xr (`use cache`) بحرانی: اجرای کد بدون احراز هویت؛ رفع **16.4.1** و 15.5.28.

🧭 قاعده‌ی ما: حداقل **16.4.1** (الان 16.4.2). هر پروژه‌ی Next.js را ماهی یک بار و بعد از هر هشدار بحرانی به‌روز کن. احراز هویت را فقط به `proxy.ts` نسپار؛ در مسیر داده‌ی سرور هم چک کن (راه‌حل خود هشدارها).

✅ تله‌متری (https://nextjs.org/telemetry): داده‌ی ناشناس می‌فرستد (دستور، نسخه، مشخصات کلی سیستم، افزونه‌ها، زمان build، نام ابزارهای MCP در حالت توسعه). خاموش کردن: `npx next telemetry disable` یا متغیر `NEXT_TELEMETRY_DISABLED=1` (در CI هم بگذار). دیدن داده بدون فرستادن: `NEXT_TELEMETRY_DEBUG=1`.

## تله‌های حالت توسعه 🔬

- (۲۰۲۶-۱۰-۲۴، پروژه یک فروشگاه مشتری، Next 16.4.2 با Turbopack) بعد از خاموش و روشن شدن رایانه، `next dev` پنل در **حلقه بارگذاری دوباره** افتاد: هر بار صفحه باز می‌شد «Compiled in 2ms» و «[Fast Refresh] rebuilding» و دوباره بارگذاری کامل، حدود هر ۱٫۲ ثانیه؛ هیچ فایلی عوض نشده بود. نشانه در آزمون‌ها: `page.goto ... networkidle` با Timeout در همه صفحه‌های واردشده. راه‌حل: سرور را بستن، پوشه `.next` را کنار گذاشتن، دوباره روشن کردن. برای دیدن علت: `.next/dev/logs/next-development.log` و شمردن ناوبری‌های صفحه با Playwright (`framenavigated`).
- (همان پروژه) `:text-is()` در Playwright کوچک‌ترین عنصری را می‌گیرد که کل متن را دارد؛ اگر کل نام داخل `<mark>` باشد، `a.name:text-is(...)` دیگر پیدا نمی‌شود. به‌جایش `locator('a.name').filter({ hasText: /^...$/ })`.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · [Tailwind CSS](tailwindcss.md) · [Vercel](vercel.md) · [Cloudflare Pages](cloudflare-pages.md) · [S123](../sources/README.md#s123)
