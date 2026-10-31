---
name: Caddy
slug: caddy
category: hosting-deploy
domains: [website, apps]
verdict: adopt
status: researched
summary: وب‌سرور و reverse proxy با HTTPS خودکار برای سایت روی سرور خودمان، جلوی Next.js
use_when: "serving a Next.js site from our own Linux server with automatic HTTPS ; setting up a reverse proxy"
how: "Install the official Caddy 2.x (.deb from GitHub with pinned sha512 or official apt repo), point DNS at the server, open ports 80 and 443, write a Caddyfile reverse_proxy to Next.js; never strip Rsc or Next-Router-* headers; keep Caddy updated"
url: https://caddyserver.com/
repo: "https://github.com/caddyserver/caddy"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S59]
found_in: [project/client]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Caddy

## چیست
✅ وب‌سرور متن‌باز (Apache-2.0، حدود ۷۸ هزار ستاره در GitHub، آخرین نسخه‌ی پایدار 2.11.7 در ۲۰۲۶-۱۰-۰۳). وقتی DNS دامنه به سرور اشاره کند و پورت‌های ۸۰ و ۴۴۳ باز باشند، گواهی HTTPS را خودش از Let's Encrypt (و اگر نشد ZeroSSL) می‌گیرد و تمدید می‌کند و HTTP را به HTTPS می‌برد.

✅ رفتارهای مهم برای جلوی Next.js: `X-Forwarded-*` بازدیدکننده را پیش‌فرض نمی‌پذیرد ولی بقیه‌ی هدرها را بدون تغییر رد می‌کند؛ پیش‌فرض `keepalive` بالادست ۲ دقیقه است؛ `flush_interval -1` بافر را خاموش می‌کند؛ `request_body max_size` بیشتر از سقف را با ۴۱۳ رد می‌کند؛ `encode` پیش‌فرض از ۵۱۲ بایت به بالا فشرده می‌کند.

## کی استفاده کنیم
🔬 سایت Next.js روی سرور لینوکسی خودمان (یک فروشگاه واقعی، دفتر پروژه‌ها): HTTPS، پاک کردن هدرهای داخلی Next.js، فشرده‌سازی، کش فایل‌های ثابت، سقف حجم، گزارش دسترسی با IP کوتاه‌شده. ⚠️ فقط در Docker و WSL آزموده شد (با `mario.localhost`)، **نه با گواهی واقعی روی دامنه‌ی زنده**. تنظیم کامل: [سرور خودمان](../domains/website/04-tech/self-hosted-server.md).

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
- ⚠️ ریسک متوسط: جلوی اینترنت می‌نشیند؛ هر اشتباه تنظیم مستقیم دیده می‌شود. نسخه را به‌روز نگه دار.
- 🔬 ۲۰۲۶-۱۰-۰۹ مخزن apt رسمی (`dl.cloudsmith.io`) جواب ۴۰۲ داد؛ پروژه به `.deb` رسمی GitHub با sha512 ثابت رفت. ✅ ۲۰۲۶-۱۰-۱۷ همان مخزن دوباره ۲۰۰ داد؛ هر دو راه قابل استفاده است.
- ⚠️ 🔬 هدرهای `Rsc` و `Next-Router-*` را پاک نکن؛ ناوبری Next.js خراب می‌شود.

## مرتبط
[سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · [تکنولوژی](../domains/website/04-tech/tech-stack.md) · [S59](../sources/README.md#s59)
