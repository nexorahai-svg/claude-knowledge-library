---
name: Nuxt
slug: nuxt
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: چارچوب سمت سرور و ساخت ایستا برای Vue؛ برای پروژه یا تیمی که روی Vue است
use_when: "a client or team already on Vue ; an SSR or static Vue site with i18n ; a content site generated with nuxt generate"
how: "npm create nuxt@latest my-site (official command in the nuxt.com docs), Node 22.22.3 or newer; nuxt generate builds a static site; our default stays Next or Astro unless the project is on Vue; pin the version"
url: https://nuxt.com
repo: "https://github.com/nuxt/nuxt"
license: "MIT"
pricing: free
risk: low
sources: [S215, S216]
found_in: [sweep-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Nuxt

## چیست
✅ (npm و GitHub API، ۲۰۲۶-۱۰-۳۱) nuxt 4.6.3 (انتشار ۲۰۲۶-۱۰-۲۷)؛ مخزن رسمی سازمان nuxt با حدود ۶۱ هزار ستاره، آخرین push ۲۰۲۶-۱۰-۳۱، بایگانی‌نشده. نیاز Node: ‎^22.22.3 یا ^24.15.0 یا ≥26. دستور رسمی شروع: `npm create nuxt@latest <project-name>` ✅ ([نصب](https://nuxt.com/docs/getting-started/installation)). ساخت ایستا (SSG) با `nuxt generate` پیش‌فرض است و صفحه‌های 200.html و 404.html می‌سازد ✅ ([استقرار](https://nuxt.com/docs/getting-started/deployment)).

## کی استفاده کنیم
🧭 فقط اگر مشتری یا تیم روی Vue است یا سایت SSR/ایستای Vue با چندزبانه‌سازی می‌خواهیم. پیش‌فرض ما [Next.js](nextjs.md) و [Astro](astro.md) می‌ماند. هنوز در هیچ پروژه‌ای آزموده نشده.

## قیمت و مجوز
✅ MIT و رایگان؛ هزینه‌ی میزبانی جداست.

## ریسک و هشدار
🧭 ریسک کم (چارچوب رسمی و فعال). Node لازم نسبتاً تازه است (۲۲.۲۲.۳)؛ نسخه را در پروژه پین کن.

## مرتبط
[تکنولوژی وبسایت](../domains/website/04-tech/tech-stack.md) · [S215](../sources/README.md#s215) · [S216](../sources/README.md#s216)

🧭 (۲۰۲۶-۱۰-۳۱: 🧪 به ✅) تصمیم مالک: در کار واقعی جوابگوست.
