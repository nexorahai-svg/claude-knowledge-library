---
name: Hao0321 social-post
slug: hao0321-social-post
category: claude-code-tooling
domains: [social-media, claude-code, security]
verdict: hold
status: researched
summary: مهارت «یادگیری صدای شما و انتشار» در FB/IG/Threads/X از راه Chrome واردشده؛ مستند چینی (سنتی) و وابسته به Codex؛ استفاده نکن
use_when: "only as reading material for how a human-approval comment and posting workflow can be structured"
how: "Do not install; for drafting posts use ig-caption or the library's publishing tools, and for scheduling use official-API tools such as Postiz"
url: https://github.com/Hao0321/claude-skill-social-post
repo: "https://github.com/Hao0321/claude-skill-social-post"
license: "MIT"
pricing: free
risk: high
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# Hao0321 social-post

## چیست
- ✅ مخزن https://github.com/Hao0321/claude-skill-social-post؛ MIT؛ نسخه‌ی v2.5.1؛ ساخته ۲۰۲۶-۰۴-۲۱؛ آخرین push ۲۰۲۶-۱۰-۱۵؛ حدود ۷۴۳ ستاره (API گیت‌هاب).
- ✅ README (چینی سنتی): مهارت برای Codex یا Claude Code که لحن را محلی یاد می‌گیرد، محتوا را برنامه‌ریزی می‌کند و «پس از تأیید» با Chrome واردشده منتشر می‌کند. بخش Comment Ops کامنت را با Chrome اسکن و پاسخ را پیش‌نویس می‌کند.
- ✅ README می‌گوید به API متا وصل نمی‌شود، کوکی یا session را صادر نمی‌کند، حالت پیش‌فرض `batch_confirm` است و پایش ۲۴ ساعته ندارد؛ پاسخ زنده نیاز به قفل‌گشایی جدا دارد.
- ✅ بخش Chrome به نسخه‌ی ثابت runtime همراه Codex وابسته است؛ برای Claude Code «یا متن‌های مستقل عمومی» کامل نیست (طبق README).
- ❓ ادعای «۸۰ هزار reach در اولین پست» ادعای خود سازنده است.

## ریسک و هشدار
- ⚠️ ✅ ابزار در نشست واردشده‌ی کاربر عمل می‌کند؛ خودکارسازی اینستاگرام/X با نشست مرورگر خطر محدود یا بسته شدن حساب دارد (🧭).
- ⚠️ ✅ دارای مسیر پاسخ به کامنت‌ها از نام ما.
- 🧭 پروژه‌ی تک‌نفره، سریع‌تغییر (فهرست «Unreleased candidate»)؛ بازبینی امنیتی ندارد. کد اجرایی خوانده نشد (❓).

## کی استفاده کنیم
⛔ برای کار واقعی نه. فقط برای ایده‌ی ساختار «تأیید انسانی پیش از ارسال» می‌شود مستند را خواند.

## قیمت و مجوز
✅ رایگان، MIT.

## مرتبط
غربال · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S165](../sources/README.md#s165)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ بخشی از ۱۷۰ اسکریپت خوانده شد (SHA `c22737a`). کلاینت HTTP خروجی دیده نشد. subprocess فقط `node` را اجرا می‌کند. workbench یک سرور محلی با توکن و CSRF است. ⚠️ ارسال نظر در Facebook، Instagram و Threads از مرورگر میزبان و با حساب واردشده‌ی تو انجام می‌شود (با دروازه‌ی مجوز). ❓ بقیه‌ی اسکریپت‌ها خوانده نشد.
