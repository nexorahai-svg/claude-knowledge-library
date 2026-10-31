---
name: Remotion Skills (رسمی)
slug: remotion-skills
category: video
domains: [social-media, claude-code]
verdict: assess
status: researched
summary: مهارت‌های رسمی Remotion برای ساخت ویدیو با کد؛ دستور شل و نصب بسته اجرا می‌کند
url: https://github.com/remotion-dev/skills
repo: "https://github.com/remotion-dev/skills"
license: "بدون فایل مجوز در مخزن"
pricing: free
risk: medium
sources: [S28, S85]
found_in: [batch-01/P08, batch-01/P24]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Remotion Skills (رسمی)

## چیست
✅ همگام‌شده از مخزن اصلی Remotion (رسمی). ۱۱ مهارت: ساخت پروژه، استودیو، رندر، زیرنویس، نقشه، تعامل، مستندات، ارتقا و غیره.

## کی استفاده کنیم
🧭 فقط وقتی واقعاً ویدیوی Remotion می‌سازی ([حوزه‌ی ویدیو](../domains/social-media/README.md)).

## قیمت و مجوز
✅ مخزن https://github.com/remotion-dev/skills در ریشه فایل مجوز ندارد (GitHub API: فهرست ریشه فقط README.md، package.json، scripts، skills، tsconfig.json؛ فیلد license خالی). مجوز خود Remotion: [کارت Remotion](remotion.md) (رایگان برای فرد و شرکت تا ۳ نفر).

## ریسک و هشدار
⚠️ مهارت‌ها دستور شل دارند (`npx remotion render`، `npx create-video@latest`، `npm i`)، مهارت مستندات به سرویس جستجوی Algolia درخواست می‌فرستد، و مهارت ارتقا بسته‌ها را به‌روز می‌کند.

## بازبینی ۲۰۲۶-۱۰-۱۸
✅ ۱۲ مهارت (best-practices، create، captions، render، …)؛ نصب: `npx skills add remotion-dev/skills`؛ به‌روز ۲۰۲۶-۱۰-۱۶. حالا افزونه‌ی رسمی Claude Code هم هست (کارت [Remotion](remotion.md)). هنوز فایل مجوز جدا ندارد.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S85](../sources/README.md#s85)
