---
name: RustDesk
slug: rustdesk
category: hosting-deploy
domains: [apps]
verdict: trial
status: researched
summary: دسترسی از راه دور به دسکتاپ، با سرور خودمیزبان
use_when: "remote support for a customer's computer"
how: "Trial first on a small task: self-host hbbs and hbbr with docker run --net=host rustdesk/rustdesk-server (hbbs / hbbr, -v ./data:/root), open TCP 21115-21117 + UDP 21116, then set ID/relay server and key in clients; AGPL-3.0"
url: https://rustdesk.com
repo: "https://github.com/rustdesk/rustdesk"
license: "AGPL-3.0"
pricing: free
risk: medium
sources: [S160]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# RustDesk

## چیست
✅ (AGPL-3.0، حدود ۱۲۷ هزار ستاره، فعال؛ آخرین انتشار 1.5.0 در ۲۰۲۶-۰۹-۳۰؛ سرور rustdesk-server نسخه‌ی 1.1.16).
✅ پورت‌ها (https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/، ۲۰۲۶-۱۰-۲۷): hbbs ‏21115 TCP و 21116 TCP+UDP؛ hbbr ‏21117 TCP. پورت 21114 (کنسول وب) فقط در نسخه‌ی Pro است. پورت‌های 21118 و 21119 فقط برای کلاینت وب‌اند؛ اگر لازم نیستند ببند، و اگر لازم‌اند فقط پشت reverse proxy بگذار، چون هدر IP در آن‌ها اعتبارسنجی نمی‌شود.
✅ قیمت (https://rustdesk.com/pricing، ۲۰۲۶-۱۰-۲۷): طرح متن‌باز خودمیزبان رایگان؛ مجوز Server Pro پولی و سالانه.
✅ نصب و اجرا (https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/، ۲۰۲۶-۱۰-۲۷): sudo docker run --name hbbs -v ./data:/root -td --net=host --restart unless-stopped rustdesk/rustdesk-server hbbs (و همین برای hbbr)

## کی استفاده کنیم
🧭 برای پشتیبانی مشتری؛ سرور relay خودت را بالا بیاور تا اتصال از سرور شخص ثالث نگذرد.
