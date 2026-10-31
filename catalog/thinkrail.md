---
name: Thinkrail (JetBrains)
slug: thinkrail
category: claude-code-tooling
domains: [claude-code, apps]
verdict: assess
status: researched
summary: IDE عاملی از انکوبیتور JetBrains بر پایه‌ی عامل کدنویسی pi با عامل‌های موازی در git worktree
use_when: "Trying a parallel-agents IDE with git worktrees ; evaluating JetBrains' agentic tooling"
how: "Do not run the curl|bash installer blindly; read it first; check MCP confirmations stay on for non-read-only calls"
url: https://github.com/JetBrains/thinkrail
repo: "https://github.com/JetBrains/thinkrail"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S205]
found_in: [watch-2026-10-29]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Thinkrail (JetBrains)

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README) IDE عاملی از انکوبیتور JetBrains، Apache-2.0، ۵٬۹۶۰ ستاره، ساخته‌شده ۲۰۲۶-۰۷-۰۸، آخرین push ۲۰۲۶-۱۰-۲۹. بر پایه‌ی عامل `pi` (@earendil-works/pi-coding-agent)؛ عامل‌های موازی در git worktree؛ MCP از `mcp.json` عامل pi با تأیید پیش از فراخوانی غیرفقط‌خواندنی و OAuth. ارائه‌دهنده‌ها از JetBrains AI یا احراز هویت pi. macOS 14+، ویندوز x64، لینوکس x64/ARM64 با glibc 2.38+؛ فرمان `thinkrail` آن را در مرورگر باز می‌کند؛ نصب با curl|bash؛ بررسی به‌روزرسانی در پس‌زمینه.
✅ README (https://github.com/JetBrains/thinkrail) اسمی از Claude نمی‌برد. ✅ تله‌متری هست: رویدادهای استفاده‌ی پایه (اجرا، ساخت چت، ارسال پیام، اتصال ارائه‌دهنده) با شناسه‌ی نصب تصادفی و گزارش خطای همیشه‌روشن؛ «اشتراک داده‌ی بیشتر» در تنظیمات Privacy یا با `thinkrail --no-analytics` / `THINKRAIL_NO_ANALYTICS=1` خاموش می‌شود.

## کی استفاده کنیم
🧭 فقط برای آزمایش؛ جایگزین Claude Code نیست.

## قیمت و مجوز
Apache-2.0، رایگان؛ هزینه‌ی مدل به ارائه‌دهنده بستگی دارد ❓.

## ریسک و هشدار
نصب‌کننده‌ی curl|bash را نخوانده اجرا نکن؛ بررسی به‌روزرسانی در پس‌زمینه؛ تله‌متری نامشخص.

## مرتبط
- https://github.com/JetBrains/thinkrail
