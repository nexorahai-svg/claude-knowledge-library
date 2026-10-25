# راهنمای پروژه: سایت کسب‌وکار

> **نوع سند:** راهنمای قدم‌به‌قدم
> **هدف این سند:** Claude در یک پروژه‌ی سایت معرفی شرکت، برند یا لندینگ‌پیج (چندزبانه، فرم تماس، سئو، سئوی محلی، میزبانی) از اولین پیام تا تحویل و نگهداری، قدم‌به‌قدم بداند چه بپرسد، چه بسازد، با کدام ابزار، و هر مرحله کی «تمام» است.
> **موضوع تحقیق:** جمع‌بندی سندها و کارت‌های کتابخانه و تجربه‌ی پروژه‌های واقعی برای این نوع پروژه (این راهنما ادعای تازه نمی‌سازد؛ هر واقعیت به سند منبعش لینک دارد).
> **منابع:** سندهای لینک‌شده در متن · دفتر پروژه‌ها
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۳
> **دفعه‌ی بعد چک شود:** وقتی حکم یکی از کارت‌های جدول پشته عوض شد (lint آن را می‌گیرد) یا پروژه‌ی تازه‌ای از این نوع تمام شد.

---

## این راهنما برای کدام پروژه است

- سایت معرفی یک شرکت یا برند، چندصفحه‌ای یا یک لندینگ‌پیج.
- بیشتر محتواست: خدمات، نمونه‌کار، تماس. کاربر وارد حساب نمی‌شود.
- یک یا چند زبان، اغلب انگلیسی و عربی و گاهی فارسی (راست‌به‌چپ).
- فرم تماس یا استعلام، ایمیل شرکتی، سئو و دیده شدن در Google Maps.
- نمونه‌های واقعی: یک سایت مشتری، Sun Shade DXB، بخش عمومی MARIO E.G.S.H (دفتر پروژه‌ها).

اگر سبد خرید و پرداخت دارد: [فروشگاه آنلاین](online-store.md). اگر ورود کاربر و پنل داده دارد: [داشبورد و نرم‌افزار وب](web-app-dashboard.md). بقیه: [فهرست راهنماها](README.md).

## پیش از شروع: پرسش‌ها از کاربر

1. **کدام زبان‌ها؟** اگر فقط فارسی ← قاعده‌های [سایت فارسی و RTL](../domains/website/02-design/persian-rtl.md). اگر چند زبان (انگلیسی، عربی، فارسی) ← علاوه بر آن، hreflang دوطرفه با `x-default` ([سئوی فنی، بخش ۴](../domains/website/09-seo/seo-and-ai-search.md)) و رقم صریح در `Intl` برای هر زبان. پیش‌فرض: انگلیسی و عربی، مثل یک سایت مشتری و Sun Shade.
2. **فقط محتوا، یا داده‌ی حساس و پنل سنگین هم دارد؟** اگر فقط محتوا ← Eleventy روی Cloudflare Pages. اگر تعامل سنگین React لازم است ← Next.js یا Astro با Tailwind ([تکنولوژی](../domains/website/04-tech/tech-stack.md)). اگر داده‌ی حساس یا هوش مصنوعی محلی ← [داشبورد و نرم‌افزار وب](web-app-dashboard.md). پیش‌فرض: Eleventy.
3. **میزبانی را چه کسی می‌پردازد؟** اگر بودجه‌ی ماهانه نیست ← Cloudflare Pages رایگان، با حساب به نام خود مشتری ([Cloudflare، «آیا مجاز است»](../domains/website/04-tech/cloudflare-full-stack.md)). اگر مشتری Vercel می‌خواهد ← فقط طرح Pro، چون طرح رایگان غیرتجاری است. GitHub Pages برای کسب‌وکار نه. پیش‌فرض: Cloudflare Pages.
4. **پیام فرم فقط ایمیل شود، یا ذخیره هم شود؟** اگر فقط اعلان ← EmailJS با `blockHeadless` و `limitRate`. اگر باید بماند ← Functions + D1 + Turnstile و ایمیل فقط اعلان ([دامنه و ایمیل، بخش ۴](../domains/website/04-tech/domain-and-email.md)). پیش‌فرض: ذخیره در D1 و اعلان، مثل یک سایت مشتری.
5. **مشتری به محل می‌آید و تابلوی دائمی با نام دقیق دارد؟** اگر بله ← Business Profile با ویدیوی تأیید. اگر کار در محل مشتری است ← کسب‌وکار خدماتی با آدرس پنهان. اگر کسب‌وکار دیگری در همان ساختمان است ← پروفایل جدا، به پروفایل دیگری دست نزن ([سئوی محلی](../domains/website/09-seo/local-business-profile.md)). پیش‌فرض: پیش از ضبط ویدیو تابلو را با عکس تأیید کن.
6. **سایت قبلی یا لوگو دارد؟** اگر سایت قبلی هست ← اول آرشیو صفحه‌ها و نقشه‌ی تغییر مسیر ۳۰۱. اگر لوگو ندارد یا مشتری راضی نیست ← اول [برند و لوگو](brand-identity.md). پیش‌فرض: لوگوی فعلی می‌ماند.

## پشته‌ی پیش‌فرض

| نیاز | انتخاب پیش‌فرض | کی چیز دیگر | جزئیات |
|---|---|---|---|
| سازنده‌ی سایت | [Eleventy](../catalog/eleventy.md) ✅ | تعامل سنگین یا چند زبان با مسیر جدا ← [Astro](../catalog/astro.md) ✅ یا [Next.js](../catalog/nextjs.md) ✅، با [Tailwind](../catalog/tailwindcss.md) ✅ (کلاس‌های منطقی `ms-*` و `me-*` برای RTL) | [تکنولوژی](../domains/website/04-tech/tech-stack.md) |
| میزبانی | [Cloudflare Pages](../catalog/cloudflare-pages.md) ✅ | مشتری پول می‌دهد ← [Vercel](../catalog/vercel.md) ✅ فقط Pro؛ داده‌ی حساس ← [Caddy](../catalog/caddy.md) ✅ روی سرور خودمان | [Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md) |
| ضد ربات فرم | [Cloudflare Turnstile](../catalog/cloudflare-turnstile.md) ✅ | — | [Cloudflare، مرحله‌ی ۵](../domains/website/04-tech/cloudflare-full-stack.md) |
| اعلان ایمیلی فرم | Function سرور | سایت بدون سرور ← [EmailJS](../catalog/emailjs.md) 🧪 | [دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md) |
| ایمیل شرکتی | [Zoho Mail](../catalog/zoho-mail.md) ✅ رایگان | Outlook یا IMAP لازم است ← طرح پولی | [دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md) |
| پنل مدیریت | [Cloudflare Access](../catalog/cloudflare-access.md) ✅ با OTP | — | [Cloudflare، مرحله‌ی ۶](../domains/website/04-tech/cloudflare-full-stack.md) |
| فونت | [Google Fonts](../catalog/google-fonts.md) ✅ (Vazirmatn؛ Readex Pro برای لاتین و عربی) | فونت فارسی پولی ← [یکان‌بخ](../catalog/yekan-bakh.md) 🧪 | [RTL](../domains/website/02-design/persian-rtl.md)، [تایپوگرافی](../domains/website/02-design/typography.md) |
| حرکت | [GSAP](../catalog/gsap.md) ✅ + [Lenis](../catalog/lenis.md) ✅، با [GSAP Skills](../catalog/gsap-skills.md) ✅ | پروژه‌ی React ← [Motion](../catalog/motion.md) ✅ | [حرکت](../domains/website/03-motion-3d/motion-animation.md) |
| کامپوننت (فقط React) | [shadcn/ui](../catalog/shadcn-ui.md) ✅ + [Magic UI](../catalog/magic-ui.md) ✅ | [Motion Primitives](../catalog/motion-primitives.md) ✅ | [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md) |
| سه‌بعدی | [Three.js](../catalog/threejs.md) ✅ | مدل در گوشی و AR ← [model-viewer](../catalog/model-viewer.md) ✅ (برای سازه‌ی بزرگ سخت بود) | [سه‌بعدی](../domains/website/03-motion-3d/3d-webgl.md) |
| تصویر و آیکون | [Squoosh](../catalog/squoosh.md) ✅، [SVGO](../catalog/svgo.md) ✅، [Phosphor](../catalog/phosphor-icons.md) ✅ | عکس آماده ← [Unsplash](../catalog/unsplash.md) ✅؛ تصویر OG ← [Satori](../catalog/satori.md) ✅ | [رسانه](../domains/website/05-media/media-guidelines.md) |
| بررسی خودکار | [Playwright](../catalog/playwright.md) ✅ + [axe-core](../catalog/axe-core.md) ✅ + [html-validate](../catalog/html-validate.md) ✅ + [Lighthouse CI](../catalog/lighthouse-ci.md) ✅ | بررسی دستی در Chrome ← [Chrome DevTools MCP](../catalog/chrome-devtools-mcp.md) ✅ | [بررسی خودکار](../domains/claude-code/verification.md) |
| ثبت در موتورها | [Search Console](../catalog/google-search-console.md) ✅، [Bing Webmaster Tools](../catalog/bing-webmaster-tools.md) ✅، [IndexNow](../catalog/indexnow.md) ✅ | کسب‌وکار محلی ← [Google Business Profile](../catalog/google-business-profile.md) ✅ | [سئوی فنی](../domains/website/09-seo/seo-and-ai-search.md) |
| پیش‌نمایش برای مشتری | [Cloudflare Tunnel](../catalog/cloudflare-tunnel.md) ✅ با `--allowed-mail` | پیش‌نمایش ماندگار ← لینک پیش‌نمایش Vercel | [تکنولوژی](../domains/website/04-tech/tech-stack.md) |

کنار بگذار: [BackstopJS](../catalog/backstopjs.md) ⛔ و [Pa11y](../catalog/pa11y.md) 👀 ([بررسی خودکار، پشته‌ی سایت](../domains/claude-code/verification.md)).

## مراحل

### مرحله‌ی ۱: شروع و بررسی خودکار
- **هدف:** پیش از هر طراحی، Claude بتواند خودش «قبول» یا «رد» بگیرد.
- **کارها:** مخزن git و commit هر مرحله‌ی سالم ([Vibe Coding](../domains/website/01-method/vibe-coding.md)). Playwright با `reducedMotion: "reduce"`، axe، html-validate و LHCI با ۳ اجرا و بارگذاری خاموش. LHCI در پوشه‌ی جدا با `package.json` خودش. از روز اول `<link rel="icon">`. همه زیر یک فرمان `npm run check`.
- **تمام یعنی:** `npm run check` روی صفحه‌ی خالی سبز است، و سه خراب‌کاری عمدی (کنتراست کم، جابه‌جایی دکمه، لینک شکسته) را می‌گیرد ([بررسی خودکار، «تست خود اوراکل»](../domains/claude-code/verification.md)).
- **بخوان:** [بررسی خودکار](../domains/claude-code/verification.md)، [کارت Lighthouse CI](../catalog/lighthouse-ci.md).

### مرحله‌ی ۲: حقیقت و محتوا
- **هدف:** همه‌ی عددها و ادعاهای سایت از داده‌ی واقعی بیاید.
- **کارها:** ابعاد، مشخصات، مناطق خدمت و قیمت‌ها را از مشتری بگیر («حقیقت اول» در [روش کار](../domains/website/01-method/claude-workflow.md)). سایت قبلی را آرشیو کن و نقشه‌ی ۳۰۱ بساز. برای هر عکس، فونت و صدا مجوز را ثبت کن ([رسانه، حقوق](../domains/website/05-media/media-guidelines.md)).
- **تمام یعنی:** یک فایل محتوا یا داده که هر عدد سایت از آن ساخته می‌شود؛ و اگر سایت قبلی هست، آزمون Playwright که برای هر آدرس قدیمی پاسخ ۳۰۱ به یک صفحه‌ی زنده بگیرد 🧭.
- **بخوان:** [روش کار](../domains/website/01-method/claude-workflow.md)، [ساختار لندینگ](../domains/website/02-design/landing-page-structure.md).

### مرحله‌ی ۳: مسیر طراحی و هیرو
- **هدف:** مشتری انتخاب کند، پیش از آن‌که کل سایت ساخته شود.
- **کارها:** ۲ یا ۳ مسیر طراحی با سبک، فونت، رنگ و ایده‌ی هیرو بده و **صبر کن** ([روش کار، پرامپت شروع](../domains/website/01-method/claude-workflow.md)). سبک را از [سبک‌های طراحی](../domains/website/02-design/design-styles.md) انتخاب کن. فقط هیرو را بساز. اگر مشتری سلیقه‌اش را نمی‌تواند بگوید، روش «یک شکل در چند سبک» ([لوگو و برند](../domains/website/02-design/logo-and-brand.md)).
- **تمام یعنی:** عکس صفحه در ۳۹۰ و ۱۴۴۰ پیکسل، نمره‌ی هر بخش از ۱۰ (بخش زیر ۸ دوباره)، تأیید مشتری، و `npm run check` سبز.
- **بخوان:** [روش کار](../domains/website/01-method/claude-workflow.md)، [رنگ و کنتراست](../domains/website/02-design/color-and-texture.md)، [حرکت](../domains/website/03-motion-3d/motion-animation.md).

### مرحله‌ی ۴: ساخت بخش‌ها و زبان‌ها
- **هدف:** همه‌ی صفحه‌ها در همه‌ی زبان‌ها، درست در RTL.
- **کارها:** بخش‌به‌بخش با commit. `lang` و `dir` برای هر زبان، ویژگی‌های منطقی CSS، فاصله‌ی حروف صفر روی فارسی، نام لاتین و تلفن در `<bdi dir="ltr">`، رقم صریح (`ar-AE-u-nu-latn`، `fa-IR-u-nu-arabext`) ([RTL](../domains/website/02-design/persian-rtl.md)). فقط `transform` و `opacity` متحرک، با `prefers-reduced-motion`. تصویر هیرو با preload و `fetchpriority="high"`، بقیه lazy ([چک‌لیست، سرعت](../domains/website/07-quality/launch-checklist.md)).
- **تمام یعنی:** `npm run check` در ۳ عرض برای هر زبان سبز؛ به‌اضافه‌ی آزمون «فاصله‌ی حروف روی فارسی» و آزمون کامل بودن ترجمه ([بررسی خودکار](../domains/claude-code/verification.md)، بخش‌های پنل Next.js و اوراکل‌های کوچک).
- **بخوان:** [RTL](../domains/website/02-design/persian-rtl.md)، [رسانه](../domains/website/05-media/media-guidelines.md)، [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md).

### مرحله‌ی ۵: فرم، ایمیل و ضد ربات
- **هدف:** هیچ پیامی گم نشود و هیچ کلیدی در مرورگر نباشد.
- **کارها:** فرم اول در D1 ذخیره شود، Turnstile در سرور بررسی شود، بعد اعلان ([Cloudflare، مرحله‌های ۲ تا ۵](../domains/website/04-tech/cloudflare-full-stack.md)). «از کجا با ما آشنا شدید؟» با گزینه‌ی دستیار هوش مصنوعی ([سئوی فنی، بخش ۹](../domains/website/09-seo/seo-and-ai-search.md)). Zoho با MX، SPF، DKIM و DMARC؛ پیش از `reject` همه‌ی فرستنده‌ها را فهرست کن ([دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md)).
- **تمام یعنی:** آزمون Playwright فرم را با کلید آزمایشی Turnstile می‌فرستد و ردیف تازه را در D1 محلی می‌بیند؛ ارسال بدون توکن رد می‌شود؛ و ایمیل آزمایشی واقعی به صندوق شرکت می‌رسد.
- **بخوان:** [دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md)، [Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md).

### مرحله‌ی ۶: سئوی فنی
- **هدف:** سایت از روز اول در گوگل، Bing و دستیارهای هوش مصنوعی پیدا شود.
- **کارها:** robots.txt با گروه‌های نام‌دار، sitemap با lastmod از اثر انگشت محتوا، hreflang، JSON-LD (LocalBusiness، Service با Offer؛ بدون Review خودستایانه)، فایل کلید IndexNow، و llms.txt از همان محتوا. قیمت‌ها از یک منبع ([سئوی فنی](../domains/website/09-seo/seo-and-ai-search.md)). تا دامنه‌ی واقعی وصل نیست، `noindex` با تابع `indexable()`.
- **تمام یعنی:** LHCI با SEO و دسترسی‌پذیری بدون خطا، html-validate سبز، و Rich Results Test برای هر نوع داده‌ی ساختاریافته بدون خطا.
- **بخوان:** [سئوی فنی](../domains/website/09-seo/seo-and-ai-search.md).

### مرحله‌ی ۷: انتشار
- **هدف:** سایت روی دامنه‌ی مشتری، امن و سریع.
- **کارها:** Pages با Git و `NODE_VERSION`؛ `_routes.json` تا فایل‌های ایستا از سهمیه‌ی Functions کم نکنند؛ Crawler Hints روشن؛ مخفی‌سازی ایمیل خاموش؛ DNSSEC با رکورد DS؛ CAA ([Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md)، [دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md)). چک‌لیست انتشار را کامل کن.
- **تمام یعنی:** همه‌ی بندهای [چک‌لیست انتشار](../domains/website/07-quality/launch-checklist.md) تیک خورده؛ `dig +dnssec` پرچم `ad` را نشان می‌دهد؛ LCP و Lighthouse روی **سایت زنده** اندازه گرفته شده، نه فقط محلی.
- **بخوان:** [چک‌لیست انتشار](../domains/website/07-quality/launch-checklist.md).

### مرحله‌ی ۸: پس از انتشار و سئوی محلی
- **هدف:** نام کسب‌وکار در جستجو، نقشه و جواب‌های هوش مصنوعی بیاید.
- **کارها:** Search Console با ویژگی Domain، Bing Webmaster Tools، ارسال sitemap، IndexNow فقط برای آدرس‌های تغییرکرده. Business Profile با چک‌لیست کامل و ویدیوی ۳۰ ثانیه‌ای پیوسته؛ نام، آدرس و تلفن همه‌جا یکسان. فهرست‌های محلی امارات ([سئوی محلی](../domains/website/09-seo/local-business-profile.md)).
- **تمام یعنی:** پاسخ IndexNow ثبت شده (۲۰۲ یعنی بعداً دوباره بفرست)، sitemap در هر دو کنسول «موفق»، و پروفایل تأییدشده با لینک آن در `sameAs` سایت.
- **بخوان:** [سئوی فنی، بخش ۹](../domains/website/09-seo/seo-and-ai-search.md)، [سئوی محلی](../domains/website/09-seo/local-business-profile.md).

## چرا این ترتیب (برای Claude)

بررسی خودکار اول می‌آید، چون بعداً اضافه کردنش گران است: یک سایت مشتری بدون تست منتشر شد و بعد ۷ ایراد واقعی پیدا شد. حقیقت پیش از طراحی می‌آید، چون هر عدد سایت باید از داده بیاید و طراحی روی عدد غلط دوباره‌کاری است. مشتری مسیر را پیش از ساخت انتخاب می‌کند، چون هر بخش ساخته‌شده هزینه‌ی تغییر را بالا می‌برد. فرم و ایمیل پیش از سئو می‌آیند، چون سایتی که پیام را گم کند، با بازدید بیشتر فقط مشتری بیشتری از دست می‌دهد. سئوی محلی آخر است، چون پروفایل به سایت زنده و تابلوی واقعی وابسته است. قاعده‌ی کلی: کاری که برگشتش گران است (حساب، دامنه، ویدیوی تأیید) را دیرتر و با تأیید مشتری انجام بده؛ کاری که ارزان است و خطا را زود نشان می‌دهد (تست، عکس صفحه) را زودتر.

## خطاهایی که در پروژه‌های خودمان دیدیم 🔬

همه از دفتر پروژه‌ها:
- **یک سایت مشتری:** بی‌تست بود؛ بعد از پشته‌ی بررسی، ۷ ایراد پیدا شد، از جمله `fetchpriority="undefined"` روی همه‌ی تصویرها. بدون `reducedMotion: "reduce"`، axe عنصرهای وسط انیمیشن را کنتراست پایین دید. مخفی‌سازی ایمیل Cloudflare لینک ایمیل را خراب کرد. گیرنده‌ی EmailJS در داشبورد عوض نشده بود. خطای `ERESOLVE` در build. ویدیوی تأیید Business Profile بدون تابلو رد شد. `_routes.json` بعد از راه‌اندازی پیدا شد.
- **Sun Shade DXB:** لوگوی تخت هندسی «کودکانه و قدیمی» رد شد. نبود favicon امتیاز LHCI را پایین آورد. `&` در عنوان SVG فایل را خراب کرد. حدس اول «صفحه‌های منطقه تکراری‌اند» با اندازه‌گیری غلط درآمد.
- **MARIO E.G.S.H:** تکرار پشت‌سرهم آزمون فرم تماس به سقف ضد سیل خورد. فیلد پیش از بالا آمدن React پاک می‌شد. axe متن روی عکس را نمی‌بیند؛ کنتراست آن‌جا با چشم.
- 🔬 یک پروژه‌ی مشتری (۲۰۲۶-۱۰-۲۳): «تمام» یعنی سفر مشتری روی ماشین تمیز و کلیک‌گذر مرورگر واقعی هم قبول شده و هر عدد تکراری از یک منبع محاسبه و در build بررسی شده است؛ سبز بودن آزمون‌های واحد کافی نیست ([بررسی خودکار](../domains/claude-code/verification.md)، [کار موازی](../domains/claude-code/parallel-agents.md)).

## پرامپت شروع (English)
```text
We are building a business website for <company>: <what they do, where, for whom>.
Languages: <English / Arabic / Persian>. Project folder: <path>.
Follow the playbook ~/Desktop/knowledge-library/playbooks/business-website.md
phase by phase. First ask me only the "before you start" questions you cannot answer from
this message or the folder. Then show me the default stack from the playbook with each
card's verdict, and wait for my OK. Set up `npm run check` (Playwright with reduced motion,
axe, html-validate, Lighthouse CI in its own folder) before any design work. Do not call a
phase done until its "done means" gate passes, and show me the output. Propose 2-3 design
directions and wait for my choice; build the hero first. Use only our own wording, our own
design and clearly licensed assets. Stop and hand over to me for any account, payment,
domain or verification step. Reply in Persian.
```

## پایان کار: چه چیزی به کتابخانه برگردد

- فقط چیز تازه یا اصلاحی: ابزار یا نسخه‌ی تازه، تغییر قیمت یا مجوز، روشی که کار کرد، ابزاری که شکست خورد ([CLAUDE.md](../CLAUDE.md)).
- یک ردیف در دفتر پروژه‌ها با نام پروژه، و کارت‌هایی که واقعاً کار کردند با 🔬.
- هر شکافی که این راهنما نداشت و پیدا کردی (پایین)، با منبع اصلی به سند مربوط.
- `python3 scripts/build_all.py` با ۰ خطا و `python3 scripts/sync.py`.

**شکاف‌های فعلی:**
- ❓ کتابخانه هنوز ندارد: سرویس ارسال ایمیل از Function سرور (سند فقط «یک سرویس ارسال ایمیل» می‌گوید).
- ❓ کتابخانه هنوز ندارد: ابزار آمار بازدید سایت با حکم (GA4 فقط در سئوی فنی نام برده شده؛ [PostHog](../catalog/posthog.md) 🧪 برای اپ بررسی شده).
- ❓ کتابخانه هنوز ندارد: صفحه‌ی حریم خصوصی، بنر رضایت کوکی و قانون امارات برای فرم سایت.
- ❓ کتابخانه هنوز ندارد: کارت برای Bing Places و Apple Business Connect.

## مرتبط

[فهرست راهنماها](README.md) · [فروشگاه آنلاین](online-store.md) · [داشبورد و نرم‌افزار وب](web-app-dashboard.md) · [برند و لوگو](brand-identity.md) · [کتابخانه‌ی پرامپت](../domains/website/08-prompts/prompt-library.md) · پرامپت شروع پروژه
