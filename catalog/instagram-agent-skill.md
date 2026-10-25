---
name: Instagram Agent Skill
slug: instagram-agent-skill
category: claude-code-tooling
domains: [social-media, claude-code]
verdict: trial
status: researched
summary: ۱۳ مهارت Claude Code برای سناریوی ریلز، کپشن، کاروسل، برنامه و پیش‌نویس پاسخ اینستاگرام؛ محلی، بدون انتشار
url: https://github.com/Jakeschincariol/instagram-agent-skill
repo: "https://github.com/Jakeschincariol/instagram-agent-skill"
license: "MIT"
pricing: free
risk: low
sources: [S78, S77, S155]
found_in: [batch-03]
last_checked: 2026-10-25
next_check: "2026-11-24"
---

# Instagram Agent Skill

## چیست
✅ مخزن Jake Schincariol (https://opusjake.ai)، افزونه‌ی Claude Code با ۱۳ مهارت (`ig-reel`، `ig-caption`، `ig-carousel`، `ig-story`، `ig-plan`، `ig-profile`، `ig-viral`، `ig-comment`، `ig-reply`، `ig-dm`، `ig-repurpose`، `ig-audit`، `ig-human`). چند اسکریپت پایتون محلی (امتیاز قلاب، طرح ضرب، بررسی کپشن، فایل الگو) دارد.
✅ (فایل‌به‌فایل خوانده شد، ۲۰۲۶-۱۰-۱۸) هیچ اسکریپتی تماس شبکه‌ای یا اجرای فرمان ندارد. README صریحاً می‌گوید هیچ مهارتی در Instagram پست نمی‌گذارد؛ خروجی همیشه متن آماده برای کپی است. `ig-viral` با مرورگر خود کاربر و با سرعت انسانی نگاه می‌کند، وارد حساب نمی‌شود و رمز نمی‌خواهد.

## کی استفاده کنیم
🧭 برای ساختار کار (قلاب، طرح ضرب، کپشن در حد بریده شدن فید، برنامه‌ی هفتگی) در محتوای انگلیسی، یا به‌عنوان الگو برای مهارت فارسی خودمان.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
⚠️ **`ig-human` نیم‌فاصله (U+200C)، ZWJ و نشانه‌های جهت (LRM، RLM، ALM) را پاک می‌کند** (`skills/ig-human/slop.json`) و متن فارسی را خراب می‌کند. روی فارسی اجرا نشود.
⚠️ فهرست واژه‌ها و قلاب‌ها فقط انگلیسی است.
⚠️ فقط دو commit در یک دقیقه (۲۰۲۶-۰۹-۱۳) با حدود ۱٬۷۶۰ ستاره؛ سابقه‌ی نگهداری ندارد. پیش از نصب نسخه‌ی تازه دوباره بخوان.
⚠️ «انسانی‌کننده» برای پنهان کردن نشانه‌ی هوش مصنوعی است؛ قانون برچسب محتوای هوش مصنوعی شبکه‌ها را در [انتشار](../domains/social-media/publishing.md) ببین.

## نصب آزمایشی ۲۰۲۶-۱۰-۲۱
✅ دوباره خوانده شد: همان دو commit سپتامبر (`d03c56b`)، بدون hook و MCP، بدون تماس شبکه یا اجرای فرمان در اسکریپت‌ها. به درخواست کاربر برای آزمون در سطح کاربر نصب شد:
```bash
claude plugin marketplace add Jakeschincariol/instagram-agent-skill
claude plugin install instagram-agent@instagram-agent-skill --scope user
```
محافظ: یک بند در `~/.claude/CLAUDE.md` کاربر که `ig-human` روی متن فارسی و عربی اجرا نشود. نتیجه‌ی آزمون هنوز ثبت نشده.


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ (۲۰۲۶-۱۰-۲۵) ادعای «۲۶ فرمول قلاب» درست است: `skills/ig-reel/hooks.json` دقیقاً ۲۶ قلاب دارد. ریلز فارسی ai.erf (۲۰۲۶-۱۰-۲۳) همین ابزار را با قیف «عدد ۱۱ را کامنت کن» تبلیغ کرد و به خطر `ig-human` برای فارسی اشاره‌ای نکرد. قلاب‌ها فقط انگلیسی‌اند (غربال ۲۰).

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md#مهارت-آماده-برای-کپشن-اینستاگرام) · [S78](../sources/README.md#s78) · غربال دسته‌ی ۰۳
