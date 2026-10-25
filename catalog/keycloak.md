---
name: Keycloak
slug: keycloak
category: database-backend
domains: [website, apps]
verdict: assess
status: queued
summary: سرور هویت کامل و متن‌باز (OpenID Connect، SAML) برای وقتی چند اپ و یک ورود مشترک لازم است
url: https://www.keycloak.org/
repo: "https://github.com/keycloak/keycloak"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: ""
---

# Keycloak

## چیست
✅ سرور هویت مستقل (Java) با OpenID Connect و SAML؛ Apache-2.0، حدود ۳۷ هزار ستاره، نسخه‌ی `26.8.1`، فعال (https://github.com/keycloak/keycloak). ❓ قابلیت‌ها، نیاز سخت‌افزاری و آگهی‌های امنیتی هنوز تحقیق نشده.
✅ گزینه‌های مشابه خودمیزبان: Zitadel (AGPL-3.0) و Logto (MPL-2.0)؛ هر دو فعال. ❓ تحقیق نشده.

## کی استفاده کنیم
🧭 فقط وقتی چند اپ جدا یک ورود مشترک (SSO) لازم دارند یا مشتری سازمانی SAML می‌خواهد. برای یک اپ یا فروشگاه، [Better Auth](better-auth.md) 🧪 ساده‌تر است. در این حالت اپ موبایل طبق RFC 8252 با مرورگر سیستم و PKCE وارد می‌شود.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
🧭 یک سرویس جدا برای نگهداری، به‌روزرسانی و پشتیبان.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125)
