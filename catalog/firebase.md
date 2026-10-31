---
name: Firebase
slug: firebase
category: database-backend
domains: [apps, website]
verdict: adopt
status: researched
summary: سکوی بک‌اند Google: Auth، Firestore، Storage، FCM، Crashlytics، Remote Config
use_when: "adding push notifications (FCM) or crash reporting to a mobile app ; needing Auth, Firestore or Remote Config on the free Spark plan"
how: "use FCM and Crashlytics almost always; do NOT put sensitive personal data in Firebase for UAE users (Auth processes only in the US, Firestore/Storage nearest regions Doha/Dammam, Crashlytics region fixed); SMS login needs paid Blaze; Test Lab shuts down 2027-09-30"
url: https://firebase.google.com
repo: ""
license: "شرایط Google Cloud"
pricing: freemium
risk: medium
sources: [S95, S99]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Firebase

## چیست
✅ FCM، App Check، Crashlytics، Performance و Analytics رایگان‌اند؛ Auth رایگان تا ۵۰ هزار کاربر فعال ماهانه؛ Firestore رایگان ۱ گیگابایت و ۵۰ هزار خواندن و ۲۰ هزار نوشتن در روز؛ Remote Config رایگان تا ۱۰۰ هزار درخواست در روز (از ۲۰۲۶-۰۹-۰۱).

## کی استفاده کنیم
🧭 برای اعلان (FCM) و گزارش خطا تقریباً همیشه؛ برای داده‌ی شخصی حساس در امارات نه.

## قیمت و مجوز
✅ طرح Spark رایگان؛ پیامک ورود فقط در Blaze و برای هر پیامک پول.

## ریسک و هشدار
⚠️ **Firebase Auth فقط در آمریکا پردازش می‌کند.** Firestore و Storage نزدیک‌ترین منطقه‌شان دوحه و دمام است، نه امارات؛ Storage در Spark سهمیه‌ی رایگان ندارد. Crashlytics منطقه‌ی قابل انتخاب ندارد. ⚠️ Firebase Test Lab ۲۰۲۷-۰۹-۳۰ خاموش می‌شود.

## مرتبط
[بک‌اند اپ](../domains/apps/app-backend.md) · [عملیات پس از انتشار](../domains/apps/app-operations.md) · [S95](../sources/README.md#s95) · [S99](../sources/README.md#s99)

🧭 (۲۰۲۶-۱۰-۳۱: 🧪 به ✅) تصمیم مالک: در کار واقعی جوابگوست.
