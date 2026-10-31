---
name: OpenReply
slug: openreply
category: social-publishing
domains: [social-media]
verdict: trial
status: researched
summary: خودکارسازی «کامنت کلیدواژه ← دایرکت» اینستاگرام با API رسمی Meta؛ جایگزین خودمیزبان ManyChat
use_when: "automating replies on Instagram/Meta via the official API"
how: "Trial first on a small task: clone the repo, then npm install, docker-compose up -d (Postgres+Redis), npm run db:generate, npm run db:migrate, npm run dev and, in a second terminal, npm run worker (the worker sends DMs); test on our own account first (MIT)"
url: https://github.com/diwenne/openreply
repo: "https://github.com/diwenne/openreply"
license: "MIT"
pricing: free
risk: medium
sources: [S162]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# OpenReply

## چیست
✅ (MIT، حدود ۳ هزار ستاره، آخرین تغییر ۲۰۲۶-۱۰-۰۵)؛ README می‌گوید فقط API رسمی، بدون خزیدن و رمز. ✅ README (۲۰۲۶-۱۰-۲۷): برای نمونه‌ی کارا آدرس عمومی HTTPS، PostgreSQL، Redis، ارسال ایمیل (ورود با لینک جادویی) و یک worker همیشه روشن لازم است؛ سیاست‌ها، پنجره‌ی پیام و سقف نرخ اینستاگرام همچنان اعمال می‌شود؛ نسخه‌ی رسمی (release) ندارد.
✅ نصب و اجرا (https://github.com/diwenne/openreply، ۲۰۲۶-۱۰-۲۷): npm install ; docker-compose up -d ; npm run db:generate ; npm run db:migrate ; npm run dev ; npm run worker

## کی استفاده کنیم
🧭 اول فقط روی حساب خودمان؛ حساب حرفه‌ای + اپ Meta + webhook لازم است؛ قواعد پیام خودکار و پنجره‌ی ۲۴ ساعته را رعایت کن ([راه‌اندازی Meta](../domains/social-media/meta-business-setup.md)).
