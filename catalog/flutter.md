---
name: Flutter
slug: flutter
category: app-frameworks
domains: [apps]
verdict: adopt
status: researched
summary: فریم‌ورک Google برای یک کد روی iOS، Android، Windows، macOS، Linux و وب
use_when: "starting a cross-platform app for mobile and desktop from one codebase ; any new Flutter project"
how: "Install stable Flutter 3.47.x (official linux tar.xz from releases_linux.json, verify sha256); not the 3.50 beta for real projects; use the Dart MCP; iOS builds need a Mac or Codemagic; fa and ar localizations are built in"
url: https://flutter.dev
repo: "https://github.com/flutter/flutter"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S38, S41, S94, S208]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-26"
---

# Flutter

## چیست
✅ نسخه‌ی پایدار 3.47.9 (۲۰۲۶-۱۰-۲۹؛ قبلی 3.47.8 در ۲۰۲۶-۱۰-۲۳ و 3.47.7 در ۲۰۲۶-۱۰-۰۸؛ Dart 3.13.5 تا 3.47.8 و 3.13.7 برای 3.47.9 (`releases_linux.json`)؛ صفحه‌ی یادداشت انتشار هنوز 3.47.8 می‌گوید و محتوای اصلاح‌ها خوانده نشد ❓؛ [S208](../sources/README.md#s208))؛ بتا 3.50.0-0.2.pre (releases_linux.json، جاروی ۲۰۲۶-۱۰-۲۸). همه‌ی سکوهای موبایل و دسکتاپ رسماً پشتیبانی می‌شوند. MCP رسمی Dart و قانون‌های رسمی عامل دارد.
🧭 یادداشت: بتای 3.50.0-0.1.pre از ۲۰۲۶-۱۰-۱۴ در فایل رسمی انتشار هست؛ نسخه‌ی اصلی ما همان پایدار است و بتا برای پروژه‌ی واقعی نیست. در جاروی بعدی دنبال 3.50 پایدار باش ([S166](../sources/README.md#s166)).

✅ روی Linux نصب و آزموده شد (۲۰۲۶-۱۰-۲۱): بایگانی رسمی `flutter_linux_3.47.7-stable.tar.xz` از `releases_linux.json`، بررسی sha256، باز شده در `~/development/flutter`، مسیر در `~/.bashrc`، آمار با `flutter --disable-analytics` خاموش. `flutter doctor`: Chrome و وب سبز؛ بعد از نصب `ninja-build` و `libgtk-3-dev` (با sudo) دسکتاپ لینوکس سبز شد؛ با [Android SDK خط فرمان](android-sdk-cli.md) Android هم سبز شد.

## دستور سریع
✅ نصب (Linux، [releases_linux.json](https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json)): بایگانی `flutter_linux_3.47.9-stable.tar.xz` را با sha256 بررسی کن و باز کن؛ بسته‌های `ninja-build` و `libgtk-3-dev` برای دسکتاپ (بالا). سپس:
```bash
flutter --disable-analytics && flutter doctor          # 🔬 آمار خاموش، وضعیت سبز
flutter create my_app && cd my_app && flutter run -d <device>   # ✅ docs.flutter.dev/reference/create-new-app
flutter build appbundle --release                      # ✅ خروجی Google Play؛ برای APK: flutter build apk
```
✅ تنظیم‌های مهم: امضای Android با `android/key.properties` و keystore (`keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -storetype JKS -keysize 2048 -validity 10000 -alias upload`)، فایل را در مخزن عمومی نگذار؛ نسخه‌ی staging و production با `flutter run --flavor staging` ([flavors](https://docs.flutter.dev/deployment/flavors)). R8 در release روشن است؛ خاموش با `--no-shrink`.
خطاهای رایج (دفتر پروژه‌ها): 🔬 با JRE تنها ساخت Gradle می‌شکند (`JAVA_COMPILER`)؛ JDK کامل ۱۷+ لازم است، و `adb: device offline` وقتی شبیه‌ساز وسط نصب بسته شود ([Android SDK](android-sdk-cli.md)). 🔬 `google_fonts` فونت را در لحظه دانلود می‌کند و با Flutter 3.47 خطای نوع داد؛ فونت را داخل اپ بگذار ([طراحی رابط اپ](../domains/apps/app-design.md)). ساخت iOS مک یا [Codemagic](codemagic.md) می‌خواهد.

## کی استفاده کنیم
🧭 انتخاب اول برای اپی که موبایل و دسکتاپ را با هم می‌خواهد.

## قیمت و مجوز
✅ رایگان، BSD-3.

## ریسک و هشدار
✅ `fa` و `ar` در Material، Cupertino و Widgets آماده‌اند (اصلاح ۲۰۲۶-۱۰-۱۹). ⚠️ ساخت iOS مک یا Codemagic می‌خواهد؛ به‌روزرسانی رسمی از راه دور ندارد. پشتیبانی مک Intel در حال حذف است.

## مرتبط
[فریم‌ورک چندسکویی](../domains/apps/cross-platform-frameworks.md) · [S38](../sources/README.md#s38) · [S41](../sources/README.md#s41)
