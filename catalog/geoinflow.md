---
name: GEOInflow
slug: geoinflow
category: seo-search
domains: [website]
verdict: assess
status: researched
summary: تحلیل‌گر خودمیزبان (Docker، Postgres، Redis، فورک Umami) برای بازدید خزنده‌های AI، ارجاع از جستجوی AI و پوشش محتوا؛ بدون کوکی؛ برای سایت کوچک سنگین است
use_when: "measuring which AI crawlers and AI search engines reach a business site from server or CDN logs ; checking which pages AI crawlers never visit"
how: "Do not install without the user's yes; self-host with sh scripts/liekan-deploy.sh only on a throwaway server, change the default admin password first, and read docs/deployment.en.md plus docs/ai.md for what leaves the machine"
url: https://github.com/yaojingang/GEOInflow
repo: "https://github.com/yaojingang/GEOInflow"
license: "MIT"
pricing: free
risk: medium
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# GEOInflow

## چیست
- ✅ مخزن MIT، حدود ۶۹۰ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۸ (فعال و پرتحول). release ندارد (GitHub API): https://github.com/yaojingang/GEOInflow
- ✅ فایل LICENSE مجوز Umami (۲۰۲۲) و «Liekan contributors» (۲۰۲۶) را دارد؛ یعنی فورک و بازبسته‌بندی Umami است. README: «منتشر شده توسط 猎看科技 و 北京日报社智源GEO».
- ✅ کار آن: شناسایی خزنده‌های AI (OpenAI، Anthropic، Perplexity، Google و...) با User-Agent، فهرست IP رسمی و شواهد DNS؛ ارجاع از جستجوی AI؛ مقایسه‌ی فهرست صفحات (sitemap/CSV/JSON) با لاگ؛ همراه با آمار سایت شبیه Umami. README خودش می‌گوید لاگ خزش فقط «دسترسی دیده‌شده» را ثابت می‌کند، نه نمایه‌شدن یا نقل در پاسخ مدل.
- ✅ پشته: Docker Compose، PostgreSQL، Redis، دو worker. نصب: `sh scripts/liekan-deploy.sh` که `.env` و رمزها را می‌سازد. ردیاب مرورگر به‌طور پیش‌فرض بدون کوکی است.
- ✅ تحلیل با مدل AI پیش‌فرض خاموش است؛ در صورت روشن‌کردن، داده‌ی سایت به مدلِ انتخابی می‌رود (docs/ai.md).
- ❓ قابلیت «GEO Weight» بتا است. ❓ تله‌متری خودِ برنامه (مثل Umami) بررسی نشد.
- ✅ مستندات انگلیسی و چینی دارد.

## کی استفاده کنیم
- 🧭 فقط اگر مشتری واقعاً بخواهد بداند خزنده‌های AI به سایتش می‌رسند یا نه و به لاگ سرور/CDN دسترسی داشته باشیم. برای سایت‌های کوچک سنگین است (چهار سرویس).
- مکمل [جستجوی AI و SEO](../domains/website/09-seo/seo-and-ai-search.md)، [claude-seo](claude-seo.md) و [open-seo](open-seo.md).

## قیمت و مجوز
- ✅ رایگان، MIT، خودمیزبان: https://github.com/yaojingang/GEOInflow/blob/main/LICENSE . هزینه‌ی سرور با خود ماست.

## ریسک و هشدار
- ✅ README می‌گوید در نصب تازه کاربر `admin` با رمز `liekan` ساخته می‌شود؛ بلافاصله عوض شود و سرویس بدون HTTPS و reverse proxy به اینترنت باز نشود.
- ✅ لاگ سرور و اطلاعات بازدیدکننده (IP) را پردازش می‌کند؛ اتصال Cloudflare نیاز به کلید Zone و OAuth دارد. هرگز بدون نیاز دسترسی ندهید.
- ✅ مستندات چینی‌محور و صاحب شرکتی چینی؛ کد باید پیش از استقرار بازبینی شود (قانون ۴).

## مرتبط
[S191](../sources/README.md#s191) · https://github.com/yaojingang/GEOInflow/blob/main/docs/deployment.en.md · [جستجوی AI و SEO](../domains/website/09-seo/seo-and-ai-search.md)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ تله‌متری از Umami به ارث رسیده است (SHA `08be770`): یک POST با نسخه و مشخصات سیستم به `api.umami.is/v1/telemetry` و یک پیکسل `i.umami.is`. هر دو با `DISABLE_TELEMETRY=1` خاموش می‌شوند و `env.example` و `liekan-deploy.sh` همین را می‌گذارند. بسته‌های api-client و mcp پیش‌فرض Umami Cloud دارند، پس `UMAMI_API_URL` خودت را بده.
- ⚠️ `liekan-agent` با root یک سرویس systemd می‌سازد و لاگ دسترسی را می‌فرستد؛ فقط وقتی اجرا می‌شود که خودت فعالش کنی. ❓ کد agent خوانده نشد.
