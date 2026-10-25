---
name: Better Auth
slug: better-auth
category: database-backend
domains: [website, apps]
verdict: trial
status: researched
summary: کتابخانه‌ی ورود کاربر TypeScript که روی سرور خودمان و با Postgres یا SQLite خودمان اجرا می‌شود؛ ایمیل و رمز، کد ایمیلی، passkey، ورود دومرحله‌ای، نقش و سازمان
url: https://better-auth.com/
repo: "https://github.com/better-auth/better-auth"
license: "MIT"
pricing: free
risk: medium
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Better Auth

## چیست
✅ کتابخانه‌ی ورود کاربر برای TypeScript که داخل سرور خود ما اجرا می‌شود (Next.js یا هر سرور Node). داده‌ی کاربر در پایگاه داده‌ی خودمان می‌ماند؛ پس محل داده همان جای سرور است (مثلاً امارات).
✅ نسخه‌ی `1.7.11` (npm، ۲۰۲۶-۱۰-۱۹)، مجوز MIT، حدود ۳۰ هزار ستاره، آخرین push همان روز (https://github.com/better-auth/better-auth).
✅ جدول‌های اصلی: `user`، `session`، `account`، `verification`. پایگاه داده با Kysely داخلی (Postgres، SQLite، MySQL، MSSQL) یا Prisma و Drizzle (https://www.better-auth.com/docs/concepts/database).
✅ افزونه‌های رسمی در مخزن: `email-otp`، `magic-link`، `passkey` (روی SimpleWebAuthn، با autofill)، `2fa` (TOTP، کد یک‌بارمصرف، کد پشتیبان، دستگاه مورد اعتماد)، `organization` (نقش owner/admin/member، دسترسی سفارشی، تیم، دعوت)، `admin` (نقش کاربر، مسدود کردن، باطل کردن نشست)، `have-i-been-pwned`، `bearer` (برای اپ موبایل)، `jwt`.
✅ پیش‌فرض‌ها: رمز با scrypt، طول ۸ تا ۱۲۸؛ نشست ۷ روز که با استفاده هر ۱ روز تمدید می‌شود؛ کوکی‌ها در حالت production همه `httpOnly` و `secure`؛ محدودیت نرخ فقط در production روشن است: ۱۰۰ درخواست در ۱۰ ثانیه، و برای `/sign-in/email` فقط ۳ در ۱۰ ثانیه. کد ایمیلی: ۶ رقم، ۳۰۰ ثانیه، ۳ تلاش (https://www.better-auth.com/docs/concepts/rate-limit، https://www.better-auth.com/docs/authentication/email-password).
✅ Auth.js از ۲۰۲۵-۰۹-۲۲ بخشی از Better Auth شده و برای پروژه‌ی تازه Better Auth را توصیه می‌کند (https://better-auth.com/blog/authjs-joins-better-auth).

## کی استفاده کنیم
🧭 پیش‌فرض ما برای ورود **مشتری** در فروشگاه، داشبورد SaaS و اپ Flutter، وقتی سرور Node خودمان را داریم یا داده باید در امارات بماند. روش کامل: [ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md).
🧭 فقط افزونه‌هایی را روشن کن که لازم است (email-otp، passkey، 2fa، admin یا organization). SSO، SCIM، OAuth provider و OAuth proxy را روشن نکن مگر واقعاً لازم باشد؛ بیشتر آگهی‌های امنیتی در همین‌ها بوده.

## قیمت و مجوز
✅ رایگان، MIT؛ استفاده‌ی تجاری آزاد. سرویس ابری جداگانه هم دارند که لازم نیست.

## ریسک و هشدار
⚠️ ✅ در ۱۲ ماه گذشته (۲۰۲۵-۱۰-۱۹ تا ۲۰۲۶-۱۰-۱۹) **۳۱ آگهی امنیتی** در مخزن منتشر شده: ۳ بحرانی، ۱۹ زیاد، ۶ متوسط، ۳ کم (https://github.com/better-auth/better-auth/security/advisories). نمونه‌ها: «state در OAuth مثل لینک جادویی برای ورود به حساب دیگران» (رفع در `1.7.7`)، «رمز مهاجم بعد از ورود با کد ایمیلی همچنان کار می‌کند» (رفع در `1.6.22`)، «کش کوکی نشست اجازه‌ی دور زدن ورود دومرحله‌ای می‌دهد» (رفع در `1.4.6`)، «دور زدن محدودیت نرخ با چرخاندن IPv6».
🧭 یعنی پروژه فعال است و آگهی‌ها را باز منتشر می‌کند، ولی سطح حمله بزرگ است. قانون ما: حداقل `1.7.11`، Dependabot یا `npm audit` هفتگی، و به‌روزرسانی در همان هفته‌ی آگهی.
⚠️ ✅ پشت Caddy، IP را از `x-forwarded-for` می‌خواند؛ `trustedProxies` یا `ipAddressHeaders` را تنظیم کن و نگذار کسی مستقیم به پورت Next.js برسد، وگرنه محدودیت نرخ با IP جعلی دور زده می‌شود.
⚠️ ✅ ابطال نشست‌های دیگر بعد از بازنشانی رمز **پیش‌فرض خاموش است**: `revokeSessionsOnPasswordReset: true`.
⚠️ ✅ مستند افزونه‌ی bearer مثال `localStorage` دارد؛ در مرورگر از کوکی استفاده کن و bearer را فقط برای اپ موبایل با ذخیره‌ی امن.
❓ هنوز در هیچ پروژه‌ی ما آزموده نشده؛ برای همین trial است.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · [S125](../sources/README.md#s125)
