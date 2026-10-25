---
name: Flutter
slug: flutter
category: app-frameworks
domains: [apps]
verdict: adopt
status: researched
summary: فریم‌ورک Google برای یک کد روی iOS، Android، Windows، macOS، Linux و وب
url: https://flutter.dev
repo: "https://github.com/flutter/flutter"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S38, S41, S94]
found_in: []
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Flutter

## چیست
✅ نسخه‌ی پایدار 3.47.7 (۲۰۲۶-۱۰-۰۸، Dart 3.13.5). همه‌ی سکوهای موبایل و دسکتاپ رسماً پشتیبانی می‌شوند. MCP رسمی Dart و قانون‌های رسمی عامل دارد.

✅ روی رایانه‌ی اصلی نصب شد (۲۰۲۶-۱۰-۲۱): بایگانی رسمی `flutter_linux_3.47.7-stable.tar.xz` از `releases_linux.json`، بررسی sha256، باز شده در `~/development/flutter`، مسیر در `~/.bashrc`، آمار با `flutter --disable-analytics` خاموش. `flutter doctor`: Chrome و وب سبز؛ بعد از نصب `ninja-build` و `libgtk-3-dev` (با sudo، کار کاربر) دسکتاپ لینوکس سبز شد؛ با [Android SDK خط فرمان](android-sdk-cli.md) Android هم سبز شد.

## کی استفاده کنیم
🧭 انتخاب اول برای اپی که موبایل و دسکتاپ را با هم می‌خواهد.

## قیمت و مجوز
✅ رایگان، BSD-3.

## ریسک و هشدار
✅ `fa` و `ar` در Material، Cupertino و Widgets آماده‌اند (اصلاح ۲۰۲۶-۱۰-۱۹). ⚠️ ساخت iOS مک یا Codemagic می‌خواهد؛ به‌روزرسانی رسمی از راه دور ندارد. پشتیبانی مک Intel در حال حذف است.

## مرتبط
[فریم‌ورک چندسکویی](../domains/apps/cross-platform-frameworks.md) · [S38](../sources/README.md#s38) · [S41](../sources/README.md#s41)
