---
name: Uptime Kuma
slug: uptime-kuma
category: hosting-deploy
domains: [website, security]
verdict: trial
status: researched
summary: پایش خودمیزبان در دسترس بودن سایت و سرویس با هشدار
use_when: "knowing a client site is down before the client does"
how: "Trial first on a small task: docker run -d --restart=always -p 127.0.0.1:3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2, then add HTTP/ping/SSL monitors and Telegram or email alerts; keep the panel behind login and a tunnel (MIT)"
url: https://github.com/louislam/uptime-kuma
repo: "https://github.com/louislam/uptime-kuma"
license: "MIT"
pricing: free
risk: low
sources: [S158]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Uptime Kuma

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 2.5.8 (۲۰۲۶-۱۰-۲۶)؛ MIT بی‌تغییر.
✅ پایشگر خودمیزبان (MIT، حدود ۹۳ هزار ستاره، فعال؛ آخرین انتشار 2.5.8 در ۲۰۲۶-۱۰-۲۶؛ README دستور bind به 127.0.0.1 را هم می‌دهد): HTTP، پینگ، گواهی SSL، با هشدار تلگرام و ایمیل.
✅ نصب و اجرا (https://github.com/louislam/uptime-kuma، ۲۰۲۶-۱۰-۲۷): docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2

## کی استفاده کنیم
🧭 برای اینکه از قطع شدن سایت مشتری پیش از خود مشتری باخبر شویم. پنلش پشت ورود و تونل، نه پورت باز.
