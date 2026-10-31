---
name: inssist MCP
slug: inssist-mcp
category: claude-code-tooling
domains: [social-media, claude-code, security]
verdict: hold
status: researched
summary: سرور MCP اینستاگرام (DM، انتشار، استوری، حذف دنبال‌کننده) داخل نشست واردشده از راه افزونه‌ی Chrome شخص ثالث؛ استفاده نکن
use_when: "never for the main account; only reading its README to see what Instagram automation through a browser session exposes"
how: "Do not install; use the official Instagram Graph API or Postiz for publishing, and never download copies named INSSIST-CRACKED"
url: https://github.com/inssist/mcp
repo: "https://github.com/inssist/mcp"
license: "MIT"
pricing: freemium
risk: high
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2026-11-28"
---

# inssist MCP

## چیست
- ✅ مخزن https://github.com/inssist/mcp؛ MIT؛ نسخه‌ی v2.0.0 (۲۰۲۶-۰۹-۲۲)؛ آخرین push ۲۰۲۶-۱۰-۱۹؛ ۲۷ ستاره.
- ✅ README: سرور MCP روی npm (`@inssist/mcp`) که از راه افزونه‌ی Chrome «INSSIST» و اتصال محلی (`ws://127.0.0.1:48231`) داخل نشست واردشده‌ی اینستاگرام ما کار می‌کند. ۶۰ ابزار: خواندن پروفایل و DM، فرستادن DM، کامنت، انتشار و زمان‌بندی، حذف پست، block، حذف دنبال‌کننده، دانلود، اسکن unfollowers و antibot.
- ✅ بخشی از ابزارها نیازمند اشتراک پولی INSSIST PRO است (freemium).
- ✅ README می‌گوید رمز را نگه نمی‌دارد و «ابر» ندارد؛ ولی خودش می‌گوید بین تماس‌ها چند ثانیه فاصله می‌گذارد تا «بلاک نرخ» نخورد، یعنی خودش تشخیص خودکارسازی را می‌شناسد.

## ریسک و هشدار
- ⚠️ ✅ ابزارهای مخرب و برگشت‌ناپذیر (`dm_send`، `ig_post_delete`، `ig_block`، `follower_remove`) با نشست اصلی.
- ⚠️ 🧭 خودکارسازی اینستاگرام با نشست مرورگر خلاف شرایط متا است و می‌تواند حساب را محدود کند.
- ⚠️ ✅ با `npx -y` کد npm هر بار دانلود و اجرا می‌شود؛ افزونه‌ی Chrome شخص ثالث به صفحه‌ی اینستاگرام دسترسی کامل دارد.
- ⚠️ ✅ مخزن جعلی `Landdradee/INSSIST-CRACKED` در گیت‌هاب هست؛ هرگز.

## کی استفاده کنیم
⛔ نه. برای انتشار از Graph API رسمی یا ابزار API رسمی استفاده کن.

## قیمت و مجوز
✅ سرور MIT؛ افزونه و ابزارهای PRO اشتراک پولی دارند (https://inssist.com/#pricing). بهای دقیق بررسی نشد (❓).

## مرتبط
غربال · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S165](../sources/README.md#s165)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ INSSIST PRO ماهی ۱۴٫۵ دلار برای هر حساب اینستاگرام است (قیمت خط‌خورده ۱۹٫۵). Free رایگان است و Lifetime یک‌بار ۱۴۵ دلار. بیش از ۵ حساب: تماس با فروش (https://inssist.com/#pricing).

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد سرور خوانده شد (SHA `0133e0b`، نسخه‌ی 2.1.1 در HEAD). یک پل محلی روی 127.0.0.1:48231 است که فقط Origin از نوع `chrome-extension://` را می‌پذیرد. توکن جفت‌سازی در `~/.inssist` با mode 0600 است. شبکه‌ی بیرونی و تله‌متری ندارد. ❓ افزونه‌ی بسته‌ی INSSIST، که اینستاگرام را واقعاً کنترل می‌کند، خوانده نشد.
