---
name: Cloudflare Access (Zero Trust)
slug: cloudflare-access
category: hosting-deploy
domains: [website, security]
verdict: adopt
status: researched
summary: قفل کردن پنل مدیریت پشت ورود با کد ایمیلی؛ رایگان تا ۵۰ کاربر
use_when: "locking an admin panel such as /admin behind email login ; avoiding building our own login for a client admin area"
how: "Cloudflare Zero Trust Access with One-time PIN and an allowed-email list (free up to 50 users); the server MUST validate the Cf-Access JWT (certs at /cdn-cgi/access/certs, check aud, iss, exp) or the pages.dev URL bypasses it"
url: https://www.cloudflare.com/zero-trust/products/access/
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: low
sources: [S53, S125]
found_in: [project/client]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Cloudflare Access (Zero Trust)

## چیست
✅ جلوی یک مسیر (مثلاً `/admin`) صفحه‌ی ورود می‌گذارد و فقط ایمیل‌های مجاز را رد می‌کند. روش **One-time PIN**: کد به ایمیل، ۱۰ دقیقه اعتبار، یک‌بارمصرف. بعد از ورود، هدر امضاشده‌ی `Cf-Access-Jwt-Assertion` به سرور می‌رسد.

## کی استفاده کنیم
✅ 🔬 برای پنل مدیریت سایت مشتری به‌جای ساختن سیستم ورود. در یک پروژه‌ی واقعی: فقط ایمیل شرکت، فقط OTP.

## قیمت و مجوز
✅ (https://www.cloudflare.com/plans/sase-zero-trust.md، ۲۰۲۶-۱۰-۱۹) طرح Free: «User Limit: 50 users»، رایگان برای همیشه؛ Pay-as-you-go: ۷ دلار برای هر کاربر در ماه. ✅ هر کاربری که یک بار از Access رد شود یک «صندلی» می‌گیرد، هر تعداد اپ؛ وقتی صندلی‌ها پر شد، ورود کاربر تازه **مسدود** می‌شود (https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/). 🧭 پس فقط برای کارکنان، نه مشتری‌ها.

## ریسک و هشدار
⚠️ ✅ (https://developers.cloudflare.com/cloudflare-one/identity/authorization-cookie/validating-json/) سرور باید JWT را خودش بررسی کند (کلیدها از `/cdn-cgi/access/certs`، `kid`، RS256، `aud`، `iss`، `exp`)؛ وگرنه از آدرس `pages.dev` دور زده می‌شود. ⚠️ 🔬 اگر «همه‌ی روش‌های ورود» روشن باشد، حساب Cloudflareِ واردشده در مرورگر خودکار استفاده و رد می‌شود؛ فقط OTP بگذار. ⚠️ 🔬 ایمیل کد ممکن است در پوشه‌ی دیگری بیفتد؛ `noreply@notify.cloudflare.com` را مجاز کن.

## مرتبط
[سایت تجاری روی Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md) · [S53](../sources/README.md#s53) · [ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125)
