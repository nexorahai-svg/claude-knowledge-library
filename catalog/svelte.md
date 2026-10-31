---
name: Svelte و SvelteKit
slug: svelte
category: site-generators
domains: [website]
verdict: adopt
status: researched
summary: چارچوب UI کامپایلری (Svelte 5) و چارچوب اپ آن (SvelteKit 3)؛ جایگزین Next و Astro وقتی حجم بسته مهم است یا مشتری روی Svelte است
use_when: "a small fast site or app where bundle size matters ; a client or team already on Svelte ; a static site via adapter-static"
how: "npx sv create my-app (official command in the svelte.dev docs), Node 22.17 or newer for SvelteKit 3; our default stays Next or Astro unless the project has a reason; read the docs and pin versions"
url: https://svelte.dev
repo: "https://github.com/sveltejs/kit"
license: "MIT"
pricing: free
risk: low
sources: [S215, S216]
found_in: [sweep-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Svelte و SvelteKit

## چیست
✅ (npm و GitHub API، ۲۰۲۶-۱۰-۳۱) svelte 5.57.3 (۲۰۲۶-۱۰-۲۶) و `@sveltejs/kit` 3.1.1 (Node ≥22.17)؛ مخزن‌های رسمی سازمان sveltejs با حدود ۸۸٬۵۰۰ و ۲۰٬۹۰۰ ستاره، آخرین push ۲۰۲۶-۱۰-۳۰، بایگانی‌نشده. Svelte کد را موقع ساخت کامپایل می‌کند، پس زمان اجرای سنگین ندارد. دستور رسمی شروع در مستندات: `npx sv create my-app` ✅ ([ساخت پروژه](https://svelte.dev/docs/kit/creating-a-project)). خروجی ایستا با `adapter-static` در مستندات SvelteKit هست ✅.

## کی استفاده کنیم
🧭 فقط وقتی مشتری یا تیم روی Svelte است، یا سایت کوچک و سریع می‌خواهیم که حجم بسته برایش مهم است. پیش‌فرض ما همچنان [Next.js](nextjs.md) و [Astro](astro.md) می‌ماند. هنوز در هیچ پروژه‌ای آزموده نشده. ❓ رفتار RTL و فارسی را نیازموده‌ایم.

## قیمت و مجوز
✅ MIT و رایگان؛ هزینه‌ی میزبانی جداست.

## ریسک و هشدار
🧭 ریسک کم (چارچوب رسمی و فعال). نکته‌ی نگهداری: SvelteKit 3 حداقل Node 22.17 می‌خواهد؛ نسخه‌ها را در پروژه پین کن. اکوسیستم کامپوننت‌های آماده کوچک‌تر از React است 🧭.

## مرتبط
[تکنولوژی وبسایت](../domains/website/04-tech/tech-stack.md) · [S215](../sources/README.md#s215) · [S216](../sources/README.md#s216)

🧭 (۲۰۲۶-۱۰-۳۱: 🧪 به ✅) تصمیم مالک: در کار واقعی جوابگوست.
