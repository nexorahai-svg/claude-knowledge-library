---
name: Playwright
slug: playwright
category: browser-testing
domains: [social-media, website]
verdict: adopt
status: researched
summary: خودکارسازی مرورگر؛ اسکرین‌شات فریم‌به‌فریم و کنترل زمان با Clock API
use_when: "capturing frames for code-driven video ; end-to-end tests of a website incl. downloads and visual comparison ; checking Persian text in WebKit"
how: "npm i -D @playwright/test; page.clock.install()/runFor() for deterministic frames, page.screenshot() for video frames (not recordVideo); toHaveScreenshot baselines per OS; also test Persian pages in WebKit"
url: https://playwright.dev
repo: "https://github.com/microsoft/playwright"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S31, S34, S139, S177]
found_in: [batch-01/P04, batch-01/P12]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# Playwright

## چیست
✅ کتابخانه‌ی Microsoft برای کنترل مرورگر. ✅ `page.screenshot()` برای گرفتن هر فریم. ✅ **Clock API** (از نسخه‌ی 1.45): `page.clock.install()` زمان، تایمرها و requestAnimationFrame را جعلی می‌کند؛ `runFor()` زمان را جلو می‌برد؛ `pauseAt()` زمان را ثابت می‌کند. ✅ ضبط ویدیو (`recordVideo`) هم دارد ولی فریم‌به‌فریم دقیق نیست.

✅ **مقایسه‌ی تصویری** (`expect(page).toHaveScreenshot()`): تصویر پایه در پوشه‌ی کنار تست ذخیره می‌شود (نام شامل مرورگر و سیستم‌عامل)؛ حدها: `threshold` (پیش‌فرض ۰.۲)، `maxDiffPixels`، `maxDiffPixelRatio`. ⚠️ رندر بین سیستم‌عامل‌ها و نسخه‌ها فرق دارد؛ تصویر پایه را در همان محیطی بساز که تست اجرا می‌شود. جزئیات: [بررسی خودکار](../domains/claude-code/verification.md).

🔬 **تست دانلود واقعی** (یک پروژه‌ی واقعی، دفتر پروژه‌ها، ۲۰۲۶-۱۰-۲۲): روی لینک کلیک کن، منتظر رویداد `download` بمان و بررسی کن نشانی تب عوض نشده؛ لینک بین‌دامنه‌ای با ویژگی `download` هم وقتی سرور `Content-Disposition: attachment` بفرستد دانلود می‌شود ([S139](../sources/README.md#s139)).

🔬 **WebKit برای متن فارسی** (۲۰۲۶-۱۰-۲۶، [S177](../sources/README.md#s177)): Playwright WebKit روی لینوکس (WPE) نقطه‌ی حروف بعضی فونت‌ها (Estedad) را نمی‌کشد و Chromium می‌کشد؛ پس سایت فارسی را در WebKit هم آزمون کن ([فونت و WebKit](../domains/website/02-design/persian-rtl.md)). ⚠️ اسکرین‌شات WebKit روی سرور محلی گاهی وسط کار گیر کرد وقتی service worker سایت فعال بود؛ `newContext({ serviceWorkers: "block" })` و یک context تازه برای هر صفحه درستش کرد.

## دستور سریع
✅ ([README](https://github.com/microsoft/playwright)، @playwright/test 1.64.1):
```bash
npm init playwright@latest
npx playwright install --with-deps chromium     # --with-deps بسته‌های سیستم را هم می‌آورد (sudo)
npx playwright test                              # بعد از شکست: npx playwright show-trace trace.zip
npx playwright test --update-snapshots           # تصویر پایه‌ی toHaveScreenshot را تازه می‌کند
```
✅ تنظیم‌های مهم: در `playwright.config` بخش `webServer: { command, url, reuseExistingServer: !process.env.CI }` سرور را خودش بالا می‌آورد ([docs](https://playwright.dev/docs/test-webserver))؛ `workers` را روی صفحه‌های سنگین پایین بیاور؛ `reducedMotion: "reduce"` برای پایداری تصویر و axe؛ تصویر پایه را در همان سیستم‌عامل بساز.
خطاهای رایج (🔬 همه در [بررسی خودکار](../domains/claude-code/verification.md)): ساخت Next.js و Playwright با ۲ worker همزمان روی صفحه‌ی سه‌بعدی پوسته را کشت؛ یک worker و `nice -n 15 ionice -c 3`. WebKit لینوکس (WPE) نقطه‌ی بعضی فونت‌های فارسی را نمی‌کشد و `backdrop-filter` را «پشتیبانی‌شده» ولی بی‌اثر گزارش می‌کند. `isMobile` با `deviceScaleFactor: 2` گاهی عکس را نیمه رسم می‌کند. با service worker فعال اسکرین‌شات WebKit گیر کرد: `newContext({ serviceWorkers: "block" })`.

## کی استفاده کنیم
🧭 موتور گرفتن فریم در روش «ویدیو با کد» و تست خودکار سایت. برای ویدیوی قطعی، اسکرین‌شات بگیر، نه ضبط ویدیو.

## قیمت و مجوز
✅ Apache-2.0، رایگان.

## ریسک و هشدار
کم.

## ضبط کلیپ گوشی ۲۰۲۶-۱۰-۳۱ 🔬

- 🔬 `recordVideo` با viewport ۳۹۰×۸۴۴ و deviceScaleFactor برابر ۲ در ابعاد ۷۸۰×۱۶۸۸، صفحه را در ربع بالا-چپ با حاشیه‌ی خاکستری گذاشت (۶ از ۶ کلیپ، chromium-1248).
- 🔬 راه کارآمد: CDP `Page.startScreencast` با jpeg کیفیت ۹۵، تأیید هر فریم، نوشتن زمان واقعی در فهرست concat، و ffmpeg با fps=25. نتیجه ۷۸۰×۱۶۸۸ کامل و حدود ۳۵۰ کیلوبایت برای ۸ ثانیه.
- 🔬 نشانه‌ی زودهنگام حجم فایل بود: ۱۰۰ تا ۱۵۰ کیلوبایت به‌جای حدود ۳۵۰. برگه‌ی نمونه روی زمینه‌ی خاکستری مشکل را پنهان کرد.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S31](../sources/README.md#s31)
