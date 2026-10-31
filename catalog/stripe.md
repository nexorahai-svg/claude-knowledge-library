---
name: Stripe
slug: stripe
category: database-backend
domains: [apps, website]
verdict: trial
status: researched
summary: درگاه پرداخت جهانی با حساب امارات، قیمت درهمی منتشرشده، حالت آزمایشی سلف‌سرویس و webhook با امضای HMAC
use_when: "adding card payments to a UAE website or shop, subscriptions, payment links ; low-volume customer without monthly fees"
how: "Trial first on a small task: use Stripe test mode (card 4242 4242 4242 4242) with hosted Checkout; verify Stripe-Signature on the raw body and dedupe event ids; secret key server-side only; needs a UAE trade/freelance licence; Iran-linked owners risk account closure so ask Stripe in writing first; Flutter has no official SDK"
url: https://stripe.com/ae
repo: "https://github.com/stripe"
license: "شرایط Stripe"
pricing: paid
risk: medium
sources: [S124, S138]
found_in: [gap-playbooks]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Stripe

## چیست
- ✅ حساب امارات وجود دارد. برای همه‌ی انواع کسب‌وکار **مجوز تجاری یا مجوز فریلنسر صادرشده در امارات** لازم است: مؤسسه‌ی فردی، مؤسسه‌ی منطقه‌ی آزاد، LLC و LLC منطقه‌ی آزاد. مدارک: پاسپورت، Emirates ID و برای مقیم خارجی ویزای اقامت؛ برای LLC اساسنامه و صورت‌حساب بانکی؛ عکس صفحه پذیرفته نمی‌شود (https://support.stripe.com/questions/uae-account-activation-requirements).
- ✅ Checkout (صفحه‌ی میزبانی‌شده)، Payment Links، Elements، اشتراک و فاکتور.
- ✅ Apple Pay در Checkout میزبانی‌شده و Payment Links «بدون تنظیم اضافه» کار می‌کند؛ در Elements باید دامنه ثبت شود (https://docs.stripe.com/apple-pay?platform=web). Google Pay هم در Checkout هست.
- ✅ **حالت آزمایشی:** کلید آزمایشی و sandbox در داشبورد؛ کارت `4242 4242 4242 4242` موفق، `4000 0000 0000 0002` رد، `4000 0000 0000 3220` با 3DS (https://docs.stripe.com/testing).
- ✅ **webhook:** هدر `Stripe-Signature` (قالب `t=…,v1=…`) با رمز `whsec_…`؛ روی بدنه‌ی خام؛ تا ۳ روز دوباره می‌فرستد؛ رویداد تکراری ممکن است، پس شناسه‌ی رویداد را ثبت کن (https://docs.stripe.com/webhooks/signature).
- ✅ SDK رسمی موبایل: iOS، Android، **React Native**. **Flutter رسمی نیست**؛ بسته‌ی `flutter_stripe` (۱۴.۲.۰) از ناشر تأییدشده‌ی flutterstripe.io است، نه stripe.com (https://docs.stripe.com/sdks · https://pub.dev/packages/flutter_stripe).
- ✅ افزونه‌ی رسمی WooCommerce Stripe Payment Gateway از WooCommerce، نسخه‌ی ۱۱.۱.۱، بیش از ۷۰۰ هزار نصب، با Apple Pay و Google Pay (https://wordpress.org/plugins/woocommerce-gateway-stripe/).

## هشدار ایران (۲۰۲۶-۱۰-۲۲)
✅ (https://stripe.com/legal/restricted-businesses) فهرست کسب‌وکارهای ممنوع، اشخاصی را که در ایران هستند، ساکن آنجایند یا شهروندش‌اند شامل می‌شود. ⚠️ برای مالک ایرانی‌تبار (مثل یک پروژه‌ی واقعی) حتی با شرکت اماراتی ریسک بسته‌شدن حساب بالاست؛ پیش از ثبت‌نام کتبی بپرس. [توضیح](../domains/apps/licensing-and-sales.md).

## کی استفاده کنیم
🧭 وب‌سایت و فروشگاه، به‌خصوص وقتی مشتری حجم کم دارد (بدون هزینه‌ی ماهانه)، یا فریلنسر با مجوز فریلنس است، یا اشتراک و پرداخت تکراری لازم است. اپ Flutter: فقط با صفحه‌ی Checkout در مرورگر، یا با `flutter_stripe` بعد از خواندن ریسکش. روش: [پرداخت در امارات](../domains/website/04-tech/payments-uae.md).

## قیمت و مجوز
✅ از https://stripe.com/ae/pricing: کارت داخلی **۲.۹٪ + ۱ درهم**؛ کارت بین‌المللی ۱٪ بیشتر؛ تبدیل ارز ۱٪ بیشتر. بدون هزینه‌ی راه‌اندازی و ماهانه. واریز عادی رایگان (روزانه‌ی غلتان، هفتگی یا ماهانه)؛ واریز فوری ۱.۵٪ (حداقل ۲ درهم). ✅ واریز اول (مستندات عمومی، https://docs.stripe.com/payouts): پس از اولین پرداخت زنده معمولاً ۷ تا ۱۴ روز، بسته به صنعت، کشور و سطح ریسک؛ عدد ویژه‌ی امارات در آن صفحه پیدا نشد ❓.

## ریسک و هشدار
- ⚠️ **چرا trial و نه adopt:** هنوز در پروژه‌ی واقعی امارات آزموده نشده. ✅ Shopify Payments برای امارات در فهرست کشورهای پشتیبانی‌شده هست (https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries).
- ⚠️ برای فروش بالای حدود ۵۰ هزار درهم در ماه، Telr ارزان‌تر است (۲.۲۵٪ + ۰.۵ درهم در برابر ۲.۹٪ + ۱ درهم). 🧭 با فروش واقعی مشتری حساب کن.
- کلید مخفی فقط روی سرور. Stripe توصیه می‌کند علاوه بر امضا، IP های Stripe هم مجاز شوند.

## مرتبط
[پرداخت در امارات](../domains/website/04-tech/payments-uae.md) · [بک‌اند اپ](../domains/apps/app-backend.md) · [S124](../sources/README.md#s124)
