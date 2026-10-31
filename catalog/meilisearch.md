---
name: Meilisearch
slug: meilisearch
category: database-backend
domains: [website, apps]
verdict: adopt
status: researched
summary: موتور جستجوی متن‌باز و سریع با مترادف، غلط تایپی و یکسان‌سازی عربی؛ نسخه‌ی 1.54.3 برای جستجوی عربی کاتالوگ انگلیسی یک مغازه آزموده شد
use_when: "shop or app catalog search must tolerate typos and a second language (e.g. Arabic customer, English catalog) and stay on our server"
how: "run getmeili/meilisearch Docker image bound to 127.0.0.1; index with synonyms plus normalised digits; give browsers only a search-only key never the master key; skip BUSL Enterprise features"
url: https://www.meilisearch.com
repo: https://github.com/meilisearch/meilisearch
license: MIT (بخش Enterprise با BUSL-1.1)
pricing: free
risk: low
sources: [S129]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Meilisearch

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v1.56.0 (۲۰۲۶-۱۰-۲۶): گزینه‌ی sampledCount برای توزیع تقریبی facet؛ محدودیت نرخ تطبیقی وقتی embedder عقب می‌ماند؛ مجوز بی‌تغییر (MIT + BUSL برای enterprise).
- ✅ موتور جستجوی متن‌باز (Rust) با API ساده‌ی HTTP: شاخص، فیلتر، مرتب‌سازی، مترادف، تحمل غلط تایپی و کلیدهای محدود (مثلاً «فقط جستجو» برای مرورگر) ([S129](../sources/README.md#s129)).
- ✅ نسخه‌ی 1.54.3 (۲۰۲۶-۱۰-۰۱)؛ مجوز `MIT AND BUSL-1.1`: هسته MIT، بخش‌های Enterprise Edition با BUSL-1.1 ([S129](../sources/README.md#s129)).
- 🔬 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۱) با Docker (`getmeili/meilisearch:v1.54.3`، فقط روی `127.0.0.1`) کنار Medusa بالا آمد؛ ۲۱۹ کالای انگلیسی با ۲۷۶ مترادف عربی ← انگلیسی و `localizedAttributes` با `ara` شاخص شد؛ ۳۴ از ۳۴ جستجوی آزمون (عربی و خلیجی، برند به عربی، غلط تایپی، ارقام عربی) درست، هر جستجو ۱ تا ۵ میلی‌ثانیه.

## کی استفاده کنیم
جستجوی کاتالوگ فروشگاه یا اپ که باید غلط تایپی و زبان دیگر مشتری را بفهمد و روی سرور خودمان بماند. برای فهرست چند ده موردی، فیلتر ساده در خود صفحه کافی است.

## قیمت و مجوز
رایگان برای خودمیزبانی (هسته MIT)؛ از بخش‌های Enterprise (BUSL) استفاده نکن مگر مجوزش را خوانده باشی ([S129](../sources/README.md#s129)).

## ریسک و هشدار
- 🔬 کاتالوگ انگلیسی، مشتری عربی: یکسان‌سازی عربی موتور (أ إ آ ← ا، ى ← ي، ة ← ه) کافی نیست؛ واژگان «کلمه‌ی عربی مشتری ← کلمه‌ی انگلیسی نام کالا» را خودت بساز و هم مترادف یک‌طرفه بده هم کلمه‌های عربی را در یک فیلد سند بنویس.
- 🔬 عدد و واحد را پیش از جستجو یکسان کن (ارقام ٠-٩ و ۰-۹، «٦٥ واط» ← 65W، «٢٠ ألف» ← 20000) و ظرفیت «20K» نام کالا را در سند به 20000 هم بنویس. در JavaScript، `\b` بعد از حرف عربی کار نمی‌کند؛ از `(?=\s|$)` استفاده کن.
- 🔬 کلید اصلی (master key) هرگز به مرورگر نرود؛ با آن یک کلید `actions: ['search']` فقط برای همان شاخص بساز.
- 🔬 همگام‌سازی با Medusa: یک subscriber برای `product.*`، `product-variant.*` و `inventory-level.*` (موجودی از راه `inventory_item.variants.product_id` به کالا می‌رسد)؛ شناسه‌ها را ۲ ثانیه جمع کن و سند را از همان سازنده‌ی ساخت کامل و از Store API بساز، و کالایی را که Store API برنمی‌گرداند حذف کن؛ تغییر موجودی و نام در ۲٫۵ ثانیه در جستجو دیده شد. خطای Meilisearch را فقط در لاگ بنویس و فروشگاه را نشکن.
- 🔬 در subscriber تایپ‌اسکریپتِ Medusa، `import()` به `require()` تبدیل می‌شود و فایل `.mjs` بار نمی‌شود؛ از `new Function('u', 'return import(u)')` با `pathToFileURL` استفاده کن.
- 🔬 جستجوی بی‌نتیجه را برای کامل کردن واژگان ثبت کن، ولی یک بار و ۲ ثانیه بعد از توقف تایپ (نه هر کلید)، و فقط متن و زبان و روز (بدون IP و مشتری).

## مرتبط
[Medusa](medusa.md) · [راهنمای فروشگاه آنلاین](../playbooks/online-store.md) · پروژه‌ها

🧭 (مرور ارتقا ۲۰۲۶-۱۰-۳۰) trial می‌ماند: فقط در یک پروژه‌ی واقعی (فروشگاه Medusa) استفاده شده و قاعده‌ی adopt دو پروژه می‌خواهد. نتیجه‌اش خوب بود (۳۴ از ۳۴ جستجوی آزمون).

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
