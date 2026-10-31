---
name: Codemagic
slug: codemagic
category: app-publishing
domains: [apps]
verdict: trial
status: researched
summary: CI برای ساخت و انتشار اپ موبایل، قوی در Flutter
use_when: "building iOS apps without owning a Mac ; CI and release for a Flutter app"
how: "Trial first on a small task: Add application on codemagic.io, authorize GitHub, pick the Flutter repo, then configure the workflow editor or a codemagic.yaml in the repo root; free 500 macOS M2 min/month, 1 build, 120 min max, then $0.095/min"
url: https://codemagic.io
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: low
sources: [S42]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-26"
---

# Codemagic

## چیست
✅ ۵۰۰ دقیقه‌ی macOS M2 رایگان در ماه، یک ساخت هم‌زمان، حداکثر ۱۲۰ دقیقه؛ بعد ۰.۰۹۵ دلار هر دقیقه.

✅ نصب و اجرا (https://docs.codemagic.io/getting-started/adding-apps/، ۲۰۲۶-۱۰-۲۷): Add application ← GitHub ← انتخاب مخزن ← codemagic.yaml در ریشه مخزن

## دستور سریع
✅ ([docs.codemagic.io](https://docs.codemagic.io/yaml-quick-start/building-a-flutter-app/)): Add application ← GitHub ← مخزن، و فایل `codemagic.yaml` با همین نام در ریشه‌ی مخزن. کمینه برای Flutter:
```yaml
workflows:
  android-workflow:
    name: Android
    max_build_duration: 60
    environment: { flutter: stable }
    scripts:
      - name: Build AAB
        script: flutter pub get && flutter build appbundle --release
    artifacts: [build/**/outputs/**/*.aab]
```
✅ تنظیم‌های مهم: `instance_type: mac_mini_m2` برای iOS (دقیقه‌ی macOS گران‌تر است)؛ `max_build_duration` سقف را می‌گذارد؛ امضای Android با `android_signing` و keystore در Codemagic؛ امضای iOS با `ios_signing` (`distribution_type: app_store`، `bundle_identifier`)، `xcode-project use-profiles` و `flutter build ipa --release --export-options-plist=/Users/builder/export_options.plist`.
خطاهای رایج: بدون `codemagic.yaml` در ریشه‌ی مخزن تنظیم YAML خوانده نمی‌شود. iOS حساب Apple Developer و کلید API App Store Connect می‌خواهد ([راهنمای اپ موبایل](../domains/apps/mobile-launch-playbook.md)). ❓ نام `instance_type` برای Linux را در مستندات نخواندم؛ پیش از استفاده از ماشین Linux بیاب.
💲 ([codemagic.io/pricing](https://codemagic.io/pricing/)، ۲۰۲۶-۱۰-۳۱): طرح فردی ۵۰۰ دقیقه‌ی macOS M2 رایگان در ماه با یک ساخت هم‌زمان؛ بعد Mac mini M2 ۰٫۰۹۵ دلار در دقیقه، Linux و Windows ۰٫۰۴۵.

## کی استفاده کنیم
🧭 ساخت iOS بدون مک خودمان، به‌خصوص Flutter.

## قیمت و مجوز
✅ (https://codemagic.io/pricing/، ۲۰۲۶-۱۰-۲۷) طرح فردی: ۵۰۰ دقیقه‌ی رایگان در ماه روی Mac mini M2، یک ساخت موازی، سقف ۱۲۰ دقیقه برای هر ساخت؛ بعد از آن ۰.۰۹۵ دلار در دقیقه (Linux/Windows ۰.۰۴۵). سرویس تجاری است.

## ریسک و هشدار
—

## مرتبط
[انتشار اپ](../domains/apps/publishing-apps.md) · [S42](../sources/README.md#s42)
