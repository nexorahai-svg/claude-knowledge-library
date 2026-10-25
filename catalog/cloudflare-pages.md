---
name: Cloudflare Pages
slug: cloudflare-pages
category: hosting-deploy
domains: [website]
verdict: adopt
status: researched
summary: میزبانی سایت با اتصال Git، Functions، D1 و R2؛ طرح رایگان برای سایت تجاری مجاز است
url: https://pages.cloudflare.com/
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: low
sources: [S53]
found_in: [project/client]
last_checked: 2026-10-22
next_check: "2026-11-16"
---

# Cloudflare Pages

## چیست
✅ میزبانی سایت ایستا با build خودکار از Git، به‌همراه **Pages Functions** (API روی Workers)، اتصال به **D1** (SQLite) و **R2** (فایل)، دامنه‌ی سفارشی و Deploy Hook.

## کی استفاده کنیم
✅ 🔬 بهترین گزینه‌ی رایگان ما برای **سایت شرکت یا مشتری**: سایت یک سایت مشتری با فرم، پایگاه داده، پنل مدیریت و طراح سه‌بعدی روی همین اجرا می‌شود (دفتر پروژه‌ها). راهنمای کامل: [سایت تجاری روی Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md).

## قیمت و مجوز
✅ (https://www.cloudflare.com/terms/ و https://www.cloudflare.com/service-specific-terms-developer-platform/) **بندی علیه استفاده‌ی تجاری نیست.** ممنوع در سایت رایگان: دریافت اطلاعات کارت بانکی (بند ۲.۲.۱h)، فروش دوباره‌ی سرویس، و **ثبت‌نام از طرف شخص ثالث** (بند ۲.۲.۱a): حساب سایت مشتری به نام خود مشتری باشد. CDN غیرسازمانی ممکن است برای ویدیو یا حجم نامتناسب فایل بزرگ محدود شود.
✅ (https://developers.cloudflare.com/pages/platform/limits/) رایگان: ۵۰۰ build در ماه، یک build هم‌زمان در حساب، ۲۰٬۰۰۰ فایل، هر فایل ۲۵ مبی‌بایت، ۱۰۰ دامنه. Functions: ۱۰۰٬۰۰۰ درخواست در روز و ۱۰ میلی‌ثانیه CPU. D1: ۵۰۰ مگابایت، ۵ میلیون خواندن و ۱۰۰٬۰۰۰ نوشتن در روز. R2: ۱۰ گیگابایت، خروجی داده رایگان.

🔬 (یک پروژه‌ی مشتری) آدرس `*.pages.dev` از گره‌های ایرانی check-host رد شد یا زمان تمام شد، دامنه‌ی سفارشی باز بود؛ آدرس pages.dev را به کاربر ایرانی نده ← [Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md#دسترسی-از-ایران-و-انتشار-فایل-بزرگ).

## ریسک و هشدار
⚠️ Email Address Obfuscation پیش‌فرض روشن است و لینک ایمیل را خراب می‌کند 🔬. ⚠️ Deploy Hook احراز هویت ندارد؛ راز نگهش دار. ⚠️ Cloudflare می‌تواند سرویس رایگان را قطع کند (بند ۲.۶). ⚠️ build از Git در یک سایت مشتری حدود ۱۲ دقیقه طول کشید 🔬.

## مرتبط
[سایت تجاری روی Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md) · [تکنولوژی](../domains/website/04-tech/tech-stack.md) · [Vercel](vercel.md) · [S53](../sources/README.md#s53)
