---
name: claude-hud
slug: claude-hud
category: claude-code-tooling
domains: [claude-code]
verdict: assess
status: researched
summary: نوار وضعیت Claude Code برای نمایش زمینه، محدودیت نرخ، ابزارها و پیشرفت کار
use_when: "wanting live context/usage and agent status in the Claude Code status line"
how: "/plugin marketplace add jarrodwatts/claude-hud; /plugin install claude-hud; /claude-hud:setup (note it edits statusLine in settings)"
url: https://github.com/jarrodwatts/claude-hud
repo: "https://github.com/jarrodwatts/claude-hud"
license: "MIT"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# claude-hud

## چیست
✅ افزونهٔ Claude Code که در نوار وضعیت میزان زمینه، محدودیت نرخ، ابزارهای فعال، عامل‌ها و پیشرفت todo را نشان می‌دهد؛ نصب با /plugin marketplace add jarrodwatts/claude-hud. ✅ نویسنده حساب قدیمی (۲۰۱۸)؛ فقط ۲ issue باز.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: wanting live context/usage and agent status in the Claude Code status line. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۲۹,۰۳۰ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- setup تنظیمات statusLine را تغییر می‌دهد؛ src/auth.ts فقط فیلد oauthAccount از ~/.claude.json را می‌خواند (نه توکن، طبق نگاه سریع). پوشهٔ dist کامپایل‌شده در مخزن است.
- ❓ dist در برابر src مقایسه نشد؛ فراخوانی شبکه‌ای فقط با grep بررسی شد و مورد مشکوکی دیده نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/jarrodwatts/claude-hud
