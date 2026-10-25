# کتابخانه‌ی پرامپت

> **نوع سند:** مرجع
> **هدف این سند:** همه‌ی پرامپت‌های آماده در یک جا: پرامپت‌های عمومی بخش‌های سایت اینجا، و فهرست پرامپت‌های تخصصی که در سندهای موضوعی هستند.
> **موضوع تحقیق:** پرامپت‌هایی که در عمل نتیجه‌ی خوب داده‌اند.
> **منابع:** همه‌ی منابع؛ پرامپت‌ها نوشته‌ی خودمان هستند (🧭 بر اساس تجربه، نه قاعده‌ی رسمی).
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۶
> **دفعه‌ی بعد چک شود:** پرامپتی که در یک پروژه‌ی واقعی خوب جواب داد یا بد جواب داد، اینجا اصلاح شود.
>
> پرامپت‌ها انگلیسی‌اند چون ابزارهای کدنویسی با آن دقیق‌تر کار می‌کنند. قسمت‌های `[براکت]` را با اطلاعات پروژه عوض کن.

---

## فهرست پرامپت‌های تخصصی (در سندهای موضوعی)

| پرامپت | کجا |
|---|---|
| شروع هر پروژه | [روش کار](../01-method/claude-workflow.md#پرامپت-شروع-هر-پروژه) |
| بررسی و نمره‌دهی | [روش کار](../01-method/claude-workflow.md#پرامپت-بررسی-و-نمرهدهی) |
| راه‌اندازی Git | [Vibe Coding](../01-method/vibe-coding.md#git-دکمهی-برگشت-تو) |
| بررسی امنیت | [Vibe Coding](../01-method/vibe-coding.md#امنیت) |
| هر سبک طراحی | [سبک‌ها](../02-design/design-styles.md) |
| تایپوگرافی | [تایپوگرافی](../02-design/typography.md) |
| پس‌زمینه‌ی گرادیانت | [رنگ و بافت](../02-design/color-and-texture.md) |
| سایت فارسی | [فارسی و RTL](../02-design/persian-rtl.md) |
| انیمیشن و اسکرول | [حرکت](../03-motion-3d/motion-animation.md) |
| «نقشه به واقعیت» سه‌بعدی | [سه‌بعدی](../03-motion-3d/3d-webgl.md#پرامپت-صفحهی-اسکرولی-نقشه-به-واقعیت) |
| تصویر توضیحی Anatomy | [سه‌بعدی](../03-motion-3d/3d-webgl.md#مطالعهی-موردی-۲-anatomy-ماشینی-که-ایده-را-توضیح-میدهد) |
| جستجوی صدا در Openverse | [کتابخانه‌ی صدا](../../social-media/sound-library.md#پرامپت-برای-claude) |
| بررسی قبل از انتشار | [چک‌لیست](../07-quality/launch-checklist.md) |

---

## پرامپت‌های عمومی بخش‌ها

### هیرو
```text
Build the hero section only. Headline: "[headline]". Subline: "[one sentence]".
Primary CTA: "[button text]". Visual: [video / 3D scene / photo / gradient].
Style: [style from design-styles.md]. Fonts: [pairing]. Must look excellent at 390px
and 1440px. Show me a screenshot of both before moving on.
```

### بخش خدمات / ویژگی‌ها
```text
Build the [services / features] section as [bento grid / pinned scroll section / cards].
Items: [list]. Each item: short title, one line of copy, [icon / small looping visual].
Match the existing hero style exactly.
```

### نمونه‌کارها
```text
Build a projects section: [number] projects, each with a large image, name, location,
and year. Hover reveals [detail]. Clicking opens [a detail page / a modal]. Images
lazy-load. Layout: [asymmetric editorial grid / horizontal scroll].
```

### CTA پایانی و فوتر
```text
Build the final CTA band and footer. CTA: big headline "[text]" with one button on a
distinct background [gradient / video / dark]. Footer: logo, contact details, address
with a map link, social links, copyright. Keep it calm and well spaced.
```

### اصلاح دقیق
```text
In the [section name] section: [exact problem, e.g. "the headline wraps into 4 lines on
mobile", "the spacing between cards is uneven"]. Fix only this, do not change anything
else, and show me before/after screenshots.
```

### استفاده از این کتاب راهنما در یک پروژه‌ی جدید
```text
Before starting, read ~/Desktop/knowledge-library/README.md and the documents
it points to that are relevant to this project. Follow its rules: we never copy other
people's designs, prompts or code; use only assets with a clear license; build in
checkpoints and wait for my approval at each one.
```
