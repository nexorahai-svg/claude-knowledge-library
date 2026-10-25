# سبک‌های طراحی وبسایت

> **نوع سند:** مرجع
> **هدف این سند:** انتخاب سبک بصری مناسب برای هر نوع کسب‌وکار، با اجزای اصلی هر سبک و یک جمله‌ی پرامپت آماده.
> **موضوع تحقیق:** الگوهای تکرارشونده در کتابخانه‌های قالب لندینگ‌پیج و نمونه‌های طراحی روز.
> **منابع:** [S01 کتابخانه‌ی قالب](../../../sources/README.md#s01) · [S15 منابع طراحی](../../../sources/README.md#s15) · [S121 Code and Chill](../../../sources/README.md#s121)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۹
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
