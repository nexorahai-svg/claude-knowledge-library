---
name: Vercel
slug: vercel
category: hosting-deploy
domains: [website]
verdict: adopt
status: researched
summary: میزبانی و انتشار سایت با پیش‌نمایش برای هر تغییر؛ طرح رایگان فقط غیرتجاری
use_when: "hosting a Next.js site with preview URLs ; operating Vercel through Claude via MCP ; choosing a host for a client or company site"
how: "claude mcp add --transport http vercel https://mcp.vercel.com then /mcp to log in (keep human approval on); CLI: npm i -g vercel, vercel for preview, vercel env pull; Hobby is personal non-commercial only so use Pro 20 USD per dev for paid sites, or Cloudflare Pages"
url: https://vercel.com/
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: low
sources: [S20]
found_in: [batch-01/P00]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Vercel

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) changelog ۲۰۲۶-۱۰-۲۷: دید ترافیک ربات‌های AI در Observability و ران‌تایم کانتینر با Dockerfile ساده. https://vercel.com/changelog
✅ سکوی میزبانی و انتشار سایت: از گیت یا CLI منتشر می‌کند، برای هر تغییر یک آدرس پیش‌نمایش می‌سازد، CDN و Functions و دامنه دارد. Next.js، Astro، SvelteKit، Nuxt، Vite، Hugo، Eleventy و… را پشتیبانی می‌کند. ✅ مستندات می‌گویند اگر فریم‌ورکی شناسایی نشود، پیش‌تنظیم «Other» انتخاب می‌شود و فرمان build را دستی می‌دهی (https://vercel.com/docs/deployments/configure-a-build)؛ این فقط وجود پیش‌تنظیم را تأیید می‌کند، نه یک نمونه‌ی HTML ساده.

## کی استفاده کنیم
🧭 بهترین تجربه‌ی کار برای Next.js و پیش‌نمایش سریع. برای دموی شخصی طرح رایگان کافی است؛ برای **سایت شرکت یا سایتی که بابتش پول گرفته‌ای، Pro لازم است**.

## قیمت و مجوز
✅ **قانون مهم** (https://vercel.com/docs/limits/fair-use-guidelines): «تیم‌های Hobby فقط برای استفاده‌ی شخصی و غیرتجاری‌اند؛ هر استفاده‌ی تجاری Pro یا Enterprise لازم دارد.» تعریف تجاری: هر سایتی که برای سود مالی **هر کسی** که در ساختش نقش داشته استفاده شود، **حتی برنامه‌نویس یا مشاور پولی**. مثال‌ها: فروش، تبلیغ کالا یا خدمت، گرفتن پول برای ساخت یا میزبانی سایت، تبلیغات. پس **سایت شرکت = تجاری**.

✅ (https://vercel.com/docs/plans/hobby) طرح رایگان در ماه: ۱۰۰ گیگابایت انتقال داده، ۱ میلیون درخواست CDN، ۱ میلیون اجرای Function، ۴ ساعت CPU فعال. با عبور از سقف باید ۳۰ روز صبر کنی (خرید اضافه ندارد).
✅ (https://vercel.com/pricing) **Pro: ۲۰ دلار در ماه برای هر توسعه‌دهنده**، شامل ۲۰ دلار اعتبار مصرف، ۱ ترابایت انتقال داده، مدیریت هزینه. رمز گذاشتن روی سایت افزونه‌ی جدا است (۲۰ دلار برای هر پروژه در ماه).

## ابزار برای Claude
✅ **MCP رسمی** (https://vercel.com/docs/agent-resources/vercel-mcp):
```bash
claude mcp add --transport http vercel https://mcp.vercel.com
```
بعد `/mcp` برای ورود. جستجوی مستندات، مدیریت پروژه و انتشار، خواندن لاگ. ⚠️ طبق خود مستندات: «همان دسترسی حساب Vercel تو را به هوش مصنوعی می‌دهد»؛ تأیید انسانی را همیشه روشن نگه دار.
✅ CLI: `npm i -g vercel` · `vercel` (انتشار پیش‌نمایش) · `vercel deploy --prod` · `vercel env pull`.

## جایگزین‌ها
| سرویس | واقعیت | وضعیت |
|---|---|---|
| GitHub Pages | ✅ «برای راه انداختن کسب‌وکار آنلاین، فروشگاه یا سایتی که عمدتاً تراکنش تجاری دارد مجاز نیست»؛ ۱ گیگ حجم، حدود ۱۰۰ گیگ ترافیک ماهانه | برای سایت شرکت توصیه نمی‌شود 🧭 |
| Cloudflare Pages | ✅ رایگان: ۵۰۰ build در ماه، ۲۰ هزار فایل در هر سایت؛ صفحه‌ی محدودیت‌ها سقف ترافیک ذکر نکرده | ✅ استفاده‌ی تجاری مجاز (جز دریافت کارت بانکی)؛ [کارت](cloudflare-pages.md) 🔬 (یک پروژه‌ی واقعی) |
| Netlify | ✅ طرح رایگان با سقف ۳۰۰ اعتبار؛ هر گیگابایت ترافیک ۲۰ اعتبار | ❓ قوانین خوانده نشده |

## ریسک و هشدار
کم برای خود میزبانی. ⚠️ استفاده از طرح رایگان برای سایت شرکت نقض قوانین است. ⚠️ MCP دسترسی کامل حساب را می‌دهد.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S20](../sources/README.md#s20)
