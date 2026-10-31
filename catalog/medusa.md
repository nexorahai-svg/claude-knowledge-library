---
name: Medusa
slug: medusa
category: database-backend
domains: [website, apps]
verdict: adopt
status: researched
summary: موتور فروشگاه متن‌باز Node.js با API فروشگاه و مدیریت، پنل مدیریت و ماژول‌های جداشدنی؛ نسخه‌ی 2.21.2 با داده‌ی واقعی یک مغازه آزموده شد
use_when: "building an online shop with full ownership of code and data on our own server ; one store API serving both website and app ; importing a POS catalog"
how: "install with create-medusa-app in a path without spaces, answer the storefront prompt via printf N plus newline |; change JWT_SECRET and COOKIE_SECRET (starter sets supersecret); import catalog with a medusa exec script; payment webhooks at /hooks/payment/<identifier>_<id>; production needs the Redis event bus, caching, workflow engine and locking modules; custom roles do not protect core /admin routes; core is MIT, Enterprise parts are not"
url: https://medusajs.com
repo: https://github.com/medusajs/medusa
license: MIT (بخش Enterprise جدا)
pricing: free
risk: low
sources: [S128, S184]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Medusa

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) آخرین نسخه v2.22.2 (۲۰۲۶-۱۰-۳۰): درگاه رسمی Adyen (بتا)، رفع جست‌وجو و به‌روزرسانی وابستگی‌ها؛ MIT به‌جز فایل‌های Enterprise: https://github.com/medusajs/medusa/releases/tag/v2.22.2 . تجربه‌های 🔬 این کارت روی 2.21.2 است.
- ✅ موتور فروشگاه متن‌باز (Node.js و PostgreSQL) با Store API برای سایت و اپ، Admin API و پنل مدیریت در `/app`، و workflowهای آماده برای کالا، دسته، قیمت، منطقه و موجودی ([S128](../sources/README.md#s128)).
- ✅ نسخه‌ی 2.21.2 (۲۰۲۶-۰۹-۲۸)؛ Node ^20.19 یا ≥22.12؛ starter فعلی (dtc-starter، یک monorepo با turbo) Node ≥22.22 می‌خواهد.
- 🔬 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۱) ۲۱۹ کالای واقعی صندوق، ۷۵ دسته‌ی دوسطحی با نام عربی در metadata، ارز AED با مالیات داخل قیمت، منطقه‌ی امارات و موجودی در یک مکان با یک اسکریپت `medusa exec` وارد شد؛ Store API در ۱۰۰ تا ۱۸۰ میلی‌ثانیه جواب داد؛ صفحه‌ی فروشگاه دوزبانه از آن خواند و axe خطایی نداد.

## کی استفاده کنیم
فروشگاه آنلاینی که مالکیت کامل کد و داده می‌خواهد (سرور خودمان)، کاتالوگ از صندوق می‌آید و سایت و اپ هر دو از یک API می‌خوانند. برای فروشگاه کوچک بدون برنامه‌نویس، سکوی آماده ساده‌تر است (مقایسه‌ی تأییدشده هنوز در کتابخانه نیست).

## قیمت و مجوز
رایگان، MIT برای هسته؛ مواد Enterprise مجوز تجاری جدا دارند ([S128](../sources/README.md#s128)).

## ریسک و هشدار
- 🔬 نصب‌کننده (`create-medusa-app`) در مسیری با فاصله می‌شکند؛ در مسیر بی‌فاصله نصب کن و اگر لازم شد پیوند بساز.
- 🔬 پرسش تعاملی «storefront نصب شود؟» با stdin بسته خطای readline می‌دهد؛ جواب را با `printf 'N\n' |` بده.
- 🔬 Store API فهرست کالاهای یک دسته را برنمی‌گرداند؛ از کالا با `fields=*categories` بشمار.
- 🔬 starter یک کاربر نمونه، ۴ کالا و منطقه‌ی اروپا می‌سازد و `JWT_SECRET` و `COOKIE_SECRET` را `supersecret` می‌گذارد؛ پیش از هر چیز عوضشان کن.
- 🔬 فیلتر مشخصات: هر مقدار را یک product tag به شکل `کلید:مقدار` کن؛ Store API با `tag_id[]` روی سرور فیلتر می‌کند ولی چند تگ را «یا» می‌گیرد، پس «و» بین ویژگی‌های مختلف را در صفحه (یا یک route سفارشی) بساز. مقدار و منبع هر مشخصه در `metadata` می‌ماند.
- 🔬 جستجوی عربی: شاخص جستجوی starter («search index has no active version») آماده نبود؛ [Meilisearch](meilisearch.md) کنارش با اسکریپتی که از Store API می‌خواند کار کرد.
- 🔬 رویداد برای برنامه‌ی پیام (یک پروژه‌ی واقعی): یک ماژول کوچک با یک جدول outbox (`model.define` + `npx medusa db:generate <module>` + `db:migrate`)، subscriber که رویداد سفارش را در همان لحظه ثبت می‌کند، و scheduled job هر دقیقه که با امضای HMAC و شناسه‌ی ثابت می‌فرستد و با فاصله‌ی ۱/۵/۱۵/۶۰ دقیقه دوباره می‌کوشد. آزمون سرتاسری با گیرنده‌ی محلی: خاموش، تلاش دوباره، تکراری، جعلی، کهنه؛ ۶ از ۶.
- 🔬 در آزمونی که گیرنده‌ی HTTP و `medusa exec` در یک پروسه‌اند، فرزند را با `execFileSync` اجرا نکن: حلقه‌ی رویداد قفل می‌شود و گیرنده جواب نمی‌دهد؛ `execFile` ناهمزمان.
- 🔬 پورت ۴۱۹۰ (و بقیه‌ی «bad ports» استاندارد fetch، مثل ۶۰۰۰ و ۱۰۰۸۰) را برای سرور محلی نگذار: `fetch` در Node با «bad port» رد می‌کند در حالی که curl کار می‌کند.
- 🔬 `medusa db:generate` روی starter، مهاجرت‌های در انتظار هسته (مثل create-super-admin-role) را هم با `db:migrate` اجرا می‌کند؛ در پروژه‌ی واقعی پیش از اجرا بخوان.
- 🔬 کلید درگاه پرداخت در پنل مدیریت، نه `.env`: یک ماژول با جدول رمزشده (AES-256-GCM، AAD = نام درگاه، کلید رمز فقط در `.env`)، API مدیریت فقط برای مالک (۴۰۳ برای بقیه)، کلید ذخیره‌شده هرگز برنمی‌گردد (فقط ۴ نویسه‌ی آخر)، بررسی شکل کلید برای حالت آزمایشی/واقعی، تاریخچه بدون مقدار. provider کلید را هنگام هر پرداخت می‌خواند (بدون راه‌اندازی دوباره). ماژول رسمی Stripe کلید را فقط در constructor می‌خواند و `validateOptions` آن `apiKey` را اجباری می‌داند: زیرکلاس با `static validateOptions() {}` و جایگزین کردن کلاینت در هر فراخوانی. صفحه‌ی مدیریت سفارشی: `src/admin/routes/<نام>/page.tsx` با `defineRouteConfig` و `@medusajs/ui`. ۱۵ آزمون API و ۲۶ آزمون provider (یک پروژه‌ی واقعی).
- 🔬 checkout امارات (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۱): (۱) اگر fulfillment set حذف شود ولی پیوندش با stock location بماند، `GET /store/shipping-options` با خطای ۵۰۰ می‌شکند؛ اول `link.dismiss` بعد حذف. (۲) هر payment provider باید در `payment_providers` همان region فعال شود، وگرنه «not enabled in the cart's region». (۳) قیمت شرطی ارسال با `rules: [{ attribute: 'item_total', operator: 'gte', value: 200 }]` روی price کار می‌کند (رایگان از آستانه). (۴) مالیات ۵٪ داخل قیمت: tax region `ae` با نرخ ۵ و `automatic_taxes: true`. (۵) ورود مشتری با موبایل و کد: auth provider سفارشی (`AbstractAuthModuleProvider`، authenticate = register) و `authMethodsPerActor: { customer: ['phone-otp'] }`؛ مشتری تازه با `POST /store/customers` و `/auth/token/refresh`؛ ورود با `POST /auth/session` (کوکی httpOnly). (۶) ردیف هزینه‌ی سفارشی بدون variant با `addToCartWorkflow` و `unit_price` کار کرد. (۷) آزمون مرورگر: سرور ایستای خودمان `.css` را با نوع درست نمی‌فرستاد و مرورگر سبک را نادیده گرفت؛ axe آن را به شکل «target-size» نشان داد، نه خطای بارگذاری.
- 🔬 پنل کارکنان جدا از `/app` (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۲): نشست در جدول خودمان (توکن تصادفی در کوکی httpOnly، فقط sha256 در پایگاه داده، ۸ ساعت و ۳۰ دقیقه بی‌کاری) و در هر درخواست یک توکن مدیریت ۵ دقیقه‌ای با `generateJwtTokenForAuthIdentity(..., { expiresIn: "5m" })` از `@medusajs/medusa/api/auth/utils/generate-jwt-token` (تابع `generateJwtTokenWithChecks` مدت را از تنظیمات کلی می‌گیرد). مسیرهای سفارشی بیرون از `/store` و `/admin` (مثل `/sme-staff/*`) هیچ احراز هویتی ندارند: با middleware و راز مشترک پنل ببند. ۵۱ آزمون (passkey مجازی Chrome، کد دستگاه تازه، قفل، نقش‌ها، پایان نشست) سبز.
- 🔬 در `model.define` ترتیب مهم است: `model.text().nullable().index()` با «index is not a function» شکست می‌خورد؛ `model.text().index().nullable()` درست است.
- 🔬 درس‌های ساخت پنل کامل روی Medusa 2.21.2 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۲): (۱) `medusa develop` با نوشتن هر فایل داخل پوشه‌ی پروژه (مثلاً عکس بارگذاری‌شده در `private-uploads/`) دوباره راه می‌افتد؛ فایل‌های خصوصی را در پوشه‌ای بگذار که watcher نادیده می‌گیرد (مثل `private/`). (۲) پاسخ ۴۰۹ با پیام عمومی جایگزین می‌شود؛ برای «تکراری» ۴۲۲ بده. (۳) metadata کلید به کلید ادغام می‌شود؛ برای حذف یک کلید `""` بفرست. (۴) رویدادهای `order.fulfillment_created` و `order.return_requested` شناسه را در `order_id` دارند نه `id`؛ با `id` پرس‌وجو بی‌فیلتر شد و رویداد برای سفارش اشتباه رفت. (۵) `order.total` بعد از بازپرداخت با خط اعتبار کم می‌شود؛ جمع سفارش را از `item_total + shipping` حساب کن.
- ✅ **نشانی webhook پرداخت:** `/hooks/payment/<identifier>_<id>` (‏identifier ثابت کلاس provider، id از `medusa-config.ts`)؛ شناسه‌ی کامل در پایگاه داده `pp_<identifier>_<id>` است؛ از 2.21.2 نشانی با پیشوند `pp_` هم پذیرفته می‌شود. مثال: `/hooks/payment/stripe_stripe` ([S184](../sources/README.md#s184)). 🔬 ‏provider‌های سفارشی Telr، Tabby و Tamara همین الگو را گرفتند (`telr_telr`، `tabby_tabby`، `tamara_tamara`).
- ✅ **production:** مستندات استقرار به‌جای ماژول‌های پیش‌فرض حافظه‌ای، Redis Caching، Redis Event Bus، Workflow Engine Redis و Redis Locking را «بسیار توصیه» می‌کنند ([S184](../sources/README.md#s184)). نمونه‌ی محلی بدون Redis کار می‌کند؛ پیش از سرور واقعی اضافه کن.
- 🔬 مسیرهای هسته‌ی `/admin/*` توکن مدیر `emailpass` را می‌پذیرند و از نقش‌های سفارشی ما خبر ندارند. اگر نقش‌ها را خودمان ساخته‌ایم، `emailpass` را در production خاموش کن (یا دست‌کم هنگام راه‌اندازی هشدار بده) و نقش را روی مسیرهای سفارشی چک کن.
- 🔬 `medusa develop` اول lint اجرا می‌کند؛ یک خطای lint (مثلاً متد ناهمزمان یا `require` تنبل) راه‌اندازی سرد را می‌بندد در حالی که سرور در حال اجرا چیزی نشان نمی‌داد. آزمون «شروع از صفر» در یک worktree تازه (lint، بررسی نوع و build هر سه برنامه) آن را می‌گیرد.
- 🔬 `medusa develop` با هر ذخیره دوباره راه می‌افتد؛ ویرایش چندفایلی نیمه‌کاره آن را لحظه‌ای از کار می‌اندازد و آزمون مرورگر در همان لحظه `ERR_CONNECTION_REFUSED` می‌گیرد. پیش از باور کردن یک FAIL، `GET /health` را چک کن و آزمون را بعد از پایان ویرایش‌ها دوباره بزن.
- 🔬 `systemd-run` و واحد systemd، Node سیستم (`/usr/bin/node`) را برمی‌دارند نه nvm را؛ `PATH` یا مسیر کامل Node را بده ([سرور خودمان، پشتیبان](../domains/website/04-tech/self-hosted-server.md)).
- 🔬 (۳۰ اکتبر ۲۰۲۶) وقتی فروشگاه فقط یک کانال فروش دارد، `GET /store/products` فیلتر کانال را حذف می‌کند (`applyMaybeLinkFilterIfNecessary`)؛ کالای برداشته‌شده از کانال در فهرست و سبد می‌ماند. middleware خودمان برای فهرست و سبد لازم است.
- 🔬 (۳۰ اکتبر ۲۰۲۶) migration ماژول سفارشی با نام کلاس تکراری (حتی در ماژول دیگر) بی‌صدا اجرا نمی‌شود؛ پسوند یکتا و بررسی `mikro_orm_migrations`.
- 🔬 (۳۰ اکتبر ۲۰۲۶) مسیرهای هسته‌ی Store (`payment-collections/:id/payment-sessions`، `carts/:id/complete`، `customers/me` با metadata، line-item metadata) قاعده‌های سفارشی ما را دور می‌زنند؛ هر قاعده‌ی کسب‌وکار باید در درگاه/ماژول خودش هم بررسی شود، نه فقط در route سفارشی. `/static` و `/admin/uploads` هم HTML/SVG سرو می‌کنند.
- 🔬 (۳۰ اکتبر ۲۰۲۶) `limit` فهرست‌های Store سقف ندارد؛ یک درخواست بی‌نام `limit=100000` با گسترش عمیق بک‌اند را چند دقیقه از کار انداخت.
- 🔬 **پاک‌سازی فایل نام‌های هم‌سن را نمی‌شناسد (یک فروشگاه، ۲۰۲۶-۱۰-۳۱):** provider فایل محلی به هر اندازه‌ی عکس `Date.now()` جدا می‌چسباند، پس نام نسخه‌ی ۴۰۰ پیکسلی گاهی ۱ میلی‌ثانیه با ۱۲۰۰ پیکسلی فرق دارد. پاک‌سازی بر پایه‌ی ریشه‌ی نام ۷۵۸ فایل در حال استفاده را حذف کرد، در حالی که dry run فقط «۸ فایل بی‌استفاده» نشان داده بود. `/static` جواب HTML 404 با nosniff داد و مرورگر با ORB بست. tsc، آزمون واحد و axe نگرفتند؛ ممیزی گوشی با تشخیص درخواست شکست‌خورده گرفت. هر ۷۵۸ از ۱۲۰۰ پیکسلی‌ها بازسازی شد.
- 🧭 قاعده: پاک‌سازی فایل باید همه‌ی ستون‌های ارجاع، از جمله JSON متادیتا مثل `url_400`، را بخواند و اول روی کپی آزموده شود. dry run کوچک را نشانه‌ی امن بودن ندان.
- ❓ ترجمه‌ی رسمی فیلدها (عربی) هنوز آزموده نشده است.

## مرتبط
[Meilisearch](meilisearch.md) · [راهنمای فروشگاه آنلاین](../playbooks/online-store.md) · [داده‌ی فروشگاه آنلاین](../domains/website/04-tech/online-store-data.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · پروژه‌ها

🔬 **چهار دام Medusa 2.21.2 (۲۰۲۶-۱۰-۳۱):**
- **هم‌نامی alias مدل:** ماژول تازه با مدلی که alias آن با ماژول دیگری یکی بود کل بک‌اند را از کار انداخت (`Cannot add alias ...`) و `tsc` هشدار نداد. پیش از افزودن ماژول، نام مدل‌ها را در `src/modules` جست‌وجو کن.
- **`db:migrate` کارهای هسته را هم اجرا می‌کند:** از جمله `create-super-admin-role` که نقش مدیر کل می‌دهد و فقط در خروجی migrate دیده می‌شود. بعد از هر migrate آزمون‌های دسترسی را دوباره اجرا کن؛ درگاه‌های سفارشی مستقل از RBAC در این مورد ۱۰۰ از ۱۰۰ ماندند.
- **import حلقوی با ثابت سطح ماژول:** در ts-node خطای `Cannot access ... before initialization` می‌دهد و `tsc` نمی‌بیند. ثابت را در ماژول برگ یا داخل تابع بساز.
- **چند عامل هم‌زمان:** هر ذخیره `medusa develop` را دوباره راه می‌اندازد و آزمون‌ها `ECONNREFUSED` می‌گیرند؛ آزمون کامل را بعد از توقف عامل‌ها اجرا کن.
