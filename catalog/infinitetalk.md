---
name: InfiniteTalk
slug: infinitetalk
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مدل بازوزن Apache-2.0 عکس + صدا به ویدیوی سخن‌گو با طول نامحدود؛ روی molab آزموده شد (۶ ثانیه در حدود ۳۰ دقیقه)
use_when: "free talking-head video from one photo and real voice when API cost matters ; longer than one clip talking video using streaming mode"
how: "Trial first on a small task: run MeiGen-AI/InfiniteTalk on a molab GPU (one job per notebook, background nohup + short polling); on Python 3.13 without flash-attn apply the listed patches (drop numpy<2 pin, stubs for decord/xformers/xfuser, flash_attn namespace fix); only your own face and voice or written consent; label as AI"
url: https://github.com/MeiGen-AI/InfiniteTalk
repo: "https://github.com/MeiGen-AI/InfiniteTalk"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S192]
found_in: []
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# InfiniteTalk

## چیست
✅ مخزن MeiGen-AI/InfiniteTalk (Apache-2.0): عکس + صدا ← ویدیوی سخن‌گو، طول نامحدود با حالت streaming. وزن‌ها: Wan-AI/Wan2.1-I2V-14B-480P + TencentGameMate/chinese-wav2vec2-base (به‌اضافه‌ی `model.safetensors` از revision `refs/pr/1`) + MeiGen-AI/InfiniteTalk فایل `single/infinitetalk.safetensors`؛ جمعاً حدود ۵۹ گیگ.

## آزمون روی molab 🔬 (۲۰۲۶-۱۰-۲۸)
🔬 RTX PRO 6000 Blackwell ۹۶ گیگ، Python 3.13.11، torch 2.14.1+cu130. ورودی: یک عکس ۷۲۰×۱۲۸۰ و ۶ ثانیه صدای واقعی ۱۶ کیلوهرتز، پرامپت انگلیسی. خروجی ۴۴۸×۸۳۲، ۲۵ فریم در ثانیه؛ چهره، عینک، ریش و لباس پایدار و حرکت سر طبیعی. ۶ ثانیه = دو کلیپ × ۴۰ گام × ۲۲ ثانیه ≈ **۳۰ دقیقه** بدون flash-attn، ۴۵ گیگ VRAM. ❓ کیفیت لب‌خوانی فارسی: قضاوت مالک مانده.

## وصله‌های لازم برای Python 3.13 و بدون flash-attn 🔬
- پین `numpy<2` را بردار (برای cp313 چرخ ندارد و کل نصب uv شکست می‌خورد).
- torchvision هم‌نسخه با torch (0.29.1+cu130 از شاخص cu130، با پین torch).
- بدل‌های ساختگی (stub) برای `decord` (فقط VideoReader/cpu)، `xformers.ops` (`memory_efficient_attention` روی SDPA تورچ با جابه‌جایی (B,L,H,D)، پذیرفتن `op=` و بدل BlockDiagonalMask) و `xfuser.core.distributed` (رتبه‌ی ۰، اندازه‌ی ۱) و `xfuser.core.long_ctx_attention`.
- در `wan/multitalk.py` خط `from inspect import ArgSpec` را بردار؛ `from kokoro import KPipeline` را در try/except بگذار.
- در `wan/modules/attention.py`: `FLASH_ATTN_2_AVAILABLE = hasattr(flash_attn, 'flash_attn_varlen_func')` (در molab یک بسته‌ی namespace خالیِ `flash_attn` در site-packages سیستم هست و import را فریب می‌دهد) و `flash_attention()` وقتی نه FA2 هست نه FA3 به `attention()` برگردد.
- فایل requirements خیلی چیز می‌خواهد (xfuser، xformers، optimum-quanto، moviepy==1.0.3 …)؛ فقط آنچه importها لازم دارند نصب کن.

## کی استفاده کنیم
🧪 وقتی تصویر و صدای واقعی خودمان را داریم و هزینه‌ی API نمی‌خواهیم و ۳۰ دقیقه برای هر ۶ ثانیه قابل تحمل است. جایگزین میزبانی: fal با ۰٫۲۰ دلار در ثانیه (۷۲۰p دو برابر) ✅ (صفحه‌ی مدل، ۲۰۲۶-۱۰-۲۸).

## ریسک و هشدار
⚠️ فقط چهره و صدای خودت یا با رضایت مکتوب؛ برچسب AI هنگام انتشار. نصب و اجرا فقط در molab (نوت‌بوک عمومی‌فهرست‌نشده، داده‌ی خصوصی نه). کد مخزن را پیش از اجرا بخوان.

## مرتبط
[Wan 2.2 S2V](wan-2-2-s2v.md) · [molab](molab.md) · [GPU ابری molab](../domains/claude-code/cloud-gpu-molab.md) · [مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [S192](../sources/README.md#s192) · دفتر پروژه‌ها
