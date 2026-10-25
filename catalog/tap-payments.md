---
name: Tap Payments
slug: tap-payments
category: database-backend
domains: [apps, website]
verdict: assess
status: researched
summary: درگاه پرداخت خلیج فارس با کارمزد درهمی منتشرشده در شرایط امارات، webhook با HMAC-SHA256 و SDK های Flutter
url: https://www.tap.company/en-ae
repo: "https://github.com/Tap-Payments"
license: "شرایط Tap"
pricing: paid
risk: medium
sources: [S124]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2026-11-18"
---

# Tap Payments

## چیست
- ✅ **webhook:** هدر `hashstring`؛ HMAC-SHA256 با کلید مخفی روی رشته‌ای از `x_id`، `x_amount`، `x_currency`، `x_gateway_reference`، `x_payment_reference`، `x_status`، `x_created`؛ مبلغ با رقم اعشار استاندارد ارز گرد می‌شود (https://developers.tap.company/docs/webhook). ❓ برنامه‌ی تلاش دوباره نوشته نشده.
- ✅ کلید آزمایشی و واقعی جدا در داشبورد؛ کلید عمومی برای SDK، کلید مخفی فقط سرور (https://developers.tap.company/docs/flutter-card-sdk).
- ✅ SDK های Flutter در سازمان رسمی GitHub (Card-Flutter، ApplePay-Flutter، TapGooglePayKit-Flutter) (https://github.com/Tap-Payments). ❓ ناشر بسته‌ها در pub.dev بررسی نشد.

## کی استفاده کنیم
🧭 گزینه‌ی دوم وقتی مشتری در چند کشور خلیج فارس می‌فروشد. برای فقط امارات، Telr و Stripe را اول ببین.

## قیمت و مجوز
✅ از شرایط امارات (https://www.tap.company/en-ae/terms-and-conditions، پیوست A): کارت داخلی ۲.۷۵٪ + ۱ درهم؛ کارت منطقه‌ای ۳.۵٪ + ۱ درهم؛ کارت جهانی ۳.۷۵٪ + ۱ درهم؛ به‌اضافه‌ی ۵٪ VAT. واریز کیف درهمی T+5 روزانه. ❓ هزینه‌ی راه‌اندازی و ماهانه در این صفحه نیست. شرط پذیرش: مجوزهای لازم کشور و فقط فعالیت‌های ثبت‌شده.

## ریسک و هشدار
⚠️ **چرا assess:** از Telr (داخلی ۲.۲۵٪ تا ۲.۴۵٪) و Stripe (۲.۹٪ + ۱ درهم) برای کارت خارجی گران‌تر است؛ شرایط ثبت‌نام و ناشر بسته‌ها ❓. Tap ممکن است تا دو سال بعد از پایان قرارداد مانده‌ای نگه دارد.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [S124](../sources/README.md#s124)
