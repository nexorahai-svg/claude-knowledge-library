---
name: Playwright
slug: playwright
category: browser-testing
domains: [social-media, website]
verdict: adopt
status: researched
summary: خودکارسازی مرورگر؛ اسکرین‌شات فریم‌به‌فریم و کنترل زمان با Clock API
url: https://playwright.dev
repo: "https://github.com/microsoft/playwright"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S31, S34, S139]
found_in: [batch-01/P04, batch-01/P12]
last_checked: 2026-10-22
next_check: "2027-01-15"
---

# Playwright

## چیست
✅ کتابخانه‌ی Microsoft برای کنترل مرورگر. ✅ `page.screenshot()` برای گرفتن هر فریم. ✅ **Clock API** (از نسخه‌ی 1.45): `page.clock.install()` زمان، تایمرها و requestAnimationFrame را جعلی می‌کند؛ `runFor()` زمان را جلو می‌برد؛ `pauseAt()` زمان را ثابت می‌کند. ✅ ضبط ویدیو (`recordVideo`) هم دارد ولی فریم‌به‌فریم دقیق نیست.

✅ **مقایسه‌ی تصویری** (`expect(page).toHaveScreenshot()`): تصویر پایه در پوشه‌ی کنار تست ذخیره می‌شود (نام شامل مرورگر و سیستم‌عامل)؛ حدها: `threshold` (پیش‌فرض ۰.۲)، `maxDiffPixels`، `maxDiffPixelRatio`. ⚠️ رندر بین سیستم‌عامل‌ها و نسخه‌ها فرق دارد؛ تصویر پایه را در همان محیطی بساز که تست اجرا می‌شود. جزئیات: [بررسی خودکار](../domains/claude-code/verification.md).

🔬 **تست دانلود واقعی** (یک پروژه‌ی مشتری، دفتر پروژه‌ها، ۲۰۲۶-۱۰-۲۲): روی لینک کلیک کن، منتظر رویداد `download` بمان و بررسی کن نشانی تب عوض نشده؛ لینک بین‌دامنه‌ای با ویژگی `download` هم وقتی سرور `Content-Disposition: attachment` بفرستد دانلود می‌شود ([S139](../sources/README.md#s139)).

## کی استفاده کنیم
🧭 موتور گرفتن فریم در روش «ویدیو با کد» و تست خودکار سایت. برای ویدیوی قطعی، اسکرین‌شات بگیر، نه ضبط ویدیو.

## قیمت و مجوز
✅ Apache-2.0، رایگان.

## ریسک و هشدار
کم.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S31](../sources/README.md#s31)
