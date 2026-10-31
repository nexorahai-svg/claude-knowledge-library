---
name: flutter_secure_storage
slug: flutter-secure-storage
category: app-frameworks
domains: [apps]
verdict: trial
status: researched
summary: بسته‌ی Flutter برای نگه داشتن توکن ورود در Keychain (iOS) و رمزنگاری با کلید Keystore (Android)
use_when: "storing a login/session token in a Flutter app ; protecting tokens with Keychain or Keystore"
how: "flutter pub add flutter_secure_storage (11.2.0, BSD-3); on iOS use accessibility first_unlock_this_device; on Flutter Web it works only over HTTPS or localhost and is weaker than Keychain, so prefer a server HttpOnly cookie; turn off Android auto backup"
url: https://pub.dev/packages/flutter_secure_storage
repo: "https://github.com/juliansteenbakker/flutter_secure_storage"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-31
next_check: "2027-01-17"
---

# flutter_secure_storage

## چیست
✅ نسخه‌ی `11.2.0` (۲۰۲۶-۰۹-۱۶)، ناشر تأییدشده `steenbakker.dev`، ۱۶۰ از ۱۶۰ امتیاز pub.dev، مجوز BSD-3-Clause (https://pub.dev/packages/flutter_secure_storage).
✅ iOS و macOS: Keychain، با گزینه‌ی `accessibility` (مثلاً `first_unlock_this_device`). Android: از نسخه‌ی ۱۰ رمزنگاری سفارشی؛ `encryptedSharedPreferences` (Jetpack Security کنارگذاشته‌شده) دیگر توصیه نمی‌شود. احراز بیومتریک اختیاری.

## دستور سریع
✅ ([pub.dev](https://pub.dev/packages/flutter_secure_storage)، 11.2.0):
```bash
flutter pub add flutter_secure_storage
```
```dart
WidgetsFlutterBinding.ensureInitialized();     // پیش از هر استفاده در main
const storage = FlutterSecureStorage();
await storage.write(key: 'token', value: t);   // خواندن: storage.read(key: 'token')؛ حذف: storage.delete(key: 'token')
await storage.write(key: 'k', value: v, iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock_this_device));
```
✅ تنظیم‌های مهم ([README](https://github.com/juliansteenbakker/flutter_secure_storage)): `accessibility` در iOS؛ در `android/app/src/main/AndroidManifest.xml` روی `<application>` مقدار `android:allowBackup="false"`؛ از نسخه‌ی ۱۰ رمزنگاری سفارشی است و `encryptedSharedPreferences` توصیه نمی‌شود؛ `minSdk` پروژه ≥ ۲۴ (README: API 23، `build.gradle` مخزن: 24).
خطاهای رایج: ✅ پشتیبان خودکار Android باعث `InvalidKeyException: Failed to unwrap key` می‌شود (allowBackup را خاموش کن، [عملیات اپ](../domains/apps/app-operations.md)). ✅ روی وب فقط HTTPS یا localhost کار می‌کند؛ 🧭 توکن وب را در کوکی `HttpOnly` سرور بگذار ([ورود مشتری](../domains/website/04-tech/customer-auth.md)). ⚠️ داده‌ی Keychain ممکن است بعد از حذف اپ بماند؛ در اولین اجرا پاکش کن.

## کی استفاده کنیم
🧭 برای نگه داشتن توکن نشست اپ Flutter که با سرور خودمان وارد می‌شود ([ورود مشتری، اپ موبایل](../domains/website/04-tech/customer-auth.md)). روی iOS گزینه‌ی `first_unlock_this_device` تا توکن به پشتیبان iCloud و گوشی دیگر نرود.

## قیمت و مجوز
✅ رایگان، BSD-3-Clause.

## ریسک و هشدار
⚠️ نسخه‌ی وب این بسته به امنیت Keychain نیست؛ در Flutter Web توکن را در کوکی `HttpOnly` سرور بگذار. ⚠️ پشتیبان خودکار اندروید را خاموش کن ([عملیات اپ](../domains/apps/app-operations.md)). ⚠️ داده‌ی Keychain ممکن است بعد از حذف اپ بماند؛ در اولین اجرا پاکش کن.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [عملیات اپ](../domains/apps/app-operations.md) · [S125](../sources/README.md#s125)
