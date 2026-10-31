---
name: Prompt Master
slug: prompt-master
category: claude-code-tooling
domains: [social-media, claude-code]
verdict: trial
status: researched
summary: اسکیل متنی Claude که ایده‌ی خام را به پرامپت آماده برای یک ابزار مشخص (Midjourney، مدل ویدیو، Cursor و…) تبدیل می‌کند
use_when: "need a ready prompt for another AI tool such as an image or video model from a rough idea ; want a checklist of common prompt mistakes before sending a long prompt"
how: "Do not install without the user's yes; read-only text skill: git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master or upload the repo ZIP in claude.ai Customize > Skills; it fires only when you ask it to write or fix a prompt"
url: https://github.com/nidhinjs/prompt-master
repo: "https://github.com/nidhinjs/prompt-master"
license: "MIT"
pricing: free
risk: low
sources: [S200]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Prompt Master

## چیست
- ✅ یک اسکیل Claude فقط متنی است: `SKILL.md` (نسخه‌ی 1.8.2، حدود ۵ هزار کلمه) و دو فایل مرجع (`references/patterns.md` و `templates.md`). هیچ اسکریپت، فرمان یا ارتباط شبکه‌ای ندارد. https://github.com/nidhinjs/prompt-master
- ✅ مجوز MIT؛ حدود ۱۵ هزار ستاره؛ ساخته‌شده ۲۰۲۶-۰۳-۱۱؛ آخرین تغییر ۲۰۲۶-۱۰-۲۲.
- ✅ کارش: ابزار مقصد را می‌شناسد (مدل زبانی، Cursor، Claude Code، Midjourney، مدل‌های ویدیو و…)، قصد کاربر را در ۹ بُعد بیرون می‌کشد و یک پرامپت آماده می‌دهد. فهرست ۳۷ الگوی اشتباه رایج پرامپت را دارد (در README و patterns.md).
- ✅ در توضیح خودش نوشته فقط وقتی فعال می‌شود که صریحاً نوشتن یا اصلاح پرامپت برای یک ابزار خواسته شود؛ برای کدنویسی، گفتگوی عادی یا نوشتن سند فعال نمی‌شود.

## ادعای ریل در مقابل واقعیت
- ⚠️ «بعضی‌ها هیچ‌وقت به سقف مصرف Claude نمی‌خورند» ادعای بازاریابی است. اسکیل فقط وقتی پرامپت برای ابزار دیگری می‌خواهید کار می‌کند؛ در کار روزمره‌ی Claude Code فعال نمی‌شود، و خود اسکیل هنگام فعال شدن چند هزار توکن به متن اضافه می‌کند. 🧭 صرفه‌جویی واقعی‌اش کمتر شدن رفت‌وبرگشت برای پرامپت تصویر و ویدیو است.
- ⚠️ «لینک را دایرکت می‌کنم» قلاب گرفتن کامنت است؛ مخزن عمومی است و لینک بالا کافی است.
- ✅ روش نصب ریل (ZIP در claude.ai → Customize → Skills) با README یکی است.

## کی استفاده کنیم
- 🧭 برای نوشتن پرامپت مدل‌های تصویر و ویدیو در کار محتوای سوشال، کنار [prompts-chat](prompts-chat.md) (فقط الهام). پرامپت نهایی را به زبان خودمان نگه داریم (قانون «کپی نکن»).
- 🧭 برای پروژه‌های کد لازم نیست؛ قانون‌های کتابخانه و STATE.md همین کار را می‌کنند.

## قیمت و مجوز
- ✅ رایگان، MIT؛ استفاده‌ی تجاری آزاد.

## ریسک و هشدار
- ✅ کم: متن خالص، بی اسکریپت و بی شبکه. 🧭 فقط از مخزن اصلی `nidhinjs/prompt-master` بگیرید، نه از ZIP دایرکت‌شده.

## مرتبط
- منبع: [S200](../sources/S200.md)

## آزمون دست‌اول (۲۰۲۶-۱۰-۲۸) 🔬
- ردیف پروژه: projects/README.md
- v1.8.2 (commit `49b3a72`) از مخزن رسمی در `~/.claude/skills/` نصب شد؛ سه فایل متنی، بدون اسکریپت.
- کاربر ۲۰۲۶-۱۰-۲۹ نصب را تأیید کرد و خواست بماند (اسکیل برایش مهم است). نصب ماند؛ حکم assess تا آزمون‌های بیشتر.
- برای Kling 3.0 و Nano Banana Pro از پرامپتی که از راهنمای رسمی خود این مدل‌ها نوشته شده بهتر نیست: راهنمای Kling آن دو خط است، `elements` و دیالوگ Kling 3.0 را نمی‌شناسد، و Nano Banana را فهرست نکرده است.
- ایده‌های مفید: قفل‌های مهم در ۳۰٪ اول پرامپت؛ یک معیار قبول صریح برای هر پرامپت.
- حکم: assess می‌ماند؛ برای پرامپت تصویر و ویدیو، راهنمای رسمی هر مدل اولویت دارد.

🧭 (مرور ارتقا ۲۰۲۶-۱۰-۳۰) assess می‌ماند: در تنها آزمون واقعی از پرامپتی که با راهنمای رسمی خود مدل نوشته شود بهتر نبود.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
