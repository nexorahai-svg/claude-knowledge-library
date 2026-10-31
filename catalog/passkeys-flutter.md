---
name: passkeys (Flutter، Corbado)
slug: passkeys-flutter
category: app-frameworks
domains: [apps]
verdict: assess
status: researched
summary: بسته‌ی Flutter برای ثبت‌نام و ورود با passkey (WebAuthn) در Android، iOS، macOS، وب و Windows، با سرور Corbado یا سرور خودمان؛ BSD-3-Clause
use_when: "adding passkey sign-in to a Flutter app after email-code login works ; connecting a Flutter client to our own WebAuthn relying-party server"
how: "dart pub add passkeys (2.23.x); pair with our own WebAuthn server, not Corbado, unless the user decides otherwise; test on a real phone with apple-app-site-association and assetlinks.json set up"
url: https://pub.dev/packages/passkeys
repo: "https://github.com/corbado/flutter-passkeys"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# passkeys (Flutter، Corbado)

## چیست
✅ بسته‌ی `passkeys` نسخه‌ی 2.23.1 (۲۰۲۶-۰۹-۱۴)، ناشر تأییدشده `corbado.com`، ۱۵۰ از ۱۶۰ امتیاز و ۱۱۴ پسند در https://pub.dev/packages/passkeys. توضیح بسته: با سرور آماده‌ی Corbado یا با relying party خودمان کار می‌کند.
- ✅ [README مخزن](https://github.com/corbado/flutter-passkeys) سکوها را Android، iOS، macOS، وب و Windows می‌گوید؛ لینوکس نه. مخزن حدود ۱۸۸ ستاره، آخرین push ۲۰۲۶-۰۹-۱۷، آرشیو نشده.
- ✅ مخزن بسته‌های دیگر هم دارد: `corbado_auth` (فقط با سرور Corbado) و `corbado_auth_firebase` که README می‌گوید «فعلاً خراب است و زمان رفع معلوم نیست». این دو را استفاده نکن.
- ✅ بسته‌ی رسمی Flutter یا گوگل برای passkey پیدا نشد؛ این بسته‌ی شرکتی است.
- ❓ هنوز آزموده نشده که با افزونه‌ی passkey در [Better Auth](better-auth.md) (SimpleWebAuthn) بدون Corbado جفت می‌شود. فایل‌های `apple-app-site-association` و `assetlinks.json` باید تنظیم شوند (راهنمای مخزن، خوانده نشد).
- ✅ تا ۲۰۲۶-۱۰-۳۰ هنوز نسخه‌ی تازه‌تری از `passkeys` 2.23.1 (۲۰۲۶-۰۹-۱۴) در https://pub.dev/api/packages/passkeys نیست و آخرین releaseهای مخزن همگی ۲۰۲۶-۰۹-۱۴ هستند (https://github.com/corbado/flutter-passkeys/releases)؛ یعنی حدود ۴۶ روز بدون انتشار.

## قیمت و مجوز
✅ بسته رایگان با BSD-3-Clause (متن در https://github.com/corbado/flutter-passkeys/blob/main/LICENSE؛ حق نسخه Corbado GmbH ۲۰۲۳)؛ استفاده‌ی تجاری آزاد با حفظ اعلان حق نسخه. ❓ سرویس Corbado قیمت جدا دارد و لازم نیست اگر سرور خودمان کافی باشد؛ بررسی نشد.

## ریسک و هشدار
- 🧭 وابستگی به یک شرکت؛ اگر نگهداری قطع شود جایگزین رسمی نداریم.
- 🧭 لاگین حساس است؛ فقط با سرور WebAuthn بازبینی‌شده و آزمون روی گوشی واقعی.

## کی استفاده کنیم
🧭 نسخه‌ی ۲ اپ، پس از اینکه ورود با کد ایمیلی کار کرد. پیش از آن، آزمون روی گوشی واقعی با سرور خودمان. ارتقا به trial: پیشنهاد نمی‌کنم تا جفت‌شدن با سرور خودمان آزموده شود.

## مرتبط
[ورود مشتری، passkey](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125) · [Better Auth](better-auth.md)
