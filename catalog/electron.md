---
name: Electron
slug: electron
category: app-frameworks
domains: [apps]
verdict: adopt
status: researched
summary: اپ دسکتاپ با HTML و JS؛ Chromium و Node درون اپ
use_when: "building a desktop-only app with web technology ; wrapping a web app for Windows, macOS and Linux"
how: "npm install electron (45.x); keep context isolation and sandbox on, nodeIntegration OFF, never load external content with Node access; budget for macOS and Windows code signing"
url: https://www.electronjs.org
repo: "https://github.com/electron/electron"
license: "MIT"
pricing: free
risk: medium
sources: [S39]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Electron

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v45.2.1 (۲۰۲۶-۱۰-۳۱؛ Chromium 156.0.8078.75 و بازگردانی وصله‌ها)؛ 46.0.0-alpha.4 پیش‌انتشار است؛ MIT بی‌تغییر: https://github.com/electron/electron/releases/tag/v45.2.1
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v45.1.0 (۲۰۲۶-۱۰-۲۷): فیلتر match/glob برای registerPreloadScript؛ رفع کرش D-Bus لینوکس و کرش onSendHeaders؛ MIT بی‌تغییر.
✅ نسخه‌ی 44.9.0. چک‌لیست امنیتی رسمی روشن؛ context isolation و sandbox پیش‌فرض.

## دستور سریع
✅ ([README مخزن](https://github.com/electron/electron) و [Forge](https://www.electronforge.io/)؛ npm: electron 45.2.0):
```bash
npm install electron@45.2.0 --save-dev      # در package.json: "main": "main.js"، "scripts": {"start": "electron ."}
npm start
npx create-electron-app@latest my-app       # راه Forge؛ اسکریپت‌های start، package، make
cd my-app && npm run make                   # بسته‌ی نصب برای همان سیستم‌عامل
```
✅ تنظیم‌های مهم ([چک‌لیست امنیتی](https://www.electronjs.org/docs/latest/tutorial/security)): `contextIsolation` روشن، `nodeIntegration` خاموش، محتوای راه دور فقط با `<webview>` یا `WebContentsView` و بدون Node؛ Electron را به‌روز نگه دار چون وصله‌های امنیتی Chromium با آن می‌آید؛ نسخه را در `package.json` قفل کن.
خطاهای رایج: ⚠️ `nodeIntegration` روشن و بارگذاری صفحه‌ی بیرونی خطر جدی است. ✅ macOS باید هم امضا و هم notarize شود و Windows امضا می‌خواهد؛ هزینه و روش‌ها: [اپ دسکتاپ](../domains/apps/desktop-apps.md) و [راهنمای امضا](https://www.electronjs.org/docs/latest/tutorial/code-signing). بسته‌ی نصب بزرگ است (Chromium داخل اپ).

## کی استفاده کنیم
🧭 کم‌ریسک‌ترین راه برای اپ فقط دسکتاپ با وب.

## قیمت و مجوز
✅ رایگان؛ امضای کد macOS و Windows هزینه دارد.

## ریسک و هشدار
⚠️ حجم نصب بزرگ؛ اگر nodeIntegration روشن شود و محتوای بیرونی باز شود، خطر جدی است.

## مرتبط
[اپ دسکتاپ](../domains/apps/desktop-apps.md) · [S39](../sources/README.md#s39)
