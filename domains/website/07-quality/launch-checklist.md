# چک‌لیست کیفیت قبل از انتشار

> **نوع سند:** دستورالعمل
> **هدف این سند:** آخرین بررسی‌ها قبل از اینکه سایت منتشر شود: طراحی، سرعت، دسترسی‌پذیری، سئو، امنیت و حقوق محتوا.
> **موضوع تحقیق:** استانداردهای رسمی سرعت (Core Web Vitals) و دسترسی‌پذیری (WCAG).
> **منابع:** [S12 WCAG 2.2](../../../sources/README.md#s12) · [S13 Core Web Vitals](../../../sources/README.md#s13) · [S18 Vibe Coding](../../../sources/README.md#s18) · [S21 Chrome DevTools MCP](../../../sources/README.md#s21) · [S53 Cloudflare](../../../sources/README.md#s53) · [S59 Caddy و Next.js](../../../sources/README.md#s59) · [S62 DNS، ایمیل و سئو](../../../sources/README.md#s62)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۷
> **دفعه‌ی بعد چک شود:** آستانه‌های Core Web Vitals (گوگل گاهی معیارها را عوض می‌کند، مثل جایگزینی FID با INP)؛ نسخه‌ی جدید WCAG.

---

## طراحی
- [ ] در عرض‌های ۳۹۰، ۷۶۸، ۱۴۴۰ و ۱۹۲۰ پیکسل بررسی شده
- [ ] حداکثر دو فونت، اندازه‌ها یکدست
- [ ] فاصله‌گذاری بر اساس یک مقیاس ثابت (مثلاً ۸، ۱۶، ۲۴، ۳۲، ۴۸، ۶۴، ۹۶) 🧭
- [ ] کنتراست متن کافی: ۴.۵ به ۱ برای متن معمولی، ۳ به ۱ برای متن بزرگ ✅ ([رنگ](../02-design/color-and-texture.md#کنتراست))

## سرعت
- [ ] ✅ **Core Web Vitals** در محدوده‌ی «خوب» ([S13](../../../sources/README.md#s13)):
  - **LCP** (زمان نمایش بزرگ‌ترین بخش): حداکثر **۲.۵ ثانیه**
  - **INP** (سرعت واکنش به کلیک): حداکثر **۲۰۰ میلی‌ثانیه**
  - **CLS** (پرش چیدمان): حداکثر **۰.۱**
- [ ] امتیاز Lighthouse عملکرد ۹۰ یا بالاتر (محدوده‌ی سبز) ✅؛ برای صفحه‌های سه‌بعدی سنگین، ۷۰ به بالا هدف واقع‌بینانه است 🧭
- [ ] تصاویر فشرده و تنبل‌بار، به‌جز عکس هیرو ([رسانه](../05-media/media-guidelines.md))
- [ ] تصویر هیرو (بزرگ‌ترین بخش صفحه) با `<link rel="preload" as="image" imagesrcset=… imagesizes=… fetchpriority="high">` در head؛ اسکریپت‌های head با `defer`؛ فقط همان یک تصویر `fetchpriority="high"` داشته باشد (نه لوگو). 🔬 در یک سایت مشتری LCP موبایل خانه از ۳.۲ به حدود ۱.۹ ثانیه رسید و «تأخیر شروع دانلود» از ۱.۲ ثانیه به صفر. ⚠️ این بهبود روی سرور محلی دیده نمی‌شود (تأخیر شبکه‌ی واقعی ندارد)؛ روی سایت زنده اندازه بگیر
- [ ] فونت‌ها با `font-display: swap`
- [ ] افکت سنگین در موبایل سبک‌تر یا جایگزین شده

## دسترسی‌پذیری
- [ ] همه‌ی تصاویر متن جایگزین (alt) دارند
- [ ] با کیبورد قابل پیمایش است
- [ ] `prefers-reduced-motion` رعایت شده (و اسکرول نرم در آن حالت خاموش است)

## سئو و محتوا
- [ ] عنوان و توضیح هر صفحه، تصویر اشتراک‌گذاری (Open Graph)
- [ ] یک تیتر H1 در هر صفحه
- [ ] robots.txt، sitemap با lastmod واقعی، داده‌ی ساختاریافته، Search Console، Bing و IndexNow: [سئوی فنی](../09-seo/seo-and-ai-search.md)
- [ ] برای کسب‌وکار محلی: [Google Business Profile](../09-seo/local-business-profile.md) با تابلو و ویدیوی تأیید
- [ ] متن‌ها، تصاویر، صداها و فونت‌ها مال خودمان یا با مجوز روشن هستند؛ صفحه‌ی «اعتبار» برای فایل‌های CC BY

## امنیت
- [ ] چک‌لیست امنیت در [Vibe Coding](../01-method/vibe-coding.md#امنیت)
- [ ] ✅ **DNSSEC** روشن و رکورد DS در ثبت‌کننده‌ی دامنه ([روش در Cloudflare](../04-tech/cloudflare-full-stack.md))
- [ ] ✅ **CAA**: فقط مرجع صدور گواهی خودمان، wildcard بسته ([دامنه و ایمیل](../04-tech/domain-and-email.md))
- [ ] ✅ HSTS بدون `preload` تا وقتی همه‌ی زیردامنه‌ها برای همیشه HTTPS دارند ([سرور خودمان](../04-tech/self-hosted-server.md))
- [ ] روی سرور خودمان: robots.txt `Disallow: /` نسخه‌ی آزمایشی برداشته شد و `noindex` فقط روی بخش‌های خصوصی مانده ([سئوی فنی](../09-seo/seo-and-ai-search.md))

## آزمون بار (سرور خودمان) 🔬
- [ ] صفحه‌ی اصلی و پرکارترین صفحه را با چند کاربر هم‌زمان بسنج و عدد درخواست در ثانیه و خطا را ثبت کن؛ بعد از هر بهبود دوباره
- نمونه از MARIO E.G.S.H (دفتر پروژه‌ها): روی **کپی داده و کامپیوتر دفتر**، نه سرور واقعی: صفحه‌ی اصلی با ۱۰ کاربر هم‌زمان از ۱۷ به ۳۱ درخواست در ثانیه رسید و با ۵۰ کاربر خطای صفر؛ صفحه‌ی فهرست خدمات با کم کردن HTML از ۱.۴۳ به ۰.۶ مگابایت (هر کارت دو بار فرستاده می‌شد) از ۱۰ به ۱۸.۶ درخواست در ثانیه. ❓ ابزار و مدت آزمون ثبت نشده؛ دفعه‌ی بعد با ابزار و مدت ثابت تکرار کن تا مقایسه‌پذیر باشد

```text
Run a pre-launch review: Core Web Vitals and Lighthouse scores for mobile and desktop,
check every image has alt text and is compressed, test keyboard navigation, test
prefers-reduced-motion, check layouts at 390/768/1440/1920px, scan for exposed secrets,
and confirm every third-party asset has a license we can use. Report problems ranked
by impact, then fix them one by one.
```

## بررسی خودکار دائمی

برای اینکه این چک‌لیست با هر تغییر خودکار اجرا شود (Playwright، axe، Lighthouse CI، html-validate) و Claude تا قبولی کار کند: [بررسی خودکار](../../claude-code/verification.md).

## تست خودکار با Chrome DevTools MCP

✅ [Chrome DevTools MCP](../../../catalog/chrome-devtools-mcp.md) به Claude اجازه می‌دهد سایت را در Chrome واقعی باز کند، عملکرد را ثبت و تحلیل کند، ممیزی Lighthouse بگیرد و کنسول و شبکه را بخواند. با `--isolated` و آمار خاموش اجرا کن ([امنیت MCP](../../claude-code/mcp-safety.md)).

```text
Using Chrome DevTools MCP in an isolated browser, open [local URL]. Record a performance
trace on mobile emulation and report LCP, INP and CLS against the "good" thresholds. Run
a Lighthouse audit for accessibility, SEO and best practices. List console errors and
failed network requests. Take screenshots at 390px and 1440px. Rank problems by impact
and wait before fixing.
```

برای تست جریان فرم در چند مرورگر: [Playwright MCP](../../../catalog/playwright-mcp.md).

