# راهنمای پروژه: اپ موبایل iOS و Android

> **نوع سند:** راهنمای قدم‌به‌قدم
> **هدف این سند:** Claude در یک پروژه‌ی اپ موبایل فروشگاهی (iOS و Android) از اولین پیام تا تحویل و نگهداری، قدم‌به‌قدم بداند چه بپرسد، چه بسازد، با کدام ابزار، و هر مرحله کی «تمام» است.
> **موضوع تحقیق:** جمع‌بندی سندها و کارت‌های کتابخانه و تجربه‌ی پروژه‌های واقعی برای اپ موبایل (این راهنما ادعای تازه نمی‌سازد؛ هر واقعیت به سند منبعش لینک دارد).
> **منابع:** سندهای لینک‌شده در متن · [برنامه‌ی کامل اولین اپ](../domains/apps/mobile-launch-playbook.md) · دفتر پروژه‌ها
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۱
> **دفعه‌ی بعد چک شود:** وقتی حکم یکی از کارت‌های جدول پشته عوض شد (lint آن را می‌گیرد)، وقتی [برنامه‌ی کامل اولین اپ](../domains/apps/mobile-launch-playbook.md) عوض شد، یا وقتی اپ MARIO E.G.S.H به فروشگاه رسید و ردیفش در دفتر پروژه‌ها ثبت شد.

---

## این راهنما برای کدام پروژه است

- اپ باید از App Store و Google Play نصب شود (نه فقط سایت روی گوشی).
- کاربر حساب می‌سازد، فرم پر می‌کند، مدرک یا عکس می‌فرستد، یا پول می‌دهد.
- اپ چندزبانه است و دست‌کم یک زبان راست‌به‌چپ دارد (عربی یا فارسی).
- یک سرور یا API پشت اپ هست یا باید ساخته شود.
- نمونه‌ی هدف کتابخانه: اپ مرکز خدمات دولتی MARIO E.G.S.H در امارات، سه‌زبانه ([برنامه‌ی کامل اولین اپ](../domains/apps/mobile-launch-playbook.md)).
- **طراحی برای هر نوع اپ** (رزرو، فروشگاه، داشبورد، بازی، سلامت، کودک…) از [سیستم طراحی اپ](../domains/apps/app-design-system.md) می‌آید: پرسش‌نامه‌ی طراحی، [کاتالوگ سبک‌ها](../domains/apps/app-styles.md)، [کاتالوگ صفحه‌ها](../domains/apps/app-screen-patterns.md) و [قالب شروع](../starters/flutter-app/README.md).

اگر اپ فقط دسکتاپ است: [اپ دسکتاپ](desktop-app.md). اگر اپ روی یک رایانه در خود کسب‌وکار اجرا می‌شود و گوشی‌ها با مرورگر وصل می‌شوند: [اپ شبکه‌ی محلی](local-business-app.md). بقیه: [فهرست راهنماها](README.md).

## پیش از شروع: پرسش‌ها از کاربر

Claude سیستم‌عامل خودش را خودش می‌بیند (`uname`) و نمی‌پرسد. اگر مک نیست، شبیه‌ساز iOS ممکن نیست و مسیر iOS از ساخت ابری و TestFlight می‌گذرد ([تست اپ، روی لینوکس](../domains/apps/app-testing.md)).

1. **شرکت شماره‌ی D-U-N-S و حساب سازمانی Apple و Google دارد؟** اگر بله ← آزمون داخلی هر دو فروشگاه حدود ۳ تا ۱۰ روز کاری شدنی است. اگر نه ← ۲ تا ۵ هفته یا بیشتر؛ کار اداری همین امروز و موازی با ساخت شروع شود. پیش‌فرض: «نه». ([واقعیت زمان‌بندی](../domains/apps/mobile-launch-playbook.md))
2. **زبان داخل خود اپ عوض شود یا از تنظیم گوشی بیاید؟** اگر داخل اپ ← Flutter (تصمیم ثبت‌شده‌ی کاربر). اگر فقط از تنظیم گوشی، و اشتراک کد با سایت Next.js یا اصلاح فوری بدون فروشگاه مهم است ← Expo را پیشنهاد کن. پیش‌فرض: داخل اپ، Flutter. ([انتخاب فریم‌ورک](../domains/apps/cross-platform-frameworks.md))
3. **قرارداد یا مقررات، نگه داشتن داده داخل امارات را الزامی می‌کند؟** اگر بله ← داده روی سرور خودمان در امارات یا AWS `me-central-1`؛ نه Supabase، نه Firebase، نه Cloudflare برای داده. اگر نه ← همان پیشنهاد کتابخانه (سرور خودمان) باز هم پیش‌فرض است. پیش‌فرض: فرض کن «بله» تا جواب بیاید. ([بک‌اند اپ](../domains/apps/app-backend.md))
4. **ورود کاربر با چه؟** اگر حساب خود اپ (ایمیل یا پیامک یک‌بارمصرف) ← Sign in with Apple لازم نیست. اگر ورود اصلی با Google یا Facebook ← یک گزینه‌ی هم‌ارز مثل Sign in with Apple هم لازم است. اگر UAE PASS ← نسخه‌ی ۲. پیش‌فرض: صفحه‌های بومی کد یک‌بارمصرف ایمیلی که API سرور خودمان را صدا می‌زنند ([Better Auth](../catalog/better-auth.md) 🧪 با افزونه‌ی bearer)؛ توکن در [flutter_secure_storage](../catalog/flutter-secure-storage.md) 🧪؛ ورود Google یا Apple فقط از مرورگر سیستم یا SDK بومی با PKCE، هرگز WebView. ([ورود مشتری](../domains/website/04-tech/customer-auth.md)، [ورود کاربر](../domains/apps/app-backend.md))
5. **پرداخت لازم است؟ برای چه؟** اگر خدمت یا کالایی که بیرون از اپ مصرف می‌شود ← خرید درون‌برنامه نه؛ صفحه‌ی پرداخت میزبانی‌شده با تأیید از webhook سرور. اگر محتوای دیجیتال داخل اپ ← ❓ کتابخانه هنوز ندارد: قانون خرید درون‌برنامه برای محتوای دیجیتال؛ اول تحقیق. پیش‌فرض: بدون پرداخت در نسخه‌ی ۱، یا صفحه‌ی میزبانی‌شده. ([پرداخت](../domains/apps/app-backend.md))
6. **اپ خدمت دولتی را تسهیل می‌کند؟** اگر بله ← جمله‌ی «نماینده‌ی هیچ نهاد دولتی نیست» در اپ و فروشگاه، فرم «اپ دولتی» در Google، بدون نشان و لوگوی وزارتخانه، حساب سازمانی. اگر نه ← فقط شرط‌های عمومی. پیش‌فرض: «بله» اگر کسب‌وکار مرکز خدمات است. ([اپ خدمات دولتی](../domains/apps/publishing-apps.md#اپ-خدمات-دولتی))

## پشته‌ی پیش‌فرض

| نیاز | انتخاب پیش‌فرض | کی چیز دیگر | جزئیات |
|---|---|---|---|
| فریم‌ورک | [Flutter](../catalog/flutter.md) ✅ | زبان فقط از گوشی، اشتراک کد با سایت ← [Expo](../catalog/expo.md) 🧪 | [انتخاب فریم‌ورک](../domains/apps/cross-platform-frameworks.md) |
| سیستم طراحی و نقطه‌ی شروع کد | [قالب شروع `starters/flutter-app`](../starters/flutter-app/README.md): توکن، ۸ سبک، ناوبری تطبیقی، حالت‌ها، فونت لاتین و فارسی، ۴۰ آزمون | اپ Expo ← همان توکن‌ها و قانون‌ها، دستی | [سیستم طراحی اپ](../domains/apps/app-design-system.md) |
| چشم و دست Claude در اپ Flutter | [Dart MCP](../catalog/dart-mcp-server.md) ✅ و افزونه‌ی رسمی `dart-flutter` | — | [تست اپ، MCPها](../domains/apps/app-testing.md#flutter) |
| تست رابط تکرارپذیر | [Maestro](../catalog/maestro.md) ✅ (فایل‌های `.maestro/`) | دیالوگ سیستم (اجازه، اعلان) مهم است ← [Patrol](../catalog/patrol.md) 🧪 | [تست اپ](../domains/apps/app-testing.md) |
| دست دوم روی دستگاه واقعی | — | لازم شد ← [mobile-mcp](../catalog/mobile-mcp.md) 🧪 با نسخه‌ی ثابت | [تست اپ](../domains/apps/app-testing.md) |
| ساخت iOS بدون مک و TestFlight | [Codemagic](../catalog/codemagic.md) 🧪 | اپ Expo ← [EAS](../catalog/eas.md) 🧪 | [انتشار، CI](../domains/apps/publishing-apps.md) |
| بک‌اند و داده | API همان سرور خودمان (Postgres)، داده در امارات 🧭 | داده‌ی حساس نیست و امارات شرط نیست ← [Supabase](../catalog/supabase.md) 🧪 یا [Firebase](../catalog/firebase.md) 🧪 | [بک‌اند اپ](../domains/apps/app-backend.md) |
| اعلان | FCM و APNs، فقط «وضعیت عوض شد» و شناسه | — | [اعلان](../domains/apps/app-backend.md) |
| پرداخت امارات | [Telr](../catalog/telr.md) 🧪 با SDK رسمی Flutter (`telr_mobile_payment_sdk`، ناشر تأییدشده)؛ سفارش را سرور می‌سازد و اپ کلید ندارد | صفحه‌ی میزبانی‌شده‌ی هر درگاه در مرورگر؛ [Stripe](../catalog/stripe.md) 🧪 (بسته‌ی Flutter رسمی نیست)؛ [N-Genius](../catalog/n-genius.md) 👀 (webhook امضا ندارد) | [پرداخت امارات](../domains/website/04-tech/payments-uae.md) |
| ورود کاربر | [Better Auth](../catalog/better-auth.md) 🧪 روی سرور خودمان + [flutter_secure_storage](../catalog/flutter-secure-storage.md) 🧪 | داده در امارات شرط نیست ← [Supabase](../catalog/supabase.md) 🧪؛ passkey در Flutter ← [passkeys](../catalog/passkeys-flutter.md) 👀 (هنوز بررسی کامل نشده) | [ورود مشتری](../domains/website/04-tech/customer-auth.md) |
| ورود دولتی | ایمیل یک‌بارمصرف در نسخه‌ی ۱ | نسخه‌ی ۲ ← [UAE PASS](../catalog/uae-pass.md) 👀 | [ورود کاربر](../domains/apps/app-backend.md) |
| گزارش خطا | [Sentry](../catalog/sentry.md) 🧪 منطقه‌ی اروپا، PII خاموش | Crashlytics از [Firebase](../catalog/firebase.md) 🧪 | [عملیات اپ](../domains/apps/app-operations.md) |
| تحلیل | هیچ در نسخه‌ی ۱ 🧭 | لازم شد ← [PostHog](../catalog/posthog.md) 🧪 اروپا، ناشناس | [عملیات اپ](../domains/apps/app-operations.md) |
| به‌روزرسانی بدون فروشگاه | هیچ؛ هر قابلیت = نسخه‌ی تازه | فقط رفع باگ و متن ← [Shorebird](../catalog/shorebird.md) 👀 (اول تحقیق) | [عملیات اپ](../domains/apps/app-operations.md) |
| آزمون مهاجم روی خروجی خودمان | [jadx](../catalog/jadx.md) 🧪، [blutter](../catalog/blutter.md) 🧪، [mitmproxy](../catalog/mitmproxy.md) 🧪، [MobSF](../catalog/mobsf.md) 🧪 | باینری بومی ← [Ghidra](../catalog/ghidra.md) 🧪 | [محافظت از اپ](../domains/apps/app-protection.md) |

استفاده نکن: [ios-simulator-mcp](../catalog/ios-simulator-mcp.md) ⛔. [REA](../catalog/rea.md) 👀 هم پیش‌فرض نیست (ریسک بالا).

## مراحل

### مرحله‌ی ۰: کار اداری، موازی با همه‌ی مرحله‌ها
- **هدف:** حساب فروشگاه‌ها تا روز انتشار آماده باشد؛ ساخت منتظر حساب نمی‌ماند.
- **کارها:** جستجوی D-U-N-S با نام دقیق مجوز تجاری؛ ایمیل و سایت روی دامنه‌ی شرکت؛ فرد دارای اختیار امضا؛ فهرست ۱۲ آزمایشگر اندروید؛ پرسش اقامت داده. صاحب حساب متن قرارداد Apple (بندهای تحریم) را خودش می‌خواند.
- **تمام یعنی:** فهرست «روز ۰» در [برنامه‌ی کامل اولین اپ](../domains/apps/mobile-launch-playbook.md) تیک خورده یا برای هر مورد باز، تاریخ و مسئول نوشته شده؛ بند «پیش از پرداخت هر هزینه» در [انتشار اپ](../domains/apps/publishing-apps.md) را کاربر خوانده است.
- **بخوان:** [واقعیت زمان‌بندی](../domains/apps/mobile-launch-playbook.md) · [حساب‌ها](../domains/apps/publishing-apps.md)

### مرحله‌ی ۱: پایه، زبان‌ها و اوراکل
- **هدف:** پروژه‌ای که از روز اول خودش را می‌سنجد و سه زبان را درست نشان می‌دهد.
- **کارها:** پروژه را از [قالب شروع](../starters/flutter-app/README.md) کپی کن و `flutter create .`؛ Flutter پایدار (نسخه در README)؛ افزونه‌ی رسمی Claude Code؛ قانون‌های پروژه با کلمات خودمان در CLAUDE.md؛ `flutter gen-l10n` با فایل‌های ARB؛ صفحه‌ی آزمون راست‌به‌چپ با تاریخ، عدد، تلفن و متن مخلوط؛ توکن‌های طراحی؛ go_router؛ لایه‌ی repository.
- **تمام یعنی:** `flutter test` سبز؛ اولین فایل Maestro روی امولاتور اندروید سبز؛ عکس صفحه‌ی آزمون در انگلیسی، عربی و فارسی با بزرگ‌ترین اندازه‌ی متن؛ یک خطای عمدی (مثلاً جهت نادرست) گذاشته شد و تست شکست خورد.
- **بخوان:** [Flutter](../domains/apps/cross-platform-frameworks.md) · [قانون‌های پروژه](../domains/apps/mobile-launch-playbook.md) · [بررسی خودکار](../domains/claude-code/verification.md)

### مرحله‌ی ۱٫۵: طراحی (سبک، توکن، فهرست صفحه‌ها)
- **هدف:** پیش از اولین قابلیت، ظاهر اپ تصمیم گرفته و در کد یک‌جا باشد؛ هر صفحه از الگو ساخته شود، نه از صفر.
- **کارها:** [پرسش‌نامه‌ی طراحی](../domains/apps/app-design-system.md#۱-پرسشنامهی-طراحی) (فقط آنچه معلوم نیست)؛ پیشنهاد سبک از [کاتالوگ سبک‌ها](../domains/apps/app-styles.md) با عکس آن سبک و سلیقه‌ی ثبت‌شده‌ی کاربر؛ تنظیم `accent` برند در `lib/design/styles.dart`؛ فهرست صفحه‌ها از [کاتالوگ صفحه‌ها](../domains/apps/app-screen-patterns.md) با پنج حالت هر صفحه؛ تصمیم ناوبری (۳ تا ۵ تب، کار اصلی اول)؛ نمایش زنده‌ی سبک به کاربر در تب «تنظیمات» قالب روی شبیه‌ساز.
- **تمام یعنی:** کاربر سبک و فهرست صفحه‌ها را تأیید کرد؛ `flutter analyze` و `flutter test` (کنتراست، دسترسی‌پذیری، golden) سبز با سبک برند؛ عکس شبیه‌ساز Android در روشن و تیره و فارسی؛ هیچ رنگ یا عدد خام در `lib/screens` (`grep -nE "Color\(0x|EdgeInsets\.all\([0-9]" lib/screens` خالی، به‌جز نمایشگر).
- **بخوان:** [سیستم طراحی اپ](../domains/apps/app-design-system.md) · [کاتالوگ سبک‌ها](../domains/apps/app-styles.md) · [کاتالوگ صفحه‌ها](../domains/apps/app-screen-patterns.md) · [طراحی رابط اپ](../domains/apps/app-design.md)

### مرحله‌ی ۲: بک‌اند، ورود و حذف حساب
- **هدف:** API نسخه‌دار و امن پیش از هر قابلیت.
- **کارها:** OpenAPI روی سرور و مدل Dart از آن؛ ورود یک‌بارمصرف؛ حذف حساب داخل اپ و روی وب؛ توکن در Keychain و Keystore (پشتیبان خودکار اندروید خاموش)؛ هیچ راز در اپ، `--dart-define` یا مخزن؛ اولین ساخت iOS در Codemagic با کلید API.
- **تمام یعنی:** تست‌های API و فایل Maestro «ثبت‌نام، ورود، حذف حساب» سبز؛ برای هر قاعده‌ی دسترسی یک تست «کاربر دیگر» در **خود مسیر API**؛ اولین ساخت iOS در TestFlight یا ساخت توسعه نصب شد.
- **بخوان:** [بک‌اند اپ](../domains/apps/app-backend.md) · [ذخیره‌ی امن](../domains/apps/app-operations.md) · [محافظت، لایه‌ی ۱](../domains/apps/app-protection.md)

### مرحله‌ی ۳: قابلیت‌ها
- **هدف:** هر قابلیت با تست خودش، نه یک‌جا در آخر.
- **کارها:** طبق فهرست صفحه‌ها (مثلاً درخواست، اسکن مدرک، آپلود با URL امضاشده‌ی کوتاه‌مدت، خط زمانی وضعیت، اعلان). مشخصات پایه و الگوهای اپ خدمات از [طراحی اپ](../domains/apps/app-design.md#مشخصات-پایه-برای-هر-دو-سکو).
- **تمام یعنی:** [دروازه‌ی کیفیت طراحی](../domains/apps/app-design-system.md#۶-دروازهی-کیفیت-طراحی-پیش-از-تمام) برای هر صفحه‌ی تازه؛ «قانون پایان کار»: فایل Maestro در `.maestro/`، سبز روی امولاتور اندروید و (با مک یا TestFlight) روی iOS، و عکس در حالت RTL با بزرگ‌ترین متن ([تست اپ](../domains/apps/app-testing.md)).
- **بخوان:** [طراحی اپ](../domains/apps/app-design.md) · [امنیت فایل مدارک](../domains/apps/app-backend.md)

### مرحله‌ی ۴: پرداخت (اگر لازم است)
- **هدف:** پرداخت بدون خرید درون‌برنامه برای خدمت بیرون از اپ، و تأیید فقط از سرور.
- **کارها:** الگوی ده‌قدمی امن در [پرداخت امارات](../domains/website/04-tech/payments-uae.md): سفارش در سرور، صفحه‌ی درگاه، webhook امضاشده، **دوباره پرسیدن وضعیت از API درگاه** (امضای Telr فقط SHA-1 است)، بررسی مبلغ و ارز و شماره، تغییر یک‌بار pending به paid، و کار دوره‌ای برای webhookهای گم‌شده.
- **تمام یعنی:** چک‌لیست آزمون حالت آزمایشی در [پرداخت امارات](../domains/website/04-tech/payments-uae.md) (کارت‌های آزمایشی درگاه): پرداخت موفق، ناموفق و webhook تکراری هر کدام یک تست سبز؛ برگشت اپ بدون webhook هیچ‌وقت «پرداخت شد» نشان نمی‌دهد.
- **بخوان:** [پرداخت](../domains/apps/app-backend.md)

### مرحله‌ی ۵: حریم خصوصی، دسترسی‌پذیری و کیفیت
- **هدف:** اپ شرط‌های رد شدن را از قبل پاس کند.
- **کارها:** سیاست حریم خصوصی داخل اپ؛ رضایت پیش از گرفتن مدرک؛ گزارش خطا بدون داده‌ی شخصی؛ صفحه‌ی اجبار به‌روزرسانی؛ راه تماس داخل اپ؛ بازبینی با «پرامپت بررسی» طراحی اپ.
- **تمام یعنی:** «چک‌لیست هر صفحه» در [طراحی اپ](../domains/apps/app-design.md) برای همه‌ی صفحه‌ها تیک خورد با عکس؛ همه‌ی بررسی‌ها با **یک فرمان** و جدول قبول/رد ([بررسی خودکار](../domains/claude-code/verification.md)).
- **بخوان:** [عملیات اپ](../domains/apps/app-operations.md) · [شرط‌هایی که اپ را رد می‌کنند](../domains/apps/publishing-apps.md)

### مرحله‌ی ۶: محافظت و آزمون مهاجم
- **هدف:** چیزی ارزشمند در فایل نصب نماند.
- **کارها:** ساخت release با `--obfuscate --split-debug-info` و نگه داشتن symbolها؛ R8 برای بخش اندروید؛ Play Integrity برای مسیرهای حساس سرور. ❓ کتابخانه هنوز ندارد: صفحه‌ی رسمی App Attest خوانده نشده.
- **تمام یعنی:** «چک‌لیست هر انتشار» در [محافظت از اپ](../domains/apps/app-protection.md): جستجوی کلید و توکن در خروجی دیکامپایل = صفر؛ بدون لاگ و پرچم debug؛ ترافیک در mitmproxy بررسی شد؛ نسخه‌ی با امضای دیگر را سرور رد کرد. همه داخل ماشین مجازی و فقط روی اپ خودمان.
- **بخوان:** [محافظت از اپ](../domains/apps/app-protection.md)

### مرحله‌ی ۷: آماده‌سازی و ارسال به فروشگاه
- **هدف:** ارسال بدون رد شدن.
- **کارها:** Xcode 26 و targetSdk ۳۶؛ `PrivacyInfo.xcprivacy`؛ فرم Data safety، رده‌ی سنی، «ویژگی مالی»، «اپ دولتی»؛ عکس‌ها (نسخه‌ی ۱ فقط iPhone)؛ متن فروشگاه (فارسی فقط در Google)؛ حساب آزمایشی برای بازبین. فرم‌های حریم خصوصی **بعد از** فهرست نهایی SDKها. ارسال فقط با «بله»ی کاربر.
- **تمام یعنی:** «چک‌لیست ارسال» در [انتشار اپ](../domains/apps/publishing-apps.md) کامل؛ TestFlight داخلی و آزمون بسته‌ی Play نصب‌شدنی؛ اگر حساب شخصی Play است، ۱۴ روز ۱۲ آزمایشگر شروع شده.
- **بخوان:** [انتشار اپ](../domains/apps/publishing-apps.md) · [فرم‌های حریم خصوصی](../domains/apps/app-operations.md)

### مرحله‌ی ۸: پس از انتشار
- **هدف:** اپ سالم بماند و قانون‌های تازه از دست نروند.
- **کارها:** پایش کرش و ANR با آستانه‌های Android vitals؛ حداقل نسخه از سرور؛ نظر داخل اپ نه پشت دکمه؛ هر قابلیت تازه نسخه‌ی تازه برای بررسی (بند 2.5.19).
- **تمام یعنی:** نرخ کرش زیر ۱.۰۹٪ و ANR زیر ۰.۴۷٪ در کل دستگاه‌ها در Play Console؛ صفحه‌ی اجبار به‌روزرسانی با بالا بردن حداقل نسخه در سرور آزموده شد.
- **بخوان:** [عملیات اپ](../domains/apps/app-operations.md) · [قوانین اکتبر ۲۰۲۶](../domains/apps/publishing-apps.md)

## چرا این ترتیب (برای Claude)

- کار اداری کندترین بخش است و کد منتظرش نمی‌ماند؛ پس مرحله‌ی ۰ موازی است، نه اول.
- اوراکل و سه زبان در مرحله‌ی ۱ می‌آیند چون راست‌به‌چپ هسته‌ی این اپ‌هاست و درست کردنش بعداً همه‌ی صفحه‌ها را عوض می‌کند.
- طراحی (مرحله‌ی ۱٫۵) پیش از قابلیت‌ها می‌آید چون عوض کردن رنگ و فاصله و ناوبری بعداً یعنی دست زدن به همه‌ی صفحه‌ها؛ با توکن، عوض کردن سبک یک خط است.
- بک‌اند پیش از قابلیت‌ها می‌آید چون محل داده، راز و حذف حساب شرط فروشگاه و قانون‌اند و جابه‌جایی‌شان گران است.
- هر چیزی که روی دستگاه است دیده می‌شود؛ پس ارزش و تصمیم امنیتی را به سرور ببر، و هر شک بین «در اپ» و «در سرور» را به نفع سرور حل کن.
- ابزار 🧪 فقط با آزمون کوچک وارد می‌شود و 👀 هرگز پیش‌فرض نیست؛ اگر ابزار لازم فقط 👀 دارد، اول کارتش را تحقیق کن یا راهی بدون آن پیدا کن.
- قانون فروشگاه‌ها مرتب عوض می‌شود؛ پیش از ارسال تاریخ «آخرین بررسی» سند انتشار را ببین و اگر کهنه است، اول به‌روزش کن.

## خطاهایی که در پروژه‌های خودمان دیدیم 🔬

خود اپ موبایل MARIO E.G.S.H هنوز ردیفی در دفتر پروژه‌ها ندارد. این درس‌ها از سرور و سایت همان پروژه و پروژه‌های دیگرند و برای بک‌اند اپ هم صدق می‌کنند:

- 🔬 MARIO E.G.S.H: از ۱۸ خطای عمدی ۱۷ گرفته شد؛ نقطه‌ی کور قفلی بود که فقط در تابع کمکی و middleware تست داشت، نه در خود مسیر API. قاعده‌ای که روی چند لایه پخش است، در هر لایه تست می‌خواهد ([بررسی خودکار](../domains/claude-code/verification.md)).
- 🔬 MARIO E.G.S.H: لینک ورود پشت Caddy به آدرس داخلی می‌رفت و کلیدها از کپی ویندوز برای همه خواندنی بودند (دفتر پروژه‌ها).
- 🔬 MARIO E.G.S.H: تست مرورگر روی داده‌ی نمایشی، با کنار گذاشتن داده‌ی واقعی و hash برابر پیش و پس ([آزمون کامل روی کامپیوتری که داده‌ی واقعی دارد](../domains/claude-code/verification.md)).
- 🔬 MARIO E.G.S.H: مهارت سراسری روی رایانه‌ی لینوکس نصب نبود؛ بدون پرامپت شروع، کتابخانه خوانده نمی‌شود (دفتر پروژه‌ها).
- 🔬 معامله‌گر هوش مصنوعی کریپتو: کتابخانه اول خوانده نشد و دو گام بدون اوراکل ساخته شد (دفتر پروژه‌ها).

## پرامپت شروع (English)

```text
We are building a store mobile app (iOS and Android) for <company>: <one sentence>.
Follow ~/Desktop/knowledge-library/playbooks/mobile-app.md step by step.
Run the library sync first. Ask me only the "before you start" questions you cannot answer
from this message or the project folder. Show me the default stack with each card's verdict,
then go phase by phase; open each phase's "read" links before starting it, and do not call a
phase done until its "done means" gate passes and you have pasted the evidence. Use Flutter
unless my answers point elsewhere. Start the code from the library's starters/flutter-app and
run the design phase (brief, style from app-styles.md, screens from app-screen-patterns.md)
before any feature; every new screen must pass the design QA gate. Never submit to a store, change signing credentials or
pay for anything without my yes. Anything the playbook marks as a gap: research it from
primary sources and label it before relying on it.
```

## پایان کار: چه چیزی به کتابخانه برگردد

- یک ردیف برای اپ در دفتر پروژه‌ها: کارت‌ها، چه کار کرد، چه نکرد. پس از آن، 🔬های بخش بالا با درس خود اپ جایگزین شوند.
- نتیجه‌ی آزمون کوچک هر ابزار 🧪 (Codemagic، Patrol، Sentry و…) در کارتش؛ دو پروژه‌ی بی‌مشکل یعنی پیشنهاد ✅.
- تحقیق هر جای ❓ (App Attest، خرید درون‌برنامه برای محتوای دیجیتال، معافیت ۱۲ آزمایشگر) در سند مربوط.
- هر رد شدن از فروشگاه با دلیل و بند، در [انتشار اپ](../domains/apps/publishing-apps.md).
- سبک یا الگوی صفحه‌ی تازه‌ای که ساخته شد، به [کاتالوگ سبک‌ها](../domains/apps/app-styles.md) یا [کاتالوگ صفحه‌ها](../domains/apps/app-screen-patterns.md)، و اگر عمومی است به [قالب شروع](../starters/flutter-app/README.md).

## مرتبط

[برنامه‌ی کامل اولین اپ](../domains/apps/mobile-launch-playbook.md) · [حوزه‌ی اپ](../domains/apps/README.md) · [اپ دسکتاپ](desktop-app.md) · [اپ شبکه‌ی محلی](local-business-app.md) · پرامپت شروع کتابخانه
