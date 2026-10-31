# کتابخانه‌های کامپوننت و ابزارهای انیمیشن

> **نوع سند:** مرجع
> **هدف این سند:** برای هر نیاز (افکت لندینگ، ریزتعامل، نقشه، Lottie، سه‌بعدی، پس‌زمینه) بدانیم از کدام کتابخانه یا ابزار استفاده کنیم و مجوزش اجازه‌ی کار مشتری را می‌دهد یا نه.
> **موضوع تحقیق:** ۳۰ کتابخانه و ابزاری که در پست‌های X به‌عنوان «ابزار رایگان طراحی وب متحرک» معرفی شدند: کارکرد واقعی، مجوز، قیمت و نگهداری.
> **منابع:** [S26 کتابخانه‌های کامپوننت](../../../sources/README.md#s26) · [S27 ابزارهای انیمیشن](../../../sources/README.md#s27) · [S28 سه‌بعدی و مهارت‌های رسمی](../../../sources/README.md#s28) · [S87 Systaliko UI](../../../sources/README.md#s87) · [S63 عنصر use در SVG](../../../sources/README.md#s63)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۹
> **دفعه‌ی بعد چک شود:** مجوزهای «❓» (RareUI، OriginKit، Liquid Glass، Kinetics)؛ شرایط کامل Aceternity، Lottielab و Jitter؛ قیمت‌ها؛ فعال ماندن پروژه‌های کوچک.

---

## انتخاب سریع

| نیاز | اول این | جایگزین | نه این |
|---|---|---|---|
| افکت آماده‌ی لندینگ (React) | [Magic UI](../../../catalog/magic-ui.md) ✅ | [Motion Primitives](../../../catalog/motion-primitives.md) ✅، [Aceternity](../../../catalog/aceternity-ui.md) 🧪 | [OriginKit](../../../catalog/originkit.md) ⛔، [RareUI](../../../catalog/rareui.md) ⛔ |
| ریزتعامل دکمه و فرم | [MicroKit](../../../catalog/microkit.md) 🧪 | [Uiverse](../../../catalog/uiverse.md) 👀 (هر قطعه را بررسی کن) | — |
| نقشه | [mapcn](../../../catalog/mapcn.md) ✅ | — | — |
| افکت canvas و WebGL | [CanvasUI](../../../catalog/canvasui.md) 🧪 | — | [Liquid Glass](../../../catalog/liquid-glass.md) ⛔ |
| انیمیشن JavaScript | [GSAP](../../../catalog/gsap.md) ✅ | [Anime.js](../../../catalog/animejs.md) ✅، [Motion](../../../catalog/motion.md) ✅ | — |
| منحنی حرکت | [Epic Easing](../../../catalog/epic-easing.md) 🧪 | — | — |
| انیمیشن Lottie | ساخت: [Lottielab](../../../catalog/lottielab.md) 🧪 (Pro) · پخش: [dotLottie Web](../../../catalog/dotlottie-web.md) ✅ | [Jitter](../../../catalog/jitter.md) 👀 (پولی) | — |
| انیمیشن تعاملی با حالت | [Rive](../../../catalog/rive.md) 👀 (فقط طرح پولی) | — | — |
| افکت متن CSS | [CSS Text Effects](../../../catalog/css-text-effects.md) 🧪 | — | — |
| loader | [Circle Loaders](../../../catalog/circle-loaders.md) 🧪 (CC0) | — | — |
| پس‌زمینه‌ی گرادیانت متحرک | [Pryzm](../../../catalog/pryzm.md) 🧪 (Pro) | نوشتن خودمان ([رنگ و بافت](../02-design/color-and-texture.md)) | [Gradient Buttons](../../../catalog/gradient-buttons.md) 👀 (فقط الهام) |
| سه‌بعدی در React | [React Three Fiber](../../../catalog/react-three-fiber.md) ✅ + [Drei](../../../catalog/drei.md) ✅ | [Postprocessing](../../../catalog/react-postprocessing.md) ✅، [Rapier](../../../catalog/react-three-rapier.md) ✅ | — |
| بهینه‌سازی SVG | [SVGO](../../../catalog/svgo.md) ✅ | — | — |
| یاد دادن کتابخانه به Claude | [GSAP Skills](../../../catalog/gsap-skills.md) ✅ | [Motion AI Kit](../../../catalog/motion-ai-kit.md) 👀 | — |

---

## درس‌های مجوز از این دسته

✅ «رایگان» در پست‌ها پنج معنی متفاوت داشت:

| نوع | یعنی | نمونه | کار مشتری |
|---|---|---|---|
| **MIT** | هر استفاده‌ای، با حفظ اعلان کپی‌رایت | Magic UI، Motion Primitives، mapcn، Anime.js، dotLottie | ✅ |
| **MIT + Commons Clause** | استفاده داخل سایت مجاز؛ فروش یا بازنشر خود کامپوننت ممنوع | CanvasUI | ✅ (بازفروش نه) |
| **CC0** | مالکیت عمومی | Circle Loaders | ✅ |
| **«همه‌ی حقوق محفوظ» یا شرایط سایت** | کپی کردن مجاز نیست مگر شرایط صریحاً اجازه دهد | Gradient Buttons، Aceternity | ❓ اول شرایط |
| **هیچ مجوزی** | از نظر قانونی یعنی **اجازه نداری** | OriginKit، Liquid Glass، Kinetics | ⛔ |

✅ ابزارهای ساخت (Lottielab، Jitter، Rive، Pryzm) در طرح رایگان **واترمارک، صفحه‌ی آغاز یا خروجی محدود** دارند؛ برای کار مشتری طرح پولی لازم است.

🧭 داده‌ی نقشه جدا از کد است: mapcn MIT است ولی کاشی‌های نقشه نیاز به ذکر OpenStreetMap و CARTO دارند.

🧭 کتابخانه‌های جامعه (Uiverse): مجوز کلی MIT است، ولی اصالت هر قطعه تضمین نشده.

---

## پشته‌ی پیشنهادی ما برای سایت متحرک

🧭 بر اساس حکم‌های بالا:
- **انیمیشن صفحه:** GSAP + ScrollTrigger + Lenis ([حرکت و انیمیشن](../03-motion-3d/motion-animation.md)) با [GSAP Skills](../../../catalog/gsap-skills.md) در Claude Code
- **کامپوننت:** shadcn/ui برای پایه + Magic UI یا Motion Primitives برای افکت
- **سه‌بعدی:** React Three Fiber + Drei (یا Three.js خالص بدون React)
- **دارایی:** SVGO برای SVG؛ dotLottie Web برای Lottie

```text
Build the [section] using shadcn/ui as the base and one effect from Magic UI or Motion
Primitives (MIT). Before adding any component, show me its source URL and license. Do not
use components from sites without a clear license. Animate only transform and opacity,
respect prefers-reduced-motion, and keep the added bundle small.
```

---

## فهرست‌های بلند در React Server Components 🔬

از یک فروشگاه واقعی (دفتر پروژه‌ها): صفحه‌ی فهرست خدمات (بیش از ۲۰۰ کارت با آیکون SVG).
- 🔬 وقتی هر کارت یک کامپوننت سرور بود، هر کارت **دو بار** فرستاده می‌شد: یک بار در HTML و یک بار در داده‌ی RSC که React برای ادامه‌ی کار در مرورگر لازم دارد؛ آیکون‌های SVG کامل هم در هر کارت تکرار می‌شدند.
- 🔬 راه‌حل: یک شبکه‌ی کامپوننت کلاینت که فقط متن‌های کوتاه آماده (نام، قیمت، لینک) می‌گیرد، و **یک اسپرایت SVG** (هر آیکون یک `<symbol>`) که هر کارت با `<use href="#id">` به آن اشاره می‌کند. ✅ طبق MDN، `<use>` گره‌ی ارجاع‌شده را کپی و همان‌جا رسم می‌کند و `href` جای `xlink:href` قدیمی است؛ ✅ CSS به نسخه‌ی کپی‌شده لزوماً ارث نمی‌رسد، پس رنگ را با `currentColor` یا `inherit` بده ([S63](../../../sources/README.md#s63)).
- 🔬 نتیجه (اندازه‌گیری محلی، نه سرور واقعی): حجم صفحه از ۱٫۴۳ به ۰٫۶ مگابایت و توان پاسخ از ۱۰ به ۱۸٫۶ درخواست در ثانیه رسید؛ مقایسه‌ی پیکسلی دو نسخه یکسان بود.
- 🧭 درس: در فهرست بلند، حجم داده‌ی RSC را هم بسنج، نه فقط HTML را.

## آیکون‌ها و Turbopack: هر آیکون یک ماژول 🔬

از یک فروشگاه واقعی (دفتر پروژه‌ها)، Next.js 16.4.0 با Turbopack، ۲۰۲۶-۱۰-۱۷ ([S105](../../../sources/README.md#s105)).
- 🔬 یک فایل `icons.tsx` با حدود ۱۰۰ آیکون Phosphor (هر کدام با وزن ثابت) باعث شد **هر صفحه‌ی عمومی همه‌ی آیکون‌ها را بگیرد**، حتی آیکون‌های پنل مدیریت. علت: Turbopack ماژول خود پروژه را **کامل** نگه می‌دارد؛ export بلااستفاده‌ی یک فایل حذف نمی‌شود. فایل «بشکه» (فقط re-export) هم کمکی نکرد: هر ماژولی که در آن نام برده شده بود وارد شد.
- 🔬 آزموده و بی‌اثر: نوشتن هر آیکون به‌شکل تابع ساده (بدون فراخوانی هنگام بارگذاری)، گزینه‌ی `turbopackRemoveUnusedExports`، و `turbopackChunking.clusters` (حتی نام فایل‌های خروجی عوض نشد).
- 🔬 آزموده و مؤثر ولی کنار گذاشته: `turbopackModuleFragments` (ماژول را تکه می‌کند)؛ ✅ تعریف خود Next آن را «در دست ساخت فعال» می‌نامد، پس برای سایت زنده نه.
- 🔬 **راه‌حل:** یک فایل برای هر آیکون (`icon-set/<Name>.tsx`) و وارد کردن مستقیم از همان فایل در همه‌جا؛ کامپوننت کلاینتی که «آیکون با نام» می‌خواهد، یک نقشه‌ی کوچک فقط با نام‌های خودش بگیرد، نه نقشه‌ی کامل. یک تست نگهبان: هیچ فایلی از فهرست کامل وارد نکند و نقشه‌ی کوچک همان گلیف‌های نقشه‌ی اصلی را داشته باشد.
- 🔬 نتیجه (جاوااسکریپت فشرده‌ی هر صفحه، اندازه‌گیری در مرورگر): صفحه‌ی اصلی ۳۰۲ ← ۲۰۱، صفحه‌ی یک خدمت ۳۲۰ ← ۲۰۵، ابزار ۳۰۰ ← ۱۹۹ کیلوبایت (حدود یک‌سوم کمتر)، بدون تغییر ظاهر.
- 🔬 ابزار: ✅ `next analyze -o` (Next 16.4، فقط Turbopack) فایل تحلیل می‌سازد و `next analyze export --route` آن را JSON Lines می‌دهد. 🔬 فیلتر `--route "/[locale]"` **همه‌ی صفحه‌های زیر آن مسیر** (پنل مدیریت هم) را می‌آورد، پس عدد «یک صفحه» را در مرورگر بسنج. 🔬 تحلیل را روی کپی پروژه اجرا کن (`node_modules` با hard link)، چون در `.next` می‌نویسد.

---

## فاصله‌ی ادعای پست‌ها با واقعیت

- پست @negahui_tech (غربال ۰۶) [Systaliko UI](../../../catalog/systaliko-ui.md) را «پر از کامپوننت‌های متفاوت» معرفی کرد: ✅ درست و رایگان (MIT)، ولی پست نگفته بود که **نسخه‌ی بتای یک‌نفره** با حدود ۳۲ ستاره است. 👀

- پست P10 هشت ابزار را «رایگان» نامیده بود: ✅ فقط Magic UI (نسخه‌ی پایه)، CanvasUI و Epic Easing واقعاً رایگان و قابل استفاده‌اند؛ Lottielab و Jitter و Pryzm خروجی رایگان محدود یا با واترمارک دارند؛ RareUI و OriginKit قابل تأیید نبودند.
- ✅ Pryzm «کتابخانه‌ی کامپوننت» نیست؛ سازنده‌ی پس‌زمینه است.
- ✅ سه سایت (Kinetics، CSS Text Effects، Gradient Buttons) و Circle Loaders از یک شبکه‌ی سازنده‌اند (Colorion، Csaba و Domi Kissi)؛ مجوزشان یکسان نیست.
