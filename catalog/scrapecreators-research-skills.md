---
name: ScrapeCreators research skills
slug: scrapecreators-research-skills
category: research-tools
domains: [social-media, claude-code]
verdict: assess
status: researched
summary: مهارت‌های پژوهش شبکه‌های اجتماعی (پست پربازدید، کامنت، رقبا، تبلیغات) روی API پولی ScrapeCreators؛ کد MIT و فقط داده‌ی عمومی
use_when: "need competitor teardown, outlier post finding, comment mining or ad-library analysis across Instagram, TikTok, YouTube ; small paid research budget available"
how: "Do not install without the user's yes; npx skills add ScrapeCreators/social-media-research-skills with SCRAPECREATORS_API_KEY from a separate low-credit key; public data only, never give it a logged-in account"
url: https://github.com/ScrapeCreators/social-media-research-skills
repo: "https://github.com/ScrapeCreators/social-media-research-skills"
license: "MIT"
pricing: freemium
risk: medium
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2026-11-28"
---

# ScrapeCreators research skills

## چیست
- ✅ مخزن رسمی https://github.com/ScrapeCreators/social-media-research-skills (سازنده‌ی خود API)؛ MIT؛ حدود ۴٬۹۹۰ ستاره؛ ساخته ۲۰۲۶-۰۶-۰۶؛ آخرین push ۲۰۲۶-۰۸-۲۶ (دو ماه بی‌تغییر)؛ نسخه‌ی رسمی (release) ندارد.
- ✅ README: ۱۳ مهارت (پیدا کردن پست پربازدید، تحلیل transcript، کامنت‌کاوی، رقبا، کتابخانه‌ی تبلیغ، ترند، influencer، تحلیل مخاطب، گوش‌دادن اجتماعی...) روی TikTok، Instagram، YouTube، Reddit، X، LinkedIn و غیره.
- ✅ همه به کلید `SCRAPECREATORS_API_KEY` نیاز دارند. README می‌گوید فقط داده‌ی عمومی می‌گیرد و داده‌ی خصوصی یا واردشده را وعده نمی‌دهد.
- ✅ ستاره‌ها بیشتر از نگهداری است: هفت commit در گزارش قبلی؛ مخزن اصلی هم تبلیغ سرویس پولی است.

## قیمت و مجوز
✅ (https://scrapecreators.com، ۲۰۲۶-۱۰-۲۸) رایگان با ۱۰۰ اعتبار بدون کارت؛ پرداخت به‌ازای مصرف: ۴۷ دلار برای ۲۵٬۰۰۰ اعتبار، ۴۹۷ دلار برای ۵۰۰٬۰۰۰؛ اعتبار منقضی نمی‌شود، اشتراک ندارد. کد مهارت‌ها MIT.

## ریسک و هشدار
- 🧭 جمع‌آوری داده‌ی عمومی با خزنده‌ی شخص ثالث حوزه‌ی خاکستری شرایط اینستاگرام است؛ خطر حساب ما کم است چون با حساب ما وارد نمی‌شود، ولی خطر حقوقی/اخلاقی دارد.
- ✅ کلید API و پرس‌وجوها به سرور شخص ثالث می‌رود.

## کی استفاده کنیم
🧭 فقط اگر تحلیل رقبا یا کامنت با بودجه‌ی کوچک لازم شد. ابتدا با ۱۰۰ اعتبار رایگان آزمایش و در پروژه‌ی واقعی ثبت شود؛ بدون اجازه‌ی کاربر نصب نشود.

## مرتبط
غربال · [S165](../sources/README.md#s165) · https://scrapecreators.com

## بررسی دوباره‌ی موردهای ❓ (۲۰۲۶-۱۰-۲۹)
- ✅ شرایط ScrapeCreators (https://scrapecreators.com/terms): داده‌ی عمومی را می‌آورد. مسئولیت پیروی از شرایط Instagram و TikTok با خود توست. حساب را هر زمان و بی‌اطلاع می‌بندد و اعتبار مصرف‌نشده ممکن است از بین برود. بازپرداخت به صلاح خودشان است. لاگ درخواست‌ها و پاسخ‌ها نگه داشته می‌شود.

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کل مخزن (۲۰ فایل) دیده شد (SHA `64ba7b4`). تنها اسکریپت (`validate-skills.py`) محلی است و شبکه ندارد. بقیه‌ی مهارت‌ها فقط Markdown‌اند و با کلید خود کاربر به `api.scrapecreators.com` وصل می‌شوند. 🧭 خروجی اسکرپ‌شده داده‌ی ناامن است (خطر تزریق prompt).
