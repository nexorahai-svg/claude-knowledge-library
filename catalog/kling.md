---
name: Kling (Kuaishou)
slug: kling
category: video
domains: [social-media]
verdict: adopt
status: researched
use_when: "short AI video clip of a person or product from an image ; walking or motion shot paired with a lip-sync model"
how: "Kling 3.0 Pro through fal.ai with the team key, upload files instead of data URIs, then lipsync-2-pro; Kling Avatar fails on close-ups; check every request and its cost before sending"
summary: مدل ویدیو Kling 3.0 با صدای بومی
url: https://kling.ai
repo: ""
license: "شرایط Kling"
pricing: paid
risk: medium
sources: [S47, S151, S155]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-24"
---

# Kling (Kuaishou)

## چیست
✅ Runway مدل‌های kling3.0 و klingO3 را با گزینه‌ی صدا می‌فروشد. ✅ قیمت و 4K از صفحه‌ی API رسمی (kling.ai/dev/pricing) تأیید شد؛ صفحه از Kling 4.0 هم نام می‌برد (طرح‌های فعلی آن را پوشش نمی‌دهند). ✅ ۳ تا ۱۵ ثانیه برای Kling 3.0 Turbo، 3.0 و 3.0 Omni؛ ۳ تا ۱۰ برای O1 و 2.6/2.5 Turbo (نقشه‌ی قابلیت رسمی). Kling 4.0 در آن نقشه نیست؛ فقط در یادداشت صفحه‌ی قیمت آمده ❓.

## دستور سریع

**نصب** (✅ [صفحه‌ی مدل در fal](https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video/api)؛ ما Kling را از راه fal می‌خریم، کلید و جزئیات کلاینت در [fal.ai](fal-ai.md)):
```bash
pip install fal-client==1.0.3 && export FAL_KEY="..."      # کلید همان تیمِ شارژشده
```
**حداقل اجرا** (✅ مستند fal؛ `start_image_url` تنها ورودی اجباری است):
```python
import fal_client
r = fal_client.run("fal-ai/kling-video/v3/pro/image-to-video", arguments={
    "start_image_url": fal_client.upload_file("start.png"),
    "prompt": "subject, action, scene, camera, light, mood",   # الگوی رسمی (کارت)
    "duration": "5", "generate_audio": False})
```
**تنظیم‌های مهم**
- ✅ `duration` از `"3"` تا `"15"`؛ `generate_audio: true` هزینه را از `$0.112` به `$0.168` بر ثانیه می‌برد.
- ✅ نسخه‌ی ارزان `…/v3/standard/image-to-video` و خروجی 4K با `…/v3/pro/image-to-video/4k`.
- 🔬 خروجی 24 فریم در ثانیه؛ لب‌خوان خود Kling فقط ۲ تا ۱۰ ثانیه می‌گیرد؛ با lipsync بیرونی صدا ۱۰۰ تا ۱۸۰ میلی‌ثانیه تأخیر خواست.

**خطاهای رایج**
- 🔬 Kling Avatar در نمای نزدیک شکست خورد؛ برای کاراکتر انیمیشنی اول ۲ ثانیه تست کن و حرکت دهان را بسنج ([fal.ai](fal-ai.md)).
- 🔬 نسخه‌ی رایگان وب در ساعت شلوغ بسته است («cannot submit new tasks») و روی آن حساب نکن.
- ⚠️ شرایط API: ریسک نقض حقوق ورودی با توست و مانده‌ی حساب بازپرداخت نمی‌شود؛ بسته‌ی پیش‌پرداخت منقضی می‌شود (بخش «قیمت و مجوز» کارت).

**هزینه** (✅ fal، ۲۰۲۶-۱۰-۳۱): Kling 3.0 Pro `$0.112/s` بی‌صدا و `$0.168/s` با صدا؛ جدول رسمی Kling (در کارت، ۲۰۲۶-۱۰-۱۷) 1080p بی‌صدا هم `0.112` است. ❓ صفحه‌ی kling.ai/dev/pricing با curl خالی می‌آید (جاوااسکریپتی)، پس دوباره خوانده نشد. محافظ: هر درخواست و هزینه‌اش را پیش از ارسال بنویس؛ ۱۲ ثانیه با lipsync ≈ `$2.3` (🔬).

## کی استفاده کنیم
🔬 کلیپ کوتاه آدم یا محصول از عکس: Kling 3.0 Pro از راه fal.ai و بعد lipsync-2-pro برای لب، حدود ۲٫۳ دلار برای ۱۲ ثانیه (دفتر پروژه‌ها، ۲۰۲۶-۱۰-۲۸). Kling Avatar در نمای نزدیک رد شد. نسخه‌ی رایگان وب در ساعت شلوغ بسته بود. پیش از کار تجاری شرایط Kling با مرورگر خوانده شود.

## قیمت و مجوز
✅ (kling.ai/dev/pricing، ۲۰۲۶-۱۰-۱۷؛ ۱ واحد = ۰.۱۴ دلار لیست) هر ثانیه:

| مدل | ۷۲۰p | ۱۰۸۰p | 4K |
|---|---|---|---|
| Kling 3.0 Turbo (با صدای بومی) | ۰.۱۱۲ | ۰.۱۴ | — |
| Kling 3.0 بدون صدا | ۰.۰۸۴ | ۰.۱۱۲ | ۰.۴۲ |
| Kling 3.0 با صدای بومی (بدون کنترل صدا) | ۰.۱۲۶ | ۰.۱۶۸ | ۰.۴۲ |
| Kling 3.0 Omni بدون ویدیوی ورودی و بدون صدا | ۰.۰۸۴ | ۰.۱۱۲ | ۰.۴۲ |

بسته‌های پیش‌پرداخت ۱۸۰ روزه از ۷۰۰ دلار (۵٬۰۰۰ واحد)، بدون انتقال یا تمدید، ۲۰ درخواست هم‌زمان؛ تخفیف ۱۰٪ از ۳۰٬۰۰۰ واحد. 🧭 پس کلیپ ۵ ثانیه‌ی 1080p بدون صدا حدود ۰.۵۶ دلار.

✅ شرایط خدمت پولی API (بند ۶): اگر روی ورودی حق قانونی داری، IP خروجی با توست (۶.۳)؛ استفاده‌ی تجاری محدود نشده، ولی خطر نقض حقوق دیگران با توست (۶.۴)؛ مانده‌ی حساب بازپرداخت نمی‌شود (۲.۵). تاریخ اجرای شرایط خوانده نشد ❓.

## ریسک و هشدار
⚠️ جبران خسارت به Kling و وابسته‌هایش اگر خروجی یا ورودی تو باعث ضرر شود (۶.۳ و ۶.۴). بسته‌ی پیش‌پرداخت منقضی می‌شود. قیمت تغییر می‌کند؛ پیش از خرید دوباره بخوان.

## آزمون طرح رایگان وب ۲۰۲۶-۱۰-۲۴ 🔬
🔬 ۶۶ اعتبار در روز؛ چهار تصویر ۴ اعتبار. در ساعت شلوغ کاربر رایگان پیام «Free track… non-member users cannot submit new tasks temporarily» گرفت و آن شب قابل‌استفاده نبود. پلن Standard پولی حدود ۶٫۹۹ دلار برای ماه اول با ۶۶۰ اعتبار دیده شد (🧭 قیمت گذرا). به‌جایش می‌شود [Google Flow](google-flow.md) را به کار برد. حکم assess می‌ماند. [S151](../sources/README.md#s151)


## آزمون ۱۲ ثانیه‌ای راه رفتن ۲۰۲۶-۱۰-۳۰ 🔬
🔬 Kling 3.0 Pro روی fal، تصویر به ویدیو: خروجی 24 fps، چهره و لباس از عکس شروع در ۱۲ ثانیه حفظ شد؛ لب‌خوان خود Kling فقط ۲ تا ۱۰ ثانیه می‌گیرد؛ با sync.so لب فقط تقریباً هماهنگ بود و صدا ۱۰۰ تا ۱۸۰ میلی‌ثانیه تأخیر خواست. اعداد و هزینه: [مدل‌های ویدیو](../domains/social-media/ai-video-models.md).

## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ **Kling 4.0 در ۲۰۲۶-۱۰-۱۵ منتشر شد**: تا ۳۰ ثانیه یک‌جا، Omni Reference تا ۱۵ مرجع و ۱۰ فریم کلیدی. fal: ‏۰٫۱۵۷ (720p) و ۰٫۲۳۵ (1080p) دلار در ثانیه. Kling 3.0 Pro در fal ‏۰٫۱۱۲ بی‌صدا، ۰٫۱۶۸ با صدا؛ در Replicate دو برابر. سیاست اعتبار: یک دلار ۶۶ اعتبار؛ اعتبار اشتراک یک ماه، اعتبار خریدنی دو سال. پرامپت رسمی: سوژه، کار، صحنه، دوربین، نور، حس.

## مرتبط
[مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [S47](../sources/README.md#s47)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
