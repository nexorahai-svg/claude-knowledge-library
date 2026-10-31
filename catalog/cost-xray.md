---
name: cost-xray
slug: cost-xray
category: cost-tokens
domains: [claude-code]
verdict: assess
status: researched
summary: ضبط محلی ترافیک API ابزارهای کدنویسی و نمایش هزینه‌ی توکن هر بخش
use_when: "finding why a Claude Code session is expensive ; measuring MCP/tool-schema token cost"
how: "install via install.sh (read it first; it fetches uv and clones to ~/.local/share/cost-xray), then wrap claude with the cx wrapper; cx stop to disable"
url: https://github.com/tigerless-labs/cost-xray
repo: "https://github.com/tigerless-labs/cost-xray"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# cost-xray

## چیست
✅ با mitmproxy محلی ترافیک API ابزارهای Claude Code/Codex را ضبط می‌کند و نشان می‌دهد هر بخش (پرامپت سیستم، MCP، نتایج ابزار) چند توکن و دلار هزینه دارد. ✅ SECURITY.md: بدون telemetry، فقط 127.0.0.1، کلیدها قبل از دیسک پنهان می‌شوند؛ برای Claude Code بدون گواهی.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: finding why a Claude Code session is expensive؛ measuring MCP/tool-schema token cost. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۵,۹۱۳ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ نصب پیشنهادی README به‌صورت curl|bash است؛ قبل از اجرا فایل را بخوانید.
- در مسیر ترافیک API می‌نشیند و پرامپت/کد را روی دیسک ذخیره می‌کند (~/.cost-xray)؛ install.sh خودش curl|sh برای uv دارد؛ سازمان تازه (۲۰۲۶-۰۵). برای Codex یک CA محلی اضافه می‌شود.
- ❓ تست‌های redaction و کد proxy اجرا یا بازبینی نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/tigerless-labs/cost-xray
