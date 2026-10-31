---
name: Thinking Orbs
slug: thinking-orbs
category: animation
domains: [website, apps]
verdict: trial
status: researched
summary: نشانگرهای بارگذاری نقطه‌ای «در حال فکر» برای رابط‌های هوش مصنوعی و عامل‌ها؛ React، MIT، بدون WebGL، با پشتیبانی کاهش حرکت
use_when: "an AI assistant or agent UI needs a calm live thinking indicator instead of a spinner"
how: "Trial first on a small task: npm i thinking-orbs@0.3.2 (React 18+, 9 orb types); pinned version, npm package built from mother repo Libraries.dev, no install script"
url: https://orbs.jakubantalik.com
repo: "https://github.com/Jakubantalik/thinking-orbs"
license: "MIT"
pricing: free
risk: low
sources: [S158]
last_checked: 2026-10-25
next_check: "2027-01-23"
---

# Thinking Orbs

## چیست
✅ کتابخانه‌ی React (`thinking-orbs` در npm، نسخه‌ی 0.3.2، حدود ۱۳۰ کیلوبایت، فقط `react >= 18` به‌عنوان peer) با ۹ نوع گوی نقطه‌ای متحرک برای حالت‌های «در حال فکر، جستجو، حل کردن، بافر» در رابط‌های چت و عامل. دو اندازه، تیره و روشن خودکار، Canvas دوبعدی بدون WebGL و فیلتر، ۶۰ فریم، توقف بیرون از صفحه و احترام به `prefers-reduced-motion`. مجوز MIT، حدود ۳٬۹۰۰ ستاره (۲۰۲۶-۱۰-۲۵).

## کی استفاده کنیم
🧭 جایی که محصول یک دستیار یا عامل هوش مصنوعی دارد و به‌جای اسپینر معمولی، وضعیت «فکر کردن» باید زنده و آرام دیده شود ([هوش مصنوعی در محصول](../domains/website/04-tech/ai-in-product.md)).
```bash
npm i thinking-orbs@0.3.2
```
نسخه‌های دیگر جامعه (همه MIT، کم‌ستاره‌تر؛ پیش از استفاده کد را بخوان): SwiftUI (`haplollc/ThinkingOrbs`)، React Native/Expo با Skia (`mahdidavoodi7/expo-thinking-orbs`)، Vue 3، و چند نسخه‌ی Flutter با صفر ستاره ❓.

## نکته‌ی امنیتی (زنجیره‌ی تأمین)
✅ نسخه‌ی 0.3.2 در npm (۲۰۲۶-۰۹-۲۲) تگی در مخزن اصلی ندارد؛ بررسی شد: از مخزن مادر همان سازنده `Jakubantalik/Libraries.dev` (پوشه‌ی `packages/thinking-orbs`، MIT) منتشر شده، اسکریپت نصب ندارد و کد مشکوکی در بسته پیدا نشد. همین الگو (نسخه‌ی npm بدون کد متناظر در مخزن) در حمله‌های واقعی هم دیده می‌شود؛ هر بار مثل همین‌جا منبع نسخه را پیدا کن ([حوزه‌ی امنیت](../domains/security/README.md)).
