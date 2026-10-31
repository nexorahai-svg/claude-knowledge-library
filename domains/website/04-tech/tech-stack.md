# تکنولوژی پیشنهادی

> **نوع سند:** مرجع
> **هدف این سند:** انتخاب فریم‌ورک، کتابخانه و میزبانی برای هر نوع پروژه، با مجوز هر کدام.
> **موضوع تحقیق:** ابزارهای استاندارد ساخت وبسایت در سال جاری و شرایط مجوزشان.
> **منابع:** [S04 GSAP](../../../sources/README.md#s04) · [S05 shadcn/ui](../../../sources/README.md#s05) · [S06 21st.dev](../../../sources/README.md#s06) · [S11 Three.js](../../../sources/README.md#s11) · [S15 Modulify و Wedoflow](../../../sources/README.md#s15) · [S19 Supabase](../../../sources/README.md#s19) · [S20 Vercel و جایگزین‌ها](../../../sources/README.md#s20) · [S23 Cloudflare Tunnel](../../../sources/README.md#s23) · [S53 Cloudflare](../../../sources/README.md#s53) · [S55 Eleventy](../../../sources/README.md#s55) · [S59 Caddy و Next.js روی سرور خودمان](../../../sources/README.md#s59) · [S123 Next.js، Astro، Vite، Tailwind](../../../sources/README.md#s123)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۸ (نسخه‌ها از npm: Next.js 16.4.3، Astro 7.4.2، Tailwind 4.3.3، Vite 8.3.5، SvelteKit 3.1.0، Nuxt 4.6.3؛ next-auth v5 هنوز بتا؛ WCAG 3.0 هنوز Working Draft)
> **دفعه‌ی بعد چک شود:** نسخه‌های اصلی جدید Next.js، Astro، Tailwind؛ پشتیبانی SRI در Next.js (هنوز آزمایشی)؛ تغییر قوانین 21st.dev؛ تغییر طرح رایگان میزبان‌ها.

---

## جدول انتخاب

| نوع پروژه | تکنولوژی | چرا |
|---|---|---|
| لندینگ ساده و سریع | HTML + CSS + JS ساده، یا Astro | بدون پیچیدگی، خیلی سریع |
| سایت شرکتی کامل | [Next.js](../../../catalog/nextjs.md) ✅ یا [Astro](../../../catalog/astro.md) ✅ + [Tailwind](../../../catalog/tailwindcss.md) ✅ | چندصفحه‌ای، سئو خوب (پایین: [انتخاب فریم‌ورک](#انتخاب-فریمورک-بر-اساس-نوع-پروژه)) |
| سایت شرکتی محتوایی، چندزبانه | [Eleventy](../../../catalog/eleventy.md) + CSS ساده | 🔬 یک پروژه‌ی واقعی: SEO ۱۰۰، PageSpeed ۹۶ تا ۹۸، بدون فریم‌ورک سمت مرورگر |
| کامپوننت‌های آماده ([راهنمای کامل](component-libraries.md)) | **shadcn/ui**، **Magic UI**، **Motion Primitives** و **21st.dev** | shadcn/ui متن‌باز (MIT) ✅. در 21st.dev هر کامپوننت مجوز خودش را دارد (پایین) |
| صحنه‌ی سه‌بعدی | Three.js (یا React Three Fiber در React) | استاندارد صنعت، MIT ✅ |
| انیمیشن | GSAP + ScrollTrigger + Lenis | قوی‌ترین ترکیب، همه رایگان ✅ ([حرکت](../03-motion-3d/motion-animation.md)) |
| میزبانی | Vercel، Cloudflare Pages، Netlify | پایین را ببین: طرح رایگان Vercel برای سایت شرکت مجاز نیست ⚠️ |
| سایت تجاری کامل بدون هزینه (فرم، پایگاه داده، پنل مدیریت) | Cloudflare Pages + Functions + D1 + R2 + Turnstile + Access | ✅ 🔬 [راهنمای کامل](cloudflare-full-stack.md) |
| ایمیل شرکتی و ارسال فرم | Zoho Mail رایگان + SPF/DKIM/DMARC | ✅ 🔬 [دامنه و ایمیل](domain-and-email.md) |
| پایگاه داده و فرم | Supabase (فقط اگر داده‌ی ماندگار لازم است) | [کارت Supabase](../../../catalog/supabase.md) |
| داده‌ی حساس، هوش مصنوعی محلی، کار پس‌زمینه | Next.js روی سرور لینوکسی خودمان، پشت [Caddy](../../../catalog/caddy.md) | 🔬 آزموده در Docker، نه روی دامنه‌ی زنده: [سرور خودمان](self-hosted-server.md) |

## انتخاب فریم‌ورک بر اساس نوع پروژه

✅ ([S123](../../../sources/README.md#s123)) هر چهار فریم‌ورک MIT و رایگان‌اند. جزئیات، نسخه و هشدارهای امنیتی در کارت هر کدام.

| نوع پروژه | انتخاب | چرا |
|---|---|---|
| سایت کسب‌وکار، فقط محتوا | [Eleventy](../../../catalog/eleventy.md) ✅ یا [Astro](../../../catalog/astro.md) ✅ | 🔬 Eleventy در یک پروژه‌ی واقعی آزموده شد. ✅ Astro مسیریابی چندزبانه‌ی داخلی دارد و برای بخش تعاملی کامپوننت React می‌پذیرد. هر دو خروجی ایستا روی Cloudflare Pages رایگان |
| سایت کسب‌وکار با چند بخش تعاملی | [Astro](../../../catalog/astro.md) ✅ + [Tailwind CSS](../../../catalog/tailwindcss.md) ✅ | ✅ فقط جزیره‌های تعاملی JavaScript می‌گیرند؛ کلاس‌های منطقی Tailwind برای RTL |
| فروشگاه آنلاین | [Next.js](../../../catalog/nextjs.md) ✅ + [Tailwind CSS](../../../catalog/tailwindcss.md) ✅، یا [Astro](../../../catalog/astro.md) ✅ اگر بیشتر کاتالوگ است | 🧭 سبد، حساب کاربری و webhook پرداخت سرور لازم دارند. ❓ موتور فروشگاه هنوز انتخاب نشده ([راهنمای فروشگاه](../../../playbooks/online-store.md)) |
| داشبورد و نرم‌افزار وب، داده‌ی حساس | [Next.js](../../../catalog/nextjs.md) ✅ + [Tailwind CSS](../../../catalog/tailwindcss.md) ✅ + shadcn/ui | 🔬 یک فروشگاه واقعی و پنل معامله‌گر کریپتو؛ روی سرور خودمان پشت Caddy. ⚠️ حداقل 16.4.1؛ هشدارهای امنیتی زیاد |
| داشبورد تک‌منظوره‌ی متحرک | [Vite](../../../catalog/vite.md) ✅ با TypeScript ساده | ✅ بدون فریم‌ورک؛ خروجی ایستا |

✅ نکته‌های میزبانی:
- Next.js روی Cloudflare: یا خروجی ایستا (`output: 'export'`، بدون `proxy`، Server Actions و ISR) روی Pages، یا vinext روی Workers که خود Cloudflare می‌گوید «در بتا است». ❓ OpenNext «Node Middleware» را پشتیبانی نمی‌کند، پس `proxy.ts` احتمالاً کار نمی‌کند ([کارت Next.js](../../../catalog/nextjs.md)).
- آداپتور سرور Astro برای Cloudflare فقط Workers است؛ سایت ایستای Astro آداپتور لازم ندارد.
- تله‌متری: `NEXT_TELEMETRY_DISABLED=1` و `ASTRO_TELEMETRY_DISABLED=1` را در CI بگذار.

## میزبانی: کدام را انتخاب کنیم؟

| موقعیت | پیشنهاد | دلیل |
|---|---|---|
| دموی شخصی بدون درآمد | Vercel رایگان (Hobby) | ✅ مجاز برای استفاده‌ی شخصی؛ بهترین تجربه‌ی کار |
| **سایت شرکت یا سایت مشتری** | **Vercel Pro (۲۰ دلار در ماه برای هر توسعه‌دهنده)** | ✅ طرح رایگان Vercel «فقط شخصی و غیرتجاری» است؛ حتی اگر فقط برنامه‌نویس پول گرفته باشد، تجاری حساب می‌شود |
| سایت شرکت، بدون هزینه | **Cloudflare Pages رایگان** | ✅ قرارداد بندی علیه استفاده‌ی تجاری ندارد؛ فقط دریافت کارت بانکی در سایت رایگان ممنوع است ([راهنما](cloudflare-full-stack.md)). 🔬 یک پروژه‌ی واقعی |
| کسب‌وکار | GitHub Pages **نه** | ✅ طبق قوانین گیت‌هاب برای کسب‌وکار آنلاین و سایت‌های تجاری مجاز نیست |

جزئیات و عددها: [کارت Vercel](../../../catalog/vercel.md).

## داده و فرم

🧭 بیشتر سایت‌های معرفی پایگاه داده لازم ندارند. اگر فرم تماس فقط باید ایمیل بفرستد، سرویس فرم ساده کافی است. وقتی پیام‌ها باید ذخیره شوند یا ورود کاربر لازم است، [Supabase](../../../catalog/supabase.md):
- ✅ طرح رایگان بعد از **یک هفته بی‌فعالیتی متوقف می‌شود** → برای سایت مشتری Pro (از ۲۵ دلار)
- ✅ منطقه‌ی خاورمیانه ندارد (نزدیک‌ترین: بمبئی یا فرانکفورت)
- ✅ RLS حتماً روشن، با سیاست «فقط درج» برای بازدیدکننده؛ کلید service_role هرگز در مرورگر

```text
Add a contact form that stores submissions in Supabase. Use only the publishable key in
the browser. Enable Row Level Security on the table with a single policy that lets anon
insert and nothing else (no select, update or delete). Keep any secret key server-side.
Show me the SQL for the table and policy before applying it.
```

## سیاست امنیت محتوا (CSP) در Next.js: nonce یا ثابت؟

✅ ([S59](../../../sources/README.md#s59)، راهنمای رسمی CSP در Next.js) از Next.js 16 فایل میانی `proxy.ts` نام دارد (قبلاً `middleware.ts`). در آن برای هر درخواست یک nonce تازه ساخته می‌شود و در هدر `Content-Security-Policy` با `'strict-dynamic'` می‌نشیند؛ Next.js nonce را خودکار روی اسکریپت‌های خودش می‌گذارد.

⚠️ ✅ هزینه‌اش: با nonce **همه‌ی صفحه‌ها باید پویا رندر شوند**. یعنی ساخت ایستا و ISR خاموش می‌شود، CDN بدون تنظیم اضافه صفحه را کش نمی‌کند، Partial Prerendering با آن سازگار نیست، و بار سرور و زمان اولین بارگذاری بیشتر می‌شود.

| روش | کی |
|---|---|
| nonce در `proxy.ts` با `'strict-dynamic'` | ✅ داده‌ی حساس، بدون `'unsafe-inline'` برای اسکریپت. 🔬 یک فروشگاه واقعی: پنل، پرونده‌ی مشتری و مدرک (دفتر پروژه‌ها) |
| CSP ثابت در `headers()` فایل `next.config` | ✅ سایت معرفی ایستا که روی CDN کش می‌شود؛ ولی برای اسکریپت `'unsafe-inline'` لازم دارد |
| SRI (هش در زمان build) | ✅ ساخت ایستا می‌ماند، ولی هنوز **آزمایشی** و فقط App Router است. ❓ در پروژه آزموده نشده |

🔬 در یک فروشگاه واقعی جواب‌های API همان CSP ثابت را نگه داشتند و فقط صفحه‌ها nonce گرفتند. 🧭 برای اسکریپت پرداخت بیرونی، نشانی‌اش را هم در `script-src` بگذار (برای مرورگری که `'strict-dynamic'` نمی‌شناسد).

## پیش‌نمایش برای مشتری

✅ [Cloudflare Quick Tunnel](../../../catalog/cloudflare-tunnel.md): یک دستور، بدون حساب، آدرس موقت. با `--allowed-mail` فقط ایمیل مشتری وارد می‌شود. فقط در زمان جلسه روشن بماند.

```bash
cloudflared tunnel --url http://localhost:3000 --allowed-mail client@example.com
```

برای پیش‌نمایش ماندگار: لینک پیش‌نمایش Vercel.

## سازنده‌های بدون کد (برای مقایسه)

✅ ([S15](../../../sources/README.md#s15)) **Modulify** یک سازنده‌ی سایت با هوش مصنوعی است و قالب‌های قابل‌کپی در دسته‌های مختلف (از جمله معماری) دارد. **Wedoflow** بیش از ۲۱۰ قالب پولی Webflow دارد (هر قالب ۲۹ تا ۱۶۹ دلار). این‌ها راه سریع‌اند، ولی کنترل و مالکیت کد کمتری نسبت به ساختن با Claude در فایل‌های خودمان می‌دهند. 🧭 برای ما مرجع الهام‌اند، نه مسیر اصلی.

## Tailwind 4: CSS خودت کلاس‌های Tailwind را می‌بَرد 🔬

✅ Tailwind 4 کلاس‌هایش را در `@layer utilities` می‌گذارد، و طبق قاعده‌ی لایه‌های CSS (MDN، Cascade layers) هر قاعده‌ی **بیرون از لایه** بر قاعده‌ی داخل لایه پیروز است، هر قدر هم ساده باشد.
🔬 در پنل معامله‌گر کریپتو (۲۰۲۶-۱۰-۱۹) دو بار دیده شد:
- `input { width: 100% }` در `globals.css` کلاس‌های `w-20` و `w-16` را بی‌اثر کرد. دو فیلد ساعت هر کدام کل خانه‌ی جدول را گرفتند و روی فیلد کناری افتادند. axe آن را با خطای target-size گرفت.
- `.dock { display: flex }` کلاس `md:hidden` را بی‌اثر کرد و منوی گوشی روی صفحه‌ی بزرگ هم دیده شد.

راه: قاعده‌های پایه‌ی خودت را در `@layer base` یا `@layer components` بنویس، یا نمایش را با media query در خود CSS کنترل کن، یا موقتاً `!w-20`.

## قبل از استفاده از کامپوننت 21st.dev

✅ ([S06](../../../sources/README.md#s06)) 21st.dev یک بازارچه است و هر کامپوننت را یک طراح جدا منتشر کرده:
- مجوز همان کامپوننت را در صفحه‌اش چک کن
- طبق قوانین سایت، اگر کامپوننتی را جای دیگری **بازنشر** کنی باید لینک واضح به صفحه‌ی اصلی‌اش بدهی
- مجوز MIT اجازه‌ی استفاده می‌دهد، نه اینکه کار دیگری را به اسم خودت منتشر کنی
- استفاده در سایت خودت با رعایت مجوز مشکلی ندارد

## دو دام Astro و CSS 🔬 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۲)
- ✅ استایل یک کامپوننت Astro scoped است (به عنصرها صفت `data-astro-cid` می‌دهد)؛ عنصری که بعداً با `innerHTML` در اسکریپت ساخته می‌شود آن صفت را ندارد و بی‌استایل می‌ماند (https://docs.astro.build/en/guides/styling/#scoped-styles). برای عنصرهای پویا `<style is:global>` با نام کلاس یکتا.
- ✅ صفت `hidden` فقط `display:none` مرورگر است؛ هر قاعده‌ی `display` نویسنده (مثل `display:flex`) آن را می‌پوشاند. برای هر جزء پنهان‌شدنی `[hidden]{display:none!important}` بگذار؛ آزمون عکس ما دکمه‌ای را که باید پنهان می‌بود نشان داد.
