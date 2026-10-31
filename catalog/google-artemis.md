---
name: artemis
slug: google-artemis
category: app-testing
domains: [apps, claude-code]
verdict: assess
status: researched
summary: عامل خودکارسازی اندروید با زبان طبیعی روی دستگاه واقعی، متصل به Claude Code با MCP
use_when: "UI-testing an Android app on a real device from Claude Code"
how: "follow README Quick Start (start.sh) and add mcp_server to Claude Code; use a spare test phone only"
url: https://github.com/google/artemis
repo: "https://github.com/google/artemis"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# artemis

## چیست
✅ عامل خودکارسازی اندروید که با دستور زبان طبیعی روی دستگاه واقعی کار می‌کند و با MCP به Claude Code/Antigravity وصل می‌شود (Logcat و اسکرین‌شات). ✅ سازمان google؛ ادعای ۹۹٪ روی AndroidWorld فقط README است.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: UI-testing an Android app on a real device from Claude Code. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۱۵,۷۸۷ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- کنترل کامل گوشی و فراخوانی LLM؛ ۱۷۹ issue باز؛ فایل‌های telemetry/llm_service در third_party وجود دارد.
- ❓ telemetry واقعی و دادهٔ ارسالی بررسی نشد؛ بنچمارک تأیید نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/google/artemis
