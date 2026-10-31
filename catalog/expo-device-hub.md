---
name: expo-device-hub
slug: expo-device-hub
category: app-testing
domains: [apps]
verdict: trial
status: researched
summary: افزونه‌ی DevTools اکسپو برای دیدن و کنترل شبیه‌ساز در مرورگر
use_when: "Expo app development with simulators and emulators in the browser ; letting an agent see device screens"
how: "use with expo start per README; try on a throwaway Expo project"
url: https://github.com/expo/expo-device-hub
repo: "https://github.com/expo/expo-device-hub"
license: "MIT (650 Industries) + بخش‌های vendored با Apache-2.0"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# expo-device-hub

## چیست
✅ افزونه DevTools اکسپو که شبیه‌ساز iOS و امولاتور اندروید را در مرورگر نشان و کنترل می‌دهد. ✅ سازمان رسمی expo؛ متن LICENSE خودش MIT است (API گیت‌هاب NOASSERTION نشان می‌دهد). ❓ هنوز ۱۲۵ issue باز.

## دستور سریع
✅ ([README رسمی](https://github.com/expo/expo-device-hub)؛ npm: 0.19.1) نیازمند Expo SDK 57 یا بالاتر:
```bash
npx expo install expo-device-hub
npx expo start        # نشانی افزونه در ترمینال چاپ می‌شود: http://localhost:8081/_expo/plugins/expo-device-hub
npx expo-device-hub   # حالت مستقل، بدون پروژه‌ی Expo
```
✅ تنظیم‌های مهم: شبیه‌ساز iOS فقط macOS با Xcode؛ امولاتور Android به SDK (`emulator`، `adb`) نیاز دارد، پس روی Linux فقط Android ([Android SDK](android-sdk-cli.md)). متغیر `EXPO_DEVICE_HUB_SCREENSHOT_DIRECTORY` هر اسکرین‌شات را در یک پوشه ذخیره می‌کند.
خطاهای رایج: 👀 این ابزار را اجرا نکردیم، فقط README خواندیم؛ روی پروژه‌ی آزمایشی امتحان کن. ❓ ۱۲۵ issue باز (بالا). دسترسی به شبیه‌ساز را به عامل فقط روی پروژه‌ی خودت بده.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: Expo app development with simulators and emulators in the browser؛ letting an agent see device screens. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (650 Industries) + بخش‌های vendored با Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۲۷۴ در تاریخ بررسی).
- قیمت: رایگان.
- ✅ بخش‌های vendored (serve-sim, serve-emu) در packages/expo-device-hub/vendor/ تحت Apache-2.0 هستند.

## ریسک و هشدار
- سطح ریسک: low.
- ابزار محلی است؛ پروژه جوان با issueهای زیاد.
- ❓ کد منبع را خط‌به‌خط نخواندم و چیزی را اجرا نکردم؛ فقط README، LICENSE، فایل‌های سطح بالا و grep برای تله‌متری/اسکریپت نصب.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/expo/expo-device-hub

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
