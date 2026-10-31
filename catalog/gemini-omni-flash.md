---
name: Gemini Omni Flash (Google)
slug: gemini-omni-flash
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: مدل ویدیوی پیشنهادی Google به‌جای پیش‌نمایش‌های Veo 3.1؛ ۹:۱۶، صدای ساخته‌شده، حدود ۰٫۱۰ دلار در ثانیه
use_when: "generating realistic video clips for scenes that code cannot make ; 9:16 or 16:9 AI video through the Gemini API"
how: "call Gemini API Interactions endpoint POST /v1beta/interactions with the Omni Flash model (about $0.10 per second at 720p); old Veo 3.1 previews and gemini-omni-flash-preview were shut down 2026-10-22; keep clips no longer than the voice and put text in with code"
url: https://ai.google.dev/gemini-api/docs/omni
repo: ""
license: "شرایط Gemini API"
pricing: paid
risk: medium
sources: [S136, S151, S155]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-24"
---

# Gemini Omni Flash (`gemini-omni-1.1-flash`)

## چیست
✅ (مستندات Gemini API، ۲۰۲۶-۱۰-۲۲) مدل ویدیوی کنونی Google در Gemini API از راه Interactions API (`POST /v1beta/interactions`)؛ نسبت ۹:۱۶ یا ۱۶:۹؛ ۳۶۰p، ۷۲۰p (پیش‌فرض)، ۱۰۸۰p و 4K (دو تای آخر بزرگ‌نمایی‌شده)؛ **صدای ساخته‌شده در خروجی**؛ کلیپ ۳ تا ۱۰ ثانیه، قابل گسترش در گام‌های ۱۰ ثانیه‌ای تا ۴۰؛ تصویر به ویدیو، فریم اول و آخر، تصویر مرجع، ویرایش چندمرحله‌ای (`previous_interaction_id`)؛ SynthID روی همه‌ی خروجی‌ها. ✅ امارات در فهرست مناطق Gemini API است.
✅ پیش‌نمایش‌های Veo 3.1 (`veo-3.1-*-preview`) و نام قدیمی `gemini-omni-flash-preview` روز ۲۰۲۶-۱۰-۲۲ خاموش شدند؛ Google به همین مدل اشاره می‌کند.

## قیمت و مجوز
✅ حدود ۰٫۱۰ دلار در ثانیه در ۷۲۰p (برآورد از قیمت توکن، صفحه‌ی قیمت). شرایط Gemini API.

## کی استفاده کنیم
🧪 تصویر واقعی‌نما برای صحنه‌هایی که با کد ساخته نمی‌شوند؛ در یک خط تولید هر کلیپ تا طول صدای صحنه بریده یا نگه داشته می‌شود.

## ریسک و هشدار
❓ اجرای واقعی با کلید در یک خط تولید هنوز آزموده نشده. ⚠️ متن روی تصویر از مدل نخواه؛ با کد بنویس. ⚠️ بخش «دوربین و پیوستگی شخصیت» صفحه‌ی مستندات خوانده نشد.

## اجرای واقعی در Google Flow 🔬
🔬 Omni 1.1 Flash در Flow با کیفیت 720p: ۶ ثانیه = ۱۰ اعتبار، ۸ ثانیه = ۱۲، ۱۰ ثانیه = ۱۵ (۴ ثانیه = ۷ طبق صفحه‌ی پشتیبانی). هر کلیپ حدود ۳۰ تا ۹۰ ثانیه؛ پیام «high demand» شب هم در نهایت تمام شد. جزئیات: [Google Flow](google-flow.md). [S151](../sources/README.md#s151)


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ هزینه در Flow: ‏۷ تا ۱۵ اعتبار در 720p (۴ تا ۷ در 360p)، ویرایش ۴۰. تنها مدل Flow با Ingredients و ۱۰ ثانیه و ویرایش ویدیو. 🧭 Artificial Analysis: تصویر به ویدیو ۱۱۳۲. پرامپت: «one continuous unbroken shot, no cuts»؛ فیلد منفی ندارد؛ هر بار یک تغییر.

## مرتبط
[ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [مدل‌های تولید ویدیو](../domains/social-media/ai-video-models.md) · [Google Veo](google-veo.md) · [S136](../sources/README.md#s136)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
