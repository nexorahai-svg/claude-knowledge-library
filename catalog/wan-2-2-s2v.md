---
name: Wan 2.2 S2V (عکس + صدا به ویدیو)
slug: wan-2-2-s2v
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مدل بازوزن Apache-2.0 Wan2.2-S2V-14B عکس + صدا به ویدیوی سخن‌گو؛ روی molab آزموده شد (۶ ثانیه در حدود ۴۵ دقیقه، ۵۴ تا ۵۶ گیگ)
use_when: "free talking video from one photo and voice with the aspect following the photo ; comparison against InfiniteTalk on the same inputs"
how: "Trial first on a small task: on a molab GPU run generate.py --task s2v-14B --size 1024*704 --offload_model True --convert_model_dtype --image <photo> --audio <wav> from Wan-Video/Wan2.2; install peft, stub decord, patch attention.py fallback and prompt_extend except; own face and voice only"
url: https://github.com/Wan-Video/Wan2.2
repo: "https://github.com/Wan-Video/Wan2.2"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S192]
found_in: []
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Wan 2.2 S2V

## چیست
✅ مدل `Wan-AI/Wan2.2-S2V-14B` (Apache-2.0)، مخزن Wan-Video/Wan2.2، وزن‌ها حدود ۴۶ گیگ. دستور رسمی تک‌GPU: `generate.py --task s2v-14B --size 1024*704 --offload_model True --convert_model_dtype --image … --audio …`؛ README دست‌کم ۸۰ گیگ VRAM می‌گوید.

## آزمون روی molab 🔬 (۲۰۲۶-۱۰-۲۸)
🔬 همان ورودی [InfiniteTalk](infinitetalk.md) (عکس ۷۲۰×۱۲۸۰ و ۶ ثانیه صدا) روی RTX PRO 6000 Blackwell، Python 3.13.11، torch 2.14.1+cu130. خروجی ۶۴۰×۱۰۸۸ (نسبت از عکس ورودی می‌آید)، ۱۶ فریم در ثانیه؛ دو کلیپ × ۴۰ گام × ۳۱ تا ۳۴ ثانیه ≈ **۴۵ دقیقه** برای ۶ ثانیه، ۵۴ تا ۵۶ گیگ VRAM. ❓ لب‌خوانی فارسی: قضاوت مالک مانده.

## وصله‌ها 🔬
- همان numpy و torchvision که در [InfiniteTalk](infinitetalk.md) آمده.
- `peft` در `requirements_s2v` نیست؛ جدا نصب شود.
- بدل `decord`.
- در `wan/utils/prompt_extend.py` عبارت `except ModuleNotFoundError` را به `except Exception` بده (بسته‌ی خالی `flash_attn` در molab `ImportError` می‌دهد نه `ModuleNotFoundError`).
- همان وصله‌ی بازگشت به `attention()` در `wan/modules/attention.py`.

## کی استفاده کنیم
🧪 وقتی نسبت تصویر باید از عکس بیاید یا برای مقایسه با InfiniteTalk. با ۱۶ فریم در ثانیه و زمان بیشتر، فعلاً InfiniteTalk (۲۵ فریم، ۳۰ دقیقه) سریع‌تر بود.

## ریسک و هشدار
⚠️ فقط چهره و صدای خودت یا با رضایت مکتوب؛ برچسب AI؛ فقط ورودی غیرخصوصی در نوت‌بوک عمومی‌فهرست‌نشده؛ کد مخزن را پیش از اجرا بخوان.

## مرتبط
[Wan 2.2](wan-2-2.md) · [InfiniteTalk](infinitetalk.md) · [molab](molab.md) · [GPU ابری molab](../domains/claude-code/cloud-gpu-molab.md) · [S192](../sources/README.md#s192) · دفتر پروژه‌ها
