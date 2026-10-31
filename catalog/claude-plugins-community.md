---
name: claude-plugins-community
slug: claude-plugins-community
category: claude-code-tooling
domains: [claude-code]
verdict: assess
status: researched
summary: آینه‌ی فقط‌خواندنی بازارچه‌ی افزونه‌های جامعه برای Claude Code
use_when: "finding a community Claude Code plugin ; checking whether a plugin is in the reviewed community marketplace"
how: "claude plugin marketplace add anthropics/claude-plugins-community; claude plugin install <name>@claude-community (read plugin files first)"
url: https://github.com/anthropics/claude-plugins-community
repo: "https://github.com/anthropics/claude-plugins-community"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# claude-plugins-community

## چیست
✅ آینهٔ فقط‌خواندنی مارکت‌پلیس افزونه‌های جامعه برای Claude Code و Cowork؛ README می‌گوید هر افزونه از طریق ارسال در claude.ai، اسکن امنیتی خودکار و تأیید گذشته است. ✅ سازمان رسمی Anthropic؛ ۲۳۲۱ نام در marketplace.json.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: finding a community Claude Code plugin؛ checking whether a plugin is in the reviewed community marketplace. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۴,۷۹۳ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- افزونه‌ها از جامعه‌اند و هر کدام ممکن است هوک یا MCP داشته باشد (نمونه: next-steps دارای hooks.json). اسکن خودکار تضمین کامل نیست.
- ❓ محتوای تک‌تک ۲۳۰۰ افزونه بررسی نشد؛ فقط ساختار و README. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/anthropics/claude-plugins-community
