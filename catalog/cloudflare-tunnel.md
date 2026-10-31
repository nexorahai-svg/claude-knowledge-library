---
name: Cloudflare Tunnel (cloudflared)
slug: cloudflare-tunnel
category: hosting-deploy
domains: [website]
verdict: adopt
status: researched
summary: آدرس موقت HTTPS برای سایت در حال ساخت روی کامپیوتر خودت، بدون حساب
use_when: "showing a site in progress on localhost to a client for one session ; testing webhooks against a local service"
how: "cloudflared tunnel --url http://localhost:3000 (Quick Tunnel, no account, URL changes each run); add --allowed-mail to restrict by email; test only, 200 concurrent request cap, no SSE; use real hosting for lasting previews"
url: https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/
repo: "https://github.com/cloudflare/cloudflared"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S23, S61, S73, S76, S114, S134]
found_in: [batch-01/P22]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Cloudflare Tunnel (cloudflared)

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) cloudflared 2026.10.7 (۲۰۲۶-۱۰-۳۰)؛ یادداشت انتشار فقط چک‌سام‌هاست و تغییر امنیتی ذکر نشده؛ Apache-2.0 بی‌تغییر؛ پروژه‌ها نسخه را از checksums همان انتشار پین کنند: https://github.com/cloudflare/cloudflared/releases
✅ (جاروی ۲۰۲۶-۱۰-۲۸) cloudflared 2026.10.5 (۲۰۲۶-۱۰-۲۷)؛ Apache-2.0 بی‌تغییر.
✅ **Quick Tunnel** یک آدرس موقت `trycloudflare.com` برای سرویسی که روی کامپیوترت اجرا می‌شود می‌سازد. **حساب Cloudflare و دامنه لازم نیست.** آدرس هر بار عوض می‌شود. ابزار `cloudflared` متن‌باز است (Apache-2.0، حدود ۱۶ هزار ستاره).
```bash
cloudflared tunnel --url http://localhost:3000
```

## کی استفاده کنیم
🧭 نشان دادن سایت در حال ساخت به مشتری برای یک جلسه، تست webhook، یا اینکه سرویس بیرونی به پروژه‌ی محلی برسد. برای پیش‌نمایش ماندگار، میزبانی معمولی (مثل پیش‌نمایش Vercel) بهتر است.

## محدودیت‌ها
✅ (صفحه‌ی رسمی، به‌روز ۲۰۲۶-۰۹-۳۰): فقط برای تست و توسعه؛ **بدون تضمین در دسترس بودن**؛ **حداکثر ۲۰۰ درخواست هم‌زمان** (بیشتر خطای ۴۲۹)؛ **Server-Sent Events پشتیبانی نمی‌شود**.

## امنیت
✅ **محدود کردن با ایمیل:** با پرچم `--allowed-mail` فقط ایمیل‌های مشخص (یا یک دامنه‌ی ایمیل) با کد یک‌بارمصرف وارد می‌شوند؛ بازدیدکننده حساب Cloudflare لازم ندارد.
```bash
cloudflared tunnel --url http://localhost:3000 --allowed-mail client@example.com
```
بدون این پرچم، **هر کس آدرس را داشته باشد** به سایت محلی‌ات می‌رسد. 🧭 هرگز پنل مدیریت، فایل `.env`، پایگاه داده یا داده‌ی واقعی مشتری را باز نکن؛ تونل را فقط در زمان جلسه روشن نگه دار.

**به `CF-Connecting-IP` فقط از loopback اعتماد کن:** ✅ Cloudflare این هدر را روی ترافیک لبه به سرور می‌فرستد، ولی هر کسی که مستقیم به سرور برسد هم می‌تواند آن را بفرستد. 🔬 (شبیه‌سازی‌شده، نه تونل واقعی) در یک پروژه‌ی سفارش با QR یک گوشی روی Wi-Fi می‌توانست خودش را «داخل» جا بزند؛ cloudflared باید روی همان رایانه باشد و سرور هدر را فقط از 127.0.0.1 یا ::1 بپذیرد ([S73](../sources/README.md#s73)، [اپ روی یک رایانه در محل](../domains/apps/local-network-app.md)).

**آدرس موقت برای webhook محصول کافی نیست:** 🔬 یک محصول واقعی به‌طور پیش‌فرض با Quick Tunnel آدرس عمومی برای webhook اینستاگرام، واتساپ و تلگرام می‌سازد. در آزمون واقعی پروژه (۲۰۲۶-۱۰-۱۰) آدرس با هر روشن شدن عوض شد، پس آدرس‌های ثبت‌شده در Meta (callback، حریم خصوصی، حذف داده) و لینک فرم و پرداختی که قبلاً برای مشتری فرستاده شده بود از کار افتاد؛ انتشار اپ Meta هم با آدرس موقت ممکن نبود. این با همان قید رسمی «فقط برای تست، بدون تضمین در دسترس بودن» جور است. 🧭 برای محصولی که پیام مشتری می‌گیرد، از روز اول تونل نام‌دار با دامنه یا دامنه‌ی خود مشتری.

🔬 **آزمون واقعی (یک پروژه‌ی سفارش با QR، ۲۰۲۶-۱۰-۱۹، cloudflared 2026.10.0 از انتشار رسمی GitHub با checksum، بدون sudo در `~/.local/bin`):** Quick Tunnel به یک کپی آزمایشی. از همان رایانه از راه آدرس `trycloudflare.com`: سرور هدر `CF-Connecting-IP` را با نشانی عمومی همان شبکه گرفت («داخل»)؛ از یک سرویس بیرونی: «بیرون». آدرس تازه حدود ۱۰ تا ۳۰ ثانیه بعد جواب داد. بعد از خاموش کردن، آدرس ۵۰۲ داد. ⚠️ ابزار WebFetch در Claude Code از خود رایانه درخواست می‌دهد؛ برای «دید از بیرون» به کار نمی‌آید ([S114](../sources/README.md#s114)).

**تونل دائمی با دامنه‌ی خودت (برای هر مشتری یک تونل، خودکار با API):** ✅ ([S134](../sources/README.md#s134)، مستندات رسمی ۲۰۲۶-۱۰)
- **هر حساب ۱٬۰۰۰ تونل** بدون هزینه دارد؛ بیشتر از آن با «Tunnels for Platforms»، **ماهی ۴٫۵ دلار برای هر تونل اضافه** (از ۲۰۲۶-۱۰-۱۶). پر شدن سقف تونل‌های موجود را قطع نمی‌کند، فقط ساخت تونل تازه رد می‌شود. هر تونل تا ۲۵ نسخه‌ی هم‌زمان cloudflared.
- **ساخت کاملاً خودکار، سه درخواست API:** `POST /accounts/<id>/cfd_tunnel` با `config_src: "cloudflare"` (پاسخ `id` و `token` دارد) → `PUT …/cfd_tunnel/<id>/configurations` با ingress (`hostname` → `http://localhost:<port>` و در آخر حتماً یک قانون `http_status:404`) → `POST /zones/<zone>/dns_records` با CNAME به `<id>.cfargotunnel.com` و `proxied: true`. توکن API فقط دو مجوز: Account › Cloudflare Tunnel › Edit و Zone › DNS › Edit.
- **نصب در محل مشتری یک دستور است:** `cloudflared service install <TUNNEL_TOKEN>` (ویندوز در Command Prompt مدیر، لینوکس با sudo). ⚠️ هر کس توکن تونل را داشته باشد همان تونل را اجرا می‌کند؛ توکن API حساب هرگز به مشتری داده نشود. توکن لو رفته → چرخاندن توکن و حذف اتصال‌ها با API.
- ⚠️ **فقط یک سطح زیردامنه رایگان گواهی دارد:** Universal SSL فقط `example.com` و `*.example.com` را می‌پوشاند. `cafe1.example.com` کار می‌کند؛ `cafe1.order.example.com` خطای TLS می‌دهد مگر Advanced Certificate Manager (افزونه‌ی پولی، ماهی ۱۰ دلار، Total TLS). 🧭 نام مشتری‌ها را مستقیم زیر دامنه‌ی اصلی بگذار.
- محافظت از پنل با Cloudflare Access.

🔬 **ساخته و آزموده در یک پروژه‌ی سفارش با QR (۲۰۲۶-۱۰-۲۱؛ هنوز بدون حساب واقعی):** ابزار `tools/provision.js` (Node بی‌بسته) برای هر کافه تونل + ingress + CNAME + یک فایل `.qro` (نشانی + توکن همان تونل، 0600) می‌سازد؛ در محل یک دستور (`connect.sh` / `connect.bat`). درس‌ها:
- 🔬 **اول آزاد بودن نام را بررسی کن، بعد چیزی بساز.** نسخه‌ی اول تونل را قبل از بررسی DNS می‌ساخت؛ نام گرفته‌شده رد می‌شد ولی تونل بی‌صاحب می‌ماند (آزمون با API جعلی گرفت).
- 🔬 رکورد DNS را با `comment` («qr-order <name>») علامت بزن و فقط رکورد علامت‌دار را عوض یا پاک کن؛ رکورد دیگران (مثلاً سایت خود محصول) دست‌نخورده.
- 🔬 در محل: توکن در فایل و `--token-file` (نه در خط فرمان، که در فهرست پردازش‌ها دیده می‌شود)؛ توکن فقط با نویسه‌های `[A-Za-z0-9+/=_-]` پذیرفته شود تا اسکریپت `.bat` یا shell آن را اجرا نکند؛ دانلود cloudflared با نسخه‌ی ثابت و sha256 از یادداشت انتشار.
- 🔬 سرویس کاربری systemd با `ProtectSystem=strict`، `ProtectHome=read-only`، بدون هیچ مسیر نوشتنی: cloudflared اجرا و به لبه‌ی Cloudflare وصل شد (`systemd-analyze --user security` = 2.3). ⚠️ `--logfile` را در سرویس نگذار: cloudflared فایل را کوتاه نمی‌کند و با توکن غلط در یک دقیقه ۲۱ کیلوبایت نوشت؛ journald کافی است. بیرون از systemd: `--loglevel warn`.
- 🔬 ابزار را با یک API جعلی Cloudflare روی 127.0.0.1 بیازما (همان مسیرها و شکل پاسخ)؛ توکن هرگز به http غیر از همین رایانه فرستاده نشود.

## قیمت و مجوز
✅ Quick Tunnel رایگان؛ cloudflared با Apache-2.0.

## جایگزین‌ها
✅ ngrok رایگان: یک دامنه، ۱ گیگ داده و ۲۰ هزار درخواست در ماه، با صفحه‌ی هشدار برای بازدیدکننده. ✅ Tailscale Funnel: هنوز بتا، روی همه‌ی طرح‌ها (فقط پورت‌های ۴۴۳، ۸۴۴۳ و ۱۰۰۰۰؛ MagicDNS و HTTPS لازم). ⚠️ ✅ ولی طرح رایگان Personal در Tailscale «فقط برای استفاده‌ی غیرتجاری» است؛ برای کار شرکت یا مشتری طرح Standard (ماهی ۸ دلار برای هر کاربر) یا [Headscale](headscale.md) ([S61](../sources/README.md#s61)). ✅ Port forwarding در VS Code: به‌طور پیش‌فرض خصوصی (ورود با گیت‌هاب).

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [اپ روی یک رایانه در محل](../domains/apps/local-network-app.md) · [S23](../sources/README.md#s23)

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: 2026.10.6 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
