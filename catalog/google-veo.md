---
name: Google Veo 3.1 و Gemini Omni Flash
slug: google-veo
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مدل‌های تولید ویدیو Google در Gemini API با صدای بومی (Veo)
use_when: "generating AI video with native audio via the Gemini API ; drafting clips cheaply"
how: "Trial first on a small task: use Gemini Omni Flash (default, about $0.10 per second) or Veo 3.1 Lite ($0.05 per second at 720p) for drafts; the Veo 3.1 preview model IDs were shut down 2026-10-22; all output has SynthID; generate clips without text and add text with code"
url: https://ai.google.dev/gemini-api/docs/video
repo: ""
license: "شرایط Gemini API"
pricing: paid
risk: medium
sources: [S47, S86, S136, S151, S155]
found_in: []
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Google Veo 3.1 و Gemini Omni Flash

## چیست
✅ Omni Flash پیش‌فرض Google: ۳ تا ۱۰ ثانیه، تا 4K، حدود ۰.۱۰ دلار در ثانیه. Veo 3.1: Standard ۰.۴۰، Fast ۰.۱۰، Lite ۰.۰۵ دلار در ثانیه (۷۲۰p)، قیمت شامل صدا.

## کی استفاده کنیم
🧭 پیش‌نویس با Lite، نهایی با Standard. کلیپ بدون متن، متن با کد.

## قیمت و مجوز
✅ Google مالکیت ادعا نمی‌کند؛ فقط از منطقه‌ی پشتیبانی‌شده.

## ریسک و هشدار
✅ DeepMind: ویدیوهای Veo با SynthID نشانه‌گذاری می‌شوند (https://deepmind.google/models/veo/). ✅ Vertex: پارامتر personGeneration مقدار پیش‌فرض allow_adult دارد (فقط بزرگسال و چهره) و با disallow هیچ آدم و چهره‌ای ساخته نمی‌شود (https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-text).

## بازبینی ۲۰۲۶-۱۰-۱۸
✅ Veo 3.1 Lite (`veo-3.1-lite-generate-preview`): ۷۲۰p ۰.۰۵ و ۱۰۸۰p ۰.۰۸ دلار در ثانیه، صدا پیش‌فرض؛ ۹:۱۶؛ تکه‌ی ۴، ۶ یا ۸ ثانیه؛ SynthID روی همه؛ فقط پرامپت انگلیسی کامل پشتیبانی می‌شود. ✅ همین مدل در fal بی‌صدا ۰.۰۳ و در Replicate ۰.۰۵ دلار.

## به‌روزرسانی ۲۰۲۶-۱۰-۲۲ ⚠️
✅ پیش‌نمایش‌های Veo 3.1 (`veo-3.1-generate-preview`، `-fast-`، `-lite-`) روز ۲۰۲۶-۱۰-۲۲ خاموش شدند (مستندات و قیمت Gemini API). Google [Gemini Omni Flash](gemini-omni-flash.md) را پیشنهاد می‌کند، یا Veo نسخه‌ی GA روی پلتفرم سازمانی (Vertex). ✅ شناسه‌های GA در مستندات رسمی Vertex آمده‌اند: `veo-3.1-generate-001` و `veo-3.1-fast-generate-001` (GA، انتشار ۲۰۲۵-۱۱-۱۷؛ بازنشستگی «۲۰۲۶-۱۱-۱۷ یا بعد»)، و `veo-3.1-lite-generate-001` هنوز Preview است (https://cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate). ✅ Runway حالا Veo 3.1 Fast با صدا را ۰٫۱۵ دلار در ثانیه می‌دهد. روی پیش‌نمایش‌ها نساز. [S136](../sources/README.md#s136)

## هم‌خانواده در Flow 🔬
🔬 در Google Flow مدل‌های Veo 3.1 (Lite، Fast، Quality) و Omni 1.1 Flash قابل‌انتخاب‌اند؛ جزئیات و هزینه‌ی اعتبار در [کارت Google Flow](google-flow.md). [S151](../sources/README.md#s151)


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ پیش‌نمایش‌های Veo 3.1 در Gemini API در ۲۰۲۶-۱۰-۲۲ بسته شدند. قیمت Vertex با صدا (هر ثانیه): Quality ‏۰٫۴۰ (720p/1080p)، ۰٫۶۰ (4K)؛ Fast ‏۰٫۱۰/۰٫۱۲/۰٫۳۰؛ Lite ‏۰٫۰۵/۰٫۰۸. بی‌صدا: Quality ‏۰٫۲۰، Fast ‏۰٫۰۸، Lite ‏۰٫۰۳.

## مرتبط
[مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [S47](../sources/README.md#s47) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S86](../sources/README.md#s86)
