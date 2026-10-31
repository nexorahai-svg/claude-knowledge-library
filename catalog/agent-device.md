---
name: agent-device (Callstack)
slug: agent-device
category: app-testing
domains: [apps, security]
verdict: assess
status: researched
summary: CLI و سرور MCP از Callstack برای کنترل و راستی‌آزمایی اپ iOS، Android، وب و دسکتاپ توسط عامل از راه درخت دسترس‌پذیری؛ MIT و فعال
use_when: "agent-driven QA of a Flutter or Expo app on a simulator or emulator ; collecting screenshot or video evidence for a bug ; comparing MCP device drivers before choosing one"
how: "Do not install without the user's yes; npm install -g agent-device@latest then agent-device mcp; use only on simulators and test devices, never a personal phone"
url: https://github.com/callstack/agent-device
repo: "https://github.com/callstack/agent-device"
license: "MIT"
pricing: free
risk: high
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# agent-device (Callstack)

## چیست
✅ ابزار متن‌باز برای اینکه عامل برنامه‌نویسی اپ در حال اجرا را ببیند و کنترل کند ([README](https://github.com/callstack/agent-device/blob/main/README.md)). سه راه ورود: CLI، سرور MCP (`agent-device mcp`) و API تایپ‌شده‌ی Node.js.
- ✅ هدف‌ها: iOS، Android، HarmonyOS (شبیه‌ساز، امولاتور و دستگاه واقعی)، تلویزیون، وب، macOS و لینوکس. عامل «snapshot» دسترس‌پذیری می‌خواند، با ارجاع و انتخابگر عمل می‌کند و اسکرین‌شات و ویدیو به‌عنوان شاهد ذخیره می‌کند.
- ✅ آخرین نسخه v0.21.33 (۲۰۲۶-۱۰-۲۷) در https://github.com/callstack/agent-device/releases؛ حدود ۵٫۲ هزار ستاره؛ آخرین push ۲۰۲۶-۱۰-۲۸؛ آرشیو نشده. هنوز زیر ۱٫۰ است.
- ✅ نیاز: Node.js 22.12 به بالا (وب: Node 24). نصب: `npm install -g agent-device@latest`.
- ✅ می‌تواند به ابر دستگاه (BrowserStack، AWS Device Farm، TestMu AI، Limrun) وصل شود؛ این بخش اختیاری است.
- ✅ خود README می‌گوید موتور موبایل ابزار [tester-army-e2e](tester-army-e2e.md) است.

## قیمت و مجوز
✅ MIT، حق نسخه ۲۰۲۶ Callstack (https://github.com/callstack/agent-device/blob/main/LICENSE)؛ استفاده‌ی تجاری آزاد. رایگان؛ هزینه‌ی ابر دستگاه (اگر خواستی) جداست.

## ریسک و هشدار
- ✅ دستگاه و شبیه‌ساز را کنترل می‌کند (نصب و اجرای اپ، ضبط صفحه)؛ پس ریسک بالاست. فقط روی شبیه‌ساز و دستگاه آزمایشی.
- ✅ سیاست امنیتی دارد؛ فقط آخرین نسخه وصله می‌گیرد ([SECURITY.md](https://github.com/callstack/agent-device/blob/main/SECURITY.md)).
- 🧭 نسخه‌ی ۰٫x: فرمان‌ها ممکن است عوض شوند. پیش از نصب فایل‌ها را بخوان (قانون ۴).

## کی استفاده کنیم
🧭 وقتی آزمون عامل‌محور اپ Flutter یا Expo روی شبیه‌ساز لازم است و می‌خواهی شاهد تصویری بگیری. مقایسه با [mobile-mcp](mobile-mcp.md) و [Maestro](maestro.md) روی یک اپ کوچک آزمایشی پیش از انتخاب. پیشنهاد ارتقا به trial: ندارم تا یک آزمون واقعی انجام شود.

## مرتبط
[S191](../sources/README.md#s191) · [آزمون اپ](../domains/apps/app-testing.md) · [mobile-mcp](mobile-mcp.md) · [Maestro](maestro.md) · [tester-army-e2e](tester-army-e2e.md)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد خوانده شد (SHA `e560224`): postinstall و تله‌متری ندارد. تنها تماس خودکار، بررسی نسخه از registry.npmjs.org است که با `AGENT_DEVICE_NO_UPDATE_NOTIFIER=1` خاموش می‌شود. ابر `cloud.agent-device.dev` فقط با ورود دستی (`auth login`) به کار می‌آید. ❓ هسته‌ی daemon کامل خوانده نشد.

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v0.21.35 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
