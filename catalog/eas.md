---
name: EAS (Expo Application Services)
slug: eas
category: app-publishing
domains: [apps]
verdict: trial
status: researched
summary: ساخت ابری، امضا و ارسال اپ Expo به فروشگاه‌ها
use_when: "building and submitting an Expo app to the stores in the cloud ; getting an iOS build without a Mac"
how: "Trial first on a small task: eas build with the free plan (15 Android + 15 iOS builds per month, slow queue); extra builds cost $1-2 Android, $2-4 iOS; first choice for Expo apps"
url: https://expo.dev/eas
repo: ""
license: "سرویس Expo"
pricing: freemium
risk: low
sources: [S42]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-16"
---

# EAS (Expo Application Services)

## چیست
✅ رایگان: تا ۱۵ ساخت Android و ۱۵ iOS، صف کند، ۴۵ دقیقه. Starter ۱۹ و Production ۱۹۹ دلار در ماه.

## دستور سریع
✅ ([docs.expo.dev/build](https://docs.expo.dev/build/setup/)، npm: eas-cli 27.2.0):
```bash
npm install --global eas-cli && eas login
eas build:configure                                 # eas.json با سه profile: development، preview، production
eas build --platform android --profile preview      # خروجی قابل نصب (distribution: internal)
eas build --platform android                        # AAB برای فروشگاه
eas submit --platform android --path ./my-app.aab   # یا --auto-submit کنار eas build
```
✅ تنظیم‌های مهم: profile `preview` برای آزمون و `production` برای فروشگاه؛ APK فقط با `distribution: internal` یا `android.buildType: apk` ساخته می‌شود و به Google Play فرستاده نمی‌شود. در `eas.json` بخش `cli` می‌شود `version` را قفل کرد و `appVersionSource` را گذاشت. پیش از ساخت iOS حساب توسعه‌دهنده‌ی فروشگاه لازم است.
خطاهای رایج: ✅ اولین `eas submit` برای Android اپ را در Play Console و یک Google Service Account می‌خواهد و نسخه‌ی اول روی مسیر آزمون داخلی می‌رود. ✅ طرح رایگان ساخت را ۴۵ دقیقه محدود می‌کند و صف کند دارد؛ حساب‌ها و هزینه‌ی فروشگاه‌ها: [انتشار اپ](../domains/apps/publishing-apps.md).
💲 ([expo.dev/pricing](https://expo.dev/pricing)، ۲۰۲۶-۱۰-۳۱): رایگان ۰ (۱۵ ساخت Android و ۱۵ iOS)، Starter ۱۹ دلار در ماه (با ۴۵ دلار اعتبار ساخت)، Production ۱۹۹ دلار (با ۲۲۵ دلار اعتبار)؛ بعد از اعتبار: ساخت متوسط Android ۱ و iOS ۲ دلار، بزرگ ۲ و ۴ ([جدول](https://docs.expo.dev/billing/usage-based-pricing/)).

## کی استفاده کنیم
🧭 اولین انتخاب برای اپ Expo.

## قیمت و مجوز
✅ اضافه‌ی هر ساخت Android ۱ تا ۲ و iOS ۲ تا ۴ دلار.

## ریسک و هشدار
—

## مرتبط
[انتشار اپ](../domains/apps/publishing-apps.md) · [S42](../sources/README.md#s42)
