---
name: Android SDK و Android CLI (خط فرمان، بدون Android Studio)
slug: android-sdk-cli
category: app-testing
domains: [apps]
verdict: adopt
status: researched
summary: نصب Android SDK، ساخت و شبیه‌ساز فقط با ابزار خط فرمان رسمی؛ Android CLI تازه‌ی Google برای عامل‌ها
use_when: "building or testing a Flutter or native Android app without Android Studio ; setting up Android SDK and emulator on a Linux machine from the command line"
how: "install Google commandlinetools to ~/Android/Sdk/cmdline-tools/latest, use a full JDK 17+ (not JRE), a human accepts licences via sdkmanager --licenses; prefer new `android sdk` over deprecated sdkmanager; follow the card steps"
url: https://developer.android.com/tools/agents/android-cli
repo: ""
license: "مجوز Android SDK (باید پذیرفته شود)"
pricing: free
risk: medium
sources: [S127]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Android SDK و Android CLI

## چیست
✅ ابزار خط فرمان رسمی Google (`commandlinetools-linux-16111833_latest.zip`) که حالا **Android CLI** (فرمان `android`، نسخه‌ی 1.0.16625370) را هم دارد. ✅ خود `sdkmanager` هنگام اجرا اعلام می‌کند منسوخ است و `android sdk` جایگزین آن است. Android CLI برای عامل‌ها ساخته شده: `android sdk`، `android emulator`، `android screen capture`، `android input tap/text`، `android create`، `android run`، `android docs search`، `android skills`، و `android init` که مهارت `android-cli` را برای عامل نصب می‌کند. ❓ پشتیبانی از MCP در مستندات نیست.

✅ (۲۰۲۶-۱۰-۳۰، [S205](../sources/README.md#s205)) فرمان‌های تازه‌ی Android Dev Summit 26: `android device remote`، `preview`، `profiler leakcanary`، `analyze`، `signals`، `build`، `skills add` و `docs search` ([وبلاگ](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance)).
✅ پلاگین رسمی Claude Code: [android/android-cli-plugin](https://github.com/android/android-cli-plugin) (Apache-2.0، Google). نصب: `/plugin marketplace add android/android-cli-plugin` و بعد `/plugin install android-cli@android-cli-plugin`. فقط یک اسکیل `android-cli` دارد؛ hook، MCP و اسکریپت ندارد. ⚠️ خود اسکیل به عامل می‌گوید CLI را با `curl … install.sh | bash` از dl.google.com نصب کند؛ اگر CLI را با روش بالا نصب کرده‌ای، این قدم را رد کن.

## دستور سریع
✅ نصب: مراحل بخش «نصب» پایین (zip رسمی `commandlinetools` در `~/Android/Sdk/cmdline-tools/latest`، JDK کامل ۱۷+، `sdkmanager --licenses` با انسان). بعد، فرمان‌های `android` ([مرجع رسمی](https://developer.android.com/tools/agents/android-cli/commands)):
```bash
printf '%s\n' '--no-metrics' >> ~/.androidrc             # ✅ هر پرچم در یک خط؛ آمار خاموش
android sdk install platform-tools                        # یا <package> @<version>
android emulator create --list-profiles && android emulator create <profile>
android emulator list && android emulator start <device> --headless
android create --list                                     # فهرست قالب‌ها؛ بعد android run <apk> و android screen capture --output=shot.png
```
✅ تنظیم‌های مهم: `--no-metrics` (آمار پیش‌فرض روشن است)، `--sdk=<مسیر>` در `.androidrc`، `--headless` برای شبیه‌ساز بی‌پنجره، `--cold` برای شروع بدون snapshot.
خطاهای رایج (دفتر پروژه‌ها): 🔬 فقط JRE: ساخت Gradle با `JAVA_COMPILER` می‌شکند؛ 🔬 `adb: device offline` اگر شبیه‌ساز وسط نصب بسته شود؛ کاربر در گروه `kvm` باشد؛ آخر کار `adb kill-server` (همه در بخش‌های پایین). `android emulator` روی Windows غیرفعال است. اسکیل پلاگین مسیر نصب `curl | bash` را به عامل می‌دهد؛ رد کن.

## کی استفاده کنیم
🧭 برای ساخت و آزمون اپ Flutter یا اپ بومی روی Android، بدون نصب Android Studio. برای آزمون رابط کنار [Maestro](maestro.md) و [Dart MCP](dart-mcp-server.md).

## نصب (Linux، روش کارکرده روی رایانه‌ی آزمون، ۲۰۲۶-۱۰-۲۱)
1. نشانی و sha1 تازه‌ترین بسته از `https://dl.google.com/android/repository/repository2-3.xml`؛ دانلود و بررسی با `sha1sum -c`؛ باز کردن در `~/Android/Sdk/cmdline-tools/latest`.
2. **JDK کامل** ۱۷ یا بالاتر، نه فقط JRE (این‌جا `openjdk-21-jdk-headless` از Debian، با sudo). ⚠️ با JRE تنها، `sdkmanager` کار می‌کند ولی ساخت Gradle با خطای `Toolchain installation ... does not provide the required capabilities: [JAVA_COMPILER]` می‌شکند.
3. پذیرش مجوز (کار انسان، نه عامل): `sdkmanager --licenses`.
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
⚠️ Android CLI به‌طور پیش‌فرض آمار استفاده می‌فرستد (نام فرمان و گزینه، نام عامل مثل CLAUDE، stack trace بی‌نام؛ نه خروجی، مسیر یا نام پروژه). خاموش کردن: `--no-metrics`. ❓ مستندات می‌گوید `~/.androidrc` پرچم‌ها را بر هر اجرا اعمال می‌کند ولی خاموشی سراسری را صریحاً تأیید نمی‌کند؛ با گذاشتن `--no-metrics` در `~/.androidrc` `android --version` بی‌خطا اجرا شد.
⚠️ `android emulator` روی Windows غیرفعال است. ⚠️ `adb emu kill` شبیه‌ساز را می‌بندد ولی سرور `adb` می‌ماند؛ آخر کار `adb kill-server`.
⚠️ تصویرهای `ps16k` (صفحه‌ی حافظه‌ی ۱۶ کیلوبایتی) برای آزمون سازگاری ۱۶KB لازم‌اند؛ برای کار روزمره تصویر عادی کافی است.

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [Flutter](flutter.md) · [اولین اپ موبایل تا فروشگاه](../domains/apps/mobile-launch-playbook.md) · [S127](../sources/README.md#s127)
