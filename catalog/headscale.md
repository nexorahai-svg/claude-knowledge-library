---
name: Headscale
slug: headscale
category: hosting-deploy
domains: [website, apps, security]
verdict: trial
status: researched
summary: سرور کنترل متن‌باز و خودمیزبان برای Tailscale؛ VPN همکاران بدون طرح پولی Tailscale
use_when: "collaborators need access to an admin panel or server SSH only from their devices, commercially ; free self-hosted Tailscale control server"
how: "Trial first on a small task: run Headscale (BSD-3) with a pinned version and sha256 behind Caddy at vpn.<domain>, DERP key owned by the headscale user, run configtest; HIGH risk because it controls who reaches the management network; keep it updated (0.29.7+ and Tailscale clients 1.104.4+, security release 2026-10-30); users use the normal Tailscale app"
url: https://headscale.net/
repo: "https://github.com/juanfont/headscale"
license: "BSD-3-Clause"
pricing: free
risk: high
sources: [S61]
found_in: [project/client]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Headscale

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v0.29.7 (۲۰۲۶-۱۰-۳۰) **انتشار امنیتی** است: یافته‌های پروژه‌ی oss-scanner شرکت Anthropic و گزارش Tailworm را رفع می‌کند؛ هیچ‌کدام بحرانی نیست ولی بعضی باعث از کار افتادن Headscale می‌شوند. ⚠️ کلاینت‌ها هم باید Tailscale v1.104.4 یا تازه‌تر شوند، چون رفع‌های SSH و Serve در `tailscaled` روی خود دستگاه‌ها اجرا می‌شود و ارتقای Headscale به‌تنهایی کافی نیست. حداقل کلاینت پشتیبانی‌شده v1.80.0: https://github.com/juanfont/headscale/releases/tag/v0.29.7
✅ پیاده‌سازی متن‌باز و خودمیزبانِ سرور کنترل Tailscale (BSD-3-Clause، حدود ۴۵ هزار ستاره). کلیدهای WireGuard دستگاه‌ها را رد و بدل می‌کند، IP می‌دهد و مسیرها را پخش می‌کند؛ دستگاه‌ها همان اپ رسمی Tailscale را دارند. ✅ فقط **یک** tailnet را پشتیبانی می‌کند. ✅ خودش می‌گوید وابسته به شرکت Tailscale نیست (یکی از نگهدارنده‌ها کارمند Tailscale است). ✅ آخرین نسخه 0.29.5 (۲۰۲۶-۱۰-۱۳).

## کی استفاده کنیم
🧭 وقتی پنل مدیریت یا SSH سرور فقط باید از دستگاه‌های همکاران باز شود و استفاده تجاری است. ✅ طرح رایگان Personal در Tailscale «فقط برای استفاده‌ی غیرتجاری» است؛ ارزان‌ترین طرح تجاری Standard ماهی ۸ دلار برای هر کاربر (https://tailscale.com/pricing).

🔬 یک فروشگاه واقعی (دفتر پروژه‌ها): Headscale 0.29.4 با sha256 ثابت، روی `https://vpn.<دامنه>` پشت Caddy، DERP داخلی (udp/3478) به‌اضافه‌ی relayهای عمومی Tailscale، سیاست دسترسی: دستگاه‌های همکاران فقط به پورت ۴۴۳ و ۲۲ سرور. نکته‌ی طراحی: آدرس خود سایت باید از داخل VPN برود، وگرنه پنل ۴۰۴ می‌ماند؛ با رکوردهای اضافه‌ی MagicDNS حل شد. در WSL آزموده شد (۲۱ از ۲۲، و قطع دسترسی بعد از حذف دستگاه با tcpdump ثابت شد). ❓ هنوز با اپ Tailscale روی گوشی واقعی و دامنه‌ی زنده آزموده نشده؛ به همین دلیل 🧪.

## قیمت و مجوز
✅ رایگان، BSD-3-Clause. اپ کاربر همان Tailscale است.

## ریسک و هشدار
- ⚠️ ریسک بالا: کنترل می‌کند چه کسی به شبکه‌ی مدیریت می‌رسد. نسخه را ثابت و به‌روز نگه دار؛ کلید خصوصی DERP باید مال کاربر `headscale` باشد (🔬 اجرای `configtest` با root کلیدی ساخت که سرویس نمی‌توانست بخواند).
- ⚠️ ✅ README پروژه می‌گوید اجرا پشت reverse proxy و در کانتینر را «پشتیبانی و تشویق نمی‌کند». ✅ صفحه‌ی reverse proxy مستندات (نوشته‌ی جامعه) شرط می‌گذارد: پشتیبانی WebSocket و ارتقای `tailscale-control-protocol`؛ Cloudflare Proxy و Tunnel پشتیبانی نمی‌شوند؛ STUN روی udp/3478 باید عمومی باشد. 🧭 پشت Caddy کار کرد (Caddy WebSocket را خودکار رد می‌کند)، ولی در صورت مشکل، پشتیبانی رسمی ندارد.
- ✅ README هدف را «مناسب استفاده‌ی شخصی» و برای خودمیزبان‌ها و سازمان‌های کوچک می‌نامد؛ برای تیم بزرگ، طرح پولی Tailscale را بسنج.

## مرتبط
[سرور خودمان](../domains/website/04-tech/self-hosted-server.md) · [Cloudflare Tunnel](cloudflare-tunnel.md) · [S61](../sources/README.md#s61)

🔬 (۲۰۲۶-۱۰-۳۱) ارتقا به 0.29.7: نسخه را از `checksums.txt` همان انتشار پین کن و هش یک دانلود واقعی را بسنج.
