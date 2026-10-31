---
name: codegraph
slug: codegraph
category: agents-memory
domains: [claude-code, security]
verdict: hold
status: researched
summary: گراف کد محلی برای ابزارهای کدنویسی؛ تله‌متری پیش‌فرض روشن است
use_when: "building a local code graph for a big repo (only after turning telemetry off)"
how: "Do not install by default; if tried: run codegraph telemetry off (or set CODEGRAPH_TELEMETRY=0 or DO_NOT_TRACK=1) before first use"
url: https://github.com/colbymchenry/codegraph
repo: "https://github.com/colbymchenry/codegraph"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# codegraph

## چیست
✅ گراف کد محلی برای Claude Code/Cursor/Codex با هستهٔ Rust. ✅ TELEMETRY.md: آمار ناشناس استفاده ارسال می‌شود و گزینهٔ نصب‌کننده به‌صورت پیش‌فرض روشن است؛ خاموش‌کردن با codegraph telemetry off یا DO_NOT_TRACK=1.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: building a local code graph for a big repo (only after turning telemetry off). وضعیت: ⛔ فعلاً استفاده نکنید.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۷۵,۹۷۷ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ تله‌متری به‌طور پیش‌فرض روشن است؛ خاموش‌کردن: codegraph telemetry off یا CODEGRAPH_TELEMETRY=0 یا DO_NOT_TRACK=1.
- ❓ تعداد ستاره تأیید نشد.
- telemetry پیش‌فرض روشن (خلاف قاعدهٔ مالک)؛ install.sh؛ ۴۲۰ issue باز؛ ستارهٔ ۷۶ هزار در ۹ ماه بدون راه تأیید.
- ❓ هستهٔ Rust و نقطهٔ پایانی telemetry-worker خوانده نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/colbymchenry/codegraph
