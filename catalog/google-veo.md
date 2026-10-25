---
name: Google Veo 3.1 و Gemini Omni Flash
slug: google-veo
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مدل‌های تولید ویدیو Google در Gemini API با صدای بومی (Veo)
url: https://ai.google.dev/gemini-api/docs/video
repo: ""
license: "شرایط Gemini API"
pricing: paid
risk: medium
sources: [S47, S86, S136, S151, S155]
found_in: []
last_checked: 2026-10-25
next_check: "2026-11-24"
---

# Google Veo 3.1 و Gemini Omni Flash

## چیست
✅ Omni Flash پیش‌فرض Google: ۳ تا ۱۰ ثانیه، تا 4K، حدود ۰.۱۰ دلار در ثانیه. Veo 3.1: Standard ۰.۴۰، Fast ۰.۱۰، Lite ۰.۰۵ دلار در ثانیه (۷۲۰p)، قیمت شامل صدا.

## کی استفاده کنیم
🧭 پیش‌نویس با Lite، نهایی با Standard. کلیپ بدون متن، متن با کد.

## قیمت و مجوز
✅ Google مالکیت ادعا نمی‌کند؛ فقط از منطقه‌ی پشتیبانی‌شده.

## ریسک و هشدار
❓ SynthID و قانون چهره برای ویدیو خوانده نشد.

## بازبینی ۲۰۲۶-۱۰-۱۸
✅ Veo 3.1 Lite (`veo-3.1-lite-generate-preview`): ۷۲۰p ۰.۰۵ و ۱۰۸۰p ۰.۰۸ دلار در ثانیه، صدا پیش‌فرض؛ ۹:۱۶؛ تکه‌ی ۴، ۶ یا ۸ ثانیه؛ SynthID روی همه؛ فقط پرامپت انگلیسی کامل پشتیبانی می‌شود. ✅ همین مدل در fal بی‌صدا ۰.۰۳ و در Replicate ۰.۰۵ دلار.

## به‌روزرسانی ۲۰۲۶-۱۰-۲۲ ⚠️
✅ پیش‌نمایش‌های Veo 3.1 (`veo-3.1-generate-preview`، `-fast-`، `-lite-`) روز ۲۰۲۶-۱۰-۲۲ خاموش شدند (مستندات و قیمت Gemini API). Google [Gemini Omni Flash](gemini-omni-flash.md) را پیشنهاد می‌کند، یا Veo نسخه‌ی GA روی پلتفرم سازمانی (Vertex). ❓ شناسه‌های GA (`veo-3.1-generate-001`) فقط از فهرست‌های شخص ثالث. ✅ Runway حالا Veo 3.1 Fast با صدا را ۰٫۱۵ دلار در ثانیه می‌دهد. روی پیش‌نمایش‌ها نساز. [S136](../sources/README.md#s136)

## هم‌خانواده در Flow 🔬
🔬 در Google Flow مدل‌های Veo 3.1 (Lite، Fast، Quality) و Omni 1.1 Flash قابل‌انتخاب‌اند؛ جزئیات و هزینه‌ی اعتبار در [کارت Google Flow](google-flow.md). [S151](../sources/README.md#s151) · دفتر پروژه‌ها (یک پروژه‌ی مشتری / Nexorah AI social، personal family videos)


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ پیش‌نمایش‌های Veo 3.1 در Gemini API در ۲۰۲۶-۱۰-۲۲ بسته شدند. قیمت Vertex با صدا (هر ثانیه): Quality ‏۰٫۴۰ (720p/1080p)، ۰٫۶۰ (4K)؛ Fast ‏۰٫۱۰/۰٫۱۲/۰٫۳۰؛ Lite ‏۰٫۰۵/۰٫۰۸. بی‌صدا: Quality ‏۰٫۲۰، Fast ‏۰٫۰۸، Lite ‏۰٫۰۳.

## مرتبط
[مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [S47](../sources/README.md#s47) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S86](../sources/README.md#s86)
