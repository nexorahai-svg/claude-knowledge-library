---
name: Lighthouse CI
slug: lighthouse-ci
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: اجرای خودکار Lighthouse با حد قبولی برای عملکرد، سئو و دسترسی‌پذیری
url: https://github.com/GoogleChrome/lighthouse-ci
repo: "https://github.com/GoogleChrome/lighthouse-ci"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S34, S105]
found_in: [batch-01/P17]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Lighthouse CI

## چیست
✅ اجرای خودکار Lighthouse با `lhci autorun`. هر حد (assertion) می‌تواند `warn` یا `error` باشد؛ `error` باعث شکست می‌شود. نمونه: `"categories:performance": ["warn", {"minScore": 0.9}]`. پیش‌تنظیم‌ها و بودجه‌ی منابع (حجم و تعداد فایل).

## کی استفاده کنیم
🧭 دروازه‌ی عملکرد و سئو قبل از انتشار. چون امتیاز بین اجراها نوسان دارد، `numberOfRuns` را ۳ یا بیشتر بگذار و حد را کمی شل بگیر.

## قیمت و مجوز
✅ Apache-2.0، رایگان. ✅ آخرین نسخه 0.15.1 (۲۰۲۵-۰۶-۲۵)؛ حدود ۱۶ ماه بدون نسخه‌ی تازه.

## ریسک و هشدار
⚠️ مقصد بارگذاری `temporary-public-storage` گزارش را برای هر کسی که لینک دارد عمومی می‌کند؛ لازم نیست، بارگذاری را خاموش بگذار.

## سنجش روی رایانه‌ی خودمان 🔬
از پروژه‌ی MARIO E.G.S.H ([S105](../sources/README.md#s105)):
- 🔬 `@lhci/cli` 0.15.1 وابستگی‌هایی با هشدار امنیتی npm دارد: در پوشه‌ی جدا (`package.json` خودش) نگه دار، نه در وابستگی‌های سایت، و هرگز روی سرور.
- ✅ گزارش خود Lighthouse (12.6.1) روش را می‌گوید: `throttlingMethod: simulate`، گوشی، کندی پردازنده ×۴. 🔬 در این حالت LCP «شبیه‌سازی‌شده» ۵ تا ۶ ثانیه بود، در حالی که LCP **مشاهده‌شده** روی همان رایانه ۰٫۳۵ تا ۰٫۶۴ ثانیه؛ عدد شبیه‌سازی‌شده تقریباً برابر «آماده شدن صفحه» بود، یعنی حجم جاوااسکریپت. هر دو عدد را بخوان (`metrics` در گزارش).
- 🔬 اگر فشرده‌سازی کار سرور جلویی (مثل Caddy) است، سرور محلی پاسخ **فشرده‌نشده** می‌دهد و Lighthouse حجم را ۳ تا ۴ برابر می‌بیند. برای عدد درست یک پروکسی کوچک gzip با همان قاعده جلوی سایت بگذار.
- 🔬 امتیاز سئو تا وقتی سایت عمداً `noindex` است پایین می‌ماند؛ برایش حد نگذار.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
