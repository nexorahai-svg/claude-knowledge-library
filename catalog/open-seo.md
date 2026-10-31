---
name: OpenSEO
slug: open-seo
category: seo-search
domains: [website]
verdict: trial
status: researched
summary: جایگزین متن‌باز Ahrefs و Semrush؛ خودمیزبان، ولی داده را از DataForSEO پولی می‌گیرد
use_when: "keyword, competitor and backlink analysis when an Ahrefs subscription is not worth it"
how: "Trial first on a small task: clone every-app/open-seo, set STORAGE_SECRET_KEY and DATAFORSEO_API_KEY in deploy/standalone/.env, then docker compose pull and docker compose up -d (4 GiB RAM); DataForSEO is pay-per-use; keep sign-in on or put it behind Tailscale (MIT)"
url: https://github.com/every-app/open-seo
repo: "https://github.com/every-app/open-seo"
license: "MIT"
pricing: freemium
risk: low
sources: [S158]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# OpenSEO

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v0.1.22 (۲۰۲۶-۱۰-۳۱؛ هنوز 0.x)؛ MIT؛ یادداشت انتشار خوانده نشد ❓: https://github.com/every-app/open-seo/releases
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v0.1.19 (۲۰۲۶-۱۰-۲۶؛ هنوز 0.x)؛ MIT بی‌تغییر.
✅ ابزار سئوی خودمیزبان (MIT، حدود ۲۵ هزار ستاره، فعال؛ آخرین انتشار v0.1.19 در ۲۰۲۶-۱۰-۲۶؛ راهنمای Docker: دست‌کم ۴ گیگابایت حافظه برای Docker، کلید DataForSEO و STORAGE_SECRET_KEY در deploy/standalone/.env): کلیدواژه، رقبا، بک‌لینک. داده از API پولی DataForSEO با پرداخت به‌ازای مصرف.
✅ نصب و اجرا (https://github.com/every-app/open-seo/blob/main/docs/SELF_HOSTING_DOCKER.md، ۲۰۲۶-۱۰-۲۷): docker compose pull ; docker compose up -d

## کی استفاده کنیم
🧭 وقتی تحلیل کلیدواژه و رقیب لازم است و اشتراک ماهانه‌ی Ahrefs نمی‌ارزد. ⚠️ پست منبع آدرس اشتباه داده بود؛ مخزن درست `every-app/open-seo` است.

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v0.1.20 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
