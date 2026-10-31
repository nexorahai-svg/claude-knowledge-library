---
name: codex-mobile-dev-plugin
slug: codex-mobile-dev-plugin
category: app-testing
domains: [apps, claude-code]
verdict: assess
status: researched
summary: افزونه‌ی Callstack برای دیدن و کنترل شبیه‌ساز و دستگاه واقعی کنار چت ایجنت
use_when: "Mobile development with an agent controlling simulators ; React Native debugging beside chat"
how: "Read PRIVACY.md, then set MOBILE_DEV_TELEMETRY=off in the environment that launches the MCP server and restart the plugin; Claude Code support is unverified"
url: https://github.com/callstackincubator/codex-mobile-dev-plugin
repo: "https://github.com/callstackincubator/codex-mobile-dev-plugin"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# codex-mobile-dev-plugin

## چیست
✅ پلاگین Callstack که شبیه‌ساز/امولاتور و دستگاه واقعی را کنار چت ایجنت نشان و کنترل می‌دهد (Codex، Claude، Cursor). ✅ PRIVACY.md می‌گوید تله‌متری پیش‌فرض روشن است و به Sentry گزارش خطا/شمارنده استفاده با شناسه نصب تصادفی می‌فرستد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Mobile development with an agent controlling simulators؛ React Native debugging beside chat. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۱۷۰ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ تله‌متری پیش‌فرض روشن است و به Sentry می‌فرستد؛ خاموش‌کردن: MOBILE_DEV_TELEMETRY=off در محیطی که MCP server را اجرا می‌کند، سپس افزونه را ریستارت کنید.
- ❓ پشتیبانی Claude Code تأیید نشد.
- تله‌متری پیش‌فرض روشن به Sentry (طبق PRIVACY.md)؛ راه خاموش‌کردن را پیدا/تأیید نکردم. Callstack شرکت شناخته‌شده RN است.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/callstackincubator/codex-mobile-dev-plugin
