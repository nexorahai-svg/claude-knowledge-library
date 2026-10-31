---
name: Satori
slug: satori
category: assets-media
domains: [website, social-media]
verdict: adopt
status: researched
summary: تبدیل HTML و JSX به SVG برای ساخت تصویر اشتراک‌گذاری (OG)
use_when: "auto-generating OG share images for each page or article"
how: "npm install satori (0.62.0, MPL-2.0); supply fonts yourself; only Flexbox/Grid/block CSS; bidi is simplified so test mixed Persian text; for Persian posts default to browser rendering and use Satori only after testing"
url: https://github.com/vercel/satori
repo: "https://github.com/vercel/satori"
license: "MPL-2.0"
pricing: free
risk: low
sources: [S30, S44]
found_in: [batch-01/P24]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Satori

## چیست
✅ کتابخانه‌ی Vercel برای ساخت خودکار تصویر OG. نسخه‌ی 0.62.0 (۲۰۲۶-۱۰-۱۶).

## کی استفاده کنیم
🧭 تصویر اشتراک‌گذاری خودکار برای هر صفحه یا مقاله.

## قیمت و مجوز
✅ MPL-2.0، رایگان.

## ریسک و هشدار
✅ محدودیت‌ها (README): CSS کامل نیست (فقط Flexbox، Grid و block)؛ state و effect در React پشتیبانی نمی‌شود؛ فونت را باید خودت بدهی. ⚠️ **راست‌به‌چپ فقط جزئی است** (ترتیب درون‌خطی برعکس نمی‌شود)؛ برای فارسی حتماً تست کن.

## مرتبط
[چک‌لیست قبل از انتشار](../domains/website/07-quality/launch-checklist.md) · [S30](../sources/README.md#s30)

## فارسی (۲۰۲۶-۱۰-۱۷)
✅ (README) `direction: rtl` و شکل‌دهی HarfBuzz دارد، ولی الگوریتم دوجهته ساده‌شده است: `unicodeBidi`، جاسازی صریح و جفت پرانتز پشتیبانی نمی‌شود. 🧭 برای پست فارسی پیش‌فرض مرورگر بدون رابط است؛ Satori فقط بعد از تست متن مخلوط. [تصویر و گرافیک پست](../domains/social-media/images-and-graphics.md)
