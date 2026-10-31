---
name: jsQR
slug: jsqr
category: browser-testing
domains: [website, apps]
verdict: adopt
status: researched
summary: کدخوان QR با جاوااسکریپت خالص؛ برای آزمودن این‌که کدهای چاپی واقعاً خوانده می‌شوند و محتوای درست دارند
use_when: "verifying printed QR cards really decode in tests ; checking QR content such as table URL or Wi-Fi code"
how: "npm i jsqr (1.4.0, Apache-2.0, unmaintained since 2021) in Node tests: draw the printed SVG to canvas and pass the RGBA pixels (base64 transfer, not JSON arrays); it is stricter than phone cameras so it gives a floor, still test on a real phone; dot style at 90% failed, 96% passed"
url: https://github.com/cozmo/jsQR
repo: "https://github.com/cozmo/jsQR"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S117]
found_in: [projects/یک پروژه‌ی سفارش با QR]
last_checked: 2026-10-31
next_check: "2027-01-17"
---

# jsQR

## چیست
✅ کتابخانه‌ی خواندن کد QR از پیکسل‌های خام (RGBA)، بدون هیچ وابستگی (npm `jsqr` 1.4.0، مجوز Apache-2.0 در فایل LICENSE مخزن). ⚠️ آخرین تغییر کد اوت ۲۰۲۱؛ نگهداری نمی‌شود.

## کی استفاده کنیم
🔬 (یک پروژه‌ی سفارش با QR، ۲۰۲۶-۱۰-۱۹) در تست مرورگر: کارت‌های چاپی را از صفحه‌ی چاپ برداشتیم (SVG ← canvas ← پیکسل به Node با base64؛ فهرست اعداد JSON خیلی کند بود) و خواندیم:
- محتوای هر کارت = آدرس میز خودش (کارت اشتباه = سفارش برای میز اشتباه)؛ کد Wi-Fi با کاراکترهای `; " , : \`
- «دوربین»: تار، کج، نور کم، JPEG؛ کوچک‌ترین اندازه‌ی خوانا
- ⚠️ طرح نقطه‌ای (نقطه‌ی ۹۰٪ با گوشه‌ی گرد) روی تصویر **خیلی واضح** (۶۰۰ dpi) فقط ۲ از ۲۶ خوانده شد؛ نقطه‌ی ۹۶٪ همه را. تصویر کوچک‌تر از اندازه‌ی چاپ با لبه‌ی نرم هم خطای کاذب داد: همیشه در وضوح واقعی چاپ بسنج.
🧭 چون از کدخوان دوربین گوشی‌ها ضعیف‌تر است، «کف» خوانایی را نشان می‌دهد؛ جای آزمون با گوشی واقعی را نمی‌گیرد.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [اپ روی یک رایانه در محل](../domains/apps/local-network-app.md)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
