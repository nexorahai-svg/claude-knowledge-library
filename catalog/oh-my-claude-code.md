---
name: Oh My Claude Code (oh-my-claudecode)
slug: oh-my-claude-code
category: claude-code-tooling
domains: [claude-code]
verdict: hold
status: researched
summary: افزونه‌ی شخص ثالث برای هماهنگی چند عامل؛ hook روی همه‌ی رویدادها و بازنویسی CLAUDE.md
url: https://github.com/Yeachan-Heo/oh-my-claudecode
repo: "https://github.com/Yeachan-Heo/oh-my-claudecode"
license: "MIT"
pricing: free
risk: high
sources: [S22]
found_in: [batch-01/P00]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Oh My Claude Code (oh-my-claudecode)

## چیست
✅ پست منبع لینک نداده بود؛ محتمل‌ترین پروژه: https://github.com/Yeachan-Heo/oh-my-claudecode (MIT، حدود ۴۰ هزار ستاره، ساخته‌شده ۲۰۲۶-۰۱-۰۹، خیلی فعال). **رسمی از Anthropic نیست**؛ حساب شخصی است. بسته‌ی npm اسم دیگری دارد (`oh-my-claude-sisyphus`).

کارش: یک افزونه با ده‌ها دستور و حالت (`/autopilot`، `/ralph`، `/team`، `/plan`…)، حالت تیمی چند عامل (حتی کارگرهای Codex و Gemini در tmux)، حالت‌هایی که با کلمه‌ی کلیدی فعال می‌شوند، نوار وضعیت، حافظه‌ی پروژه و ردیابی هزینه.

## کی استفاده کنیم
🧭 **برای ما فعلاً هیچ‌وقت.** تقریباً همه‌ی کارهایش را Claude Code خودش دارد: زیرعامل‌ها، تیم عامل‌ها، skillها، افزونه‌ها، hookها، worktree و نوار وضعیت. ایده‌هایش (حلقه‌ی ادامه تا پایان کار، برنامه‌ریزی قبل از ساخت) را یاد بگیر، نصبش نکن.

## نصب (فقط برای آگاهی)
✅ از راه بازار افزونه‌ها: `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` و بعد `/plugin install oh-my-claudecode`، سپس `/omc-setup`.

## ریسک و هشدار
✅ (از hooks.json و مستندات مخزن):
- **hook روی ۱۱ رویداد**، از جمله هر پرامپت تو، قبل و بعد از **هر** ابزار، و درخواست مجوز. یعنی کدش همه‌ی پرامپت‌ها و عمل‌ها را می‌بیند. ❓ اینکه hook درخواست مجوز خودکار تأیید می‌کند یا نه، بررسی نشد.
- مرحله‌ی نصب در حالت سراسری **فایل `~/.claude/CLAUDE.md` را بازنویسی می‌کند** و بعد از هر به‌روزرسانی باید دوباره اجرا شود.
- یک سرور MCP داخلی دارد؛ به‌روزرسانی خودکار و کارگرهای مدل‌های دیگر به‌طور پیش‌فرض مجازند (فقط حالت `OMC_SECURITY=strict` آن‌ها را می‌بندد).
- حالت‌های «ادامه تا تمام شدن» توکن زیادی مصرف می‌کنند.
- کد کامپایل‌شده‌ی حجیم؛ بازبینی سخت.

## مرتبط
[امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S22](../sources/README.md#s22)
