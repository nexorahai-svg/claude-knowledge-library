---
name: Claude-Code-Usage-Monitor
slug: claude-code-usage-monitor
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: داشبورد زنده‌ی مصرف در ترمینال با پیش‌بینی زمان رسیدن به سقف طرح
use_when: "often hitting the 5-hour subscription limit ; wanting a live terminal usage dashboard with time-to-limit forecast"
how: "Trial first on a small task: uv tool install claude-monitor, then claude-monitor --plan max5 (or pro, max20, team); for simple reports ccusage is enough"
url: https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
repo: "https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor"
license: "MIT"
pricing: free
risk: low
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Claude-Code-Usage-Monitor

## چیست
✅ داشبورد زنده در ترمینال: سرعت مصرف و زمان تخمینی رسیدن به سقف طرح (Pro، Max، Team). خروجی ماشین‌خوان و یک انبار داده‌ی محلی اختیاری که از پاک شدن ۳۰ روزه‌ی لاگ‌ها جلوگیری می‌کند. حدود ۸.۷ هزار ستاره؛ آخرین فعالیت ۲۰۲۶-۰۷-۰۵.

## کی استفاده کنیم
🧭 فقط اگر زیاد به سقف ۵ ساعته‌ی اشتراک می‌خوری. برای گزارش ساده، [ccusage](ccusage.md) کافی است.
```bash
uv tool install claude-monitor
```
بعد `claude-monitor --plan max5` (یا pro، max20، team).

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
کم به‌طور پیش‌فرض. ⚠️ پرچم آزمایشی `--api` از اعتبار OAuth حساب Claude تو استفاده می‌کند؛ روشنش نکن مگر لازم باشد.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
