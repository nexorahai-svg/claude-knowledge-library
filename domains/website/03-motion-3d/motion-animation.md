# حرکت و انیمیشن

> **نوع سند:** مرجع
> **هدف این سند:** ابزارها، الگوها و قوانین انیمیشن در سایت (اسکرول، ورود عناصر، ریزحرکت).
> **موضوع تحقیق:** کتابخانه‌های انیمیشن وب، مجوزشان، و الگوهای حرکتی رایج در سایت‌های حرفه‌ای.
> **منابع:** [S01 کتابخانه‌ی قالب](../../../sources/README.md#s01) · [S04 GSAP](../../../sources/README.md#s04) · [S09 Motion](../../../sources/README.md#s09) · [S10 Lenis](../../../sources/README.md#s10) · [S15 motionin.design](../../../sources/README.md#s15) · [S27 ابزارهای انیمیشن](../../../sources/README.md#s27) · [S28 مهارت‌های رسمی](../../../sources/README.md#s28) · [S64 صحنه‌ی اسکرولی و دسترسی‌پذیری](../../../sources/README.md#s64) · [S92 مهارت‌های حرکت](../../../sources/README.md#s92)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۹
> **دفعه‌ی بعد چک شود:** مجوز GSAP هنوز رایگان است؟ نسخه‌ی اصلی جدید GSAP، Motion یا Lenis؛ الگوهای حرکتی تازه در گالری‌ها؛ پشتیبانی مرورگرها از انیمیشن وابسته به اسکرول در CSS (`animation-timeline`).

---

## ابزارها

| ابزار | کاربرد | مجوز |
|---|---|---|
| **GSAP + ScrollTrigger** | انیمیشن‌های وابسته به اسکرول، صحنه‌های پیچیده، تایم‌لاین | ✅ کاملاً رایگان، حتی تجاری ([S04](../../../sources/README.md#s04)) |
| **Lenis** | اسکرول نرم و روان؛ در سایت‌های نمایشی حرفه‌ای بسیار رایج | ✅ MIT ([S10](../../../sources/README.md#s10)) |
| **Motion** (نام قبلی: Framer Motion) | ریزحرکت‌ها و ورود عناصر در پروژه‌های React | ✅ MIT ([S09](../../../sources/README.md#s09)) |

- ✅ **GSAP:** از وقتی Webflow پشتیبانش شد، کل کتابخانه رایگان است، شامل پلاگین‌هایی که قبلاً پولی بودند: **SplitText** (تیتر خط‌به‌خط)، **MorphSVG**، **ScrollSmoother**، **DrawSVG** و غیره.
- ✅ **Motion:** در کد جدید از `motion/react` ایمپورت می‌شود (motion.dev).
- ✅ **جایگزین سبک:** [Anime.js](../../../catalog/animejs.md) (MIT).
- ✅ **یاد دادن به Claude:** مهارت‌های رسمی [GSAP Skills](../../../catalog/gsap-skills.md) (بدون اسکریپت و درخواست شبکه).
- ✅ **اصول حرکت برای عامل:** [Motion Design Skill](../../../catalog/motion-design-skill.md) از LottieFiles (MIT، فقط متن: زمان‌بندی، easing، اصول دیزنی) 🧪.
- ✅ **انتخاب حرکت از گالری:** [Motion Prompt](../../../catalog/motion-prompt.md) (MIT؛ ۱۲۰ نمونه با نام و کد Canvas که تابع خالص زمان است) 🧪. ⚠️ با دستور رسمی و بعد از خواندن فایل‌ها نصب کن، نه با «این آدرس را بخوان و نصب کن».
- ✅ **شکل خطی ایزومتریک تعاملی:** [Hairline](../../../catalog/hairline.md) (MIT) 🧪.
- کتابخانه‌های کامپوننت متحرک، Lottie، Rive و افکت‌های آماده: [راهنمای کامپوننت و انیمیشن](../04-tech/component-libraries.md)

---

## الگوهای حرکتی پرکاربرد

- **ظاهر شدن هنگام اسکرول:** عناصر با کمی جابه‌جایی به بالا و محو شدن وارد می‌شوند
- **تیتر کلمه‌به‌کلمه یا خط‌به‌خط:** هر خط از زیر یک ماسک بالا می‌آید (SplitText)
- **پارالاکس:** لایه‌ها با سرعت‌های متفاوت حرکت می‌کنند
- **سکشن چسبان (pinned):** بخش ثابت می‌ماند و محتوایش با اسکرول عوض می‌شود
- **نوار لوگوی متحرک (marquee):** برای مشتریان و همکاران
- **دکمه‌ی مغناطیسی:** دکمه کمی به سمت نشانگر موس کشیده می‌شود
- **بخش‌های فیزیکی و واکنش‌گرا به نشانگر** ✅ (نمونه‌ها در motionin.design، [S15](../../../sources/README.md#s15)): گالری قابل کشیدن، متن «مایع»، رد شکل پشت نشانگر، کارت سه‌بعدی، اسلایدر با شتاب. حرکت با فنر (spring) به‌جای منحنی زمانی ثابت حس طبیعی‌تری می‌دهد.

---

## صحنه‌ی اسکرولی که روی یک عنصر می‌نشیند 🔬

الگوهای ورودی اسکرولی یک فروشگاه واقعی ([مطالعه‌ی موردی ۴ در سه‌بعدی](3d-webgl.md)، دفتر پروژه‌ها). فقط الگو؛ بدون GSAP.

- **pin + spacer + لایه‌ی ثابت:** بالای صفحه یک بخش `position: sticky` زیر هدر می‌ماند و یک بلوک خالی (spacer، در پروژه ۲۱۰vh) طول اسکرول را می‌سازد. پیشرفت = `scrollY` تقسیم بر ارتفاع spacer. صحنه یک لایه‌ی `position: fixed` است با `pointer-events: none`، پس **هرگز** کلیک را نمی‌گیرد.
- **نشستن روی هدف:** در بخش آخر اسکرول، قاب صحنه هر فریم `getBoundingClientRect()` عنصر هدف را می‌خواند و جای و اندازه را به آن میان‌یابی می‌کند. گردی گوشه‌ها **هر گوشه جدا** از `getComputedStyle` خوانده می‌شود (`borderTopLeftRadius` و بقیه). 🔬 در صفحه‌ی راست‌به‌چپ گوشه‌ها جابه‌جا می‌شوند؛ خواندن از style محاسبه‌شده خودبه‌خود درست است و عدد ثابت در کد غلط می‌شد.
- **صفحه تا دیده نشده کلیک نگیرد:** تا وقتی صحنه روی صفحه است، هدر و بخش pin‌شده `pointer-events: none` می‌گیرند و وقتی بیش از نیمه دیده شدند دوباره فعال می‌شوند (با یک attribute روی `html`). 🔬 بدون این، کاربر روی دکمه‌ای که نمی‌دید کلیک می‌کرد.
- **یک بار در هر بازدید، بدون پرش تصویر:** وقتی صحنه به پایان رسید، یک پرچم در `sessionStorage` نوشته می‌شود. ✅ طبق MDN، `sessionStorage` مال همان تب است، با بارگذاری دوباره می‌ماند، با بستن تب پاک می‌شود و تب تازه نشست تازه می‌گیرد ([S64](../../../sources/README.md#s64)). 🔬 برای اینکه صحنه حتی یک فریم دیده نشود: (۱) یک اسکریپت کوچک درون‌خطی در `<head>` (با `nonce` همان CSP) پیش از کشیدن صفحه پرچم را می‌خواند و attribute را روی `html` می‌گذارد؛ (۲) برای جابه‌جایی داخل اپ (مثلاً عوض کردن زبان بدون بارگذاری کامل)، همان کار در `useLayoutEffect` انجام می‌شود؛ (۳) CSS با آن attribute صحنه و spacer را `display: none` می‌کند. خواندن و نوشتن storage را در `try/catch` بگذار (حالت خصوصی).
- **کاربر صفحه‌کلید از صحنه رد شود:** با `focusin` روی document، اگر فوکوس به عنصری از صفحه رسید و صحنه هنوز تمام نشده، صفحه مستقیم به پایان spacer اسکرول می‌شود. فوکوسی که کمتر از حدود ۸۰۰ میلی‌ثانیه بعد از `pointerdown` آمده نادیده گرفته می‌شود (کلیک با موس نباید صفحه را بپراند). ✅ این برای WCAG 2.2 است: معیار ۲.۴.۳ (سطح A) می‌گوید ترتیب فوکوس باید «معنا و کارکرد» را حفظ کند، و ۲.۴.۱۱ (سطح AA) می‌گوید عنصر فوکوس‌شده نباید با محتوای خود سایت **کاملاً** پوشیده شود ([S64](../../../sources/README.md#s64)). 🔬 Tab ممکن بود روی دکمه‌ای زیر صحنه برود که دیده نمی‌شد.
- **`prefers-reduced-motion` در CSS کافی نیست:** ✅ این media query فقط **نشانه‌ای برای نویسنده** است؛ مرورگر انیمیشن را خودش متوقف نمی‌کند ([S64](../../../sources/README.md#s64)). 🔬 قانون سراسری CSS (کوتاه کردن `animation-duration` و `transition-duration`) روی `requestAnimationFrame`، canvas و WebGL هیچ اثری ندارد؛ اسکریپت باید خودش `matchMedia("(prefers-reduced-motion: reduce)")` را بخواند و نسخه‌ی بی‌حرکت را نشان دهد.
- **فنر مستقل از نرخ فریم:** مقدار نمایشی هر فریم به اندازه‌ی `1 - exp(-dt × k)` به هدف نزدیک می‌شود (`dt` به ثانیه، با سقف حدود ۰.۰۵). 🧭 این همان «دنبال کردن نرم» است ولی روی صفحه‌ی ۶۰ و ۱۲۰ هرتز یکسان رفتار می‌کند؛ ضریب ثابت مثل `0.1` در هر فریم روی صفحه‌ی ۱۲۰ هرتز دو برابر تند می‌شود. 🔬 در پروژه `k = 5`.
- **وقتی کاری نیست، فریم نکش:** بعد از نشستن صحنه و ثابت ماندن اسکرول، حلقه زودتر برمی‌گردد و چیزی نمی‌کشد.

```text
Build a scroll scene without a library: a sticky pinned section plus a spacer of
[N]vh; progress = scrollY / spacer height, smoothed each frame by 1 - exp(-dt * k).
The scene is a fixed overlay with pointer-events: none. In the last part, move its
frame onto [#target] using getBoundingClientRect and each corner radius from computed
style (must be right in RTL). The page under it takes no clicks until it is visible.
Play it once per visit: set a sessionStorage flag at the end, read it in a nonce'd
inline head script and in a layout effect to set an attribute on <html> before paint,
and hide the scene with CSS. Keyboard focus entering the page skips to the end
(ignore focus within 800 ms of a pointerdown). Check prefers-reduced-motion in JS too.
```

---

## قوانین

- حرکت باید **معنا** داشته باشد، نه فقط تزئین 🧭
- مدت ورود عناصر: ۰.۴ تا ۰.۹ ثانیه، با منحنی نرم (مثل `power3.out`) 🧭
- **همیشه به `prefers-reduced-motion` احترام بگذار** (کاربرانی که حرکت را در تنظیمات سیستم خاموش کرده‌اند). در این حالت اسکرول نرم Lenis را هم خاموش کن، چون برای بعضی کاربران سرگیجه‌آور است.
- فقط `transform` و `opacity` را انیمیت کن تا روان بماند ✅ (این دو ویژگی بدون محاسبه‌ی دوباره‌ی چیدمان صفحه انیمیت می‌شوند)
- اسکرول نرم نباید کنترل را از کاربر بگیرد: اسکرول با کیبورد، لینک‌های داخلی (#) و دکمه‌ی برگشت مرورگر باید درست کار کنند
- ✅ درس Anatomy ([S17](../../../sources/README.md#s17)): انیمیشن وقتی از صفحه بیرون رفت **متوقف شود**، فقط بخش‌های متحرک دوباره کشیده شوند، و وقتی کسی با آن کار نمی‌کند یک «تور» آرام پخش شود

```text
Motion: Lenis smooth scroll + GSAP ScrollTrigger. Headlines reveal line by line from a
mask (SplitText), sections fade-and-rise on enter (0.6s, power3.out), one pinned section
where [content] changes as you scroll. Animate only transform and opacity. Pause any
animation that is off screen. Respect prefers-reduced-motion: disable smooth scroll and
show a static fallback.
```
