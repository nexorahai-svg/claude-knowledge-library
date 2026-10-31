---
name: Tailscale
slug: tailscale
category: hosting-deploy
domains: [website, security]
verdict: trial
status: researched
summary: شبکه‌ی خصوصی WireGuard بین دستگاه‌ها برای دسترسی امن به سرورها بدون پورت باز
use_when: "admin access to a customer server without exposing SSH to the internet"
how: "Trial first on a small task: on each machine run curl -fsSL https://tailscale.com/install.sh | sh then sudo tailscale up and log in; Tailscale SSH for admin access; control plane is Tailscale cloud (free tier limits), self-host alternative is Headscale"
url: https://tailscale.com
repo: "https://github.com/tailscale/tailscale"
license: "BSD-3-Clause (کلاینت)"
pricing: freemium
risk: low
sources: [S160]
last_checked: 2026-10-27
next_check: "2026-11-26"
---

# Tailscale

## چیست
✅ کلاینت متن‌باز (BSD-3، حدود ۳۸ هزار ستاره)؛ سرور هماهنگی سرویس ابری است مگر با [Headscale](headscale.md). آخرین انتشار v1.104.2 در ۲۰۲۶-۱۰-۲۱.
✅ قیمت (https://tailscale.com/pricing، ۲۰۲۶-۱۰-۲۷): طرح Personal رایگان، تا ۶ کاربر؛ طرح‌های تیمی پولی (از ۸ دلار برای هر کاربر در صفحه‌ی قیمت).
✅ نصب و اجرا (https://tailscale.com/docs/install/linux، ۲۰۲۶-۱۰-۲۷): curl -fsSL https://tailscale.com/install.sh | sh ; sudo tailscale up

## کی استفاده کنیم
🧭 برای دسترسی مدیریتی به سرور مشتری بدون باز کردن SSH روی اینترنت.
