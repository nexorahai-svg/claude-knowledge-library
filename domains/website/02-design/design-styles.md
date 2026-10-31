# سبک‌های طراحی وبسایت

> **نوع سند:** مرجع
> **هدف این سند:** انتخاب سبک بصری مناسب برای هر نوع کسب‌وکار، با اجزای اصلی هر سبک و یک جمله‌ی پرامپت آماده.
> **موضوع تحقیق:** الگوهای تکرارشونده در کتابخانه‌های قالب لندینگ‌پیج و نمونه‌های طراحی روز.
> **منابع:** [S01 کتابخانه‌ی قالب](../../../sources/README.md#s01) · [S15 منابع طراحی](../../../sources/README.md#s15) · [S121 Code and Chill](../../../sources/README.md#s121) · [S172 بازطراحی شیشه‌ای روشن](../../../sources/README.md#s172) · [S176 Enkis Web Studio](../../../sources/README.md#s176)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۰
> **دفعه‌ی بعد چک شود:** سبک‌های جدید در گالری‌های الهام ([منابع طراحی](../06-resources/design-resources.md))؛ آیا سبکی از مد افتاده یا سبک تازه‌ای رایج شده؟

---

## روش استخراج

این سبک‌ها از تحلیل یک کتابخانه‌ی قالب لندینگ‌پیج استخراج شده‌اند ([S01](../../../sources/README.md#s01): ۸۱۳ قالب ادعاشده؛ ۵۸۹ قالب با متن کامل تحلیل شد). فقط الگوها شمرده و خلاصه شدند و هیچ متنی کپی نشد. «رایج» در این سند یعنی «رایج در همان کتابخانه»، نه در کل وب. 🧭

---

## ۱. سینمایی تیره (Cinematic Dark)
**رایج‌ترین سبک در کتابخانه‌ی بررسی‌شده.** مناسب: تکنولوژی، هوش مصنوعی، خودرو، برندهای لوکس، استارتاپ.
- پس‌زمینه‌ی تقریباً سیاه (نه سیاه خالص؛ مثلاً `#0a0a0b`)
- ویدیوی تمام‌صفحه پشت هیرو، کمی تیره‌شده با لایه‌ی گرادیانت تا متن خوانا بماند
- تیتر خیلی بزرگ (۷۲ تا ۱۴۴ پیکسل در دسکتاپ) با فاصله‌ی حروف کم
- یک رنگ تأکیدی تند (نارنجی، قرمز، فیروزه‌ای) فقط برای دکمه و کلمه‌ی کلیدی

```text
Style: cinematic dark. Near-black background, full-bleed muted background video in the
hero with a dark gradient overlay for legibility, oversized tight headline, one vivid
accent color used only for the CTA and one key word.
```

## ۲. شیشه‌ای (Glassmorphism / Liquid Glass)
مناسب: اپ، فین‌تک، SaaS، محصولات دیجیتال.
- کارت‌های نیمه‌شفاف با `backdrop-filter: blur()` روی پس‌زمینه‌ی رنگی یا ویدیو
- حاشیه‌ی ۱ پیکسلی روشن و کم‌رنگ دور کارت‌ها
- **هشدار:** روی پس‌زمینه‌ی ساده جلوه ندارد. حتماً پشتش گرادیانت، تصویر یا حرکت باشد.

```text
Style: frosted glass. Translucent cards with backdrop blur over a rich animated gradient,
1px light borders at low opacity, soft inner highlights. Keep text contrast WCAG AA.
```

**نمونه‌ی واقعی: داشبورد شیشه‌ای Code and Chill** ✅ ([کارت](../../../catalog/code-and-chill.md)، [S121](../../../sources/README.md#s121)). دستور ساختش، از کد عمومی دموی Tavola و به زبان خودمان:
- **پس‌زمینه:** سرمه‌ای خیلی تیره، با چهار لکه‌ی نور بزرگ و محو (`radial-gradient` با `closest-side`) در لایه‌ی پشت. شیشه بدون این لکه‌ها جلوه ندارد.
- **شیشه:** گرادیانت مورب نیمه‌شفاف سفید، روشن‌تر در گوشه‌ها و کم‌رنگ در وسط، به‌همراه `backdrop-filter: blur(~26px) saturate(~165%)`. اشباع رنگ پشت شیشه را زنده نگه می‌دارد. همه در متغیرهای CSS تعریف شده تا تم روشن فقط مقدارها را عوض کند.
- **رنگ:** یک رنگ گرم تأکیدی (مرجانی یا نارنجی) برای عدد اصلی و دکمه. رنگ وضعیت‌ها (سبز، کهربایی) با `color-mix` به نسخه‌ی پاستلی و کم‌رنگ می‌رسد، مثل کارت‌های کرم، صورتی و نعنایی تخته‌ی آشپزخانه.
- **حرف:** یک فونت گرد هندسی با وزن متغیر (Urbanist، OFL). عددهای بزرگ و پررنگ، برچسب‌های کوچک.
- **حرکت:** یک منحنی ease برای همه (`cubic-bezier(.2,.8,.2,1)`)؛ ورود بخش‌ها با GSAP؛ خط نمودار SVG که کشیده می‌شود؛ کارت‌ها با pointer کشیده می‌شوند. وقتی کاربر «حرکت کمتر» خواسته، حرکت خاموش است.
- **ساختار:** نوار ناوبری قرصی با برگه‌ها، کارت عدد بزرگ، تخته‌ی کانبان، نقشه‌ی میزها، نمودار پراکندگی. هر صفحه یک کار روشن دارد.
- **تم:** یک اسکریپت کوچک پیش از اولین نقاشی صفحه، تم ذخیره‌شده را می‌گذارد تا رنگ اشتباه یک لحظه هم دیده نشود.

```text
Build an operations dashboard in plain TypeScript + Vite (no framework), frosted-glass style:
very dark navy background with 3-4 large blurred radial light blobs behind the content;
glass panels = diagonal translucent white gradient + backdrop-filter blur(24-28px) saturate(160%);
all colours and glass values as CSS variables with a light theme override; one warm accent
colour for key numbers and actions; status colours softened with color-mix into pastel cards;
a rounded geometric variable font; one shared easing curve; GSAP entrance animations; charts as
hand-built SVG; drag with pointer events; respect prefers-reduced-motion; set the saved theme
before first paint. Use our own brand, data and copy. Show me one screen before the rest.
```

### شیشه روی پس‌زمینه‌ی روشن (کرم، سفید) 🔬
دستور بالا (و داشبورد Code & Chill) برای پس‌زمینه‌ی تیره با لکه‌های نور است؛ روی پس‌زمینه‌ی روشن یکدست، شیشه تقریباً دیده نمی‌شود. در یک پروژه‌ی واقعی این نسخه جواب داد:
- ته‌رنگ گرم نیمه‌شفاف (نه سفید خالص)، لبه‌ی ۱ پیکسلی روشن، سایه‌ی لایه‌ای نرم؛ حس عمق از سایه و لبه می‌آید، نه از blur.
- `backdrop-filter` فقط روی لایه‌های شناور (هدر، منو، کارت روی تصویر)، نه همه‌ی کارت‌ها.
- **شیشه‌ی تو در تو کار نمی‌کند:** لایه‌ی blur داخل هدرِ blurشده فقط والدش را تار می‌کند، نه صفحه را؛ منوی کشویی داخل هدر شیشه‌ای باید پرِ تقریباً مات بگیرد.
- جایگزین مات برای `prefers-reduced-transparency` و مرورگر بدون پشتیبانی.

### شیشه‌ای خالص: همه‌ی سطح‌ها شیشه 🔬
(روش اندازه‌گیری کنتراست روی شیشه‌ی تار: [بررسی خودکار](../../claude-code/verification.md#ممیزی-کنتراست-واکنشگرایی-و-دامهای-playwright-).)
وقتی کل سایت (هدر، منو، کارت، حباب، دکمه، فیلد، پانویس، پنجره) باید شیشه باشد، روی موبایل و کامپیوتر یکسان. در یک پروژه‌ی سایت ساخته و آزموده شد (پروژه‌ها، ۲۰۲۶-۱۰-۲۶).
- **صحنه‌ی پشت:** یک لایه‌ی `position: fixed; z-index: -1` با ۴ لکه‌ی نور بزرگ و محو (حدود `60vmax`، `radial-gradient(closest-side, رنگ, transparent)`) به رنگ‌های برند که آهسته (۲۰ تا ۳۴ ثانیه) جابه‌جا می‌شوند. در تم روشن لکه‌ها پررنگ‌تر، وگرنه شیشه دیده نمی‌شود. عکس‌های واقعی هم جزو صحنه‌اند.
- **یک کلاس برای همه، تاری روی `::before`:** 🔬 `backdrop-filter` روی خود کادر، آن را «ریشه‌ی پس‌زمینه» می‌کند و کادر داخلی فقط والدش را تار می‌کند. تاری را روی `::before` (با `z-index: -1` و `isolation: isolate` روی کادر) بگذار تا شیشه‌ی تو در تو هم درست کار کند. مقدار شروع: `blur(28px) saturate(180%)`.
- **لبه‌ی درخشان:** `::after` با `padding: 1px` و ماسک `content-box` / `exclude` و گرادیانت ۱۵۵ درجه (گوشه‌ی بالا روشن، وسط کم‌رنگ، پایین رنگ برند).
- **سایه‌ی لایه‌ای:** خط نور داخلی بالا، خط تیره‌ی داخلی پایین، سایه‌ی نزدیک، میانی و یک سایه‌ی دور به رنگ برند.
- **سه غلظت برای عمق:** پنل‌های دور `blur` بیشتر (حدود ۴۰)، کارت‌ها ۲۸، دکمه و حباب و منو ۱۸ با `saturate` بیشتر.
- **برق سطح:** لایه‌ی `radial-gradient` روشن با `mix-blend-mode: soft-light` که موقعیتش از `pointermove` می‌آید (لمس هم کار می‌کند). دانه‌ی نویز حدود ۴ درصد نوار شدن گرادیانت را می‌گیرد 🧭.
- **حرکت:** یک منحنی (`cubic-bezier(.2,.8,.2,1)`)، ورود پلکانی با `opacity` و `translateY`، باز شدن بادبزنی کارت‌ها، عمق میدان در فهرست (مورد فعال واضح، بقیه `blur(3px)` و کم‌رنگ، با IntersectionObserver)، parallax. همه زیر `prefers-reduced-motion` خاموش.
- **شکست نور (Liquid Glass) با فیلتر SVG در `backdrop-filter: url(#…)`:** ❓ فقط Chromium؛ در پروژه کنار گذاشته شد.
- **حذف‌نشدنی‌ها:** 🔬 کنتراست متن روی شیشه با آزمون پیکسل واقعی در هر زبان، هر تم، گوشی و کامپیوتر (AA قبول شد)؛ جایگزین مات با `@supports not (backdrop-filter: blur(1px))` و `prefers-reduced-transparency`؛ بدون ایتالیک در فارسی و عربی (تأکید با رنگ و وزن).
- **آزمون:** WebKit بی‌صفحه‌ی لینوکس تاری نمی‌کشد ([verification](../../claude-code/verification.md))؛ در Astro لایه‌ی تم سراسری پیشوند قوی‌تر لازم دارد ([کارت Astro](../../../catalog/astro.md)).

```text
Make every surface of the site glass (header, menu, cards, bubbles, buttons, fields, footer, dialogs), same on
mobile and desktop, keeping our own colours and current fonts. Fixed scene layer behind everything: 4 large blurred
radial blobs in brand colours drifting slowly; stronger blobs in the light theme. One .glass class: put
backdrop-filter blur(28px) saturate(180%) on ::before (z-index -1, element isolation:isolate) so nested glass works;
1px gradient rim on ::after via mask exclude; layered shadows (inner top highlight, near, mid, far brand-tinted).
Three depths (far 40px, mid 28px, near 18px + more saturation). Pointer-driven soft-light shine. One easing curve,
staggered entrances, fan-in cards, depth-of-field lists. Text must pass WCAG AA on glass in every theme and language
(check real pixels); matte fallback for no backdrop-filter and reduced transparency; no italic in Arabic script;
motion off under prefers-reduced-motion. Build one demo page first and show it before the rest.
```

## ۳. ادیتوریال لوکس (Luxury Editorial)
مناسب: معماری، املاک، هتل، جواهر، مد، رستوران، برندهای گران.
- ترکیب فونت سریف شیک برای تیتر و فونت ساده برای متن ([تایپوگرافی](typography.md))
- فضای خالی زیاد؛ چیدمان شبیه مجله
- عکس‌های بزرگ با کادربندی سینمایی
- رنگ‌های خنثی: کرم، سنگی، مشکی، با یک رنگ گرم

```text
Style: luxury editorial. Elegant serif display headings with a clean sans for body,
generous whitespace, magazine-like asymmetric grid, large cinematic photography,
neutral palette (cream, stone, ink) with one warm accent.
```

## ۴. سه‌بعدی و تعاملی (3D / WebGL)
مناسب: محصول فیزیکی، معماری، تکنولوژی، هر جا که «تجربه» مهم‌تر از «اطلاعات» است.
- ذرات، شیدر، اشیای معلق، پس‌زمینه‌ای که به موس واکنش نشان می‌دهد
- جزئیات و پرامپت‌ها: [سه‌بعدی و WebGL](../03-motion-3d/3d-webgl.md)

## ۵. ایزومتریک توضیحی (Isometric Explainer)
مناسب: توضیح «یک محصول چطور کار می‌کند»، صنعت، مهندسی، نرم‌افزار.
- ✅ از روش Anatomy ([S17](../../../sources/README.md#s17)): به‌جای نمودار جعبه و فلش، یک «ماشین» واقعی که کارکردش همان مفهوم است
- دوربین ایزومتریک ثابت (۳۰ درجه از گوشه)، بدون پرسپکتیو
- چهار سایه‌ی رنگ بر اساس جهت نور، فقط **یک** قطعه‌ی رنگی برای جلب توجه
- هیچ متنی روی خود تصویر نیست؛ توضیح‌ها دور آن
- جزئیات: [سه‌بعدی و WebGL](../03-motion-3d/3d-webgl.md#مطالعهی-موردی-۲-anatomy-ماشینی-که-ایده-را-توضیح-میدهد)

## ۶. بنتو گرید (Bento Grid)
مناسب: معرفی ویژگی‌های محصول، خدمات چندگانه، داشبورد.
- کاشی‌های با اندازه‌های مختلف (یک بزرگ، چند کوچک) شبیه جعبه‌ی غذای ژاپنی
- هر کاشی یک ویژگی با یک تصویر کوچک یا انیمیشن کوتاه

```text
Features section as a bento grid: one large tile and 4–5 smaller tiles of varied sizes,
each with a short title, one line of copy, and a small looping visual. Collapses to a
single column on mobile.
```

## ۷. معماری و نقشه‌ی فنی (Architectural / Blueprint)
مناسب: معماری، ساختمان‌سازی، مهندسی، صنعت، تولید.
- خطوط راهنما، شماره‌گذاری بخش‌ها (۰۱ / ۰۷)، مُهر نقشه (شماره‌ی برگه، مقیاس)
- فونت مونو برای برچسب‌ها و اعداد
- کاغذ روشن با جوهر مشکی، یا برعکس (بلوپرینت آبی)
- نمونه‌ی برجسته: Casa Serra ([S02](../../../sources/README.md#s02))

```text
Style: architectural drawing. Paper-white background with black ink lines, visible
grid and dimension lines, section numbering like "01 / 07", a title block with sheet
number and scale, monospace labels for numbers and captions.
```

## ۸. کنتراست بالا و جسورانه (Bold / Brutalist)
مناسب: آژانس خلاق، برند جوان، رویداد، موسیقی.
- تایپوگرافی عظیم، رنگ‌های تخت و تند، حاشیه‌های ضخیم
- عمداً «زمخت» ولی دقیق

---

## ۹. روایت اسکرولی محصول (Scroll-driven Product Story) ⭐ 🧭
مناسب: برند محصول لوکس یا خوراکی (عطر، قهوه، شکلات، نوشیدنی، جواهر)، صفحه‌ی فرود و صفحه‌ی اصلی فروشگاه. نمونه‌ی کامل این سبک: کارهای استودیو Enkis ([S176](../../../sources/README.md#s176)).
- **محصول قهرمان است و با اسکرول «تبدیل» می‌شود:** هر بخش یک مرحله از داستان محصول؛ مثلاً قطره‌ی طلایی ← نوار مایع پیچان با دانه‌های قهوه ← ریختن در فنجان؛ یا چنگال با اسپاگتی ← رشته‌ها در هوا ← بشقاب.
- **بخش‌های شماره‌دار و نام‌دار:** «۰۱ — قطره‌ی طلایی»، «۰۲ — تبدیل»، «۰۳ — ریختن کامل»؛ نشانگر پیشرفت کنار صفحه.
- **تیتر سریف بسیار درشت و ادیتوریال** پشت یا جلوی محصول (محصول روی حروف می‌افتد، عمق می‌دهد)؛ یک جمله‌ی کوتاه و یک دکمه‌ی گرد.
- **پالت:** کرم و قهوه‌ای اسپرسو، یا یک رنگ برند پررنگ (زرشکی، سبز تیره) با کرم؛ عکس محصول فوق‌واقع‌گرا روی زمینه‌ی ساده؛ ناوبری مینیمال، دکمه‌ی گفتگوی شناور.
- **ساخت:** هر تبدیل یک کلیپ کوتاه ویدیوی هوش مصنوعی با «فریم اول و آخر» (مثلاً Veo، Kling یا Seedance در [مدل‌های ویدیو](../../social-media/ai-video-models.md))؛ فریم آخر هر کلیپ = فریم اول کلیپ بعد تا دوخت دیده نشود. پخش وابسته به اسکرول با GSAP ScrollTrigger: یا دنباله‌ی تصویر روی canvas (کنترل دقیق، WebP/AVIF)، یا `video.currentTime` روی ویدیوی بدون فریم کلیدی دور (هر فریم keyframe، `-g 1` در FFmpeg). متن و دکمه HTML واقعی روی آن (سئو و چندزبانه؛ متن فارسی هرگز داخل ویدیو).
- **موبایل:** دنباله‌ی کوتاه‌تر و کم‌حجم‌تر، بارگذاری تنبل بخش به بخش، پوستر ثابت برای شبکه‌ی کند و `prefers-reduced-motion`؛ اولین بخش بدون انتظار دیده شود (LCP). یافته‌های سرعت در [چک‌لیست انتشار](../07-quality/launch-checklist.md).
- **نسخه‌ی فروشگاه عطر:** ۰۱ قطره‌ی عطر در نور ← ۰۲ قطره به بطری تبدیل می‌شود ← ۰۳ هرم نت‌ها (گل‌ها، چوب، ادویه) دور بطری پخش می‌شوند ← ۰۴ بطری روی سکوی لوکس با دکمه‌ی خرید. رنگ برند (مثلاً مشکی و زرشکی) زمینه‌ی بخش‌ها.
- ⚠️ اصول را بگیر، نه طرح و دارایی‌شان را؛ ویدیوها را از محصول واقعی مشتری یا با مدل ویدیو بساز.

## جدول انتخاب سریع 🧭

| نوع کسب‌وکار | سبک اول | سبک مکمل |
|---|---|---|
| معماری، ساختمان، نما | نقشه‌ی فنی | ادیتوریال لوکس، سه‌بعدی |
| املاک و هتل | ادیتوریال لوکس | سینمایی تیره |
| صنعت و تولید | ایزومتریک توضیحی | نقشه‌ی فنی |
| نرم‌افزار و SaaS | بنتو گرید | شیشه‌ای |
| هوش مصنوعی و تکنولوژی | سینمایی تیره | سه‌بعدی |
| آژانس خلاق | جسورانه | سینمایی تیره |
| مد و جواهر | ادیتوریال لوکس | — |

## اصول از دو نمونه‌ی تازه‌ی Awwwards (۲۰۲۶-۱۰-۲۸، فقط اصول، کپی ممنوع) ✅
**Forge Automotive** (۲۰۲۶-۱۰-۲۵، https://www.awwwards.com/sites/forge-automotive):
- پالت دورنگ سیاه و زرشکی.
- مقدمه‌ای که با اسکرول جلو می‌رود.
- منو با clip-path.
- صفحه‌ی ۴۰۴ با WebGL.

**ESR Bespoke** (۲۰۲۶-۱۰-۲۳، https://www.awwwards.com/sites/esr-bespoke):
- سیاه‌وسفید خالص با عکس بزرگ.
- فوتری که خودش عنصر طراحی است.
- نمره‌ی دسترس‌پذیری‌اش فقط ۶٫۴ است.

اصول قابل‌استفاده: پالت لوکس دورنگ، مقدمه‌ی کوتاه، ۴۰۴ با هویت برند، و فوتر به‌عنوان بخشی از طرح ([فوتر](../../../catalog/footer-design.md)، [۴۰۴](../../../catalog/404s-design.md)). ⚠️ دسترس‌پذیری را از این برنده‌ها یاد نگیر. منبع: [S191](../../../sources/README.md#s191).
