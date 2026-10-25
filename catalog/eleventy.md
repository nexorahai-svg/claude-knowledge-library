---
name: Eleventy (11ty)
slug: eleventy
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: سازنده‌ی سایت ایستای ساده و سریع؛ خروجی HTML خالص، مناسب سایت شرکتی چندزبانه
url: https://www.11ty.dev/
repo: "https://github.com/11ty/eleventy"
license: "MIT"
pricing: free
risk: low
sources: [S55]
found_in: [project/client]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Eleventy (11ty)

## چیست
✅ سازنده‌ی سایت ایستا با Node (حداقل نسخه‌ی ۱۸)، قالب‌های Nunjucks، Liquid، Markdown و JavaScript؛ خروجی HTML بدون فریم‌ورک سمت مرورگر. آخرین نسخه‌ی پایدار ✅ **3.1.7**؛ نسخه‌ی ۴ هنوز آلفا (با نام تازه‌ی «Build Awesome»).

## کی استفاده کنیم
🔬 سایت شرکتی چندصفحه‌ای و دوزبانه که بیشتر محتواست: یک سایت مشتری (۶۰ صفحه، انگلیسی و عربی) با Lighthouse SEO ۱۰۰ و PageSpeed ۹۶ تا ۹۸ (دفتر پروژه‌ها). 🧭 وقتی تعامل سنگین React لازم نیست، از Next.js سبک‌تر و ساده‌تر است؛ در کنار Astro گزینه‌ی دوم ما برای سایت شرکتی.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
✅ (https://github.com/11ty/eleventy-img/releases) در `@11ty/eleventy-img` نسخه‌ی ۷، `Image.statsSync` حذف شد؛ به‌جایش گزینه‌ی `statsOnly`. 🔬 shortcode ناهمگام داخل `{% set %}` خروجی خالی داد؛ ما یک نشانه‌گذار و transform ناهمگام ساختیم.

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [S55](../sources/README.md#s55)
