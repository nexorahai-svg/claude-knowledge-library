---
name: Keycloak
slug: keycloak
category: database-backend
domains: [website, apps, security]
verdict: assess
status: researched
summary: سرور هویت و دسترسی متن‌باز (OpenID Connect، SAML، SSO) برای وقتی چند اپ یک ورود مشترک یا مشتری سازمانی SAML می‌خواهد؛ Apache-2.0
use_when: "several separate apps need one shared sign-in (SSO) ; an enterprise client requires SAML or an identity provider we host ourselves"
how: "Do not deploy without the user's yes; run only a pinned release (26.8.x) from https://www.keycloak.org/ on its own host, never expose the admin console publicly; mobile apps sign in through the system browser with PKCE (RFC 8252)"
url: https://www.keycloak.org/
repo: "https://github.com/keycloak/keycloak"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Keycloak

## چیست
✅ سرور مستقل مدیریت هویت و دسترسی ([README](https://github.com/keycloak/keycloak)): ورود یکپارچه (SSO)، OpenID Connect، SAML، اتصال به دایرکتوری کاربران (user federation)، احراز هویت قوی و مجوزدهی ریزدانه.
- ✅ آخرین نسخه 26.8.1 (۲۰۲۶-۱۰-۱۳)، پیش‌تر 26.8.0 (۱۰-۰۱) و 26.7.5 (۰۹-۳۰) در https://github.com/keycloak/keycloak/releases؛ حدود ۳۷٫۶ هزار ستاره؛ آخرین push ۲۰۲۶-۱۰-۲۸؛ آرشیو نشده. نشان‌های OpenSSF و CLOMonitor در README هست و سیاست افشای آسیب‌پذیری دارد ([SECURITY.md](https://github.com/keycloak/keycloak/blob/main/SECURITY.md)).
- ✅ نوشته‌شده با Java؛ پروژه‌ای بالغ و پرنگهدارنده است.
- ✅ نیاز حافظه و پردازنده و آگهی‌های امنیتی ۲۰۲۶ در بخش «بررسی دوباره» پایین همین کارت از منبع رسمی آمده؛ هزینه‌ی نگهداری عدد منتشرشده ندارد (منتشر نشده، بسته به سرور و زمان تو).
- ✅ گزینه‌های مشابه خودمیزبان: Zitadel (AGPL-3.0) و Logto (MPL-2.0)؛ ✅ مجوزها دوباره با GitHub API دیده شد (https://github.com/zitadel/zitadel ، https://github.com/logto-io/logto).

## قیمت و مجوز
✅ Apache-2.0 (https://github.com/keycloak/keycloak/blob/main/LICENSE.txt)؛ رایگان و استفاده‌ی تجاری آزاد. هزینه‌ی واقعی: سرور، پشتیبان‌گیری و زمان نگهداری.

## ریسک و هشدار
- 🧭 سرور ورود، هدف مهم حمله است: به‌روزرسانی سریع نسخه‌های وصله‌ای، کنسول مدیریت پشت شبکه‌ی خصوصی یا VPN، پشتیبان رمزگذاری‌شده.
- 🧭 یک سرویس سنگین جداگانه برای نگهداری؛ برای یک اپ یا یک فروشگاه زیادی است.

## کی استفاده کنیم
🧭 فقط وقتی چند اپ جدا یک ورود مشترک لازم دارند یا مشتری سازمانی SAML می‌خواهد. برای یک اپ یا فروشگاه، [Better Auth](better-auth.md) 🧪 ساده‌تر است. اپ موبایل طبق RFC 8252 با مرورگر سیستم و PKCE وارد می‌شود. ارتقا: پیشنهاد نمی‌کنم؛ نیاز فعلی وجود ندارد.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125)

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ راهنمای رسمی اندازه‌گیری (https://www.keycloak.org/high-availability/multi-cluster/concepts-memory-and-cpu-sizing): حدود ۱۲۵۰MB رم پایه برای هر پاد (حد کانتینر حدود ۱۳۶۰MB). هر ۱ vCPU حدود ۱۵ ورود با گذرواژه در ثانیه را جواب می‌دهد. ۱۵۰٪ حاشیه بگذار. حداقل مطلق گفته نشده است.
- ✅ ۱۷ آگهی امنیتی در ۲۰۲۶ تا ۲۰۲۶-۱۰-۲۹ (https://github.com/keycloak/keycloak/security/advisories)؛ آخرین مورد شدت high در ۲۰۲۶-۰۹-۱۶. پس به‌روزرسانی منظم لازم است.
- ✅ مجوزها دوباره دیده شد: Zitadel با AGPL-3.0 و Logto با MPL-2.0 (GitHub API).
