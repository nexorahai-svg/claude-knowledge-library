---
name: Tauri
slug: tauri
category: app-frameworks
domains: [apps]
verdict: trial
status: researched
summary: اپ دسکتاپ و موبایل با WebView سیستم و هسته‌ی Rust؛ حجم کم
use_when: "building a desktop-only app with small size and strict permissions"
how: "Trial first on a small task: npm create tauri-app@latest, cd into it, npm install, npm run tauri dev (Tauri 2.12, needs Rust toolchain; v3 is alpha); per-window capability files; update signing is mandatory; careful with external-URL capabilities on Linux and Android"
url: https://tauri.app
repo: "https://github.com/tauri-apps/tauri"
license: "Apache-2.0 یا MIT"
pricing: free
risk: low
sources: [S39]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-25"
---

# Tauri

## چیست
✅ tauri 2.12.5 (۲۰۲۶-۱۰-۲۱)، CLI 2.12.4 (۲۰۲۶-۱۰-۲۱)؛ v3 فقط alpha (3.0.0-alpha.5 در crates.io). دسترسی‌ها با فایل capability برای هر پنجره. امضای به‌روزرسانی اجباری.
✅ نصب و اجرا (https://v2.tauri.app/start/create-project/، ۲۰۲۶-۱۰-۲۷): npm create tauri-app@latest ; npm run tauri dev

## دستور سریع
✅ ([v2.tauri.app](https://v2.tauri.app/start/prerequisites/)) پیش‌نیاز Debian و Rust (نصب بسته‌ها با sudo کار انسان است):
```bash
sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh     # اسکریپت را اول بخوان
npm create tauri-app@latest && cd tauri-app && npm install
npm run tauri dev          # اجرا؛ برای بسته‌ی نهایی: npm run tauri build
```
✅ تنظیم‌های مهم: دسترسی هر پنجره در `src-tauri/capabilities` (کمینه بده، آدرس بیرونی فقط وقتی لازم است)؛ نسخه‌ی v2 (2.12.x)، نه alpha v3؛ برای به‌روزرسانی خودکار کلید امضا بساز: `npm run tauri signer generate -- -w ~/.tauri/myapp.key`.
خطاهای رایج: ✅ اگر کلید امضا گم شود دیگر نمی‌توانی به‌روزرسانی برای اپ‌های نصب‌شده منتشر کنی؛ از آن نسخه‌ی پشتیبان امن بگیر. ⚠️ capability برای آدرس بیرونی روی Linux و Android پرخطر است (بالا). ✅ انتشار macOS نیاز به امضا و notarize با عضویت پولی Apple دارد ([اپ دسکتاپ](../domains/apps/desktop-apps.md)).

## کی استفاده کنیم
🧭 اپ فقط دسکتاپ که حجم کم و دسترسی سخت‌گیرانه مهم است.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
⚠️ کمی Rust لازم است؛ ❓ بلوغ موبایل؛ capability برای آدرس بیرونی روی Linux و Android پرخطر است.

## مرتبط
[اپ دسکتاپ](../domains/apps/desktop-apps.md) · [S39](../sources/README.md#s39)
