---
name: Maestro و Maestro MCP
slug: maestro
category: app-testing
domains: [apps]
verdict: adopt
status: researched
summary: تست رابط اپ موبایل با فایل YAML و MCP داخلی برای عامل
use_when: "writing end-to-end tests for a mobile app on iOS or Android ; letting an agent drive a device and save YAML tests"
how: "claude mcp add maestro -- maestro mcp; agent writes YAML flows kept in the repo; install script is curl | bash so read it first; it controls the device"
url: https://maestro.dev
repo: "https://github.com/mobile-dev-inc/Maestro"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S41]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-27"
---

# Maestro و Maestro MCP

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی cli-2.12.0 (۲۰۲۶-۱۰-۲۶)؛ Apache-2.0 بی‌تغییر.
✅ cli-2.11.0. iOS، Android و وب. MCP داخل CLI: `claude mcp add maestro -- maestro mcp`. عامل صفحه را می‌بیند و تست YAML می‌نویسد که در مخزن می‌ماند.

## دستور سریع
✅ ([README](https://github.com/mobile-dev-inc/Maestro)، cli-2.12.0): Java 17+ لازم است؛ نصب با `curl | bash` است، اسکریپت را پیش از اجرا بخوان.
```bash
java -version && curl -fsSL "https://get.maestro.mobile.dev" | bash
printf 'appId: com.google.android.contacts\n---\n- launchApp:\n    clearState: true\n- tapOn: "Create contact"\n' > contacts.yaml
maestro test contacts.yaml          # شبیه‌ساز Android روشن باشد
claude mcp add maestro -- maestro mcp
```
✅ تنظیم‌های مهم: `clearState: true` در `launchApp` هر اجرا را از حالت تازه شروع می‌کند؛ فایل‌های flow را در مخزن نگه دار؛ در CI اگر درایور دیر بالا آمد `MAESTRO_DRIVER_STARTUP_TIMEOUT` را بالا ببر (پیش‌فرض ۱۵۰۰۰ میلی‌ثانیه Android، ۱۲۰۰۰۰ iOS).
خطاهای رایج: ⚠️ MCP دستگاه را کنترل می‌کند؛ فقط روی اپ و دستگاه خودت. iOS بدون macOS و Xcode ممکن نیست ([تست اپ](../domains/apps/app-testing.md))). اگر `maestro` پیدا نشد، `~/.maestro/bin` را به PATH اضافه کن (مسیر از مستندات رسمی نصب Linux).
💲 ([maestro.dev/pricing](https://maestro.dev/pricing)): CLI، MCP و Studio رایگان؛ Maestro Cloud ۲۵۰ دلار در ماه برای هر دستگاه هم‌زمان.

## کی استفاده کنیم
🧭 لایه‌ی اصلی تست هر اپ موبایل.

## قیمت و مجوز
✅ CLI رایگان؛ Maestro Cloud پولی؛ Studio رایگان ولی کد بسته.

## ریسک و هشدار
⚠️ نصب با `curl … | bash`؛ اسکریپت را اول بخوان. به دستگاه دسترسی دارد.

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41)
