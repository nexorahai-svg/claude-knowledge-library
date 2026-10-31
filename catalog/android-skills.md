---
name: Android Skills (Google)
slug: android-skills
category: claude-code-tooling
domains: [apps]
verdict: adopt
status: researched
summary: مخزن رسمی Google از skillهای استاندارد برای عامل‌ها در کارهای Android مثل تحلیل R8 و انتشار
use_when: "Android-specific tasks in a Flutter app such as R8 analysis or release publishing ; looking for official Google agent skills for Android"
how: "use the official `android` org skills repo (Apache-2.0); set the skill folder to Claude Code since the default install targets Gemini; read the skill files before enabling"
url: https://github.com/android/skills
repo: "https://github.com/android/skills"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S166]
found_in: [inbox/2026-10-19-watch]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Android Skills (Google)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v1.0.18 (۲۰۲۶-۱۰-۲۶): چهار مهارت تازه، از جمله mlkit-agent-api و Jetpack Ink؛ Apache-2.0 بی‌تغییر.
✅ (۲۰۲۶-۱۰-۱۹، بخش اول README و API گیت‌هاب؛ نصب نشد) مخزن skillهای استاندارد (SKILL.md) از سازمان `android`، بر پایه‌ی راهنمای developer.android.com. تمرکز روی کارهایی که مدل‌ها در آن ضعیف‌اند. نصب با Android CLI (`android skills add <نام>` یا `--all`)؛ اگر پوشه‌ی عاملی پیدا نشود به‌طور پیش‌فرض برای Gemini و Antigravity نصب می‌کند. نمونه: تحلیل R8. حدود ۸٬۸۰۰ ستاره، Apache-2.0، آخرین تغییر ۲۰۲۶-۱۰-۱۶.
❓ فهرست کامل skillها و صفحه‌ی developer.android.com خوانده نشد.

## کی استفاده کنیم
🧭 بخش Android اپ‌های Flutter (R8، انتشار). اول ببین با Claude Code هم کار می‌کنند؛ پوشه‌ی skill را به‌جای نصب پیش‌فرض خودت مشخص کن.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
⚠️ skill دستور می‌دهد؛ پیش از فعال کردن فایل‌هایش را بخوان. نصب پیش‌فرض برای Gemini است نه Claude.

## مرتبط
[انتشار اپ](../domains/apps/publishing-apps.md) · [Android SDK خط فرمان](android-sdk-cli.md) · [S166](../sources/README.md#s166)

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v1.0.19 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
