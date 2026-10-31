---
name: fx0 (Vercel Labs)
slug: fx0
category: design-inspiration
domains: [website]
verdict: assess
status: researched
summary: نمونه‌ی متن‌باز عامل طراحی Vercel Labs که از یک توضیح، صفحه را در یک فایل HTML می‌نویسد؛ اجرای خودمیزبان به Vercel، Neon، Upstash و AI Gateway وابسته است
use_when: "studying how a prompt-to-single-HTML design agent is built on libfx ; trying the hosted fx0.vercel.dev demo for a quick page idea"
how: "Reference only, do not install without the user's yes; self-hosting needs a Vercel sign-in plus Neon, Upstash and AI Gateway billed to your Vercel team, and we already have frontend-design, designmd and google-stitch for the same job"
url: https://github.com/vercel-labs/fx0
repo: "https://github.com/vercel-labs/fx0"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S198]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-28
next_check: "2026-11-27"
---

# fx0 (Vercel Labs)

## چیست
- ✅ مخزن Apache-2.0، حدود ۴۱۶ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۷؛ release ندارد (GitHub API، ۲۰۲۶-۱۰-۲۸): https://github.com/vercel-labs/fx0
- ✅ README: «عامل طراحی سبک ساخته‌شده با libfx؛ صفحه را توصیف می‌کنی و عامل آن را در یک فایل HTML می‌نویسد.» همچنین نمونه‌ای از اپ ساخته‌شده روی libfx است (جلسه‌های پایدار، تلاش مجدد، استریم).
- ✅ هر نوبت نسخه‌ی طرح را نگه می‌دارد؛ HTML را می‌شود کپی یا دانلود کرد. عامل می‌تواند وب را جست‌وجو کند و از پیش‌نمایش عکس بگیرد. با ۱۰ سبک `design.md` از awesome-design-md شروع می‌شود.
- ✅ دمو: https://fx0.vercel.dev . پنج درخواست رایگان به‌ازای هر IP (مدل Opus 5.5 Fast)، بعد باید با Vercel وارد شوی و هزینه‌ی مدل از طریق AI Gateway روی تیم خودت می‌رود.
- ✅ معماری: Redis و Neon برای تاریخچه، Vercel Queues و Workflow برای پایداری، AI Gateway برای مدل؛ هر نوبت حداکثر ۶۴ گام مدل.
- 🧭 این یک ابزار آماده برای ما نیست بلکه مرجع معماری است؛ خروجی فقط یک فایل HTML است.

## کی استفاده کنیم
- 🧭 فقط مرجع ساختار عامل طراحی. همین کار را [frontend-design](frontend-design.md)، [designmd](designmd.md) و [Google Stitch](google-stitch.md) انجام می‌دهند. به درد اپ موبایل یا محتوای شبکه‌ی اجتماعی نمی‌خورد.

## قیمت و مجوز
- ✅ کد Apache-2.0 (استفاده‌ی تجاری آزاد با حفظ مجوز و NOTICE): https://github.com/vercel-labs/fx0/blob/main/LICENSE
- ✅ اجرای خودمیزبان هزینه‌ی Vercel، Neon، Upstash و AI Gateway دارد؛ مدل به حساب تیم Vercel شما صورت‌حساب می‌شود (README).

## ریسک و هشدار
- ✅ ورود با OAuth ویرکل و ذخیره‌ی توکن در Redis (README)؛ هزینه روی حساب Vercel جمع می‌شود. سقف خرج جدا تنظیم شود.
- 🧭 وابستگی کامل به یک فروشنده؛ از ایران دسترسی به دمو و سرویس‌ها جداگانه سنجیده شود.

## مرتبط
[S198](../sources/README.md#s198) · [سبک‌های طراحی](../domains/website/02-design/design-styles.md)
