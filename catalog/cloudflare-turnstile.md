---
name: Cloudflare Turnstile
slug: cloudflare-turnstile
category: hosting-deploy
domains: [website, security]
verdict: adopt
status: researched
summary: ضد ربات رایگان برای فرم‌ها، بدون معمای تصویری؛ توکن در سرور بررسی می‌شود
use_when: "protecting a contact or inquiry form from bots ; replacing CAPTCHA"
how: "Add the Turnstile widget (free, 20 widgets) to the form and ALWAYS verify the token server-side with the secret key (Function); real keys only in the Pages build, official test keys locally"
url: https://www.cloudflare.com/products/turnstile/
repo: ""
license: "سرویس رایگان"
pricing: free
risk: low
sources: [S53]
found_in: [project/client]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Cloudflare Turnstile

## چیست
✅ جایگزین CAPTCHA: ویجتی که بدون حل معما توکن می‌سازد؛ سرور توکن را با کلید مخفی بررسی می‌کند. روی هر سایتی کار می‌کند، لازم نیست سایت روی Cloudflare باشد.

## کی استفاده کنیم
✅ 🔬 روی هر فرم تماس یا استعلام. در یک پروژه‌ی واقعی: کلید واقعی فقط در build روی Pages، کلید آزمایشی رسمی در محیط محلی.

## قیمت و مجوز
✅ (https://developers.cloudflare.com/turnstile/plans/) رایگان: ۲۰ ویجت در حساب، ۱۰ دامنه برای هر ویجت، آمار ۷ روزه. Enterprise: ویجت نامحدود، ۲۰۰ دامنه، حذف نام Cloudflare.

## ریسک و هشدار
⚠️ اگر توکن فقط در مرورگر بررسی شود، هیچ محافظتی ندارد؛ همیشه در سرور (Function) بررسی کن.

## مرتبط
[سایت تجاری روی Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md) · [S53](../sources/README.md#s53)
