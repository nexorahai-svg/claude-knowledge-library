---
name: Patrol
slug: patrol
category: app-testing
domains: [apps]
verdict: trial
status: researched
summary: توسعه‌ی تست یکپارچه‌ی Flutter برای لمس دیالوگ‌های بومی
use_when: "Flutter integration tests that must interact with system dialogs, permissions or notifications"
how: "Trial first on a small task: flutter pub global activate patrol_cli, patrol doctor, flutter pub add patrol --dev, add a patrol section in pubspec.yaml, then patrol test -t patrol_test/example_test.dart; needs native Android/iOS setup"
url: https://patrol.leancode.co
repo: "https://github.com/leancodepl/patrol"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S41]
found_in: []
last_checked: 2026-11-01
next_check: "2026-12-01"
---

# Patrol

## چیست
✅ patrol 4.10.0 (۲۰۲۶-۰۹-۱۵ در pub.dev)، patrol_cli 4.8.0 (۲۰۲۶-۱۰-۲۷). اجازه‌ها و اعلان‌های سیستم را هم لمس می‌کند.
✅ نصب و اجرا (https://patrol.leancode.co/getting-started، ۲۰۲۶-۱۰-۲۷): flutter pub global activate patrol_cli ; flutter pub add patrol --dev ; patrol test -t patrol_test/example_test.dart

## کی استفاده کنیم
🧭 وقتی تست Flutter باید با دیالوگ سیستم کار کند.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
✅ patrol_mcp 0.2.1 (README و سورس مخزن leancodepl/patrol، ۲۰۲۶-۱۱-۰۱): سرور MCP با `dart run patrol_mcp`؛ اجرای آزمون، نشست develop با hot restart، لاگ، اسکرین‌شات و درخت رابط بومی. هنوز 0.x و نزد ما نیازموده؛ جدول سازگاری با patrol_cli را در مستندات ببین.

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41)
