---
name: IndexNow
slug: indexnow
category: seo-search
domains: [website]
verdict: adopt
status: researched
summary: خبر دادن فوری تغییر صفحه‌ها به Bing، Yandex، Naver، Seznam و Yep
url: https://www.indexnow.org/
repo: ""
license: "پروتکل باز"
pricing: free
risk: low
sources: [S51, S62]
found_in: [project/client, project/client]
last_checked: 2026-10-22
next_check: "2027-01-15"
---

# IndexNow

## چیست
✅ پروتکل باز: فایل کلید در ریشه‌ی سایت و یک POST به `https://api.indexnow.org/indexnow` با فهرست آدرس‌ها (تا ۱۰٬۰۰۰). گوگل عضو نیست.

## کی استفاده کنیم
🔬 بعد از هر انتشار، فقط آدرس‌های تغییرکرده (در یک سایت مشتری با اسکریپت بر اساس lastmod؛ بار اول همه‌ی ۶۰ آدرس، پاسخ ۲۰۲). ✅ اگر سایت پشت Cloudflare است، Crawler Hints خودکار می‌فرستد.

✅ (https://www.indexnow.org/documentation) پاسخ‌ها: ۲۰۰ فقط یعنی «رسید»، نه نمایه شدن؛ ۲۰۲ رسید ولی بررسی کلید در انتظار است؛ ۴۰۳ کلید نامعتبر؛ ۴۲۲ آدرس مال این میزبان نیست؛ ۴۲۹ ارسال زیاد. ✅ فایل کلید با نام دیگر هم مجاز است، با `keyLocation` در هر ارسال؛ ولی فقط آدرس‌های زیر پوشه‌ی همان فایل را پوشش می‌دهد (ریشه توصیه می‌شود).

🔬 **سایت پویا** (MARIO E.G.S.H، دفتر پروژه‌ها): کار پس‌زمینه هر ۶ ساعت از sitemap آدرس‌های تازه یا با تاریخ عوض‌شده را می‌فرستد، فهرست ارسال‌شده را نگه می‌دارد، ۲۰۰ و ۲۰۲ را رسیده می‌داند و بقیه را دفعه‌ی بعد دوباره می‌فرستد؛ تا آدرس واقعی https نباشد چیزی نمی‌فرستد. با آزمون واحد سنجیده شد؛ ❓ هنوز از دامنه‌ی زنده ارسال نشده. روش: [سئوی فنی](../domains/website/09-seo/seo-and-ai-search.md).

🔬 (یک پروژه‌ی مشتری) ارسال دوباره‌ی ۱٬۰۸۹ آدرس: پاسخ ۲۰۰ (فقط رسید) ← [سئو](../domains/website/09-seo/seo-and-ai-search.md).

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
✅ فقط آدرس تغییرکرده بفرست؛ ارسال تکراری بی‌فایده است.

## مرتبط
[سئوی فنی و جستجوی هوش مصنوعی](../domains/website/09-seo/seo-and-ai-search.md) · [S51](../sources/README.md#s51) · [S62](../sources/README.md#s62)
