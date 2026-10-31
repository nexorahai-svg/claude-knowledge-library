---
name: Appllama Skills
slug: appllama-skills
category: claude-code-tooling
domains: [apps]
verdict: trial
status: researched
summary: دو اسکیل متنی برای طراحی صفحه‌ی بومی Expo و React Native؛ اسکیل طراحی بدون MCP کار می‌کند و اسکیل پژوهش به MCP پولی Appllama نیاز دارد.
use_when: "polishing Expo or React Native screens ; reviewing motion, navigation and native controls in a mobile UI ; a checklist against AI-looking mobile screens"
how: "Read files first, then only with the user's yes: npx skills@latest add appllama/appllama-skills --skill appllama-app-design-skill; skip the paid Appllama MCP unless approved; the iOS Simulator steps need a Mac, so use the Android emulator on Linux."
url: https://appllama.io/
repo: "https://github.com/Appllama/appllama-skills"
license: "MIT"
pricing: freemium
risk: low
sources: [S221]
found_in: [instagram-2026-10-31]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Appllama Skills

## چیست
✅ مخزن رسمی شرکت Antmind Ventures با دو اسکیل (MIT، حدود ۳٬۹۰۰ ستاره، ساخت ۲۰۲۶-۰۸-۱۳، آخرین push ۲۰۲۶-۰۹-۰۶):

- `appllama-app-design-skill`: معیار ساخت صفحه‌ی بومی در Expo و React Native، با HIG، رنگ معنایی، ناوبری، حرکت و حلقه‌ی آزمون در شبیه‌ساز. بدون MCP هم کار می‌کند.
- `appllama-usage`: راهنمای پژوهش روی کتابخانه‌ی طراحی اپ‌های پردرآمد، که به MCP پولی وابسته است.

## ادعای پست در برابر واقعیت
پست [zanavco](https://www.instagram.com/reel/DfCzGg0tZfu/) ابزار را کلی معرفی می‌کند و لینک را در ازای کامنت می‌دهد. ادعاها درست‌اند، ولی این‌ها را نمی‌گوید:

- ✅ «بررسی الگوهای موفق» به MCP پولی نیاز دارد.
- ✅ فقط Expo و React Native است، نه Flutter.
- ✅ مسیر اصلی شبیه‌ساز iOS است که Mac می‌خواهد؛ Android emulator در رتبه‌ی دوم می‌آید.

## کی استفاده کنیم
برای پروژه‌ی Expo یا React Native. برای [starter Flutter](../starters/flutter-app/) ما مستقیم کاربرد ندارد. 🧭 قاعده‌های ناوبری و حرکت را می‌شود به‌عنوان چک‌لیست خواند.

## قیمت و مجوز
✅ اسکیل‌ها MIT و رایگان‌اند. ✅ MCP بخشی از Pro است: ۱۶ دلار در ماه، با تخفیف موقت ۱۰ دلار تا ۲۰۲۶-۱۰-۳۱، ۱٬۵۰۰ اعتبار در ماه و هر فراخوانی یک اعتبار.

## ریسک و هشدار
- ✅ کد را خواندیم: ۱۷ فایل متنی، بدون اسکریپت اجرایی و بدون دستور پنهان. تنها اتصال بیرونی `.mcp.json` به `mcp.appllama.io` است.
- ⚠️ نصب کامل این MCP را هم وارد می‌کند؛ اگر پولی نمی‌خواهی فقط `--skill appllama-app-design-skill` را نصب کن.
- ❓ نزد ما آزموده نشده است.

## مرتبط
[Expo](expo.md) · [Expo Skills](expo-skills.md) · [Apple Design Skills](apple-design-skills.md) · [Android Skills](android-skills.md)
