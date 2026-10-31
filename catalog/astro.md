---
name: Astro
slug: astro
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: فریم‌ورک سایت محتوایی با خروجی HTML و جزیره‌های تعاملی؛ مسیریابی چندزبانه‌ی داخلی؛ از ۲۰۲۶ متعلق به Cloudflare
use_when: "building a content-heavy or multilingual marketing website ; need mostly static HTML with a few interactive islands"
how: "npm create astro@latest (v7.x, Node 22.22+ required, MIT); after upgrading to v7 check build errors for unclosed tags and visually verify Persian/Arabic spacing because compressHTML now defaults to jsx"
url: https://astro.build
repo: "https://github.com/withastro/astro"
license: "MIT"
pricing: free
risk: low
sources: [S123]
found_in: [gap-playbooks]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Astro

## چیست
✅ فریم‌ورک سایت محتوایی: صفحه‌ها پیش‌فرض HTML ایستا می‌شوند و فقط بخش‌های تعاملی («جزیره‌ها») JavaScript می‌گیرند؛ کامپوننت React، Vue، Svelte و… را هم می‌پذیرد. حدود ۶۳ هزار ستاره، فعال.
✅ نسخه‌ی پایدار (npm): **7.4.4** (۲۰۲۶-۱۰-۲۸؛ قبلی 7.4.2 در ۲۰۲۶-۱۰-۲۱). نسخه‌ی ۷٫۰٫۰ در ۲۰۲۶-۰۶-۲۲ آمد. Node حداقل 22.22.0 (فیلد `engines` در npm).
✅ مالکیت (https://astro.build/blog/joining-cloudflare/، ۲۰۲۶-۰۱-۱۶): شرکت The Astro Technology Company به Cloudflare پیوست و کارمندانش کارمند Cloudflare شدند. طبق همان پست Astro متن‌باز و MIT می‌ماند، برای همه‌ی میزبان‌ها کار می‌کند و حکمرانی باز و نقشه‌ی راه جامعه‌محور حفظ می‌شود. 🧭 این وعده است؛ هر سه ماه ببین آداپتورهای غیر Cloudflare عقب نمانند.

✅ تغییرهای شکننده‌ی نسخه‌ی ۷ (https://docs.astro.build/en/guides/upgrade-to/v7/):
- Vite 8 به جای Vite 7.
- کامپایلر تازه با Rust، سخت‌گیرتر: تگ بسته‌نشده خطای build می‌دهد و تودرتویی نادرست HTML دیگر خودکار درست نمی‌شود.
- پردازشگر Markdown پیش‌فرض عوض شد؛ افزونه‌های remark و rehype باید با `unified()` وصل شوند.
- پیش‌فرض `compressHTML` از `true` به `'jsx'` رفت و ممکن است فاصله‌ی بین عنصرهای درون‌خطی حذف شود. 🧭 در متن فارسی و عربی این را حتماً با چشم چک کن.
- `@astrojs/db` حذف شد.

## کی استفاده کنیم
🧭 سایت شرکتی، لندینگ و وبلاگ چندزبانه که کمی تعامل React لازم دارد (فرم پیچیده، پیکربندی‌کننده‌ی کالا، نقشه). کنار [Eleventy](eleventy.md) گزینه‌ی اول ما برای سایت کسب‌وکار. ❓ هنوز در پروژه‌ی خودمان آزموده نشده.

✅ چندزبانه (https://docs.astro.build/en/guides/internationalization/): مسیریابی زبان داخلی است. در `astro.config` کلید `i18n` با `locales`، `defaultLocale`، `routing.prefixDefaultLocale`، `fallback` و `domains`؛ کمکی‌ها در `astro:i18n` مثل `getRelativeLocaleUrl()` و `Astro.currentLocale`. مسیریابی پایه روی سایت ایستا هم کار می‌کند؛ ولی `domains` و مسیر سفارشی زبان رندر سرور و آداپتور لازم دارند. ❓ سند رسمی درباره‌ی `dir="rtl"` چیزی نمی‌گوید؛ در layout از روی `Astro.currentLocale` خودت `dir` را بگذار ([فارسی و RTL](../domains/website/02-design/persian-rtl.md)).

## میزبانی
✅ سایت ایستا آداپتور لازم ندارد و روی هر میزبان ایستا (Cloudflare Pages، Netlify، سرور خودمان) می‌نشیند (https://docs.astro.build/en/guides/integrations-guide/cloudflare/).
✅ رندر سرور روی Cloudflare با `@astrojs/cloudflare` (14.4.1) **فقط روی Workers**؛ طبق سند از نسخه‌ی ۱۳ آداپتور دیگر Pages را پشتیبانی نمی‌کند. محدودیت: CommonJS در workerd کار نمی‌کند؛ API های Node پرچم `nodejs_compat` لازم دارند.
🧭 Vercel هم آداپتور رسمی دارد؛ قاعده‌ی «Hobby فقط غیرتجاری» همان است ([کارت Vercel](vercel.md)).

## قیمت و مجوز
✅ رایگان، MIT. فایل LICENSE علاوه بر MIT خود Astro، متن MIT بخش‌هایی را که از SvelteKit و Vite آمده‌اند هم دارد (برای همین GitHub آن را «NOASSERTION» نشان می‌دهد). استفاده‌ی تجاری آزاد است.

## ریسک و هشدار
کم برای سایت ایستا. ✅ هشدارهای امنیتی ۱۲ ماه گذشته (https://github.com/withastro/astro/security/advisories) بیشتر در رندر سرور و آداپتورها هستند. مهم‌ترین‌ها:
- ۲۰۲۵-۱۱-۱۹ · GHSA-ggxq-hp9w-j794 (CVE-2025-64765) متوسط: دور زدن چک احراز هویت middleware با نشانی کدشده؛ رفع 5.15.8 (و GHSA-whqg-ppgf-wp8c دور زدن همین).
- ۲۰۲۶-۰۶-۱۲ · GHSA-2pvr-wf23-7pc7 بالا: SSRF با هدر Host؛ رفع 6.4.6. ۲۰۲۶-۰۷-۰۱ · GHSA-vj59-8hwv-xxmv بالا: دور زدن مجوز؛ رفع 6.4.8.
- ۲۰۲۶-۰۸-۲۷ · GHSA-26w7-cxv4-gfx2 **بحرانی**: اجرای کد از راه دور با بهینه‌سازی تصویر AVIF؛ رفع **7.2.8**. GHSA-376h-93r7-7g6f متوسط: دور زدن مجوز با `base`؛ رفع 7.2.4.
- ۲۰۲۶-۱۰-۱۲ · GHSA-98hj-9722-w3j8 متوسط: XSS در JSX و MDX؛ رفع 7.3.2. GHSA-mpr7-6m5w-76rw کم: تزریق CSS در View Transitions؛ رفع 7.3.3. GHSA-m8p5-r7qv-cx4c متوسط: SSRF در `/_image` آداپتور Node؛ رفع `@astrojs/node` 11.1.7.

🧭 قاعده‌ی ما: حداقل 7.3.3 (الان 7.4.4) و آداپتور به‌روز.

🔬 **استایل scoped و لایه‌ی تم سراسری:** Astro به قاعده‌های CSS هر کامپوننت یک انتخاب‌گر ویژگی (`[data-astro-cid-…]`) اضافه می‌کند و اولویتشان بالا می‌رود؛ لایه‌ی تم سراسری (مثلاً کلاسی روی `html` که همه‌ی سطح‌ها را شیشه‌ای می‌کند) بدون پیشوند قوی‌تر (مثل `html.theme .card`) می‌بازد. راه دیگر ✅: گزینه‌ی `scopedStyleStrategy: 'where'` در تنظیمات Astro که همین انتخاب‌گر را داخل `:where()` می‌گذارد و اولویت اضافه نمی‌دهد (https://docs.astro.build/en/reference/configuration-reference/#scopedstylestrategy). (آزموده در یک پروژه‌ی سایت، ۲۰۲۶-۱۰-۲۶)

✅ تله‌متری (https://astro.build/telemetry/): داده‌ی ناشناس (دستور، نسخه، سیستم، عامل هوش مصنوعی‌ای که CLI را صدا زده، integration ها، خطای پاک‌شده). خاموش کردن: `npx astro telemetry disable` (برای کل دستگاه) یا `ASTRO_TELEMETRY_DISABLED=1`.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [Eleventy](eleventy.md) · [Vite](vite.md) · [Tailwind CSS](tailwindcss.md) · [Cloudflare Pages](cloudflare-pages.md) · [S123](../sources/README.md#s123)
