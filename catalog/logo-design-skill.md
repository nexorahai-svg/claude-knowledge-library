---
name: Logo Design Skill (kaankiziltug)
slug: logo-design-skill
category: icons-logos
domains: [website, apps, social-media]
verdict: trial
status: researched
summary: skill طراحی لوگو برای Claude Code از بریف تا فایل نهایی SVG؛ سه کانسپت، آزمون ۱۶ پیکسل و تک‌رنگ، تخته‌ی ارائه، نسخه‌های favicon و آیکون اپ؛ کتابخانه‌ی مرجع ۱٬۴۳۲ لوگوی واقعی
use_when: "a client site or app has no proper logo ; we need three logo concepts with a 16 px and one-colour test before building ; we need favicon, app icon and webmanifest from an approved mark ; critiquing or redesigning an existing logo"
how: "Trial first on a small task: /plugin marketplace add kaankiziltug/logo-design-skill then /plugin install logo-design@logo-design-skill (project scope); stop at the concept checkpoint, outline Persian or Arabic text to paths with our own local font, never ship anything close to a library logo"
url: https://github.com/kaankiziltug/logo-design-skill
repo: "https://github.com/kaankiziltug/logo-design-skill"
license: "MIT (code and guidance; the 1,432 reference logos are third-party trademarks, not covered)"
pricing: free
risk: medium
sources: [S196]
found_in: [batch-23]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Logo Design Skill (kaankiziltug)

## چیست
✅ مخزن MIT، ساخت ۲۰۲۶-۰۹-۲۶، حدود ۴٬۹۰۰ ستاره، آخرین push ۲۰۲۶-۱۰-۲۰ (GitHub API، ۲۰۲۶-۱۰-۲۸). برای Claude، Gemini CLI و Codex.
✅ روند کامل: بریف (حداکثر پنج پرسش یا فرض صریح)، سه کانسپت، **توقف اجباری پس از کانسپت** برای انتخاب سفارش‌دهنده، بعد کیت کامل (رنگی، سیاه‌وسفید، با نام و بدون نام، favicon، آیکون اپ، webmanifest، راهنمای برند).
✅ آزمون‌ها: اندازه‌ی ۱۶ و ۳۲ پیکسل، تک‌رنگ، معکوس، تار، «آزمون قفسه» کنار رقیبان. تخته‌ی ارائه با ماکاپ مخصوص هر صنعت.
✅ کتابخانه‌ی مرجع: دقیقاً ۱٬۴۳۲ فایل SVG لوگوی واقعی با دسته‌بندی نوع، تکنیک، هندسه و صنعت (`search_library.py`).
✅ ۹ اسکریپت پایتون بی‌وابستگی؛ هیچ تماس شبکه ندارد. `render_png.py` فقط ابزار محلی (rsvg-convert، Inkscape، Chrome بی‌سر) را صدا می‌زند.

## سنجش ادعاهای ریلز (@aradazr.dev، ۲۰۲۶-۱۰-۲۵)
- «رایگان، MIT» ✅ (فقط کد؛ لوگوهای مرجع نه).
- «بیش از ۱۴۰۰ لوگوی واقعی» ✅ ۱٬۴۳۲.
- «۱۶ پیکسل هم خواناست، تک‌رنگ هم خوب است، شبیه رقیب نیست» ✅ این‌ها آزمون‌های skill است، نه تضمین نتیجه.
- «ایده می‌گیرد، کپی نمی‌کند» 🧭 فقط دستور SKILL.md است؛ شباهت را خودمان باید بسنجیم.
- «Claude را طراح لوگوی حرفه‌ای می‌کند» 🧭 اغراق؛ خروجی SVG هندسی است و کیفیتش آزموده نشده.

## کی استفاده کنیم
🧪 برای کانسپت اول لوگو در پروژه‌ی سایت یا اپ بدون لوگو، و برای ساختن خودکار favicon و آیکون‌ها از لوگوی تأییدشده. روش پیدا کردن سلیقه‌ی مشتری و درس «لوگوی تخت هندسی کودکانه دیده شد» در [سند لوگو](../domains/website/02-design/logo-and-brand.md) را کنارش نگه دار.

## حسن و عیب
- حسن: روند منظم با توقف برای تأیید، آزمون‌های اندازه‌ی کوچک، خروجی کامل وب، اسکریپت‌های قابل‌خواندن و بدون شبکه.
- عیب: خروجی SVG کدنویسی‌شده معمولاً تخت و هندسی است (برای لوگوی سه‌بعدی یا خوشنویسی کافی نیست). `svg_audit.py` متن زنده را خطا می‌گیرد، پس نوشته‌ی فارسی و عربی باید با فونت محلی خودمان به مسیر تبدیل شود. ۱٬۴۳۲ SVG حجم نصب را بالا می‌برد.

## قیمت و مجوز
✅ رایگان. MIT برای کد و راهنما. طبق `TRADEMARKS.md` خود مخزن، لوگوهای کتابخانه علامت تجاری صاحبانشان‌اند و هیچ حقی منتقل نمی‌شود؛ فقط برای مطالعه.

## ریسک و هشدار
⚠️ لوگوی تازه نباید شبیه هیچ لوگوی کتابخانه یا رقیب باشد؛ قانون «کپی نکن» کتابخانه این را سخت‌تر می‌خواهد. هیچ فایل از `assets/library/svg/` را در کار مشتری نگذار.
⚠️ skill اسکریپت محلی اجرا می‌کند؛ پیش از نصب در پروژه‌ی تازه، نسخه را بخوان یا پین کن.

## مرتبط
[S196](../sources/README.md#s196) · غربال ۲۳ · [لوگو و هویت برند](../domains/website/02-design/logo-and-brand.md) · [LogoToUse](logotouse.md)
