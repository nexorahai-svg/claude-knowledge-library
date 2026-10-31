# راهنمای پروژه: داشبورد و نرم‌افزار وب

> **نوع سند:** راهنمای قدم‌به‌قدم
> **هدف این سند:** Claude در یک پروژه‌ی داشبورد، پنل مدیریت یا نرم‌افزار تحت وب با ورود کاربر، داده، نمودار و به‌روزرسانی زنده، از اولین پیام تا تحویل و نگهداری، قدم‌به‌قدم بداند چه بپرسد، چه بسازد، با کدام ابزار، و هر مرحله کی «تمام» است.
> **موضوع تحقیق:** جمع‌بندی سندها و کارت‌های کتابخانه و تجربه‌ی پروژه‌های واقعی برای این نوع پروژه (این راهنما ادعای تازه نمی‌سازد؛ هر واقعیت به سند منبعش لینک دارد).
> **منابع:** سندهای لینک‌شده در متن · دفتر پروژه‌ها
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۰
> **دفعه‌ی بعد چک شود:** وقتی حکم یکی از کارت‌های جدول پشته عوض شد (lint آن را می‌گیرد) یا پروژه‌ی تازه‌ای از این نوع تمام شد.

---

## این راهنما برای کدام پروژه است

- کاربر وارد حساب می‌شود و داده‌ی خودش یا کسب‌وکار را می‌بیند و تغییر می‌دهد.
- نمودار، جدول، عدد زنده، تخته‌ی کانبان یا نقشه دارد.
- پنل مدیریت یک سایت، پورتال مشتری یا نرم‌افزار شبیه SaaS است.
- گاهی داده‌ی حساس (مدرک، پرونده‌ی مشتری) یا کار پس‌زمینه دارد.
- نمونه‌های واقعی: پنل معامله‌گر هوش مصنوعی کریپتو، بخش وب پنل قرارداد (a-project)، پنل مدیریت یک فروشگاه واقعی (دفتر پروژه‌ها).

اگر فقط پنل کوچک پشت یک سایت معرفی است: [سایت کسب‌وکار](business-website.md) با Cloudflare Access. اگر روی رایانه‌ی خود کسب‌وکار و Wi-Fi اجرا می‌شود: [اپ شبکه‌ی محلی](local-business-app.md). بقیه: [فهرست راهنماها](README.md).

## پیش از شروع: پرسش‌ها از کاربر

1. **داده چقدر حساس است؟** اگر مدرک، شناسه یا داده‌ی شخصی ← Next.js روی سرور لینوکسی خودمان پشت Caddy، CSP با nonce ([سرور خودمان](../domains/website/04-tech/self-hosted-server.md)، [تکنولوژی، CSP](../domains/website/04-tech/tech-stack.md))؛ محل داده را با [بک‌اند اپ](../domains/apps/app-backend.md) بسنج. اگر داده‌ی کاری ساده ← میزبان آماده. پیش‌فرض: هر داده‌ی شخصی را حساس بدان.
2. **چه کسی وارد می‌شود؟** اگر فقط مالک و تیم ← [Cloudflare Access](../catalog/cloudflare-access.md) ✅ با OTP و بررسی JWT در سرور، یا فقط از شبکه‌ی دفتر و VPN. اگر مشتری‌ها هم ← [Better Auth](../catalog/better-auth.md) 🧪 روی سرور خودمان با کد یک‌بارمصرف ایمیلی، passkey بعد از اولین ورود، و افزونه‌ی organization با بررسی `hasPermission` در سرور ([ورود مشتری](../domains/website/04-tech/customer-auth.md)). پیش‌فرض: فقط تیم، پشت Access.
3. **کد از قبل هست؟** اگر بله ← همان فریم‌ورک را نگه دار. اگر نه و کامپوننت زیاد React لازم است ← Next.js با shadcn/ui. اگر یک داشبورد تک‌منظوره و متحرک است ← TypeScript ساده با Vite، مثل دستور شیشه‌ای ([سبک‌های طراحی، شیشه‌ای](../domains/website/02-design/design-styles.md)). پیش‌فرض: کد موجود.
4. **به‌روزرسانی زنده لازم است؟** اگر بله ← ❓ کتابخانه هنوز روش تأییدشده‌ای ندارد؛ پیش از ساخت از منبع اصلی تحقیق کن (کارت Supabase می‌گوید realtime دارد). اگر نه ← خواندن دوباره با فاصله‌ی ثابت. پیش‌فرض: نه، تا کاربر نیازش را بگوید.
5. **سبک دیداری چیست و ریل معرفی هم می‌خواهد؟** اگر شیشه‌ای ← دستور شیشه‌ای با پس‌زمینه‌ی لکه‌های نور. اگر ساده و خوانا ← بنتو گرید یا جدول. اگر ریل هم می‌خواهد ← «حالت ضبط» `?record` از روز اول ([ویدیو با کد](../domains/social-media/code-to-video.md)). پیش‌فرض: ساده و خوانا.
6. **هوش مصنوعی داخل پنل لازم است؟** اگر بله ← [هوش مصنوعی در محصول و عامل](ai-feature-agent.md) با لایه‌ی حریم خصوصی، بودجه و جایگزین محلی. اگر نه ← نسخه‌ی ۱ بدون آن. پیش‌فرض: بدون آن.

## پشته‌ی پیش‌فرض

| نیاز | انتخاب پیش‌فرض | کی چیز دیگر | جزئیات |
|---|---|---|---|
| فریم‌ورک | [Next.js](../catalog/nextjs.md) ✅ (حداقل ۱۶٫۴٫۱؛ هر ماه هشدارهای امنیتی) + [Tailwind](../catalog/tailwindcss.md) ✅ | داشبورد تک‌منظوره ← TypeScript + [Vite](../catalog/vite.md) ✅ بدون فریم‌ورک | [تکنولوژی](../domains/website/04-tech/tech-stack.md)، [سبک‌های طراحی](../domains/website/02-design/design-styles.md) |
| کامپوننت | [shadcn/ui](../catalog/shadcn-ui.md) ✅ | — | [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md) |
| آیکون | [Phosphor](../catalog/phosphor-icons.md) ✅، یک فایل برای هر آیکون | — | [کامپوننت‌ها، Turbopack](../domains/website/04-tech/component-libraries.md) |
| نمودار | SVG ساخته‌شده با کد | ❓ کتابخانه‌ی نمودار با حکم نداریم | [سبک‌های طراحی، شیشه‌ای](../domains/website/02-design/design-styles.md) |
| نقشه | [mapcn](../catalog/mapcn.md) ✅ | — | [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md) |
| حرکت | [GSAP](../catalog/gsap.md) ✅ | پروژه‌ی React ← [Motion](../catalog/motion.md) ✅ | [حرکت](../domains/website/03-motion-3d/motion-animation.md) |
| صحنه‌ی سه‌بعدی (اختیاری) | [Three.js](../catalog/threejs.md) ✅ | React ← [React Three Fiber](../catalog/react-three-fiber.md) ✅ | [سه‌بعدی](../domains/website/03-motion-3d/3d-webgl.md) |
| میزبانی، داده‌ی حساس | سرور خودمان پشت [Caddy](../catalog/caddy.md) ✅ | داده‌ی ساده ← [Cloudflare Pages](../catalog/cloudflare-pages.md) ✅ یا [Vercel](../catalog/vercel.md) ✅ فقط Pro | [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) |
| ورود مشتری و نقش‌ها | [Better Auth](../catalog/better-auth.md) 🧪 (نسخه‌ی تازه؛ هشدارهای امنیتی را دنبال کن) | داده در امارات شرط نیست و تیم کوچک ← [Supabase](../catalog/supabase.md) 🧪؛ استفاده نکن: [Auth.js](../catalog/authjs.md) ⛔، [Lucia](../catalog/lucia.md) ⛔ | [ورود مشتری](../domains/website/04-tech/customer-auth.md) |
| ورود تیم | [Cloudflare Access](../catalog/cloudflare-access.md) ✅ | شبکه‌ی همکاران ← [Headscale](../catalog/headscale.md) 🧪 | [Cloudflare، مرحله‌ی ۶](../domains/website/04-tech/cloudflare-full-stack.md) |
| پایگاه داده | SQLite روی سرور خودمان | سرویس آماده ← [Supabase](../catalog/supabase.md) 🧪 یا [Firebase](../catalog/firebase.md) ✅ | [سرور خودمان، پشتیبان](../domains/website/04-tech/self-hosted-server.md)، [بک‌اند اپ](../domains/apps/app-backend.md) |
| بررسی خودکار | [Playwright](../catalog/playwright.md) ✅ + [axe-core](../catalog/axe-core.md) ✅ + [html-validate](../catalog/html-validate.md) ✅ + [Lighthouse CI](../catalog/lighthouse-ci.md) ✅ | تست جهشی کد منطقی ← [Stryker](../catalog/stryker.md) 👀 (هنوز پیش‌فرض نیست؛ خطای عمدی دستی) | [بررسی خودکار](../domains/claude-code/verification.md) |
| گزارش خطا و آمار (اختیاری) | [Sentry](../catalog/sentry.md) 🧪 اروپا | آمار ناشناس ← [PostHog](../catalog/posthog.md) 🧪 | [عملیات پس از انتشار](../domains/apps/app-operations.md) |
| مدل محلی (اگر هوش مصنوعی) | [llama.cpp](../catalog/llama-cpp.md) ✅ | [Ollama](../catalog/ollama.md) ✅ | [هوش مصنوعی ابری در محصول](../domains/website/04-tech/ai-in-product.md) |
| پیش‌نمایش برای مشتری | [Cloudflare Tunnel](../catalog/cloudflare-tunnel.md) ✅ | — | [تکنولوژی](../domains/website/04-tech/tech-stack.md) |

الگو برای سبک شیشه‌ای: [Code and Chill](../catalog/code-and-chill.md) 🧪، فقط برای یاد گرفتن اصول؛ کد و طرحش کپی نمی‌شود. لنز [Liquid Glass](../catalog/liquid-glass.md) ⛔ نه.

## مراحل

### مرحله‌ی ۱: شروع و «همه‌ی بررسی‌ها با یک فرمان»
- **هدف:** پیش از هر قابلیت، یک فرمان بگوید چه چیزی قبول و چه چیزی رد است.
- **کارها:** یک اسکریپت: نوع‌ها، تست‌های واحد، تست مرورگر روی **داده‌ی نمایشی**، ممیزی زبان، و در پایان جدول قبول و رد. کار سنگین با یک worker و `nice`؛ ساخت در فرمان جدا؛ اجرای سنگین با سقف حافظه ([کار موازی، حافظه](../domains/claude-code/parallel-agents.md)).
- **تمام یعنی:** فرمان یک‌جا روی پروژه‌ی خالی جدول «قبول» می‌دهد و یک خراب‌کاری عمدی آن را «رد» می‌کند ([بررسی خودکار، همه‌ی بررسی‌ها با یک فرمان](../domains/claude-code/verification.md)).
- **بخوان:** [بررسی خودکار](../domains/claude-code/verification.md).

### مرحله‌ی ۲: مدل داده و مرزهای دسترسی
- **هدف:** پیش از صفحه‌ها، معلوم باشد چه کسی چه چیزی را می‌بیند و سقف هر کار چیست.
- **کارها:** هر قاعده‌ی دسترسی و هر سقف را فهرست کن. برای هر بررسی مالکیت یک تست «کاربر دیگر»، برای هر سقف یک تست دقیقاً روی سقف و یک واحد آن طرف. قاعده‌ای که روی تابع، middleware و مسیر API پخش است، در هر لایه تست جدا دارد. «تازه بودن» پایگاه داده را با محتوا تشخیص بده، نه با بودن فایل (دام SQLite).
- **تمام یعنی:** دور خطای عمدی روی ۱۰ تا ۱۵ نقطه‌ی حیاتی؛ همه گرفته شوند جز موارد هم‌ارز، که جدا شمرده می‌شوند ([بررسی خودکار](../domains/claude-code/verification.md)).
- **بخوان:** [بررسی خودکار](../domains/claude-code/verification.md)، [بک‌اند اپ](../domains/apps/app-backend.md).

### مرحله‌ی ۳: طراحی، یک صفحه اول
- **هدف:** مالک یک صفحه‌ی کامل را تأیید کند، بعد بقیه.
- **کارها:** برای شیشه‌ای، دستور [سبک‌های طراحی](../domains/website/02-design/design-styles.md): پس‌زمینه‌ی سرمه‌ای با ۳ تا ۴ لکه‌ی نور، شیشه با `backdrop-filter: blur()` و `saturate()`، همه‌ی مقدارها در متغیر CSS با تم روشن، یک رنگ تأکیدی گرم، رنگ وضعیت با `color-mix`، یک منحنی حرکت مشترک، تم ذخیره‌شده پیش از اولین نقاشی. برای فارسی، قاعده‌های [RTL](../domains/website/02-design/persian-rtl.md)؛ نقطه‌ی وسط (·) کنار رقم فارسی نه.
- **تمام یعنی:** عکس صفحه در ۳۹۰، ۷۶۸ و ۱۴۴۰ پیکسل در تم روشن و تیره، axe بدون خطای کنتراست، و تأیید مالک. متن روی عکس یا صحنه‌ی WebGL را با چشم هم ببین، چون axe آن را نمی‌بیند.
- **بخوان:** [سبک‌های طراحی](../domains/website/02-design/design-styles.md)، [رنگ و کنتراست](../domains/website/02-design/color-and-texture.md).

### مرحله‌ی ۴: ساخت صفحه‌ها و نمودارها
- **هدف:** همه‌ی صفحه‌ها، درست در همه‌ی عرض‌ها و زبان‌ها.
- **کارها:** در Tailwind 4 قاعده‌های پایه‌ی خودت را در `@layer base` بنویس ([تکنولوژی، Tailwind 4](../domains/website/04-tech/tech-stack.md)). یک فایل برای هر آیکون؛ فهرست بلند با کامپوننت کلاینت و اسپرایت SVG ([کامپوننت‌ها](../domains/website/04-tech/component-libraries.md)). تاریخ و ساعت بعد از mount. فیلدی که کاربر اول تایپ می‌کند، مقدار پیش از hydration را نگه دارد. نمودار SVG با کد؛ حرکت فقط با `prefers-reduced-motion`.
- **تمام یعنی:** فرمان یک‌جا سبز، شامل: بدون خطای کنسول در ۳ عرض، آزمون فاصله‌ی حروف فارسی با `TreeWalker`، و نبودن خطای `scrollable-region-focusable` ([بررسی خودکار، نکته‌های پنل Next.js](../domains/claude-code/verification.md)).
- **بخوان:** [بررسی خودکار](../domains/claude-code/verification.md)، [کامپوننت‌ها](../domains/website/04-tech/component-libraries.md).

### مرحله‌ی ۵: امنیت و سرور خودمان
- **هدف:** سرور امن، با به‌روزرسانی تقریباً بدون قطعی و برگشت سریع.
- **کارها:** Caddy جلوی Next.js با پاک کردن هدرهای داخلی (نه `Rsc` و `Next-Router-*`)، سرویس systemd سخت‌شده، دانلود با نسخه و چک‌سام ثابت، نسخه‌ی امضاشده‌ی Ed25519، به‌روزرسانی با دو پوشه، پشتیبان `VACUUM INTO` و rclone crypt. redirect پشت پروکسی با `Location` نسبی. CSP با nonce و تست «تخلف CSP = خطای کنسول».
- **تمام یعنی:** کیت در کانتینر Docker با systemd آزموده شده: نصب تازه، به‌روزرسانی، برگشت و build شکسته بدون خواب سایت؛ `systemd-analyze security` برای هر سرویس؛ zip بی‌امضا یا تغییرکرده رد می‌شود ([سرور خودمان، بخش‌های ۵ تا ۸](../domains/website/04-tech/self-hosted-server.md)).
- **بخوان:** [سرور خودمان](../domains/website/04-tech/self-hosted-server.md)، [محافظت از اپ](../domains/apps/app-protection.md).

### مرحله‌ی ۶: بازبینی انتقادی پیش از انتشار
- **هدف:** ایرادهایی که تست‌ها نمی‌بینند، پیش از کاربر واقعی پیدا شوند.
- **کارها:** پنج بازبین فقط‌خواندنی هم‌زمان (پایگاه داده، بار، امنیت، درستی منطق، کیت سرور). هر یافته پیش از رفع در خود کد تأیید شود. رفع‌ها با مالکیت سخت فایل ([کار موازی](../domains/claude-code/parallel-agents.md)).
- **تمام یعنی:** هر یافته «رفع با تست»، «رد با دلیل» یا «باز» ثبت شده و کل تست‌ها سبز است ([بررسی خودکار، بازبینی پنج‌بعدی](../domains/claude-code/verification.md)).
- **بخوان:** [بررسی خودکار](../domains/claude-code/verification.md).

### مرحله‌ی ۷: انتشار و نگهداری
- **هدف:** نسخه‌ی زنده با داده‌ی واقعی، بدون خطر برای همان داده.
- **کارها:** آزمون کامل روی رایانه‌ای که داده‌ی واقعی دارد: سرویس‌ها را ببند، از همه‌ی فایل‌های داده sha256 بگیر، پوشه را تغییر نام بده، روی داده‌ی نمایشی آزمون بگیر، و فقط با hash و تعداد فایل برابر برگردان. آزمون بار روی صفحه‌ی اصلی و پرکارترین صفحه. صفحه‌های پنل، ورود و `/api` با `X-Robots-Tag: noindex`.
- **تمام یعنی:** hash و تعداد فایل‌ها بعد از برگرداندن برابر است؛ عدد درخواست در ثانیه و خطا با ابزار و مدت ثابت ثبت شده ([چک‌لیست انتشار، آزمون بار](../domains/website/07-quality/launch-checklist.md))؛ بقیه‌ی [چک‌لیست انتشار](../domains/website/07-quality/launch-checklist.md) تیک خورده.
- **بخوان:** [بررسی خودکار، آزمون کامل روی داده‌ی واقعی](../domains/claude-code/verification.md)، [سئوی فنی، بخش ۱۰](../domains/website/09-seo/seo-and-ai-search.md).

### مرحله‌ی ۸ (اختیاری): ریل معرفی از خود داشبورد
- **هدف:** ویدیوی معرفی از همان صفحه‌ی واقعی، با داده‌ی نمایشی.
- **کارها:** حالت `?record`: تم و تنظیمات ذخیره‌شده نادیده، صبر تا آماده شدن ابزار ضبط، شروع از حالت ثابت. فریم با اسکرین‌شات، نه ضبط ویدیو.
- **تمام یعنی:** دو رندر پشت‌سرهم از همان حالت، فریم‌های یکسان می‌دهند 🧭، و فایل نهایی با [مشخصات شبکه](../domains/social-media/platform-specs.md) می‌خواند.
- **بخوان:** [ویدیو با کد](../domains/social-media/code-to-video.md)، [محتوای شبکه‌های اجتماعی](social-content.md).

## چرا این ترتیب (برای Claude)

در داشبورد، خطای خطرناک «دیدن داده‌ی کاربر دیگر» است، نه زشتی؛ پس مرزهای دسترسی و سقف‌ها پیش از صفحه‌ها تست می‌شوند. سبز بودن همه‌ی تست‌ها چیزی درباره‌ی مرزها نمی‌گوید؛ فقط خطای عمدی نشان می‌دهد تست‌ها کورند یا نه. طراحی با یک صفحه شروع می‌شود، چون دستور سبک (رنگ، شیشه، حرکت) در متغیرها می‌نشیند و بعد ارزان در همه‌جا تکرار می‌شود. سرور پیش از بازبینی ساخته می‌شود تا بازبین‌ها کیت واقعی را ببینند. داده‌ی واقعی آخر از همه و فقط با hash لمس می‌شود، چون برگشت‌ناپذیر است. اگر به حالتی رسیدی که این‌جا نیست، بپرس: «کدام خط کد دقیقاً جلوی این را می‌گیرد، و کدام تست آن را ثابت می‌کند؟»

## خطاهایی که در پروژه‌های خودمان دیدیم 🔬

از دفتر پروژه‌ها:
- **پنل معامله‌گر کریپتو:** کتابخانه اول خوانده نشد و دو گام بازطراحی بدون اوراکل ساخته شد. ساخت و Playwright با ۲ worker با کد ۱۳۷ کشته شد. Playwright و axe روی ۱۲ صفحه در ۳ عرض فاصله‌ی حروف روی فارسی، خطای React ۴۱۸، کنتراست ۳٫۴ به ۱، ناحیه‌ی اسکرولی بی‌فوکوس و فیلدهای روی‌هم (Tailwind 4) را گرفت. `next build` با `node_modules` لینک‌شده در worktree شکست خورد.
- **یک فروشگاه واقعی:** پایگاه داده‌ی تازه سه هفته پر نمی‌شد (دام SQLite). لینک ورود پشت Caddy به آدرس داخلی می‌رفت. کلیدها از کپی ویندوز برای همه خواندنی بودند. قفل «ورود تیم فقط از شبکه‌ی دفتر» در خود مسیر API تست نداشت. برچسب با `backdrop-filter` روی صحنه‌ی WebGL دیده نشد. وابستگی‌های LHCI هشدار امنیتی دارند؛ در پوشه‌ی جدا ماند.
- **پنل قرارداد (a-project):** برنامه فقط مسیر Edge و Chrome ویندوز را می‌شناخت و روی لینوکس PDF نمی‌ساخت؛ با پیدا کردن Chrome از PATH و `--print-to-pdf` حل شد.
- 🔬 یک پروژه‌ی واقعی (۲۰۲۶-۱۰-۲۳): «تمام» یعنی سفر مشتری روی ماشین تمیز و کلیک‌گذر مرورگر واقعی هم قبول شده و هر عدد تکراری از یک منبع محاسبه و در build بررسی شده است؛ سبز بودن آزمون‌های واحد کافی نیست ([بررسی خودکار](../domains/claude-code/verification.md)، [کار موازی](../domains/claude-code/parallel-agents.md)).

## پرامپت شروع (English)
```text
We are building a web app / dashboard for <who>: <what data, who logs in, which screens>.
Data sensitivity: <none / business / personal documents>. Project folder: <path>.
Follow the playbook ~/Desktop/knowledge-library/playbooks/web-app-dashboard.md
phase by phase. First ask me only the "before you start" questions you cannot answer from
this message or the folder. Show me the default stack with each card's verdict, mark what
the library has not verified yet (realtime, charts), and
wait for my OK. Build the one-command check first and run every browser test on demo data,
never on real data. Before building screens, list every access rule and limit and write a
test for each, then run a deliberate-error round. Design one screen and show it to me
before the rest. Do not call a phase done until its "done means" gate passes, and show me
the output. Use our own design, wording and data. Reply in Persian.
```

## پایان کار: چه چیزی به کتابخانه برگردد

- هر روشی که یکی از شکاف‌های پایین را بست، با منبع اصلی و برچسب، در سند مربوط ([CLAUDE.md](../CLAUDE.md)).
- دام تازه‌ی فریم‌ورک، سرور یا تست در [بررسی خودکار](../domains/claude-code/verification.md) یا [سرور خودمان](../domains/website/04-tech/self-hosted-server.md).
- یک ردیف در دفتر پروژه‌ها با نام پروژه و شمار خطای عمدی گرفته و نگرفته.
- `python3 scripts/build_all.py` با ۰ خطا و `python3 scripts/sync.py`.

**شکاف‌های فعلی:**
- ❓ کتابخانه هنوز ندارد: روش تأییدشده‌ی ورود مشتری (رمز، passkey، OTP) برای وب‌اپ خودمان؛ فقط Access برای تیم و ورود Supabase.
- ❓ کتابخانه هنوز ندارد: روش به‌روزرسانی زنده (WebSocket، رویداد از سرور) و سقف‌هایش.
- ❓ کتابخانه هنوز ندارد: کتابخانه‌ی نمودار با حکم؛ فقط «SVG با کد».
- ❓ کتابخانه هنوز ندارد: نقش‌ها و سطح دسترسی (RBAC) و ابزار مهاجرت پایگاه داده برای Postgres.
- ✅ طرح Free زیر ۵۰ کاربر است؛ طبق [Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md) و https://www.cloudflare.com/plans/sase-zero-trust.md .

## مرتبط

[فهرست راهنماها](README.md) · [سایت کسب‌وکار](business-website.md) · [فروشگاه آنلاین](online-store.md) · [هوش مصنوعی در محصول و عامل](ai-feature-agent.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · پرامپت شروع پروژه
