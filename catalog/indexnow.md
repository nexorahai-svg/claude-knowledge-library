---
name: IndexNow
slug: indexnow
category: seo-search
domains: [website]
verdict: adopt
status: researched
summary: خبر دادن فوری تغییر صفحه‌ها به Bing، Yandex، Naver، Seznam و Yep
use_when: "after every site publish ; telling Bing, Yandex, Naver, Seznam, Yep about changed pages quickly"
how: "Put the key file in the site root and POST changed URLs (up to 10,000) to https://api.indexnow.org/indexnow; send only changed URLs; 200 means received not indexed, 403 bad key, 422 wrong host; Google does not use it"
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
🔬 بعد از هر انتشار، فقط آدرس‌های تغییرکرده (در یک پروژه‌ی واقعی با اسکریپت بر اساس lastmod؛ بار اول همه‌ی ۶۰ آدرس، پاسخ ۲۰۲). ✅ اگر سایت پشت Cloudflare است، Crawler Hints خودکار می‌فرستد.

✅ (https://www.indexnow.org/documentation) پاسخ‌ها: ۲۰۰ فقط یعنی «رسید»، نه نمایه شدن؛ ۲۰۲ رسید ولی بررسی کلید در انتظار است؛ ۴۰۳ کلید نامعتبر؛ ۴۲۲ آدرس مال این میزبان نیست؛ ۴۲۹ ارسال زیاد. ✅ فایل کلید با نام دیگر هم مجاز است، با `keyLocation` در هر ارسال؛ ولی فقط آدرس‌های زیر پوشه‌ی همان فایل را پوشش می‌دهد (ریشه توصیه می‌شود).

🔬 **سایت پویا** (یک فروشگاه واقعی، دفتر پروژه‌ها): کار پس‌زمینه هر ۶ ساعت از sitemap آدرس‌های تازه یا با تاریخ عوض‌شده را می‌فرستد، فهرست ارسال‌شده را نگه می‌دارد، ۲۰۰ و ۲۰۲ را رسیده می‌داند و بقیه را دفعه‌ی بعد دوباره می‌فرستد؛ تا آدرس واقعی https نباشد چیزی نمی‌فرستد. با آزمون واحد سنجیده شد؛ ❓ هنوز از دامنه‌ی زنده ارسال نشده. روش: [سئوی فنی](../domains/website/09-seo/seo-and-ai-search.md).

🔬 (یک پروژه‌ی واقعی) ارسال دوباره‌ی ۱٬۰۸۹ آدرس: پاسخ ۲۰۰ (فقط رسید) ← [سئو](../domains/website/09-seo/seo-and-ai-search.md).

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
✅ فقط آدرس تغییرکرده بفرست؛ ارسال تکراری بی‌فایده است.

## مرتبط
[سئوی فنی و جستجوی هوش مصنوعی](../domains/website/09-seo/seo-and-ai-search.md) · [S51](../sources/README.md#s51) · [S62](../sources/README.md#s62)
