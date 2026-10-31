# پرداخت آنلاین در امارات: انتخاب درگاه و اتصال امن

> **نوع سند:** دستورالعمل
> **هدف این سند:** برای فروشگاه آنلاین، اپ موبایل و مرکز خدمات در امارات (کارت، Apple Pay، Google Pay، درهم) بدانیم کدام درگاه را بگیریم، چطور امن وصلش کنیم، چطور آزمونش کنیم و پیش از انتخاب از کسب‌وکار چه بپرسیم.
> **موضوع تحقیق:** Telr، N-Genius (Network International)، Stripe، Checkout.com، Tap و PayTabs: چه کسی حساب می‌گیرد، قیمت منتشرشده، راه‌های اتصال، حالت آزمایشی، امضای webhook، دامنه‌ی PCI، افزونه‌ها؛ و قاعده‌ی SAQ A در PCI DSS v4.0.1.
> **منابع:** [S124 درگاه‌های پرداخت امارات](../../../sources/README.md#s124) · [S95 بک‌اند، ورود، پرداخت](../../../sources/README.md#s95) · [S131 اتصال Telr، Tabby و Tamara](../../../sources/README.md#s131) · [S184 CSP در Stripe و Next.js](../../../sources/README.md#s184)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۸
> **دفعه‌ی بعد چک شود:** قیمت Telr و Stripe امارات؛ قیمت N-Genius، Checkout.com و PayTabs (هنوز ❓)؛ اینکه N-Genius امضای webhook اضافه کرده یا نه؛ جدول کد وضعیت سفارش Telr؛ راه گرفتن کلید آزمایشی Telr بدون حساب فروشنده؛ Shopify Payments در امارات.

---

## خلاصه

- 🧭 **پیش‌فرض ما:** صفحه‌ی پرداخت میزبانی‌شده‌ی درگاه، تأیید فقط از سرور، و هیچ‌وقت اعتماد به برگشت مرورگر.
- 🧭 فروش کم یا فریلنسر یا اشتراک ← [Stripe](../../../catalog/stripe.md) 🧪. فروش متوسط و زیاد یا اپ Flutter ← [Telr](../../../catalog/telr.md) 🧪.
- ✅ هیچ درگاهی بدون مجوز صادرشده در امارات حساب واقعی نمی‌دهد (Telr: مجوز تجاری؛ Stripe و PayTabs: مجوز تجاری یا مجوز فریلنسر).
- هیچ‌کدام هنوز با حساب آزمایشی واقعی (sandbox) در پروژه‌ی ما آزموده نشده؛ برای همین بهترین حکم 🧪 است، نه ✅. 🔬 اتصال Telr، Tabby، Tamara و Stripe روی Medusa با جایگزین‌های محلی ساخته‌شده از مستندات آزموده شد (کارت هر درگاه).

---

## ۱. جدول مقایسه (فقط از منبع اصلی)

| | [Telr](../../../catalog/telr.md) 🧪 | [Stripe](../../../catalog/stripe.md) 🧪 | [N-Genius](../../../catalog/n-genius.md) 👀 | [Checkout.com](../../../catalog/checkout-com.md) 👀 | [Tap](../../../catalog/tap-payments.md) 👀 | [PayTabs](../../../catalog/paytabs.md) 👀 |
|---|---|---|---|---|---|---|
| حساب واقعی | ✅ مجوز تجاری الزامی | ✅ مجوز تجاری یا فریلنسر امارات | ❓ | ❓ فروش‌محور | ✅ مجوزهای لازم کشور | ✅ مجوز فریلنسر پذیرفته |
| کارمزد کارت داخلی | ✅ ۲.۲۵٪ تا ۲.۴۵٪ + ۰.۵ تا ۱ درهم، به‌اضافه‌ی ماهانه‌ی ۰ تا ۲۴۹ درهم | ✅ ۲.۹٪ + ۱ درهم، بدون ماهانه | ❓ | ❓ | ✅ ۲.۷۵٪ + ۱ درهم | ❓ |
| کارت خارجی | ✅ ۰.۵٪ بیشتر | ✅ ۱٪ بیشتر (+۱٪ اگر تبدیل ارز) | ❓ | ❓ | ✅ ۳.۵٪ تا ۳.۷۵٪ + ۱ درهم | ❓ |
| صفحه‌ی میزبانی‌شده | ✅ | ✅ Checkout | ✅ | ✅ | ✅ | ✅ |
| Apple Pay و Google Pay | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Apple Pay در Flutter |
| حالت آزمایشی | ✅ فیلد `test` و کارت آزمایشی؛ ❓ کلید بدون حساب | ✅ سلف‌سرویس | ✅ سلف‌سرویس | ✅ حساب آزمایشی رایگان | ✅ کلید آزمایشی در داشبورد | ❓ |
| امضای webhook | ✅ SHA-1 با کلید در فیلد `tran_check` | ✅ HMAC در `Stripe-Signature` | ⛔ امضا ندارد، دوباره نمی‌فرستد | ✅ HMAC در `Cko-Signature` | ✅ HMAC در `hashstring` | ✅ HMAC در `Signature` |
| Flutter رسمی | ✅ ناشر تأییدشده telr.com | ❌ فقط `flutter_stripe` جامعه | ❌ | ❌ | ✅ GitHub رسمی؛ ❓ ناشر pub.dev | ⚠️ ناشر تأییدنشده |
| React Native رسمی | ✅ | ✅ | ✅ | ❌ | ❓ | ❓ |
| WooCommerce | ✅ | ✅ رسمی، بیش از ۷۰۰ هزار نصب | ✅ | ✅ | ❓ | ❓ |
| Shopify | ✅ راهنما | ❓ | ✅ | ✅ | ❓ | ❓ |

آدرس دقیق هر ادعا در کارت همان درگاه است.

### قسطی (BNPL): Tabby و Tamara

کنار درگاه کارت، نه به‌جای آن. جزئیات و منبع هر سطر در کارت‌ها ([S131](../../../sources/README.md#s131)):

| | [Tabby](../../../catalog/tabby.md) 🧪 | [Tamara](../../../catalog/tamara.md) 🧪 |
|---|---|---|
| کارمزد فروشنده | ❓ منتشر نمی‌شود (قرارداد) | ❓ منتشر نمی‌شود |
| صفحه | ✅ صفحه‌ی خود Tabby (ریدایرکت) | ✅ صفحه‌ی خود Tamara (ریدایرکت) |
| حالت آزمایشی | ✅ کلید `sk_test_` روی همان `api.tabby.ai`؛ OTP آزمایشی `8888` | ✅ میزبان جدا `api-sandbox.tamara.co` |
| امنیت webhook | ⛔ امضا ندارد؛ سرآیند ثابت خودمان یا IP مجاز، بعد پرداخت را از API بگیر | ✅ JWT با HS256 در `Authorization: Bearer`؛ الگوریتم را ثابت بگیر |
| کار ما بعد از تأیید مشتری | ✅ capture تا ۲۱ روز (وگرنه خود Tabby) | ✅ `authorise` در ۷۲ ساعت، capture هنگام ارسال |
| افزونه‌ی Medusa 2 | ❌ provider سفارشی | ❌ provider سفارشی (افزونه‌ی موجود برای Medusa 1) |
| SDK رسمی Node | ❌ | ❌ (`tamara-sdk` از ۲۰۲۳ به‌روز نشده) |
| الزام نمایش | ✅ نام دقیق «Pay later with Tabby» و snippet در صفحه‌ی کالا و سبد | ❓ |

### هزینه با فروش واقعی 🧭

حساب ما از قیمت‌های منتشرشده، با فرض میانگین سفارش ۲۰۰ درهم، فقط کارت داخلی، بدون VAT:

| فروش ماهانه | Stripe | Telr |
|---|---|---|
| ۵ هزار درهم | حدود ۱۷۰ درهم | ۲۴۹ درهم (Startup) |
| ۱۰ هزار درهم | حدود ۳۴۰ درهم | حدود ۴۹۴ درهم (Entry) |
| ۲۵ هزار درهم | حدود ۸۵۰ درهم | حدود ۷۵۰ درهم (Small) |
| ۵۰ هزار درهم | حدود ۱٬۷۰۰ درهم | حدود ۱٬۲۵۰ درهم (Medium) |

🧭 نقطه‌ی سربه‌سر حدود ۲۰ تا ۲۵ هزار درهم در ماه است. زیر آن Stripe، بالای آن Telr. با میانگین سفارش واقعی مشتری دوباره حساب کن.

---

## ۲. کدام درگاه برای کدام وضعیت

| وضعیت | انتخاب | چرا |
|---|---|---|
| مشتری از قبل قرارداد درگاه دارد | همان درگاه | 🧭 عوض کردن درگاه هزینه و زمان می‌خواهد. اگر N-Genius است، الگوی «webhook فقط زنگ است» (بخش ۳) اجباری است. |
| فروشگاه آنلاین، فروش ماهانه زیر حدود ۲۰ هزار درهم | [Stripe](../../../catalog/stripe.md) 🧪 | ✅ بدون هزینه‌ی ماهانه؛ ✅ افزونه‌ی رسمی WooCommerce. |
| فروشگاه آنلاین، فروش بالاتر | [Telr](../../../catalog/telr.md) 🧪 | ✅ کارمزد کمتر؛ ✅ WooCommerce و Shopify. |
| اپ Flutter | [Telr](../../../catalog/telr.md) 🧪 | ✅ تنها SDK رسمی Flutter با ناشر تأییدشده در میان این‌ها. یا صفحه‌ی میزبانی‌شده‌ی هر درگاه در مرورگر. |
| اپ React Native | [Stripe](../../../catalog/stripe.md) 🧪 یا [Telr](../../../catalog/telr.md) 🧪 | ✅ هر دو SDK رسمی دارند. |
| فریلنسر بدون مجوز تجاری | [Stripe](../../../catalog/stripe.md) 🧪، بعد [PayTabs](../../../catalog/paytabs.md) 👀 | ✅ هر دو مجوز فریلنسر امارات را می‌پذیرند؛ Telr مجوز تجاری می‌خواهد. |
| اشتراک ماهانه | [Stripe](../../../catalog/stripe.md) 🧪 | ✅ اشتراک و فاکتور آماده؛ Telr هم Repeat billing دارد. |
| مرکز خدمات، بیعانه یا پیش‌پرداخت | لینک پرداخت: Stripe Payment Links یا Telr QuickLinks و فاکتور | 🧭 بدون سبد خرید؛ لینک با مبلغ بیعانه برای هر سفارش از سرور ساخته شود. |
| شرکت بزرگ، چند کشور | [Checkout.com](../../../catalog/checkout-com.md) 👀 یا [Tap](../../../catalog/tap-payments.md) 👀 | ❓ قیمت فروش‌محور؛ پیش‌فرض ما نیستند. |

---

## ۳. الگوی امن اتصال

این الگو برای همه‌ی درگاه‌ها یکی است 🧭:

1. **سرور سفارش می‌سازد.** مبلغ و ارز را سرور از پایگاه داده‌ی خودش می‌خواند، نه از مرورگر یا اپ. شماره‌ی سفارش ما (مثلاً `cartid` در Telr) یکتا باشد. وضعیت: `pending`.
2. **سرور جلسه‌ی پرداخت را از درگاه می‌گیرد** و فقط لینک صفحه را به مرورگر یا اپ می‌دهد. کلید مخفی (`authkey`، `sk_…`، کلید API) هیچ‌وقت در اپ یا مرورگر نیست. ✅ Telr هم صریح می‌گوید اپ کلید ندارد.
3. **مشتری در صفحه‌ی درگاه پرداخت می‌کند** (کارت، Apple Pay، Google Pay).
4. **برگشت مرورگر فقط صفحه‌ی «در حال بررسی» است.** هیچ‌وقت از روی برگشت، سفارش را «پرداخت‌شده» نکن. آن صفحه وضعیت را از سرور ما می‌پرسد.
5. **webhook روی سرور:**
   - بدنه‌ی **خام** را نگه دار (Stripe و Checkout.com روی بدنه‌ی خام امضا می‌کنند ✅).
   - امضا را با مقایسه‌ی زمان‌ثابت بررسی کن. امضای غلط یا بی‌امضا ← ۴۰۰ و ثبت در لاگ.
   - N-Genius امضا ندارد ✅: هدر مخفی دلخواه بگذار و بعد حتماً قدم ۶.
6. **از درگاه دوباره بپرس.** با کلید سرور، وضعیت سفارش را از API درگاه بخوان (Telr: `method: "check"`؛ N-Genius: `GET …/orders/{ref}`؛ Stripe: خواندن Checkout Session یا PaymentIntent). 🧭 برای Telr (امضای SHA-1) و N-Genius (بی‌امضا) اجباری؛ برای بقیه توصیه.
7. **بررسی کن:** مبلغ، ارز و شماره‌ی سفارش پاسخ درگاه با سفارش ما یکی باشد.
8. **به‌روزرسانی idempotent:** شناسه‌ی رویداد یا تراکنش را در جدولی با کلید یکتا ثبت کن. اگر قبلاً دیده شده، فقط ۲۰۰ برگردان. تغییر وضعیت فقط `pending → paid` (یک بار). ✅ Stripe و Checkout.com می‌گویند رویداد تکراری می‌آید؛ ✅ N-Genius برای یک پرداخت چند رویداد می‌فرستد.
9. **سریع ۲۰۰ برگردان** و کار سنگین (ایمیل، انبار) را در صف انجام بده. ✅ مهلت‌ها: Checkout.com ۱۰ ثانیه، N-Genius ۱۵ ثانیه.
10. **جبران پیام گم‌شده:** کار زمان‌بندی‌شده هر چند دقیقه سفارش‌های `pending` قدیمی‌تر از ۱۰ دقیقه را از API درگاه می‌پرسد. ✅ N-Genius دوباره نمی‌فرستد؛ ✅ Telr فقط ۳ بار با فاصله‌ی ۵ ثانیه.

---

## ۴. فهرست آزمون با حالت آزمایشی

پیش از رفتن به حالت واقعی، هر کدام یک آزمون سبز 🧭:

- [ ] پرداخت موفق با کارت آزمایشی ← سفارش `paid` فقط بعد از webhook.
- [ ] پرداخت ردشده (Stripe `4000 0000 0000 0002`؛ Telr: CVV برابر کد رد؛ N-Genius: کارت declined) ← سفارش `pending` یا `failed` می‌ماند.
- [ ] 3DS با چالش (Stripe `4000 0000 0000 3220`؛ N-Genius: کارت‌های EMV 3DS 2.0).
- [ ] مشتری صفحه را می‌بندد یا «لغو» می‌زند ← سفارش پرداخت‌شده نمی‌شود.
- [ ] باز کردن دستی نشانی برگشت «موفق» بدون پرداخت ← «پرداخت شد» نشان داده **نمی‌شود**.
- [ ] webhook بی‌امضا، با امضای غلط، یا با مبلغ دست‌کاری‌شده ← ۴۰۰ و بدون تغییر سفارش.
- [ ] همان webhook دو بار ← فقط یک بار اثر.
- [ ] webhook گم‌شده ← کار زمان‌بندی‌شده سفارش را درست می‌کند.
- [ ] بازپرداخت کامل و جزئی از API.
- [ ] Apple Pay و Google Pay روی دستگاه واقعی. ✅ در Stripe آزمون Apple Pay با کارت واقعی و کلید آزمایشی است و پول کم نمی‌شود.
- [ ] خطای عمدی: بررسی امضا را در کد حذف کن؛ آزمون‌ها باید قرمز شوند.
- [ ] کلید مخفی در بسته‌ی اپ یا کد سمت مرورگر پیدا نشود (جست‌وجو در خروجی build).

ابزار کمکی: ✅ Stripe CLI با `stripe listen` webhook را به سرور محلی می‌فرستد. برای Telr که کلید آزمایشی بدون حساب ندارد ❓، تا ثبت‌نام مشتری با webhook ساختگی و امضای محلی آزمون کن.

---

## ۵. PCI DSS

- ✅ **SAQ A:** شورای PCI (۲۸ فوریه‌ی ۲۰۲۵) می‌گوید معیار تازه‌ی «سایت در برابر اسکریپت آسیب‌پذیر نیست» فقط برای سایتی است که فرم پرداخت را **در صفحه‌ی خودش** (مثلاً iframe) جاسازی می‌کند. **ریدایرکت** به صفحه‌ی درگاه و فرستادن لینک پرداخت این معیار را ندارند (https://blog.pcisecuritystandards.org/faq-clarifies-new-saq-a-eligibility-criteria-for-e-commerce-merchants).
- ✅ برای iframe دو راه هست: محافظت مثل الزام ۶.۴.۳ و ۱۱.۶.۱ روی صفحه‌ی خودمان، یا تأیید کتبی درگاه که راه‌حلش صفحه را محافظت می‌کند.
- 🧭 پس **ریدایرکت کامل ساده‌ترین مسیر است.** Telr `framed=1`، Stripe Checkout جاسازی‌شده، Hosted Session N-Genius و Flow در Checkout.com همه iframe در صفحه‌ی ما هستند.
- ✅ Checkout.com هر سه راهش را SAQ-A می‌داند. ✅ Telr می‌گوید صفحه‌ی میزبانی‌شده و Mobile API گواهی PCI نمی‌خواهد؛ Remote API (گرفتن کارت روی سرور ما) PCI کامل می‌خواهد.
- ✅ N-Genius: هر فروشنده‌ی آنلاین سالانه خودارزیابی PCI دارد.
- ✅ روی طرح رایگان Cloudflare گرفتن اطلاعات کارت در خود سایت ممنوع است ([Cloudflare](cloudflare-full-stack.md)). صفحه‌ی میزبانی‌شده مشکلی ندارد.
- 🧭 نوع SAQ را آخر سر بانک یا درگاه مشتری تأیید می‌کند؛ از آن‌ها بپرس.

### Stripe: Payment Element در برابر Checkout میزبانی‌شده
- 🔬 (یک فروشگاه روی Medusa 2.21.2) provider رسمی Stripe در Medusa با PaymentIntent کار می‌کند و فرم کارت در سایت خودمان با **Payment Element** (iframe ‏Stripe.js) نشان داده می‌شود؛ صفحه‌ی میزبانی‌شده‌ی Stripe Checkout در آن نیست. (دفتر پروژه‌ها)
- 🧭 پس طبق بند اول همین بخش، این حالت «فرم جاسازی‌شده در صفحه‌ی ما» است، نه ریدایرکت: صفحه‌ی پرداخت خودمان باید در برابر اسکریپت محافظت شود (فهرست اسکریپت‌ها، CSP، تشخیص تغییر صفحه؛ الزام ۶.۴.۳ و ۱۱.۶.۱) یا Stripe کتباً بگوید پوشش می‌دهد. دامنه‌اش از ریدایرکت کامل بزرگ‌تر است؛ نوع دقیق SAQ را از Stripe و بانک بپرس. راه ساده‌تر: Stripe Checkout با ریدایرکت (provider سفارشی).
- ✅ CSP لازم برای Stripe.js (https://docs.stripe.com/security/guide): `script-src` با `https://js.stripe.com` و `https://*.js.stripe.com`؛ `frame-src` با همین دو و `https://hooks.stripe.com` (برای 3DS)؛ `connect-src` با `https://api.stripe.com`. برای Checkout میزبانی‌شده: `https://checkout.stripe.com` در `connect-src`، `frame-src` و `script-src`. CSP در Next.js: [کارت Next.js](../../../catalog/nextjs.md#csp-و-metadata-در-nextjs-16).

---

## ۶. پیش از انتخاب، از کسب‌وکار بپرس

1. مجوز تجاری دارید یا مجوز فریلنسر؟ صادرشده در کدام امارت یا منطقه‌ی آزاد؟ فعالیت «تجارت الکترونیک» در مجوز هست؟
2. حساب بانکی شرکتی در امارات دارید؟ (برای LLC در Stripe صورت‌حساب لازم است ✅.)
3. الان با درگاهی یا بانکی قرارداد دارید؟ دستگاه کارت‌خوان از کدام بانک است؟
4. فروش آنلاین ماهانه‌ی تقریبی و میانگین هر سفارش؟ چند درصد مشتری کارت خارجی دارد؟
5. اشتراک، بیعانه، قسطی (Tabby یا Tamara) یا بازپرداخت زیاد لازم است؟
6. سایت روی WooCommerce، Shopify یا سایت سفارشی ما؟ اپ Flutter یا React Native؟
7. چه کسی صاحب حساب درگاه است؟ 🧭 حساب به نام و ایمیل خود مشتری باشد و ما فقط دسترسی توسعه‌دهنده داشته باشیم.
8. چه کسی بازپرداخت و اختلاف (chargeback) را جواب می‌دهد؟

---

## ۷. پرامپت پیاده‌سازی

```text
Implement online payments for this project with <GATEWAY> using its hosted payment page
(full redirect, not an iframe), currency AED. Read the gateway's official docs first;
do not guess field names. Rules:
1. The server creates the order: amount and currency come from our database, never from
   the client. Each order has a unique reference and starts as "pending".
2. The server creates the payment session with the secret key kept in server environment
   variables. The client (browser or app) only receives the payment page URL.
3. The return URL only shows "checking payment"; it never marks an order paid. It polls
   our server for the order status.
4. Webhook endpoint: read the raw body, verify the gateway signature with a constant-time
   comparison (or, if the gateway does not sign, a secret header), reject anything else
   with 400. Then re-fetch the order or payment from the gateway API with the server key
   and check amount, currency and our reference before changing anything.
5. Idempotency: store each event or transaction id with a unique constraint; a repeat
   returns 200 and does nothing. The only allowed change is pending -> paid, once.
6. Return 200 fast; send emails and update stock from a queue.
7. A scheduled job re-checks "pending" orders older than 10 minutes against the gateway API.
8. Write tests in test mode: success, decline, 3DS challenge, cancel, forged return URL,
   unsigned webhook, wrong signature, tampered amount, duplicate webhook, missed webhook,
   full and partial refund. Then remove the signature check on purpose and show that the
   tests fail; restore it.
9. Confirm no secret key appears in the client bundle or app build.
Stop and ask me before switching to live keys or changing any merchant account setting.
```

---

## مرتبط

[بک‌اند اپ، پرداخت](../../apps/app-backend.md) · [سایت روی Cloudflare](cloudflare-full-stack.md) · [داده‌ی فروشگاه آنلاین](online-store-data.md) · کارت‌ها: [Telr](../../../catalog/telr.md) 🧪، [Stripe](../../../catalog/stripe.md) 🧪، [N-Genius](../../../catalog/n-genius.md) 👀، [Checkout.com](../../../catalog/checkout-com.md) 👀، [Tap](../../../catalog/tap-payments.md) 👀، [PayTabs](../../../catalog/paytabs.md) 👀، [Tabby](../../../catalog/tabby.md) 🧪، [Tamara](../../../catalog/tamara.md) 🧪
