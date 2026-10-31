---
name: mobile-mcp
slug: mobile-mcp
category: app-testing
domains: [apps, security]
verdict: trial
status: researched
summary: MCP برای کنترل شبیه‌ساز iOS، امولاتور Android و دستگاه واقعی
use_when: "driving an iOS simulator or real device from an agent ; second mobile test tool next to Maestro MCP"
how: "Trial first on a small task: pin @mobilenext/mobile-mcp version (not @latest) and set MOBILEMCP_DISABLE_TELEMETRY=1; start with the simulator only; since 1.0.15 mobile_clear_app_data wipes app data, so keep it off real devices; it runs xcrun and adb and installs apps"
url: https://github.com/mobile-next/mobile-mcp
repo: "https://github.com/mobile-next/mobile-mcp"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S41]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# mobile-mcp

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی 1.0.15 (۲۰۲۶-۱۰-۳۰): ابزار تازه‌ی `mobile_clear_app_data` (Android و شبیه‌ساز iOS) و رفع نوشتن اسکرین‌شات و لاگ. ⚠️ این ابزار داده‌ی اپ را پاک می‌کند: https://github.com/mobile-next/mobile-mcp/releases/tag/1.0.15
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 1.0.14 (۲۰۲۶-۱۰-۲۶)؛ Apache-2.0 بی‌تغییر.
✅ ‎@mobilenext/mobile-mcp 1.0.11. اول درخت دسترسی‌پذیری را می‌خواند، بعد عکس صفحه. لمس، کشیدن، نصب و اجرای اپ، ضبط صفحه.

## کی استفاده کنیم
🧭 ابزار دوم کنار Maestro MCP، برای iOS و دستگاه واقعی.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
⚠️ `xcrun` و `adb` اجرا می‌کند و اپ نصب می‌کند. نسخه را ثابت کن (نه `@latest`). تله‌متری PostHog و Scarf: `MOBILEMCP_DISABLE_TELEMETRY=1`. اول فقط شبیه‌ساز.

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41)
