---
name: mcp_flutter (Flutter MCP Toolkit)
slug: mcp-flutter
category: app-testing
domains: [apps, security]
verdict: trial
status: researched
summary: سرور MCP و بسته‌ی Flutter برای دیدن، لمس، hot reload و خواندن لاگ اپ Flutter در حال اجرا؛ MIT، نگهدارنده‌ی تک‌نفره
use_when: "letting an agent inspect and drive a running Flutter app in debug mode ; semantic snapshots, taps, typing, hot reload and logs in one closed loop ; exposing app-specific actions to an agent"
how: "Trial first on a small task: add the mcp_toolkit package and run flutter run --debug, MCP registry name io.github.Arenukvern/flutter-mcp-toolkit; debug builds and test data only, remove the package from release builds"
url: https://github.com/Arenukvern/mcp_flutter
repo: "https://github.com/Arenukvern/mcp_flutter"
license: "MIT"
pricing: free
risk: high
sources: [S166]
found_in: [inbox/2026-10-19-watch]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# mcp_flutter (Flutter MCP Toolkit)

## چیست
✅ سرور MCP نوشته‌شده با Dart به‌همراه بسته‌ی `mcp_toolkit` برای اپ ([README](https://github.com/Arenukvern/mcp_flutter)). عامل می‌تواند اپ در حال اجرا را بررسی کند، snapshot معنایی بگیرد، روی ویجت‌ها بزند، در فرم تایپ کند، hot reload کند و لاگ بخواند؛ خود اپ هم می‌تواند ابزار MCP اختصاصی ثبت کند.
- ✅ نسخه v7.0.1 (۲۰۲۶-۱۰-۱۷)، پیش‌تر v7.0.0 (۱۰-۰۳) و v6.0.0 (۱۰-۰۲) در https://github.com/Arenukvern/mcp_flutter/releases؛ سه نسخه‌ی اصلی در دو هفته یعنی API هنوز سریع تغییر می‌کند. حدود ۳۹۴ ستاره؛ آخرین push ۲۰۲۶-۱۰-۱۷؛ آرشیو نشده؛ ۱۷ مشارکت‌کننده، نگهدارنده‌ی اصلی یک نفر.
- ✅ ثبت‌شده در ثبت رسمی MCP با نام `io.github.Arenukvern/flutter-mcp-toolkit`. نیاز به Flutter 3.44 به بالا (طبق نشان README) و اجرای `flutter run --debug`.
- 🧭 Flutter خودش هم سرور MCP رسمی دارد (افزونه‌ی dart-flutter در این ماشین)؛ این ابزار کنترل ورودی و snapshot معنایی را بیشتر می‌دهد. مقایسه نشده.

## قیمت و مجوز
✅ MIT، حق نسخه ۲۰۲۵ Anton Malofeev (https://github.com/Arenukvern/mcp_flutter/blob/main/LICENSE)؛ رایگان، استفاده‌ی تجاری آزاد.

## ریسک و هشدار
- ✅ اپ را کنترل می‌کند (لمس، تایپ، اجرای کنش‌های اختصاصی)؛ پس ریسک بالاست.
- 🧭 بسته‌ی `mcp_toolkit` فقط باید در بیلد debug و آزمایشی بماند؛ در انتشار نهایی حذف شود تا درگاه کنترل در محصول نباشد.
- 🧭 نگهدارنده‌ی تک‌نفره و تغییر سریع نسخه‌ها؛ نسخه را ثابت کن. پیش از نصب کد را بخوان (قانون ۴).

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: a debug-only test app, after reading the server code. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
🧭 چون Flutter انتخاب ماست، برای حلقه‌ی «تغییر، hot reload، دیدن نتیجه» در توسعه با عامل ارزش آزمون دارد؛ کنار [mobile-mcp](mobile-mcp.md) و [agent-device](agent-device.md). ارتقا به trial: بله پس از خواندن کد، فقط روی اپ آزمایشی، چون MIT است و فعال و Flutter-اختصاصی.

## مرتبط
[آزمون اپ](../domains/apps/app-testing.md) · [S166](../sources/README.md#s166) · [mobile-mcp](mobile-mcp.md)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد سرور خوانده شد (SHA `a58f120`، ۸۸ فایل از ۹۱). تله‌متری ندارد. شبکه فقط محلی است (VM service و CDP روی 127.0.0.1). تنها تماس بیرونی، خلاصه‌ساز خطای اختیاری OpenAI است که پیش‌فرض خاموش است و رضایت صریح و کلید خود کاربر را می‌خواهد. `install.sh` چکسام SHA256 را می‌سنجد.
- 🧭 سرور به VM service اپ دسترسی کامل دارد (tap، type، hot reload). پس فقط روی اپ debug به کار برو. شرط «پس از خواندن کد» در دامنه‌ی آزمون حالا برآورده شده است.
