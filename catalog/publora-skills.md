---
name: Publora skills
slug: publora-skills
category: social-publishing
domains: [social-media]
verdict: assess
status: researched
summary: ۹ مهارت رسمی Publora برای پیش‌نویس و زمان‌بندی پست در ده شبکه (از جمله اینستاگرام) از راه MCP و API رسمی؛ طرح رایگان دارد
use_when: "need an agent to create drafts or schedule posts to Instagram, LinkedIn, Threads, TikTok, YouTube from one connector ; compare with Postiz before choosing a scheduler"
how: "Do not install without the user's yes; claude mcp add --transport http --scope user publora https://mcp.publora.com/mcp then /mcp to sign in with OAuth; create drafts only (omit scheduledTime), the skills add no approval step"
url: https://github.com/publora/skills
repo: "https://github.com/publora/skills"
license: "MIT"
pricing: freemium
risk: medium
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2026-11-28"
---

# Publora skills

## چیست
- ✅ مخزن رسمی https://github.com/publora/skills؛ MIT؛ نسخه‌ی v1.1.0 (۲۰۲۶-۱۰-۱۲)؛ آخرین push ۲۰۲۶-۱۰-۲۷؛ حدود ۶۱ ستاره.
- ✅ README: نه فایل SKILL.md که به عامل یاد می‌دهند از راه سرور MCP سرویس Publora (۲۰ ابزار) پست را پیش‌نویس یا زمان‌بندی کند: LinkedIn، X، Instagram، Threads، TikTok، YouTube، Facebook، Bluesky، Mastodon، Telegram. ورود با OAuth یا کلید API.
- ✅ بدون `scheduledTime` پست پیش‌نویس می‌ماند؛ با زمان آینده زمان‌بندی می‌شود. README می‌گوید مهارت‌ها مرحله‌ی تأیید جدا ندارند.
- ✅ در بازارچه‌ی رسمی Anthropic فقط Postiz هست؛ این مورد نیست ([Postiz](postiz.md)).

## قیمت و مجوز
- ✅ کد مهارت‌ها MIT. سرویس (https://publora.com/pricing، ۲۰۲۶-۱۰-۲۸): Starter رایگان با ۳ حساب و ۱۵ پست در ماه و دسترسی API و MCP، بدون X؛ Pro از ۲۹٫۹۵ دلار در ماه برای ۵ حساب؛ Agency سفارشی.
- ❓ برای Starter زمان‌بندی فقط ۷ روز آینده و ۳ پست هم‌زمان گزارش شد؛ پیش از تصمیم دوباره روی صفحه‌ی قیمت ببین.

## ریسک و هشدار
- ✅ مسیر رسمی API است، پس خطر بسته شدن حساب از ورودکننده‌های مرورگری کمتر است.
- 🧭 توکن انتشار یعنی پست به نام ما؛ فقط پیش‌نویس، و خود ما پیش از انتشار بازبینی کنیم.
- 🧭 سرویس شخص ثالث است و محتوا و توکن حساب‌ها را نگه می‌دارد؛ حریم و در دسترس بودن آن در ایران بررسی نشد (❓).
- ❓ کد MCP سرور خود Publora (بسته نیست) بررسی نشد.

## کی استفاده کنیم
🧭 اگر زمان‌بندی چندشبکه‌ای با عامل لازم شد و Postiz یا ابزارهای [انتشار](../domains/social-media/publishing.md) کافی نبودند. فعلاً زیر نظر؛ بدون اجازه‌ی کاربر نصب نشود.

## مرتبط
غربال · [S165](../sources/README.md#s165) · https://publora.com/pricing · https://docs.publora.com/mcp/client-setup

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ Starter رایگان: ۳ حساب، ۱۵ پست در ماه، ۳ پست زمان‌بندی‌شده‌ی هم‌زمان، تا ۷ روز جلو، بدون X، ویدیو تا ۵۰MB، با API و MCP. Pro از ۵٫۹۹ دلار برای هر حساب در ماه، با X و پست نامحدود (https://publora.com/pricing).
- ❓ دسترسی از ایران هیچ منبعی ندارد؛ باید از داخل ایران آزموده شود.
