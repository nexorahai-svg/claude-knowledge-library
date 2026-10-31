---
name: TesterArmy e2e
slug: tester-army-e2e
category: app-testing
domains: [apps, website]
verdict: assess
status: researched
summary: چارچوب آزمون سرتاسری وب و موبایل با گام‌های زبان طبیعی؛ گام موفق ضبط و بدون مدل بازپخش می‌شود؛ Apache-2.0، آمار ناشناس با امکان خاموش‌کردن
use_when: "E2E tests for a Flutter or Expo app where scripted flows are too brittle ; a web app test suite that mixes scripted steps and agent steps ; replaying agent-recorded steps in CI without model calls"
how: "Trial only on a throwaway project and not without the user's yes; npx e2e init with E2E_TELEMETRY_DISABLED=1 set first; expect API changes before 1.0"
url: https://github.com/tester-army/e2e
repo: "https://github.com/tester-army/e2e"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# TesterArmy e2e

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) برچسب `@e2e-dev/testmu` زیربسته است؛ جریان اصلی e2e@0.22.0 (۲۰۲۶-۱۰-۳۰) و `@e2e-dev/web` 0.15.4؛ Apache-2.0؛ هنوز پیش از ۱.۰: https://github.com/tester-army/e2e/releases
✅ چارچوب آزمون TypeScript ([README](https://github.com/tester-army/e2e)): `agent.act('...')` و `agent.assert('...')` با زبان طبیعی کنار locator و `expect` معمولی. گامی که assertion بعدی تأییدش کند ضبط می‌شود و اجرای بعدی بدون فراخوانی مدل بازپخش می‌شود تا اپ عوض شود؛ آزمون بدون گام عامل اصلاً مدل نمی‌خواهد. اشتراک، کلید API یا مدل محلی خودت.
- ✅ بسته‌ها: `e2e` (نسخه 0.21.3، ۲۰۲۶-۱۰-۲۳)، موتور وب (Playwright: Chromium، Firefox، WebKit)، موتور موبایل (شبیه‌ساز و امولاتور iOS و Android از راه agent-device، یعنی [agent-device](agent-device.md)) و گزارشگر GitHub. نسخه‌ها در https://github.com/tester-army/e2e/releases.
- ✅ نمونه‌ی کامل برای Vite، Next.js، Astro، Angular، Expo، SwiftUI، Compose، Kotlin Multiplatform، Flutter و .NET MAUI در پوشه‌ی `examples/`.
- ✅ حدود ۱۲٫۱ هزار ستاره؛ آخرین push ۲۰۲۶-۱۰-۲۸؛ آرشیو نشده. README می‌گوید در مسیر ۱٫۰ است و API و پیکربندی بین نسخه‌های جزئی عوض می‌شود.
- ❓ کیفیت واقعی بازپخش روی اپ Flutter آزموده نشد. ستاره‌ها بسیار سریع جمع شده‌اند (README به نشان «GitHub Trending» اشاره می‌کند)؛ تعداد ستاره را معیار کیفیت نگیر.

## قیمت و مجوز
✅ چارچوب Apache-2.0 (https://github.com/tester-army/e2e/blob/main/LICENSE) و رایگان؛ استفاده‌ی تجاری آزاد. سازنده TesterArmy است که پلتفرم تجاری آزمون عامل‌محور دارد (https://tester.army)؛ ❓ قیمت آن بررسی نشد و برای چارچوب لازم نیست. هزینه‌ی مدل (توکن) جداست.

## ریسک و هشدار
- ✅ CLI آمار استفاده‌ی ناشناس می‌فرستد (فرمان‌ها، موتورها، محل شکست؛ بدون محتوای آزمون و اپ و بدون اعتبارنامه). خاموش‌کردن: `npx e2e telemetry disable` یا `E2E_TELEMETRY_DISABLED=1` (فهرست فیلدها: https://e2e.tester.army/docs/telemetry).
- 🧭 گام‌های زبان طبیعی به مدل نیاز دارند: کلید API و هزینه‌ی توکن؛ و عامل روی اپ کنترل دارد، پس فقط روی داده‌ی آزمایشی.
- 🧭 README تبلیغ شرکت سازنده را دارد (پیوند utm).

## کی استفاده کنیم
🧭 وقتی جریان‌های [Maestro](maestro.md) شکننده شدند یا آزمون وب و موبایل را در یک چارچوب می‌خواهیم. اول آزمون کوچک روی پروژه‌ی بی‌خطر. ارتقا پیشنهاد نمی‌شود تا ۱٫۰ یا یک آزمون واقعی.

## مرتبط
[S191](../sources/README.md#s191) · [آزمون اپ](../domains/apps/app-testing.md) · [Maestro](maestro.md) · [Playwright MCP](playwright-mcp.md) · [agent-device](agent-device.md)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ پلتفرم TesterArmy: Free صفر (۵ اجرا)، Hobby ماهی ۹۹ دلار (۲۵۰ اجرا)، Startup ماهی ۲۹۹ دلار (۱٬۰۰۰ اجرا)، Enterprise سفارشی؛ سالانه ۱۵٪ تخفیف (https://tester.army/pricing).
- ✅ چارچوب رایگان به ابر آن‌ها نیاز ندارد؛ مدل یا کلید خودت را می‌آوری. فقط تله‌متری ناشناس دارد که با `E2E_TELEMETRY_DISABLED=1` یا `npx e2e telemetry disable` خاموش می‌شود (https://e2e.tester.army/docs/telemetry).
