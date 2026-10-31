# ورود مشتری و نقش‌ها (فروشگاه، داشبورد، اپ موبایل، پنل کارکنان)

> **نوع سند:** دستورالعمل
> **هدف این سند:** برای هر پروژه‌ای که مشتری یا کارمند باید وارد شود، یک روش ثابت و تأییدشده داشته باشیم: کدام ابزار، چه قانون‌هایی برای رمز و نشست، passkey، کد ایمیلی یا پیامکی، نقش‌ها، و چه آزمون‌هایی پیش از انتشار.
> **موضوع تحقیق:** OWASP (Authentication، Session Management، Password Storage، MFA)، NIST SP 800-63B-4، passkeys.dev، RFC 8252؛ Better Auth، Auth.js، Lucia، Keycloak؛ Supabase Auth، Firebase Auth، Clerk، Cloudflare Access؛ flutter_secure_storage و passkey در Flutter.
> **منابع:** [S125 ورود مشتری و نقش‌ها](../../../sources/README.md#s125) · [S95 بک‌اند، ورود، پرداخت](../../../sources/README.md#s95) · [S53 Cloudflare](../../../sources/README.md#s53) · [S184 Express، npm](../../../sources/README.md#s184)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۰
> **دفعه‌ی بعد چک شود:** آگهی‌های امنیتی تازه‌ی Better Auth (ماهانه)؛ نسخه‌ی پایدار Auth.js ۵ یا توقف کامل آن؛ منطقه‌ی خاورمیانه در Supabase و Clerk؛ passkey در Supabase Auth؛ بسته‌ی رسمی passkey برای Flutter؛ نسخه‌ی تازه‌ی برگه‌های OWASP.

این سند جای خالی «ورود مشتری و نقش‌ها» در راهنماهای [داشبورد](../../../playbooks/web-app-dashboard.md) و [اپ موبایل](../../../playbooks/mobile-app.md) را پر می‌کند. ⚠️ مسیر Better Auth هنوز در پروژه‌ی واقعی آزموده نشده و ابزار اصلی‌اش trial است. 🔬 الگوی «کد موبایل + passkey» برای مشتری و «فقط passkey» برای کارکنان روی Medusa ساخته و آزموده شد (بخش ۵ و دفتر پروژه‌ها).

---

## ۱. جدول تصمیم

| موقعیت | پیش‌فرض | جایگزین | چرا |
|---|---|---|---|
| مشتری‌های فروشگاه آنلاین | [Better Auth](../../../catalog/better-auth.md) 🧪 روی سرور خودمان، ورود با **کد ایمیلی** (بدون رمز) | ورود با Google یا Apple به‌عنوان گزینه‌ی دوم | مشتری فروشگاه رمز تازه نمی‌خواهد 🧭؛ داده در پایگاه خودمان ✅ |
| کاربران داشبورد SaaS | Better Auth 🧪 با کد ایمیلی یا رمز، افزونه‌ی `organization` برای تیم و نقش، passkey | نمونه‌ی سریع بدون داده‌ی حساس ← [Clerk](../../../catalog/clerk.md) 👀؛ پروژه‌ی Supabase ← [Supabase](../../../catalog/supabase.md) 🧪 با RLS | سازمان، دعوت و بررسی دسترسی سمت سرور آماده است ✅ |
| پنل مدیریت کارکنان | [Cloudflare Access](../../../catalog/cloudflare-access.md) ✅ با کد ایمیلی و بررسی JWT در سرور | پنل داخل همان اپ ← Better Auth با نقش `admin` و **ورود دومرحله‌ای اجباری** | رایگان تا ۵۰ کاربر ✅؛ کارمند جدا از مشتری |
| اپ موبایل Flutter | صفحه‌ی ورود بومی که به API سرور خودمان (Better Auth با افزونه‌ی `bearer`) کد ایمیلی می‌فرستد؛ توکن در [flutter_secure_storage](../../../catalog/flutter-secure-storage.md) 🧪 | Google یا Apple ← SDK بومی یا مرورگر سیستم با PKCE (RFC 8252)؛ نسخه‌ی ۲ ← [UAE PASS](../../../catalog/uae-pass.md) 👀 | هیچ WebView برای ورود ✅ |
| داده باید در امارات بماند | Better Auth روی سرور خودمان در امارات (یا AWS `me-central-1`) با Postgres یا SQLite همان‌جا | چند اپ با یک ورود مشترک ← [Keycloak](../../../catalog/keycloak.md) 👀 (اول تحقیق) | Supabase منطقه‌ی خاورمیانه ندارد ✅، Firebase Auth فقط آمریکا ✅، Clerk فقط آمریکا ✅ |

✅ کتابخانه‌هایی که برای پروژه‌ی تازه **نه**: [Auth.js](../../../catalog/authjs.md) ⛔ (از ۲۰۲۵-۰۹-۲۲ بخشی از Better Auth و فقط وصله‌ی امنیتی؛ نسخه‌ی ۵ هنوز beta) و [Lucia](../../../catalog/lucia.md) ⛔ (مارس ۲۰۲۵ کنار گذاشته شد). [Firebase](../../../catalog/firebase.md) ✅ برای اعلان خوب است، ولی Auth آن فقط در آمریکا پردازش می‌کند ([بک‌اند اپ](../../apps/app-backend.md)).

## ۲. چرا Better Auth پیش‌فرض است

- ✅ کتابخانه است، نه سرویس: داخل سرور Next.js یا Node خودمان اجرا می‌شود و کاربر و نشست در پایگاه داده‌ی خودمان می‌ماند. پس محل داده را خودمان انتخاب می‌کنیم.
- ✅ MIT، نسخه‌ی `1.7.11`، فعال‌ترین گزینه؛ خود Auth.js پروژه‌ی تازه را به آن می‌فرستد.
- ✅ همه‌ی چیزهایی که لازم داریم افزونه‌ی رسمی دارد: کد ایمیلی، passkey، TOTP و کد پشتیبان، نقش و سازمان، مدیر، بررسی رمز لو رفته، توکن برای موبایل.
- ⚠️ ✅ ولی ۳۱ آگهی امنیتی در ۱۲ ماه (۳ بحرانی). 🧭 جبرانش: کمترین افزونه، به‌روزرسانی سریع، و آزمون‌های بخش ۸ روی **خود مسیرهای API**.
- 🧭 Clerk سریع‌تر راه می‌افتد، ولی داده فقط در آمریکاست و passkey و ورود دومرحله‌ای پولی است. Supabase Auth خوب است اگر کل پروژه روی Supabase است و محل داده مهم نیست.

## ۳. قانون‌های رمز

اگر رمز داریم (برای مشتری فروشگاه کد ایمیلی را ترجیح بده):

| قانون | عدد | منبع |
|---|---|---|
| کمترین طول | **۱۵** اگر رمز تنها عامل است؛ **۸** اگر حتماً با عامل دوم است | ✅ NIST 800-63B-4 بخش ۳.۱.۱، OWASP Authentication |
| بیشترین طول | دست‌کم **۶۴** نویسه، بدون بریدن بی‌صدا | ✅ NIST (SHOULD)، OWASP |
| ترکیب اجباری (حرف بزرگ، عدد، نماد) | **ممنوع** | ✅ NIST «SHALL NOT» |
| تعویض دوره‌ای | **ممنوع**؛ فقط اگر نشانه‌ی لو رفتن هست | ✅ NIST |
| فهرست رمزهای لو رفته | اجباری؛ کل رمز مقایسه شود و دلیل رد برای کاربر بیان شود | ✅ NIST؛ افزونه‌ی `have-i-been-pwned` فقط ۵ نویسه‌ی اول SHA-1 را می‌فرستد ✅ |
| ذخیره | Argon2id با کمینه‌ی `m=19456` (۱۹ مگابایت)، `t=2`، `p=1`؛ یا scrypt با `N=2^17`، `r=8`، `p=1` | ✅ OWASP Password Storage |
| پیام خطا | یکسان برای «کاربر نیست» و «رمز غلط»؛ زمان پاسخ و کد HTTP هم یکسان | ✅ OWASP |

✅ پیش‌فرض Better Auth: scrypt و طول ۸ تا ۱۲۸. 🧭 پس `minPasswordLength` را ۱۵ بگذار مگر ورود دومرحله‌ای اجباری باشد. ✅ پارامترهای scrypt داخلی Better Auth (کد `@better-auth/utils`، https://raw.githubusercontent.com/better-auth/utils/main/src/password.node.ts): `N=16384`، `r=16`، `p=1`، کلید ۶۴ بایت، نمک ۱۶ بایت؛ یعنی ضعیف‌تر از عدد OWASP بالا (`N=2^17`، `r=8`). اگر عدد OWASP مهم است، با `password.hash` و `password.verify` به Argon2id (`@node-rs/argon2`، MIT) عوض کن.

## ۴. قانون‌های نشست و محدودیت نرخ

- ✅ کوکی نشست: `Secure`، `HttpOnly`، `SameSite=Lax` یا `Strict`، بدون `Domain`، ترجیحاً پیشوند `__Host-` (OWASP Session Management). Better Auth در production کوکی را `httpOnly` و `secure` می‌کند ✅؛ 🧭 `useSecureCookies: true` را هم صریح بگذار.
- ✅ هیچ توکن نشست در `localStorage` یا `sessionStorage` (OWASP و NIST هر دو).
- ✅ شناسه‌ی نشست: دست‌کم ۶۴ بیت تصادفی از مولد امن (NIST بخش ۵، OWASP).
- ✅ **بعد از ورود و هر تغییر سطح دسترسی، شناسه‌ی نشست تازه** (ضد session fixation). باطل کردن نشست در خود سرور هنگام خروج اجباری است.
- ✅ زمان‌ها (NIST): AAL1 کل نشست حداکثر ۳۰ روز. AAL2 حداکثر ۲۴ ساعت و بی‌کاری حداکثر ۱ ساعت. 🧭 ترجمه برای ما: مشتری فروشگاه ۷ تا ۳۰ روز (پیش‌فرض Better Auth ۷ روز با تمدید روزانه ✅)؛ پنل کارکنان ۸ ساعت کل و ۳۰ دقیقه بی‌کاری (OWASP: ۴ تا ۸ ساعت برای یک روز کاری، ۱۵ تا ۳۰ دقیقه برای کم‌خطر ✅).
- ✅ کار حساس (عوض کردن ایمیل، رمز، اطلاعات پرداخت، حذف حساب) دوباره ورود می‌خواهد (OWASP). در Better Auth: `freshAge` (پیش‌فرض ۱ روز ✅)؛ 🧭 برای پنل ۵ دقیقه.
- ✅ بعد از بازنشانی رمز، همه‌ی نشست‌های دیگر باطل: `revokeSessionsOnPasswordReset: true` (پیش‌فرض خاموش است ✅). دکمه‌ی «خروج از همه‌ی دستگاه‌ها» با `revokeOtherSessions`.
- ✅ محدودیت نرخ: NIST حداکثر ۱۰۰ تلاش ناموفق پشت‌سرهم برای هر حساب؛ OWASP شمارش بر اساس **حساب**، نه فقط IP، و بدون قفل دائمی که مهاجم بتواند با آن کاربر را بیرون کند. Better Auth پیش‌فرض: `/sign-in/email` سه بار در ۱۰ ثانیه، و فقط در production ✅. 🧭 ذخیره‌ی شمارش را `database` بگذار (حافظه با راه‌اندازی دوباره پاک می‌شود)، و پشت Caddy `trustedProxies` را تنظیم کن.

## ۵. passkey

- ✅ NIST 800-63B-4: در سطح AAL2 باید دست‌کم یک گزینه‌ی مقاوم در برابر فیشینگ **پیشنهاد** شود؛ passkey همگام‌شده (syncable) در AAL2 مجاز است (پیوست B).
- ✅ پشتیبانی (https://passkeys.dev/device-support/): passkey همگام‌شده از iOS 16، macOS 13 و Android 9؛ پیشنهاد خودکار در فیلد ورود (conditional UI) از Safari 16.1، Chrome 108، Edge 122 و Firefox 122.
- ✅ OWASP MFA: passkey فقط وقتی عامل دوم حساب می‌شود که سرور «user verification» را بخواهد و بررسی کند.
- 🧭 برنامه‌ی ما:
  1. نسخه‌ی ۱ وب: کد ایمیلی + دکمه‌ی «ساخت passkey» بعد از اولین ورود؛ فیلد ایمیل با `autocomplete="username webauthn"` تا passkey خودکار پیشنهاد شود ✅ (افزونه‌ی `@better-auth/passkey`).
  2. پنل کارکنان داخل اپ: passkey یا TOTP اجباری.
  3. اپ Flutter: نسخه‌ی ۲. ❓ بسته‌ی رسمی Flutter نیست؛ [passkeys از Corbado](../../../catalog/passkeys-flutter.md) 👀 اول تحقیق شود.

### آزموده روی Medusa 2 🔬

(یک فروشگاه امارات روی Medusa 2.21.2، اکتبر ۲۰۲۶)، بدون Better Auth:
- **مشتری:** ورود با موبایل و کد ۶ رقمی (auth provider سفارشی Medusa، کوکی httpOnly با `POST /auth/session`)، بدون رمز و بدون خرید مهمان. بعد از ثبت‌نام passkey پیشنهاد می‌شود. کتابخانه‌ی سرور [`@simplewebauthn/server`](https://www.npmjs.com/package/@simplewebauthn/server) ‏14.0.3، MIT ✅ (npm، ۲۰۲۶-۱۰-۲۸). کار حساس (تغییر موبایل، حساب بانکی، خرج اعتبار، حذف حساب) passkey تازه یا کد ایمیلی می‌خواهد. آزمون passkey ‏۵۹ مورد.
- **کارکنان:** پنل جدا که **فقط با passkey** باز می‌شود؛ کد یک‌بارمصرف فقط برای دستگاه تازه و بلافاصله ساخت passkey؛ نشست ۸ ساعت و ۳۰ دقیقه بی‌کاری در جدول خودمان؛ ۵ کد غلط = قفل ۱۵ دقیقه با خبر به مالک؛ چهار نقش (مالک، مدیر مغازه، فروشنده، تکنسین) با جدول مجوز در بک‌اند و بررسی روی خود مسیر API؛ قیمت، بازپرداخت، کف سود و تغییر نقش دوباره passkey (step-up). ۵۱ آزمون. جزئیات Medusa: [کارت Medusa](../../../catalog/medusa.md).
- ⚠️ ورود ایمیل و رمز پیش‌فرض Medusa (`emailpass`) فقط برای آزمون محلی روشن ماند و برنامه در production با آن هشدار می‌دهد، چون مسیرهای هسته‌ی `/admin` همان توکن را بی‌توجه به نقش‌های ما می‌پذیرند.

## ۶. کد ایمیلی یا پیامک

- ✅ NIST: پیامک و تماس صوتی «authenticator محدودشده» است؛ باید جایگزین بدون محدودیت هم داشته باشیم و ریسک را به کاربر بگوییم. OWASP: پیامک برای اپ پرارزش یا دارای داده‌ی شخصی توصیه نمی‌شود (SIM swap، شنود SS7).
- ✅ NIST: ایمیل را **نباید** برای احراز out-of-band به‌کار برد؛ ولی کد بازیابی به ایمیل مجاز است (۲۴ ساعت اعتبار). OWASP: امنیت ایمیل به حساب ایمیل کاربر بستگی دارد.
- 🧭 نتیجه برای ما: ورود با کد ایمیلی برای مشتری فروشگاه یا داشبورد کم‌خطر **کافی است**، چون در عمل همان سطح «بازیابی رمز با ایمیل» است. برای داده‌ی حساس یا پنل کارکنان، کد ایمیلی فقط قدم اول است و passkey یا TOTP لازم است.
- 🧭 پیامک: فقط اگر مشتری ایمیل ندارد؛ هزینه‌ی هر پیامک با ماست ([بک‌اند اپ](../../apps/app-backend.md)).
- 🔬 کدی که از راه صف رویداد (outbox) به پیام‌رسان بیرونی داده می‌شود، در payload همان صف می‌ماند. بعد از تحویل، شکست نهایی یا انقضا آن را `[redacted]` کن و کد منقضی را دیگر نفرست (کمینه‌سازی داده، مثل PDPL امارات ❓ تفسیر با وکیل). یک job دوره‌ای ردیف‌های قدیمی را هم پاک کند. در گزارش پیام‌های مشتری هم کد ننویس.
- 🔬 کلید HMAC کد و لینک امضاشده هرگز مقدار پیش‌فرض نداشته باشد: الگوی `process.env.KEY ?? '...'` در سه فایل پخش شده بود و بدون کلید، کد با رازی عمومی امضا می‌شد. بدون کلید **خطا بده** (fail closed) و یک تابع مشترک بساز؛ با `grep -rn "?? '" src` همه را پیدا کن.
- ✅ تنظیم Better Auth `email-otp`: پیش‌فرض ۶ رقم، ۳۰۰ ثانیه، ۳ تلاش. ✅ ارسال ایمیل را `await` نکن تا زمان پاسخ وجود حساب را لو ندهد (مستند Better Auth). ارسال ایمیل از سرور: [دامنه و ایمیل](domain-and-email.md).

## ۷. نقش‌ها (RBAC ساده)

🧭 الگو:

1. جدول نقش: `user_roles(user_id, role)` و در صورت نیاز `role_permissions(role, permission)`. نقش‌ها کم و روشن: `customer`، `staff`، `admin`.
2. **هر درخواست** در سرور: نشست را بخوان، نقش یا مجوز را بررسی کن، و **مالکیت ردیف** را هم (`WHERE owner_id = session.user.id`). پنهان کردن دکمه در رابط کاربری امنیت نیست.
3. ✅ Better Auth: افزونه‌ی `admin` برای نقش کاربر (پیش‌فرض `user`)، و `organization` برای تیم با نقش owner/admin/member؛ بررسی سمت سرور با `auth.api.hasPermission`. ✅ `checkRolePermission` فقط سمت کاربر است و نقش پویا را نمی‌بیند؛ برای تصمیم واقعی نه.
4. ✅ Supabase: نقش در جدول، «custom access token hook» آن را در JWT می‌گذارد، و تابع `authorize()` داخل سیاست RLS بررسی می‌کند. جدول بدون RLS برای همه باز است و view از RLS می‌گذرد ([Supabase](../../../catalog/supabase.md) 🧪). برای اجبار ورود دومرحله‌ای: سیاست `as restrictive` با `aal2` ✅.
5. ✅ مدیر و کاربر پرامتیاز: ورود دومرحله‌ای اجباری (OWASP MFA)، و نشست کوتاه‌تر.

🔁 تجربه‌ی یک پروژه‌ی واقعی: قفلی که فقط در middleware تست داشت، در خود مسیر API نشت کرد. برای هر قاعده‌ی دسترسی، تست «کاربر دیگر» روی **خود مسیر API**.

## ۸. اپ موبایل Flutter

- ✅ RFC 8252 (BCP 212): اگر اپ با OAuth وارد می‌شود (Google، Apple، Keycloak)، **باید** از مرورگر سیستم استفاده کند و **نباید** WebView داخلی باشد؛ PKCE اجباری؛ اپ «کلاینت عمومی» است و راز ثابت نباید داشته باشد؛ آدرس بازگشت ترجیحاً `https` ادعاشده (Universal Link و App Link). بسته‌ها: `flutter_appauth` (BSD-3-Clause، ۱۲.۱.۰) یا `flutter_web_auth_2` (MIT، ۵.۱.۰) ✅ pub.dev.
- 🧭 ورود با حساب خود اپ (پیش‌فرض ما): صفحه‌ی بومی ایمیل و کد که مستقیم API خودمان را صدا می‌زند؛ سرور Better Auth با افزونه‌ی `bearer` توکن نشست را در هدر `set-auth-token` برمی‌گرداند ✅، و اپ آن را در `Authorization: Bearer` می‌فرستد. ⚠️ ✅ مستند bearer خودش می‌گوید با احتیاط و فقط برای کلاینتی که کوکی ندارد.
- ✅ توکن فقط در [flutter_secure_storage](../../../catalog/flutter-secure-storage.md) 🧪 (Keychain با `first_unlock_this_device`؛ Android با رمزنگاری کلید Keystore). پشتیبان خودکار اندروید خاموش ([عملیات اپ](../../apps/app-operations.md)).
- 🧭 خروج: هم توکن را از گوشی پاک کن، هم نشست را در سرور باطل کن.
- ✅ Apple 4.8: اگر Google یا Facebook ورود اصلی است، یک گزینه‌ی هم‌ارز مثل Sign in with Apple هم لازم است ([بک‌اند اپ](../../apps/app-backend.md)).

## ۹. حذف حساب

✅ اپی که حساب می‌سازد باید **حذف حساب داخل اپ** داشته باشد (Apple 5.1.1(v))؛ Google علاوه بر آن لینک وب حذف می‌خواهد ([انتشار اپ، شرط‌های رد](../../apps/publishing-apps.md)). 🧭 برای سایت و داشبورد هم همین را بساز: حذف با دوباره‌ورود، باطل کردن همه‌ی نشست‌ها، و حذف یا ناشناس کردن داده‌ی شخصی در پشتیبان طبق سیاست حریم خصوصی.

## ۱۰. چک‌لیست آزمون پیش از انتشار

هر مورد یک تست خودکار ([Playwright](../../../catalog/playwright.md) ✅ یا تست API)، روی سرور با تنظیم production:

- [ ] **محدودیت نرخ:** ۱۰ ورود غلط پشت‌سرهم به یک حساب ← ۴۲۹؛ همین با `X-Forwarded-For` جعلی **از بیرون Caddy** دور زده نمی‌شود؛ درخواست کد ایمیلی هم محدود است.
- [ ] **IP مشتری پشت پراکسی:** ✅ در Express بدون `trust proxy`، `req.ip` نشانی سوکت است، یعنی پشت Caddy همه‌ی مشتری‌ها یک IP (خود پراکسی) دارند و یک نفر سقف نرخ همه را پر می‌کند ([S184](../../../sources/README.md#s184)). 🧭 فقط وقتی همتای مستقیم یک پراکسی مطمئن (فهرست ثابت در تنظیم) است، `X-Forwarded-For` را از راست به چپ بخوان و اولین نشانی نامطمئن را بردار (همان قاعده‌ی Express). 🔬 سرآیند IP اختصاصی (مثلاً از پنل خودمان) را هم فقط همراه کلید مشترک بپذیر، نه با توکن کارمند تنها؛ آزمون واحد با `X-Forwarded-For` جعلی. 🔬 آزمون یکپارچه: ۲۰ درخواست کد هر کدام با `X-Forwarded-For` و سرآیند IP ساختگی متفاوت، بیست‌ویکمی ۴۲۹، نشانی ذخیره‌شده نشانی واقعی؛ خرابی عمدی (باور کردن `X-Forwarded-For`) ۴ از ۴ گرفته شد. آزمون باید کدها و رویدادهای خودش را پاک کند، وگرنه سقف ساعتی آزمون‌های بعدی را پر می‌کند؛ نشانی ساختگی را از بازه‌ی مستندسازی (198.51.100.0/24) بگیر تا پاک‌سازی، حتی پس از خرابی، پیدایش کند.
- [ ] **کد ایمیلی:** بعد از ۳ تلاش غلط باطل؛ بعد از ۵ دقیقه باطل؛ یک بار مصرف.
- [ ] **session fixation:** کوکی نشست پیش و پس از ورود فرق دارد؛ کوکی ساختگی پذیرفته نمی‌شود.
- [ ] **پرچم کوکی:** `Secure`، `HttpOnly`، `SameSite` در پاسخ واقعی.
- [ ] **خروج از همه‌جا:** دو مرورگر وارد؛ «خروج از همه‌ی دستگاه‌ها» در یکی ← دیگری با درخواست بعدی ۴۰۱. همین بعد از بازنشانی رمز.
- [ ] **IDOR:** کاربر A شناسه‌ی سفارش یا پرونده‌ی کاربر B را در آدرس و بدنه‌ی API می‌گذارد ← ۴۰۳ یا ۴۰۴، برای **هر** مسیر خواندن، نوشتن و حذف.
- [ ] **نقش:** کاربر `customer` مسیرهای `/admin` و API مدیر را صدا می‌زند ← ۴۰۳ (نه فقط دکمه‌ی پنهان).
- [ ] **شمارش حساب:** پیام و زمان پاسخ «ایمیل نیست» و «رمز غلط» و ثبت‌نام با ایمیل تکراری یکسان است.
- [ ] **رمز لو رفته:** `password` و `12345678` رد می‌شود.
- [ ] **ورود دومرحله‌ای مدیر:** بدون عامل دوم هیچ مسیر مدیر جواب نمی‌دهد، حتی با کوکی کش‌شده.
- [ ] **حذف حساب:** بعد از حذف، توکن قدیمی ۴۰۱ می‌گیرد.
- [ ] **وابستگی:** `npm audit` بدون آگهی زیاد یا بحرانی برای `better-auth`.

## ۱۱. پرامپت (English)

```text
Add customer sign-in and role-based access to this project. Use Better Auth (latest
1.7.x or newer, check npm and the GitHub security advisories first) running inside our
own server, with our own database (Postgres or SQLite) so user data stays where the
server is. Do not use a hosted auth service unless I say so.

Sign-in:
- Email one-time code as the main method (email-otp plugin: 6 digits, 5 minutes,
  3 attempts). Do not await the email send. Same response for known and unknown emails.
- Offer "create a passkey" after the first sign-in (@better-auth/passkey, conditional UI
  with autocomplete="username webauthn").
- If passwords are enabled: minimum 15 characters (8 only when a second factor is
  required), maximum at least 64, no composition rules, have-i-been-pwned plugin,
  Argon2id (m=19456, t=2, p=1 or stronger) via custom hash/verify.
- Staff and admin accounts must use TOTP or a passkey as a second factor.

Sessions:
- Cookies Secure, HttpOnly, SameSite=Lax, useSecureCookies true. No tokens in
  localStorage. New session after sign-in and after any role change.
- Customers: 7-day session with daily refresh. Staff: 8 hours total, 30 minutes idle,
  freshAge 5 minutes for sensitive actions.
- revokeSessionsOnPasswordReset true; a "sign out of all devices" button.
- Rate limiting on in production with database storage; set trustedProxies for Caddy.

Roles:
- user_roles table (customer, staff, admin). Check the session, the role and row
  ownership on the server in every API route and server action, never only in the UI.
  Use auth.api.hasPermission for organization permissions.

Mobile (Flutter):
- Native email-code screens calling our API; bearer plugin on the server; store the
  token only in flutter_secure_storage (iOS first_unlock_this_device). No WebView for
  any sign-in; social sign-in through the system browser with PKCE (RFC 8252).

Account deletion inside the app and on the web, with re-authentication.

Enable only the plugins listed here. Then write automated tests for: rate limiting
(including a spoofed X-Forwarded-For), one-time code expiry and attempts, session
fixation, cookie flags, sign-out everywhere, IDOR on every route (user A asks for
user B's records), role checks on admin API routes, equal responses for unknown
accounts, breached password rejection, admin second factor, and deletion. Show me the
test results before saying it is done.
```

## مرتبط

[سرور خودمان](self-hosted-server.md) · [Cloudflare، پنل امن](cloudflare-full-stack.md) · [بک‌اند اپ](../../apps/app-backend.md) · [انتشار اپ](../../apps/publishing-apps.md) · [Better Auth](../../../catalog/better-auth.md) 🧪 · [S125](../../../sources/README.md#s125)
