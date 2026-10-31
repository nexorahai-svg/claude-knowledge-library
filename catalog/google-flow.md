---
name: Google Flow
slug: google-flow
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: استودیوی ویدیوی Google با شخصیت ثابت؛ Omni 1.1 Flash و Veo 3.1
use_when: "making emotional animation with a consistent character ; AI video when code animation looks weak"
how: "flow.google.com, create a Character with a portrait (Nano Banana 2.1, free), then generate clips with Omni 1.1 Flash; free 50 credits per day, 720p 6 s costs 10 credits; commercial licence of output unread"
url: https://flow.google.com
repo: ""
license: "شرایط Google"
pricing: freemium
risk: medium
sources: [S151, S155]
found_in: []
last_checked: 2026-11-01
next_check: "2026-12-01"
---

# Google Flow

## چیست
🔬 برنامه‌ی وب تولید ویدیو با هوش مصنوعی (flow.google.com). بخش «Characters»: شرح بنویس ← پرتره با Nano Banana 2.1 (رایگان، بدون اعتبار) ← با «What do you want to change?» اصلاح کن (مثلاً شیک‌تر، خانه‌ی مدرن) ← نسخه‌ی دلخواه را از تاریخچه به‌عنوان پرتره انتخاب، نام‌گذاری، توضیح شخصیت و Done. چهره و مو در ۱۲ صحنه ثابت ماند؛ لباس وقتی در پرامپت هر صحنه نوشته شد عوض شد. کیفیت 3D سبک پیکسار عالی بود. در پرامپت متن ننویس؛ زیرنویس را با کد بگذار.

## کی استفاده کنیم
🔬 انیمیشن احساسی با شخصیت ثابت (جایگزین انیمیشن SVG ضعیف با کد، که کیفیتش ضعیف بود). کد فقط برای زیرنویس و روکش.

## قیمت و مجوز
- ✅ رایگان: ۵۰ اعتبار در روز؛ امارات پشتیبانی می‌شود (https://support.google.com/flow/answer/16526234).
- ✅ منطقه (https://support.google.com/flow/answer/16353544، ۲۰۲۶-۱۱-۰۱): امارات در فهرست است، ایران نیست. ⛔ ترفندهای «نجات حساب» با عوض کردن ریجن (ریل‌های [S224](../sources/README.md#s224)) را اجرا نکن؛ راهنمای رسمی می‌گوید VPN دسترسی نمی‌دهد. اگر در منطقه‌ی مجاز خطا داری، از پشتیبانی Google One بپرس.
- ✅ Google AI Plus در امارات: قیمت فهرست ۱۸٫۹۹ درهم در ماه (ماه اول هنگام پرداخت ۴٫۹۵ درهم با تخفیف خودکار)، ۲۰۰ اعتبار Flow در ماه، Omni Flash؛ Pro ۷۶٫۹۹ درهم با ۱۰۰۰ اعتبار (دیده‌شده ۲۰۲۶-۱۰-۲۴؛ https://one.google.com/about/google-ai-plans).
- 🔬 هزینه‌ی Omni 1.1 Flash 720p: ۶ ثانیه ۱۰، ۸ ثانیه ۱۲، ۱۰ ثانیه ۱۵ اعتبار. ویدیوی ۹۰ ثانیه‌ای با ۱۲ صحنه حدود ۱۰۰ اعتبار.
- مجوز تجاری خروجی: ❓ خوانده نشد.

## ریسک و هشدار
- 🔬 جلسه‌ی agent: تنظیمات ← «Confirm before generating: Always» (هزینه را نشان می‌دهد، Approve)؛ مدل پیش‌فرض قابل‌انتخاب است. یک پیام می‌تواند چند ویدیو بخواهد و یک‌جا هزینه می‌پرسد.
- 🔬 منوی دانلود: GIF 270p، اصل 720p، «Upscaled» 1080p (در Plus؛ حدود یک دقیقه برای هر کدام و هشدار که چند تا هم‌زمان شروع نشود)، 4K نیاز به طرح بالاتر. Chrome سه دانلود موازی آخر را بی‌صدا انداخت ← جایگزین: 720p و بالاکشی ffmpeg (بنگر [FFmpeg](ffmpeg.md)).
- 🔬 کلیپ‌ها صدای محیط دارند ← `-an`.


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ طرح‌های امارات: Plus ‏۱۸٫۹۹ درهم (۲۰۰ اعتبار)، Pro ‏۷۶٫۹۹ (۱٬۰۰۰)، **Ultra 5x از ۳۶۹٫۹۹ (۱۰٬۰۰۰)**، Ultra 20x ‏۷۶۹٫۹۹ (۲۵٬۰۰۰)؛ ۵۰ اعتبار روزانه برای همه؛ انتقال به ماه بعد ندارد. هزینه‌ی هر کلیپ (غیر Ultra/Ultra): Veo 3.1 Lite ‏۱۰/۵، Fast ‏۲۰/۱۰، Quality ‏۱۰۰، Omni 720p ‏۷ تا ۱۵، ویرایش Omni ‏۴۰. Omni Flash 1.1 تنها مدل با Ingredients و طول ۱۰ ثانیه است؛ Quality مرجع ندارد. SynthID روی همه؛ واترمارک دیدنی اختیاری. 🧭 برای ۳۰ ریلز: Ultra 5x (Pro برای این حجم کافی نیست و اعتبار زود تمام می‌شود). شرایط مصرفی برای تبلیغ پولی خوانده نشد ❓. پرامپت آماده‌ی شخصیت ثابت: [ابزارهای پولی](../domains/social-media/paid-ai-tools.md).

## مرتبط
[مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [Gemini Omni Flash](gemini-omni-flash.md) · [Google Veo](google-veo.md) · [Nano Banana](nano-banana.md) · [Kling](kling.md) · [S151](../sources/README.md#s151)
