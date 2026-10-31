---
name: Motion (Framer Motion)
slug: motion
category: animation
domains: [website]
verdict: adopt
status: researched
summary: انیمیشن و ریزحرکت در React؛ نام قبلی Framer Motion
use_when: "animating React or Next.js UI (entrances, hover, layout animation)"
how: "npm install motion and import from motion/react (renamed from Framer Motion, MIT, v14.9.0 checked on 2026-10-31); read the repo CHANGELOG before upgrading; official agent kit is Motion AI Kit"
url: https://motion.dev/
repo: "https://github.com/motiondivision/motion"
license: "MIT"
pricing: free
risk: low
sources: [S09, S208]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Motion (Framer Motion)

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) npm latest: 14.9.0 (۲۰۲۶-۱۰-۳۰، CHANGELOG مخزن): بهبود دسترسی صفحه‌کلید در Reorder و گزینه‌های داخلی؛ breaking ندارد: https://raw.githubusercontent.com/motiondivision/motion/main/CHANGELOG.md
✅ کتابخانه‌ی انیمیشن React. نامش از Framer Motion به Motion تغییر کرده و در کد جدید از `motion/react` ایمپورت می‌شود.
✅ نسخه‌ی npm: 14.3.0 در ۲۰۲۶-۱۰-۱۵ منتشر شد؛ در ۲۰۲۶-۱۰-۲۸ آخرین نسخه 14.7.1 (۲۰۲۶-۱۰-۲۷) بود و در ۲۰۲۶-۱۰-۳۰ npm latest روی **14.8.0** است (شماره‌ی اصلی ۱۴؛ [S208](../sources/README.md#s208)). ✅ CHANGELOG مخزن برای 14.0.0 (۲۰۲۶-۱۰-۰۲) فقط حذف APIهای داخلی را ثبت کرده و در ورودی‌های 14.0 تا 14.7 عبارت «breaking» نیست (https://raw.githubusercontent.com/motiondivision/motion/main/CHANGELOG.md)؛ پیش از ارتقا CHANGELOG مخزن را بخوان ([S168](../sources/README.md#s168)).

## دستور سریع
✅ ([motion.dev/docs/react-quick-start](https://motion.dev/docs/react-quick-start)، npm: motion 14.9.0):
```bash
npm install motion
```
```tsx
import { motion } from "motion/react";      // نه framer-motion
<motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }} />
```
✅ تنظیم‌های مهم: در Next.js App Router فایل را `"use client"` کن یا `import * as motion from "motion/react-client"`؛ `<MotionConfig reducedMotion="user">` را بالای اپ بگذار چون پیش‌فرض `"never"` است و ترجیح کاهش حرکت را نمی‌خواند؛ برای حجم کمتر `LazyMotion` با `domAnimation` و `motion/react-m` (حدود ۵ کیلوبایت برای اولین رندر طبق مستندات).
خطاهای رایج: عدد ۵۰ کیلوبایت در Bundlephobia گمراه‌کننده است؛ فقط چیزی که import می‌کنی در bundle می‌رود ([docs](https://motion.dev/docs/react-reduce-bundle-size)). ✅ پیش از ارتقای اصلی `CHANGELOG` مخزن را بخوان (در ورودی‌های 14.0 تا 14.7 «breaking» نیامده). import از `framer-motion` قدیمی است.
💲 کتابخانه MIT و رایگان؛ Motion+ پرداخت یکباره برای هر توسعه‌دهنده است و تیم‌های دو نفر و بیشتر سالانه‌اند (عدد قیمت در [motion.dev/plus](https://motion.dev/plus) با جاوااسکریپت بارگذاری می‌شود و خوانده نشد ❓).

## کی استفاده کنیم
پروژه‌های React و Next.js برای ورود عناصر، hover، layout animation.

## قیمت و مجوز
✅ کتابخانه‌ی اصلی MIT. ✅ بخش پولی Motion+ است: پرداخت یکباره برای نمونه‌ها، Motion UI و AI Kit و Studio با به‌روزرسانی مادام‌العمر (https://motion.dev/plus)؛ کتابخانه‌ی اصلی MIT و رایگان می‌ماند.

## ریسک و هشدار
کم.

✅ کیت رسمی Motion برای عامل‌ها: [Motion AI Kit](motion-ai-kit.md) (بخشی پولی، با MCP میزبانی‌شده).

## مرتبط
[حرکت و انیمیشن](../domains/website/03-motion-3d/motion-animation.md) · [S09](../sources/README.md#s09)
