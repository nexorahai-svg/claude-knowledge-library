---
name: Instagram Agent FA
slug: instagram-agent-fa
category: claude-code-tooling
domains: [social-media, claude-code]
verdict: trial
status: researched
summary: بازنویسی فارسی مهارت‌های اینستاگرام با ۲۷ قلاب فارسی که نیم‌فاصله و نشانه‌ی جهت را نگه می‌دارد
use_when: "writing Persian Instagram captions and hooks ; planning a Persian content calendar (Shamsi) without damaging ZWNJ"
how: "Trial first on a small task: READ all files before installing (unknown author); use its 27 Persian hooks for captions and review the drafts, then post manually; it keeps ZWNJ and direction marks; never give it a Graph API token"
url: https://github.com/omidkhavari1708-pixel/instagram-agent-fa
repo: "https://github.com/omidkhavari1708-pixel/instagram-agent-fa"
license: "MIT"
pricing: free
risk: medium
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-25
next_check: "2027-01-23"
---

# Instagram Agent FA

## چیست
✅ (فایل‌ها خوانده شد، ۲۰۲۶-۱۰-۲۵؛ نصب نشد) بازنویسی فارسی همان ۱۳ مهارت [Instagram Agent Skill](instagram-agent-skill.md): ۲۷ قلاب فارسی با مثال، تقویم شمسی، کلمه‌شمار فارسی و دو لحن محاوره و کتابی. ۰ ستاره، ۳ commit (۲۰۲۶-۱۰-۲۴)، MIT.
✅ نیم‌فاصله و نشانه‌ی جهت را **نگه می‌دارد**؛ یعنی عیب `ig-human` نسخه‌ی اصلی را ندارد.

## کی استفاده کنیم
🧭 برای کپشن و قلاب فارسی، به‌جای انسانی‌ساز نسخه‌ی اصلی. اول پیش‌نویس بخوان، بعد انتشار دستی.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
⚠️ سازنده‌ی ناشناس و بی‌سابقه؛ پیش از نصب همه‌ی فایل‌ها دوباره خوانده شود.
⚠️ یک اسکریپت اختیاری با توکن Graph API خودت آمار می‌خواند (فقط خواندن) در حالی که README می‌گوید «بدون اتصال به حساب»؛ توکن نده.
⚠️ روی متن **عربی** «ي» را «ی» و رقم عربی را فارسی می‌کند؛ روی عربی اجرا نشود.
⚠️ هرگز `ig-human` نسخه‌ی اصلی را روی متن فارسی یا عربی اجرا نکن.

## مرتبط
غربال · [کپشن و متن](../domains/social-media/captions-and-copy.md#مهارت-آماده-برای-کپشن-اینستاگرام) · [S165](../sources/README.md#s165)
