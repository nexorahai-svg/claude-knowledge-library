---
name: Android Studio
slug: android-studio
category: app-frameworks
domains: [apps]
verdict: trial
status: researched
summary: محیط رسمی Google برای Android؛ نسخه‌ی Rabbit 2 بیش از ۴۰ عامل کدنویسی (Claude Agent، Codex، Junie، Antigravity) را از راه ACP وصل می‌کند
use_when: "Android part of a Flutter or native app needs emulator, Logcat and build access for an AI agent ; reviewing agent-made changes inside the IDE ; testing XR emulators"
how: "Settings > Tools > AI > Agents to pick and authenticate an agent (e.g. Claude Agent); skills at Settings > Tools > AI > Skills; /review for Change Review; check what data a third-party agent receives first"
url: https://developer.android.com/studio
repo: ""
license: "رایگان (Android Studio؛ شرایط Google)"
pricing: free
risk: low
sources: [S205]
found_in: [watch-2026-10-29]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Android Studio

## چیست
✅ (۲۰۲۶-۱۰-۲۹، سه پست رسمی developer.android.com) نسخه‌ی پایدار Rabbit 2 (۲۰۲۶-۱۰-۲۸). بیش از ۴۰ عامل کدنویسی از راه ACP، از جمله Claude Agent، Codex، Junie و Antigravity؛ انتخاب در پنجره‌ی عامل یا Settings > Tools > AI > Agents و سپس احراز هویت. عامل‌ها به شبیه‌ساز، سیستم بیلد، Logcat و skillهای Android دسترسی دارند. مدیر skill در Settings > Tools > AI > Skills، بازبینی تغییرات با `/review` (Change Review) و شبیه‌سازهای XR پایدار.
❓ روش احراز هویت Claude (کلید API یا اشتراک)، هزینه و نحوه‌ی برخورد با داده‌ی عاملهای شخص ثالث در پست‌ها نیامده است.

## دستور سریع
✅ نصب Linux ([developer.android.com/studio/install](https://developer.android.com/studio/install)): `android-studio-rabbit2-linux.tar.gz` (Rabbit 2، 2026.2.2) را در `~/` یا `/opt/` باز کن، کتابخانه‌های ۶۴ بیتی را نصب کن و اجرا:
```bash
./android-studio/bin/studio
~/Android/Sdk/emulator/emulator -accel-check     # ✅ باید «KVM ... is installed and usable» بدهد
```
✅ تنظیم‌های مهم: عامل در Settings > Tools > AI > Agents (انتخاب و احراز هویت، مثلاً Claude Agent با کلید API شخصی)، skillها در Settings > Tools > AI > Skills، بازبینی تغییرات با `/review`. جدول رسمی سیستم‌نیاز (نسخه‌ی Windows خوانده شد): ۸ گیگابایت RAM برای Studio و ۱۶ گیگابایت برای Studio همراه شبیه‌ساز ❓ جدول Linux را هم ببین.
خطاهای رایج: بدون KVM شبیه‌ساز بسیار کند است؛ کاربر را در گروه `kvm` بگذار ([Android SDK](android-sdk-cli.md)). ❓ عامل‌های شخص ثالث کد و لاگ پروژه را به سرویس خود می‌فرستند؛ پیش از پروژه‌ی مشتری بررسی کن. 🧭 ورود با اشتراک claude.ai آزموده نشده؛ کلید API فرض شود (بالا). برای کار سبک بدون IDE: [Android CLI](android-sdk-cli.md).
💲 Android Studio رایگان است؛ هزینه‌ی عامل با ارائه‌دهنده‌اش (کلید API Anthropic).

## کی استفاده کنیم
🧭 بخش Android اپ‌های Flutter یا بومی، وقتی عامل باید اپ را روی شبیه‌ساز اجرا و Logcat را بخواند. اول روی یک پروژه‌ی کوچک امتحان شود.

## قیمت و مجوز
Android Studio رایگان است (شرایط Google). ✅ Google برای Claude هزینه‌ای نمی‌گیرد و هزینه با خود ارائه‌دهنده است: Claude Agent را با ورود یا کلید API شخصی Anthropic وصل می‌کنی ([AI in Android](https://developer.android.com/ai-in-android)، [وبلاگ ۲۰۲۶-۰۹](https://android-developers.googleblog.com/2026/09/build-your-way-use-any-ai-agent-in-android-studio.html)). 🧭 شرایط Agent SDK اجازه‌ی ورود با اشتراک claude.ai در محصول شخص ثالث را بدون تأیید Anthropic نمی‌دهد ([legal](https://code.claude.com/docs/en/legal-and-compliance))؛ پس کلید API را فرض کن و ورود با اشتراک را تا تأیید رسمی آزموده‌نشده بدان.

## ریسک و هشدار
ریسک پایین برای خود IDE. ❓ عامل‌های شخص ثالث کد و لاگ پروژه را به سرویس خود می‌فرستند؛ پیش از استفاده روی پروژه‌ی مشتری بررسی شود.

## مرتبط
- [android-sdk-cli](android-sdk-cli.md)
- [android-skills](android-skills.md)
- https://developer.android.com/blog/posts/ai-agents-android-studio-integration
- https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance
- https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
