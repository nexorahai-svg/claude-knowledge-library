---
name: Android SDK و Android CLI (خط فرمان، بدون Android Studio)
slug: android-sdk-cli
category: app-testing
domains: [apps]
verdict: trial
status: researched
summary: نصب Android SDK، ساخت و شبیه‌ساز فقط با ابزار خط فرمان رسمی؛ Android CLI تازه‌ی Google برای عامل‌ها
url: https://developer.android.com/tools/agents/android-cli
repo: ""
license: "مجوز Android SDK (باید پذیرفته شود)"
pricing: free
risk: medium
sources: [S127]
found_in: []
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# Android SDK و Android CLI

## چیست
✅ ابزار خط فرمان رسمی Google (`commandlinetools-linux-16111833_latest.zip`) که حالا **Android CLI** (فرمان `android`، نسخه‌ی 1.0.16625370) را هم دارد. ✅ خود `sdkmanager` هنگام اجرا اعلام می‌کند منسوخ است و `android sdk` جایگزین آن است. Android CLI برای عامل‌ها ساخته شده: `android sdk`، `android emulator`، `android screen capture`، `android input tap/text`، `android create`، `android run`، `android docs search`، `android skills`، و `android init` که مهارت `android-cli` را برای عامل نصب می‌کند. ❓ پشتیبانی از MCP در مستندات نیست.

## کی استفاده کنیم
🧭 برای ساخت و آزمون اپ Flutter یا اپ بومی روی Android، بدون نصب Android Studio. برای آزمون رابط کنار [Maestro](maestro.md) و [Dart MCP](dart-mcp-server.md).

## نصب (Linux، روش کارکرده روی رایانه‌ی اصلی، ۲۰۲۶-۱۰-۲۱)
1. نشانی و sha1 تازه‌ترین بسته از `https://dl.google.com/android/repository/repository2-3.xml`؛ دانلود و بررسی با `sha1sum -c`؛ باز کردن در `~/Android/Sdk/cmdline-tools/latest`.
2. **JDK کامل** ۱۷ یا بالاتر، نه فقط JRE (این‌جا `openjdk-21-jdk-headless` از Debian، با sudo، کار کاربر). ⚠️ با JRE تنها، `sdkmanager` کار می‌کند ولی ساخت Gradle با خطای `Toolchain installation ... does not provide the required capabilities: [JAVA_COMPILER]` می‌شکند.
3. پذیرش مجوز (کار کاربر یا با تأیید صریح او): `sdkmanager --licenses`.
4. بسته‌ها، هم‌راستا با Flutter 3.47 (compileSdk پیش‌فرض ۳۶):
```bash
sdkmanager --install "platform-tools" "emulator" "platforms;android-36" "platforms;android-37.0" \
  "build-tools;37.0.0" "build-tools;36.1.0" "system-images;android-37.0;google_apis_playstore;x86_64"
avdmanager create avd -n pixel_api37 -k "system-images;android-37.0;google_apis_playstore;x86_64" -d pixel_8
flutter config --android-sdk ~/Android/Sdk && flutter doctor --android-licenses
```
5. `ANDROID_HOME` و مسیرهای `cmdline-tools/latest/bin`، `platform-tools`، `emulator` در `~/.bashrc`.

✅ نتیجه: `flutter doctor` برای Android سبز (SDK 37.0.0). کاربر باید در گروه `kvm` باشد. شبیه‌ساز 37.2.12 با `-no-window` در حدود ۵ ثانیه با Android 17 (API 37) بالا آمد و `flutter devices` آن را دید. حجم کل حدود ۴٫۴ گیگابایت.

## آزمون اپ نمونه ۲۰۲۶-۱۰-۲۱
✅ `flutter create --platforms android` و `flutter run -d emulator-5554 --no-resident`: اولین ساخت (با دانلود Gradle و وابستگی‌ها) حدود ۴ دقیقه و ۲۰ ثانیه که به‌خاطر نبود JDK شکست؛ بعد از نصب JDK ساخت debug حدود ۱ دقیقه و ۱۵ ثانیه. اپ روی شبیه‌ساز API 37 باز شد و `adb exec-out screencap -p` از صفحه تصویر گرفت (روش بررسی بی‌دخالت انسان). ⚠️ اگر شبیه‌ساز وسط نصب بسته شود، `adb: device offline` می‌آید؛ APK ساخته‌شده را با `adb install -r` و `adb shell monkey -p <package> -c android.intent.category.LAUNCHER 1` بی‌ساخت دوباره اجرا کن.

## قیمت و مجوز
✅ رایگان؛ مجوز Android SDK باید پیش از نصب بسته‌ها پذیرفته شود.

## ریسک و هشدار
⚠️ Android CLI به‌طور پیش‌فرض آمار استفاده می‌فرستد (نام فرمان و گزینه، نام عامل مثل CLAUDE، stack trace بی‌نام؛ نه خروجی، مسیر یا نام پروژه). خاموش کردن: `--no-metrics`. ❓ مستندات می‌گوید `~/.androidrc` پرچم‌ها را بر هر اجرا اعمال می‌کند ولی خاموشی سراسری را صریحاً تأیید نمی‌کند؛ ما `--no-metrics` را در `~/.androidrc` گذاشتیم و `android --version` بی‌خطا اجرا شد.
⚠️ `android emulator` روی Windows غیرفعال است. ⚠️ `adb emu kill` شبیه‌ساز را می‌بندد ولی سرور `adb` می‌ماند؛ آخر کار `adb kill-server`.
⚠️ تصویرهای `ps16k` (صفحه‌ی حافظه‌ی ۱۶ کیلوبایتی) برای آزمون سازگاری ۱۶KB لازم‌اند؛ برای کار روزمره تصویر عادی کافی است.

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [Flutter](flutter.md) · [اولین اپ موبایل تا فروشگاه](../domains/apps/mobile-launch-playbook.md) · [S127](../sources/README.md#s127)
