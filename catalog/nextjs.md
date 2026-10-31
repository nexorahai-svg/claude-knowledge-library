---
name: Next.js
slug: nextjs
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: فریم‌ورک React از Vercel برای سایت و نرم‌افزار وب با رندر سرور، ساخت ایستا و API؛ باید همیشه به‌روز بماند
use_when: "building a web app or dashboard with user login, sensitive data and Server Actions ; React project with many components"
how: "npx create-next-app (16.4.3, Node >= 20.9, Turbopack default); await cookies()/headers()/params; use proxy.ts not middleware.ts; set canonical/hreflang in each page generateMetadata (layout alternates leak to every page); nonce CSP only on fully dynamic apps, static CSP with Cache Components; for content-only sites prefer Eleventy or Astro; upgrade with npx @next/codemod@canary upgrade latest; Vercel Hobby is non-commercial only"
url: https://nextjs.org
repo: "https://github.com/vercel/next.js"
license: "MIT"
pricing: free
risk: medium
sources: [S123, S182, S184]
found_in: [gap-playbooks]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Next.js

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) ⚠️ اعلان پیش‌از‌موعد (۲۰۲۶-۱۰-۲۷): انتشار امنیتی زمان‌بندی‌شده در **۲۰۲۶-۱۱-۰۳** برای هفت آسیب‌پذیری با شدت متوسط؛ همان روز پروژه‌های Next.js را به‌روز کن. https://nextjs.org/blog/upcoming-nextjs-security-release-november-2026
✅ فریم‌ورک React با App Router، Server Components، Server Actions، رندر سرور، ساخت ایستا و ISR. مالک و نگهدارنده: Vercel (متن مجوز: «Copyright (c) 2025 Vercel, Inc.»). حدود ۱۴۳ هزار ستاره، فعال.
✅ نسخه‌ی پایدار (npm، `latest`): **16.4.3** (۲۰۲۶-۱۰-۲۳؛ قبلی 16.4.2 در ۲۰۲۶-۱۰-۱۵). نسخه‌ی ۱۶٫۰٫۰ در ۲۰۲۵-۱۰-۲۲ آمد. شاخه‌ی ۱۵ فقط وصله‌ی امنیتی می‌گیرد (`backport`: 15.5.28). Node حداقل 20.9.

✅ تغییرهای شکننده‌ی نسخه‌ی ۱۶ (https://nextjs.org/docs/app/guides/upgrading/version-16):
- Turbopack پیش‌فرض `next dev` و `next build` است؛ پیکربندی `webpack` سفارشی build را می‌شکند مگر با `--webpack`.
- `cookies()`، `headers()`، `draftMode()`، `params` و `searchParams` فقط async؛ دسترسی همگام کاملاً حذف شد.
- `middleware.ts` منسوخ و `proxy.ts` جایش آمد؛ `proxy` فقط روی Node اجرا می‌شود، نه edge.
- پیش‌فرض‌های `next/image` سخت‌تر: `qualities` فقط `[75]`، `minimumCacheTTL` چهار ساعت، IP محلی بسته، حداکثر ۳ redirect.
- حذف شد: AMP، دستور `next lint`، `serverRuntimeConfig` و `publicRuntimeConfig`. همه‌ی اسلات‌های parallel route فایل `default.js` لازم دارند.
- ابزار ارتقا: `npx @next/codemod@canary upgrade latest`.

## کی استفاده کنیم
✅ 🔬 نرم‌افزار وب و داشبورد با ورود کاربر، داده‌ی حساس، Server Actions و کامپوننت‌های زیاد React (با [shadcn/ui](shadcn-ui.md)). در یک فروشگاه واقعی روی سرور خودمان پشت [Caddy](caddy.md) و در پنل معامله‌گر کریپتو به کار رفت (دفتر پروژه‌ها).
🧭 برای سایت معرفی که فقط محتواست، [Eleventy](eleventy.md) یا [Astro](astro.md) سبک‌ترند.

✅ چندزبانه و RTL (https://nextjs.org/docs/app/guides/internationalization): App Router مسیریابی زبان آماده ندارد. خودت پوشه‌ی `app/[lang]` می‌سازی، در `proxy.ts` زبان را از `Accept-Language` پیدا و redirect می‌کنی، و با `generateStaticParams` صفحه‌ی هر زبان را ایستا می‌سازی. ✅ در راهنمای رسمی بین‌المللی‌سازی (https://nextjs.org/docs/app/guides/internationalization) و صفحه‌ی layout (https://nextjs.org/docs/app/api-reference/file-conventions/layout) نشانی از rtl یا dir نیست (۲۰۲۶-۱۰-۳۰)؛ `lang` و `dir` را خودت در `app/[lang]/layout` بگذار ([فارسی و RTL](../domains/website/02-design/persian-rtl.md)). کتابخانه‌هایی مثل `next-intl` فقط در فهرست منابع سند آمده‌اند، نه به‌عنوان توصیه.

## میزبانی
| میزبان | واقعیت | منبع |
|---|---|---|
| خروجی ایستا (`output: 'export'`) | ✅ هر میزبان فایل ایستا، از جمله Cloudflare Pages. ولی این‌ها کار نمی‌کنند: cookies، rewrites، redirects، headers، `proxy`، ISR، بهینه‌سازی تصویر با loader پیش‌فرض، Draft Mode، Server Actions، مسیر پویا بدون `generateStaticParams` | https://nextjs.org/docs/app/guides/static-exports |
| Cloudflare (سرور) | ✅ صفحه‌ی راهنما ‏«Middleware and proxy routes» را «Supported» می‌نویسد (شامل `middleware.ts` و `proxy.ts`). Cloudflare حالا **vinext** را پیش‌فرض می‌داند: افزونه‌ی Vite که API نکست را دوباره پیاده می‌کند، روی Workers، و خودش می‌گوید «در بتا است». OpenNext فقط برای اپ‌های موجود OpenNext. Pages فقط برای خروجی ایستا | https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/ |
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

🧭 قاعده‌ی ما: حداقل **16.4.1** (الان 16.4.3). هر پروژه‌ی Next.js را ماهی یک بار و بعد از هر هشدار بحرانی به‌روز کن. احراز هویت را فقط به `proxy.ts` نسپار؛ در مسیر داده‌ی سرور هم چک کن (راه‌حل خود هشدارها).

✅ تله‌متری (https://nextjs.org/telemetry): داده‌ی ناشناس می‌فرستد (دستور، نسخه، مشخصات کلی سیستم، افزونه‌ها، زمان build، نام ابزارهای MCP در حالت توسعه). خاموش کردن: `npx next telemetry disable` یا متغیر `NEXT_TELEMETRY_DISABLED=1` (در CI هم بگذار). دیدن داده بدون فرستادن: `NEXT_TELEMETRY_DEBUG=1`.

## صفحه‌ی ۴۰۴ خالی در 16.3 به بعد ✅ 🔬

- ✅ ([S182](../sources/README.md#s182)) از 16.3 هر `notFound()` (و هر نشانی ناشناخته‌ای که با مسیر `[...rest]` به `notFound()` می‌رسد) پاسخ ۴۰۴ با یک سند **خالی** `<html id="__next_error__">` می‌دهد: بی `lang`، بی layout، بی متن. صفحه‌ی `not-found.tsx` فقط در داده‌ی RSC است و مرورگر با جاوااسکریپت آن را می‌سازد. علت: مرز ۴۰۴ کامپوننت سمت کاربر است و React مرز خطا را هنگام رندر سرور اجرا نمی‌کند. issue باز است؛ PR #100648 هنوز ادغام نشده (۲۰۲۶-۱۰-۲۷).
- ✅ 🔬 **`loading.tsx` روی مسیر با کنترل دسترسی وضعیت ۴۰۴ را به ۲۰۰ تبدیل می‌کند** (بررسی ۲۰۲۶-۱۰-۳۰، Next.js 16.4.3). طبق [مستندات](https://nextjs.org/docs/app/api-reference/file-conventions/loading) شروع جریان سرصفحه و وضعیت را قفل می‌کند، پس `notFound()`، `forbidden()` یا `unauthorized()` بعد از آن فقط با `noindex` نمایش داده می‌شوند و وضعیت ۲۰۰ می‌ماند. در یک آزمون امنیتی، صفحه‌ی پرونده‌ی کاربر دیگر با `loading.tsx` جواب ۲۰۰ داد و با حذف آن دوباره ۴۰۴ شد (۵۲ از ۵۲ آزمون). روی این مسیرها بررسی دسترسی را پیش از مرز `loading` و `Suspense` انجام بده. محتوای محافظت‌شده نشت نمی‌کند، ولی آزمون‌ها و خزنده‌ها وضعیت غلط می‌بینند.
- 🔬 **تابع از صفحه‌ی سرور به کامپوننت کلاینت (۲۰۲۶-۱۰-۳۱، Next.js 16.4.3):** `tsc` و آزمون واحد پاس می‌شوند، ولی صفحه در اجرا ۵۰۰ می‌دهد (`Functions cannot be passed directly to Client Components`). هفت آزمون وابسته هم با آن افتادند. رشته یا داده بفرست و نشانی‌ها را روی سرور حساب کن. بعد از تغییر صفحه‌های سرور، یک آزمون سریع همه‌ی مسیرها را واقعاً باز کند.
- 🔬 (یک فروشگاه واقعی، 16.4.2) پیامدها: html-validate روی HTML سرور ۴۰۴ خطای `lang` و `close-order` می‌دهد؛ اسکریپت تم در `<head>` layout اجرا نمی‌شود و حالت شب در ۴۰۴ گم می‌شود. یک `app/not-found.tsx` که layout زبان را دور صفحه بپیچد **کمکی نکرد**. کار ما: html-validate ۴۰۴ را کنار بگذار و آزمون جدا بنویس که صفحه‌ی ساخته‌شده در مرورگر را بسنجد (کد ۴۰۴، `lang`/`dir`، سربرگ، تیتر، `noindex`، حالت شب)؛ تم را یک بار هم در `useEffect` یک کامپوننت layout دوباره بگذار. موتور جستجو کد ۴۰۴ و `noindex` را درست می‌گیرد.

## CSP و metadata در Next.js 16

- ✅ **metadata سطحی ادغام می‌شود** ([S184](../sources/README.md#s184)): فیلدی که صفحه نگذارد، از layout بالاتر ارث می‌رسد. پس `alternates` (canonical و hreflang) که در layout زبان بگذاری، روی **همه‌ی** صفحه‌ها همان نشانی را می‌گذارد. canonical و hreflang را در `generateMetadata` هر صفحه بساز؛ `metadataBase` را یک بار در layout ریشه از یک متغیر نشانی عمومی بگذار (نشانی نسبی بدون `metadataBase` خطای build می‌دهد ✅).
- 🔬 (یک فروشگاه دوزبانه، 16.4.2) canonical و hreflang هر صفحه (`en-AE`، `ar-AE`، `x-default`) از `NEXT_PUBLIC_SITE_URL`؛ صفحه‌های خصوصی `noindex`؛ `sitemap.ts` و `robots.ts` پشت یک کلید «سایت زنده است» (پیش از انتشار sitemap خالی و robots همه را می‌بندد). قاعده‌ی کلی hreflang: [سئوی فنی، بخش ۴](../domains/website/09-seo/seo-and-ai-search.md).
- ✅ **nonce فقط با رندر پویا:** nonce در رندر سرور هر درخواست گذاشته می‌شود؛ صفحه‌ی ایستا، ISR و Partial Prerendering (پایه‌ی Cache Components) با CSP مبتنی بر nonce ناسازگارند. بدون nonce، راه رسمی CSP ثابت در `next.config` با `script-src 'self' 'unsafe-inline'` است؛ SRI آزمایشی هم هست ([S184](../sources/README.md#s184)).
- 🔬 دو راه در یک پروژه: فروشگاه با Cache Components ← CSP ثابت در `next.config` با `'unsafe-inline'` و دامنه‌های Stripe.js، به‌اضافه‌ی `nosniff`، `Referrer-Policy`، `Permissions-Policy`، `X-Frame-Options: DENY`، HSTS فقط روی HTTPS واقعی. پنل کاملاً پویا ← nonce تازه برای هر درخواست با `'strict-dynamic'` در `proxy.ts` و بدون `'unsafe-inline'`؛ پاسخ‌های API یک CSP ثابت `default-src 'none'` دارند.
- 🔬 **آزمون درست CSP:** اسکریپت بی‌nonce را **در HTML پاسخ** بگذار (`page.route` + `route.fetch()` + `route.fulfill` با بدنه‌ی دست‌کاری‌شده) و ببین اجرا نمی‌شود. ⚠️ اسکریپتی که با `page.evaluate` به DOM اضافه می‌کنی، زیر `'strict-dynamic'` اجرا **می‌شود** (اسکریپت مطمئن مجاز است اسکریپت تازه بسازد)، پس آزمون غلط سبز یا قرمز می‌دهد.
- 🔬 **ریدایرکت زبان در `proxy.ts`:** `/` به `/en` یا `/ar` با ۳۰۲ (نه ۳۰۸، چون به زبان مرورگر بستگی دارد) و `Vary: Accept-Language, Cookie` تا کش یا CDN یک زبان را برای همه نگه ندارد. نشانی بازگشت درگاه پرداخت از نشانی عمومی سایت ساخته شود، نه از درخواست.

## تله‌های حالت توسعه 🔬

- (۲۰۲۶-۱۰-۲۴، پروژه یک پروژه‌ی واقعی، Next 16.4.2 با Turbopack) بعد از خاموش و روشن شدن رایانه، `next dev` پنل در **حلقه بارگذاری دوباره** افتاد: هر بار صفحه باز می‌شد «Compiled in 2ms» و «[Fast Refresh] rebuilding» و دوباره بارگذاری کامل، حدود هر ۱٫۲ ثانیه؛ هیچ فایلی عوض نشده بود. نشانه در آزمون‌ها: `page.goto ... networkidle` با Timeout در همه صفحه‌های واردشده. راه‌حل: سرور را بستن، پوشه `.next` را کنار گذاشتن، دوباره روشن کردن. برای دیدن علت: `.next/dev/logs/next-development.log` و شمردن ناوبری‌های صفحه با Playwright (`framenavigated`).
- (همان پروژه) `:text-is()` در Playwright کوچک‌ترین عنصری را می‌گیرد که کل متن را دارد؛ اگر کل نام داخل `<mark>` باشد، `a.name:text-is(...)` دیگر پیدا نمی‌شود. به‌جایش `locator('a.name').filter({ hasText: /^...$/ })`.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · [Tailwind CSS](tailwindcss.md) · [Vercel](vercel.md) · [Cloudflare Pages](cloudflare-pages.md) · [S123](../sources/README.md#s123)

🔬 **`cacheLife` کوتاه در layout (۲۰۲۶-۱۰-۳۱، Next.js 16.4.2):** مقدار `stale` زیر ۵ دقیقه در یک تابع awaited داخل layout همه‌ی صفحه‌ها را با خطای `URL data during prerendering ... outside <Suspense>` شکست. `cacheLife('minutes')` کش را در پوسته‌ی برنامه نگه داشت.
