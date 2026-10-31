---
name: Lighthouse CI
slug: lighthouse-ci
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: اجرای خودکار Lighthouse با حد قبولی برای عملکرد، سئو و دسترسی‌پذیری
use_when: "adding a performance/SEO gate before releasing a website ; checking Core Web Vitals budgets automatically"
how: "lhci autorun with numberOfRuns >= 3 and slightly loose assertions (warn/error); install @lhci/cli in a separate folder never on a server; do not use temporary-public-storage upload (makes report public); no asserts on SEO while site is noindex"
url: https://github.com/GoogleChrome/lighthouse-ci
repo: "https://github.com/GoogleChrome/lighthouse-ci"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S34, S105]
found_in: [batch-01/P17]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# Lighthouse CI

## چیست
✅ اجرای خودکار Lighthouse با `lhci autorun`. هر حد (assertion) می‌تواند `warn` یا `error` باشد؛ `error` باعث شکست می‌شود. نمونه: `"categories:performance": ["warn", {"minScore": 0.9}]`. پیش‌تنظیم‌ها و بودجه‌ی منابع (حجم و تعداد فایل).

## دستور سریع
✅ ([مستندات LHCI](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md)، @lhci/cli 0.15.1 با Lighthouse 12.6.1) در پوشه‌ی جدا نصب کن، نه در وابستگی‌های سایت:
```bash
mkdir -p tools/lhci && (cd tools/lhci && npm init -y && npm i -D @lhci/cli@0.15.1)
tools/lhci/node_modules/.bin/lhci autorun          # از ریشه‌ی پروژه، کنار lighthouserc.js
```
```js
// lighthouserc.js
module.exports = { ci: {
  collect: { url: ['http://localhost:3000/'], startServerCommand: 'npm run start', numberOfRuns: 3 },
  assert: { assertions: { 'categories:performance': ['warn', { minScore: 0.9 }], 'categories:accessibility': ['error', { minScore: 1 }] } },
  upload: { target: 'filesystem', outputDir: '.lighthouseci' } } };
```
✅ تنظیم‌های مهم: `numberOfRuns` ۳ یا بیشتر (پیش‌فرض ۳)؛ حد `warn` یا `error` (فقط `error` شکست می‌دهد)؛ `chromePath` برای Chrome مشخص (🔬 Chromium خود Playwright)؛ در `autorun` پرچم‌ها با `=` نوشته می‌شوند (`--collect.numberOfRuns=5`).
خطاهای رایج: ✅ `upload.target: temporary-public-storage` گزارش را عمومی می‌کند؛ از `filesystem` استفاده کن. 🔬 پکیج هشدار امنیتی npm دارد، هرگز روی سرور. 🔬 `next dev` عدد عملکرد بی‌معنا می‌دهد؛ روی build تولیدی بسنج. 🔬 تا سایت `noindex` است برای سئو حد نگذار. 🔬 سرور محلی بدون فشرده‌سازی حجم را ۳ تا ۴ برابر می‌بیند. جایگزین بدون LHCI و جزئیات: بخش‌های پایین.

## کی استفاده کنیم
🧭 دروازه‌ی عملکرد و سئو قبل از انتشار. چون امتیاز بین اجراها نوسان دارد، `numberOfRuns` را ۳ یا بیشتر بگذار و حد را کمی شل بگیر.

## قیمت و مجوز
✅ Apache-2.0، رایگان. ✅ آخرین نسخه 0.15.1 (۲۰۲۵-۰۶-۲۵)؛ حدود ۱۶ ماه بدون نسخه‌ی تازه.

## ریسک و هشدار
⚠️ مقصد بارگذاری `temporary-public-storage` گزارش را برای هر کسی که لینک دارد عمومی می‌کند؛ لازم نیست، بارگذاری را خاموش بگذار.

## سنجش روی رایانه‌ی خودمان 🔬
از یک فروشگاه واقعی ([S105](../sources/README.md#s105)):
- 🔬 `@lhci/cli` 0.15.1 وابستگی‌هایی با هشدار امنیتی npm دارد: در پوشه‌ی جدا (`package.json` خودش) نگه دار، نه در وابستگی‌های سایت، و هرگز روی سرور.
- ✅ گزارش خود Lighthouse (12.6.1) روش را می‌گوید: `throttlingMethod: simulate`، گوشی، کندی پردازنده ×۴. 🔬 در این حالت LCP «شبیه‌سازی‌شده» ۵ تا ۶ ثانیه بود، در حالی که LCP **مشاهده‌شده** روی همان رایانه ۰٫۳۵ تا ۰٫۶۴ ثانیه؛ عدد شبیه‌سازی‌شده تقریباً برابر «آماده شدن صفحه» بود، یعنی حجم جاوااسکریپت. هر دو عدد را بخوان (`metrics` در گزارش).
- 🔬 اگر فشرده‌سازی کار سرور جلویی (مثل Caddy) است، سرور محلی پاسخ **فشرده‌نشده** می‌دهد و Lighthouse حجم را ۳ تا ۴ برابر می‌بیند. برای عدد درست یک پروکسی کوچک gzip با همان قاعده جلوی سایت بگذار.
- 🔬 امتیاز سئو تا وقتی سایت عمداً `noindex` است پایین می‌ماند؛ برایش حد نگذار.

## بدون LHCI: Node API خود Lighthouse 13 🔬

(یک فروشگاه Next.js 16، ۲۰۲۶-۱۰-۲۸)
- ✅ npm: `lighthouse` 13.6.0 (۲۰۲۶-۱۰-۲۷) و 13.5.0 (۲۰۲۶-۰۹-۱۸)؛ `@lhci/cli` هنوز 0.15.1 با Lighthouse 12.6.1. 🧭 به‌جای LHCI، خود `lighthouse` (نسخه‌ی دست‌کم دو هفته‌ای، اینجا 13.5.0) را در پوشه‌ی جدا نصب کن و با `chrome-launcher` و `chromium.executablePath()` Playwright صدا بزن؛ میانه‌ی ۳ اجرا و حدها را خودت در ۴۰ خط بنویس. 🔬 `npm audit` روی آن پوشه صفر هشدار.
- 🔬 روی `next dev` عدد عملکرد بی‌معناست (۰٫۲۶ تا ۰٫۴۸ در برابر ۰٫۶۱ تا ۰٫۸۴ روی `next build && next start`). روی سرور توسعه فقط دسترس‌پذیری و Best Practices را قضاوت کن؛ عملکرد را روی build تولیدی روی درگاه جدا (`next start -p 3100`). Next 16 خروجی dev را در `.next/dev` نگه می‌دارد، پس build کنار سرور dev در حال اجرا ممکن است.
- 🔬 بزرگ‌ترین عامل CLS یک **نوار ثابت** (`position:fixed`) بود که اول پایین صفحه کشیده می‌شد و یک فریم بعد با `useEffect` بالای نوار پایینی می‌رفت: CLS ۰٫۳۴. اندازه‌گیری با `useLayoutEffect` پیش از اولین نقاشی ← ۰. ممیزی `layout-shifts` گره‌ی مقصر را نام می‌برد؛ همیشه آن را بخوان.
- ⚠️ برای بستن سرور تولیدی با `pkill -f "next-server"` **سرورهای dev را هم کشتیم**؛ سرور را با `setsid` اجرا کن و با PID خودش ببند.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [S34](../sources/README.md#s34)
