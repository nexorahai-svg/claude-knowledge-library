---
name: Medusa
slug: medusa
category: database-backend
domains: [website, apps]
verdict: trial
status: researched
summary: موتور فروشگاه متن‌باز Node.js با API فروشگاه و مدیریت، پنل مدیریت و ماژول‌های جداشدنی؛ نسخه‌ی 2.21.2 با داده‌ی واقعی یک مغازه آزموده شد
url: https://medusajs.com
repo: https://github.com/medusajs/medusa
license: MIT (بخش Enterprise جدا)
pricing: free
risk: low
sources: [S128]
found_in: []
last_checked: 2026-10-22
next_check: 2027-01-19
---

# Medusa

## چیست
- ✅ موتور فروشگاه متن‌باز (Node.js و PostgreSQL) با Store API برای سایت و اپ، Admin API و پنل مدیریت در `/app`، و workflowهای آماده برای کالا، دسته، قیمت، منطقه و موجودی ([S128](../sources/README.md#s128)).
- ✅ نسخه‌ی 2.21.2 (۲۰۲۶-۰۹-۲۸)؛ Node ^20.19 یا ≥22.12؛ starter فعلی (dtc-starter، یک monorepo با turbo) Node ≥22.22 می‌خواهد.
- 🔬 (یک فروشگاه مشتری، ۲۰۲۶-۱۰-۲۱) ۲۱۹ کالای واقعی صندوق، ۷۵ دسته‌ی دوسطحی با نام عربی در metadata، ارز AED با مالیات داخل قیمت، منطقه‌ی امارات و موجودی در یک مکان با یک اسکریپت `medusa exec` وارد شد؛ Store API در ۱۰۰ تا ۱۸۰ میلی‌ثانیه جواب داد؛ صفحه‌ی فروشگاه دوزبانه از آن خواند و axe خطایی نداد.

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
- 🔬 رویداد برای برنامه‌ی پیام (یک پروژه‌ی مشتری): یک ماژول کوچک با یک جدول outbox (`model.define` + `npx medusa db:generate <module>` + `db:migrate`)، subscriber که رویداد سفارش را در همان لحظه ثبت می‌کند، و scheduled job هر دقیقه که با امضای HMAC و شناسه‌ی ثابت می‌فرستد و با فاصله‌ی ۱/۵/۱۵/۶۰ دقیقه دوباره می‌کوشد. آزمون سرتاسری با گیرنده‌ی محلی: خاموش، تلاش دوباره، تکراری، جعلی، کهنه؛ ۶ از ۶.
- 🔬 در آزمونی که گیرنده‌ی HTTP و `medusa exec` در یک پروسه‌اند، فرزند را با `execFileSync` اجرا نکن: حلقه‌ی رویداد قفل می‌شود و گیرنده جواب نمی‌دهد؛ `execFile` ناهمزمان.
- 🔬 پورت ۴۱۹۰ (و بقیه‌ی «bad ports» استاندارد fetch، مثل ۶۰۰۰ و ۱۰۰۸۰) را برای سرور محلی نگذار: `fetch` در Node با «bad port» رد می‌کند در حالی که curl کار می‌کند.
- 🔬 `medusa db:generate` روی starter، مهاجرت‌های در انتظار هسته (مثل create-super-admin-role) را هم با `db:migrate` اجرا می‌کند؛ در پروژه‌ی واقعی پیش از اجرا بخوان.
- 🔬 کلید درگاه پرداخت در پنل مدیریت، نه `.env`: یک ماژول با جدول رمزشده (AES-256-GCM، AAD = نام درگاه، کلید رمز فقط در `.env`)، API مدیریت فقط برای مالک (۴۰۳ برای بقیه)، کلید ذخیره‌شده هرگز برنمی‌گردد (فقط ۴ نویسه‌ی آخر)، بررسی شکل کلید برای حالت آزمایشی/واقعی، تاریخچه بدون مقدار. provider کلید را هنگام هر پرداخت می‌خواند (بدون راه‌اندازی دوباره). ماژول رسمی Stripe کلید را فقط در constructor می‌خواند و `validateOptions` آن `apiKey` را اجباری می‌داند: زیرکلاس با `static validateOptions() {}` و جایگزین کردن کلاینت در هر فراخوانی. صفحه‌ی مدیریت سفارشی: `src/admin/routes/<نام>/page.tsx` با `defineRouteConfig` و `@medusajs/ui`. ۱۵ آزمون API و ۲۶ آزمون provider (یک فروشگاه مشتری).
- 🔬 checkout امارات (یک فروشگاه مشتری، ۲۰۲۶-۱۰-۲۱): (۱) اگر fulfillment set حذف شود ولی پیوندش با stock location بماند، `GET /store/shipping-options` با خطای ۵۰۰ می‌شکند؛ اول `link.dismiss` بعد حذف. (۲) هر payment provider باید در `payment_providers` همان region فعال شود، وگرنه «not enabled in the cart's region». (۳) قیمت شرطی ارسال با `rules: [{ attribute: 'item_total', operator: 'gte', value: 200 }]` روی price کار می‌کند (رایگان از آستانه). (۴) مالیات ۵٪ داخل قیمت: tax region `ae` با نرخ ۵ و `automatic_taxes: true`. (۵) ورود مشتری با موبایل و کد: auth provider سفارشی (`AbstractAuthModuleProvider`، authenticate = register) و `authMethodsPerActor: { customer: ['phone-otp'] }`؛ مشتری تازه با `POST /store/customers` و `/auth/token/refresh`؛ ورود با `POST /auth/session` (کوکی httpOnly). (۶) ردیف هزینه‌ی سفارشی بدون variant با `addToCartWorkflow` و `unit_price` کار کرد. (۷) آزمون مرورگر: سرور ایستای خودمان `.css` را با نوع درست نمی‌فرستاد و مرورگر سبک را نادیده گرفت؛ axe آن را به شکل «target-size» نشان داد، نه خطای بارگذاری.
- 🔬 پنل کارکنان جدا از `/app` (یک فروشگاه مشتری، ۲۰۲۶-۱۰-۲۲): نشست در جدول خودمان (توکن تصادفی در کوکی httpOnly، فقط sha256 در پایگاه داده، ۸ ساعت و ۳۰ دقیقه بی‌کاری) و در هر درخواست یک توکن مدیریت ۵ دقیقه‌ای با `generateJwtTokenForAuthIdentity(..., { expiresIn: "5m" })` از `@medusajs/medusa/api/auth/utils/generate-jwt-token` (تابع `generateJwtTokenWithChecks` مدت را از تنظیمات کلی می‌گیرد). مسیرهای سفارشی بیرون از `/store` و `/admin` (مثل `/sme-staff/*`) هیچ احراز هویتی ندارند: با middleware و راز مشترک پنل ببند. ۵۱ آزمون (passkey مجازی Chrome، کد دستگاه تازه، قفل، نقش‌ها، پایان نشست) سبز.
- 🔬 در `model.define` ترتیب مهم است: `model.text().nullable().index()` با «index is not a function» شکست می‌خورد؛ `model.text().index().nullable()` درست است.
- 🔬 درس‌های ساخت پنل کامل روی Medusa 2.21.2 (یک فروشگاه مشتری، ۲۰۲۶-۱۰-۲۲): (۱) `medusa develop` با نوشتن هر فایل داخل پوشه‌ی پروژه (مثلاً عکس بارگذاری‌شده در `private-uploads/`) دوباره راه می‌افتد؛ فایل‌های خصوصی را در پوشه‌ای بگذار که watcher نادیده می‌گیرد (مثل `private/`). (۲) پاسخ ۴۰۹ با پیام عمومی جایگزین می‌شود؛ برای «تکراری» ۴۲۲ بده. (۳) metadata کلید به کلید ادغام می‌شود؛ برای حذف یک کلید `""` بفرست. (۴) رویدادهای `order.fulfillment_created` و `order.return_requested` شناسه را در `order_id` دارند نه `id`؛ با `id` پرس‌وجو بی‌فیلتر شد و رویداد برای سفارش اشتباه رفت. (۵) `order.total` بعد از بازپرداخت با خط اعتبار کم می‌شود؛ جمع سفارش را از `item_total + shipping` حساب کن.
- ❓ ترجمه‌ی رسمی فیلدها (عربی) هنوز آزموده نشده است.

## مرتبط
[Meilisearch](meilisearch.md) · [راهنمای فروشگاه آنلاین](../playbooks/online-store.md) · [داده‌ی فروشگاه آنلاین](../domains/website/04-tech/online-store-data.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · پروژه‌ها
