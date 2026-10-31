---
name: reanimate
slug: reanimate
category: animation
domains: [website]
verdict: assess
status: researched
summary: skill Claude Code که یک انیمیشن (سایت زنده، ویدیو، gif یا Lottie) را ضبط و اندازه‌گیری می‌کند، در کد بازسازی می‌کند و تا انطباق عددی تکرار می‌کند
use_when: "measuring the timing and easing of a motion reference to learn its principles ; checking that our own animation matches a spec we wrote ; studying how a motion is built before designing our own"
how: "Trial first on a small task: read SKILL.md and scripts first (rule 4), install only with the user's yes via npx skills add NiazMorshed2007/reanimate, needs Bun 1.1 and about 250 MB of ffmpeg and Chromium downloads; use it to learn principles, never to ship a copy of someone else's animation (rule 1)"
url: https://github.com/NiazMorshed2007/reanimate
repo: "https://github.com/NiazMorshed2007/reanimate"
license: "MIT"
pricing: free
risk: medium
sources: [S216]
found_in: [watch-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# reanimate

## چیست
✅ (GitHub API و README، ۲۰۲۶-۱۰-۳۱) مالک فرد NiazMorshed2007؛ ساخته ۲۰۲۶-۱۰-۲۹، آخرین push ۲۰۲۶-۱۰-۳۰، ۲۶۳ ستاره، MIT. جریان README: ضبط مرجع در مرورگر headless با نرخ فریم ثابت، جدول مشخصات (شروع، مدت، از←به، easing، stagger)، ساخت با ابزار خود پروژه (CSS، Framer Motion، GSAP، three.js)، ضبط نسخه‌ی ساخته‌شده و مقایسه‌ی زمان‌بندی و پیکسل، و تکرار ۲ تا ۵ دور. سطح پیش‌فرض «همان حرکت»؛ با «دقیقاً» تا ۲٪ اختلاف پیکسل. روی macOS و Linux با Bun؛ ویندوز آزموده نشده. نمونه‌هایش بازسازی انیمیشن سایت‌های واقعی (Stripe، Clerk، Resend و…) است.

## کی استفاده کنیم
🧭 یادگیری اصول زمان‌بندی و easing از یک مرجع حرکتی، یا بررسی عددی اینکه انیمیشن خودمان با مشخصات می‌خواند. با [Motion](motion.md)، [claude-motion](claude-motion.md) و [code-animation-prompts](code-animation-prompts.md) همپوشانی دارد. هنوز در هیچ پروژه‌ای آزموده نشده.

## قیمت و مجوز
✅ MIT و رایگان.

## ریسک و هشدار
⚠️ کارکرد اصلی «کپی» انیمیشن سایت‌های دیگر است؛ طبق قانون ۱ و ریسک مالکیت معنوی، فقط برای یادگیری اصول و ساخت نسخه‌ی خودمان، نه بازتولید حرکت و کد و دارایی دیگران. اجرای آن Chromium و ffmpeg (حدود ۲۵۰ مگابایت) دانلود می‌کند و سایت‌های واقعی را باز می‌کند؛ فایل‌ها پیش از نصب خوانده شود.

## مرتبط
[طراحی حرکت](../domains/social-media/motion-design-styles.md) · [S216](../sources/README.md#s216)
