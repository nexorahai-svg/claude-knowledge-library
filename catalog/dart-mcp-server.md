---
name: Dart و Flutter MCP Server
slug: dart-mcp-server
category: app-testing
domains: [apps]
verdict: adopt
status: researched
summary: MCP رسمی تیم Dart که عامل را به اپ Flutter در حال اجرا وصل می‌کند
use_when: "working on any Flutter project with an agent ; running the app, hot reload, tests and widget tree inspection from Claude"
how: "claude mcp add dart --scope user -- ~/development/flutter/bin/dart mcp-server (Dart SDK 1.2.1, experimental); verify with claude mcp list; it starts/stops processes and runs tests, so use it on our own projects; hot reload after code changes"
url: https://docs.flutter.dev/ai/mcp-server
repo: "https://github.com/dart-lang/ai"
license: "BSD-3-Clause"
pricing: free
risk: medium
sources: [S41, S38]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-26"
---

# Dart و Flutter MCP Server

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 1.2.2 (۲۰۲۶-۱۰-۲۷): listConnectedApps بدون اپ دیگر خطا نمی‌دهد؛ پیام خطای پیش از اتصال، URI‌های DTD و فرمان connect دقیق را می‌گوید؛ اتصال دوباره به DTD وصل‌شده موفق است. BSD-3-Clause بی‌تغییر (https://github.com/dart-lang/ai/releases/tag/dart_mcp_server-v1.2.2).
✅ dart_mcp_server 1.2.1، همراه Dart SDK؛ فرمان `dart mcp-server`. اجرا و توقف اپ، hot reload، تست، لاگ، درخت ویجت. برچسب «آزمایشی».

## دستور سریع
✅ ([README رسمی](https://github.com/dart-lang/ai/tree/main/pkgs/dart_mcp_server)، dart_mcp_server 1.2.2؛ Dart 3.9 یا بالاتر؛ برچسب آزمایشی):
```bash
claude mcp add dart --scope user -- ~/development/flutter/bin/dart mcp-server   # 🔬 کار کرد، «Connected» (دفتر پروژه‌ها: ../projects/README.md)
claude mcp list
cd my_app && flutter run --print-dtd                # عامل نشانی DTD را از خروجی می‌خواند
# اپ Dart خالص: dart --observe --print-dtd bin/main.dart   (هر دو پرچم پیش از نام فایل)
```
✅ تنظیم‌های مهم: همه‌ی ابزارها پیش‌فرض روشن نیستند؛ با `--enable flutter_app_lifecycle` (دسته‌ی اجرای اپ) به `args` اضافه کن و فهرست کامل را با `dart mcp-server --help` ببین. اپ Flutter در حالت debug یا profile خودش در DTD ثبت می‌شود، مگر با `--no-dds`.
خطاهای رایج: ابزارهای اپ در حال اجرا تا به DTD وصل نشوی کار نمی‌کنند: اول `listDtdUris` و بعد `connect` با ابزار `dtd` (دستور خود سرور). بعد از هر تغییر کد hot reload یا hot restart بزن. ⚠️ سرور پروسه اجرا و متوقف می‌کند و تست اجرا می‌کند؛ روی پروژه‌ی خودت.

## کی استفاده کنیم
🧭 هر پروژه‌ی Flutter.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
⚠️ پروسه اجرا و متوقف می‌کند و تست اجرا می‌کند. ✅ دستوری که روی رایانه‌ی آزمون کار کرد و `claude mcp list` آن را «Connected» نشان داد (۲۰۲۶-۱۰-۲۱، Dart 3.13.5):
```bash
claude mcp add dart --scope user -- ~/development/flutter/bin/dart mcp-server
```

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41) · [S38](../sources/README.md#s38)
