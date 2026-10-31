---
name: Wan 2.2 (A14B و TI2V-5B)
slug: wan-2-2
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: مدل ویدیوی بازوزن Apache-2.0؛ نسخه‌ی A14B روی GPU رایگان molab آزموده شد (۵ ثانیه‌ی ۴۸۰p در ۴ دقیقه)؛ بی‌صدا
use_when: "free commercial-licensed realistic product or b-roll clip from a text prompt when API cost matters ; short silent shots to combine with MOSS-TTS 8B voice and our own music"
how: "Run Wan-AI/Wan2.2-T2V-A14B-Diffusers with diffusers WanPipeline on a molab GPU (public prompts only); with transformers 5 tie pipe.text_encoder.encoder.embed_tokens.weight = pipe.text_encoder.shared.weight after loading or the prompt is ignored; 480p full GPU (75 GB, 4 min at 20 steps), with a higher frame rate (more frames exported at 24 fps, or frame interpolation; untested); 720p 40 steps needs enable_model_cpu_offload (35 GB, ~29 min); parallel clips in separate molab clones; check a frame against the prompt before using a clip"
url: https://github.com/Wan-Video/Wan2.2
repo: "https://github.com/Wan-Video/Wan2.2"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S136, S187]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-26"
---

# Wan 2.2 (A14B و TI2V-5B)

## چیست
✅ Apache-2.0 (کارت مدل Hugging Face). TI2V-5B: ۷۲۰p (۱۲۸۰×۷۰۴) با ۲۴ فریم در ثانیه؛ README دست‌کم ۲۴ گیگابایت با offload می‌گوید، ولی مستندات ComfyUI می‌گوید «روی ۸ گیگابایت خوب جا می‌شود» با offload خودش. ✅ مدل‌های A14B (دو «متخصص» ۱۴B که پشت هم کار می‌کنند) طبق کارت مدل «دست‌کم ۸۰ گیگابایت» برای یک GPU می‌خواهند. ❓ Wan 2.5 تا 3.0 بازوزن تأیید نشدند ([Wan 3](wan-3.md) فقط API).

## دستور سریع

**نصب** (✅ [کارت مدل](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers) و 🔬 آزمون ما روی GPU ابری؛ `diffusers 0.42.1` که `WanPipeline` دارد). ✅ README: A14B دست‌کم **۸۰ گیگ** VRAM و TI2V-5B دست‌کم **۲۴ گیگ** می‌خواهد → روی RTX 4060 با ۸ گیگ اجرای مستقیم A14B شدنی نیست (❓ 5B با offload مستندات ComfyUI «۸ گیگ» می‌گوید، آزموده نشده):
```bash
pip install "diffusers==0.42.1" transformers accelerate     # 🔬 با transformers 5.0.0 آزموده شد
```
**حداقل اجرا** (✅ کارت مدل، 🔬 تنظیم ما: ۴۸۰p، ۲۰ گام، ۴ دقیقه، ۷۵ گیگ VRAM):
```python
import torch
from diffusers import WanPipeline, AutoencoderKLWan
from diffusers.utils import export_to_video
mid = "Wan-AI/Wan2.2-T2V-A14B-Diffusers"
vae = AutoencoderKLWan.from_pretrained(mid, subfolder="vae", torch_dtype=torch.float32)
pipe = WanPipeline.from_pretrained(mid, vae=vae, torch_dtype=torch.bfloat16).to("cuda")
pipe.text_encoder.encoder.embed_tokens.weight = pipe.text_encoder.shared.weight   # 🔬 با transformers 5 لازم است
out = pipe(prompt="...", height=480, width=832, num_frames=81, guidance_scale=4.0,
           guidance_scale_2=3.0, num_inference_steps=20).frames[0]
export_to_video(out, "out.mp4", fps=16)
```
**تنظیم‌های مهم**
- 🔬 ۷۲۰p با ۴۰ گام روی ۹۶ گیگ بعد از ۲۷ دقیقه در رمزگشایی VAE OOM داد؛ با `pipe.enable_model_cpu_offload()` (به‌جای `.to("cuda")`) ۳۵ گیگ و ۲۹ دقیقه.
- 🔬 ۴۸۰p هفت برابر سریع‌تر است و در بازبینی بصری بهتر از ۷۲۰p با ۱۶ فریم؛ ❓ برای روانی بیشتر `num_frames=121` با `fps=24` (باید `4k+1` باشد) آزمون نشده.
- 🔬 دانلود اول حدود ۷۰ گیگ و ۴ تا ۵ دقیقه است و هر نوت‌بوک از نو می‌گیرد.

**خطاهای رایج**
- 🔬 با transformers 5 بدون خط وصل‌کردن `embed_tokens` متن نادیده گرفته می‌شود و ویدیوی بی‌ربط بدون خطا می‌آید → بخش «دام مهم: متن نادیده گرفته می‌شود» همین کارت؛ یک فریم را با متن مقایسه کن.
- 🔬 فقط متن و تصویر عمومی در نوت‌بوک ابری؛ خروجی بی‌صداست (صدا جدا).
- ✅ کارت HF می‌گوید این مدل در زمان انتشار به diffusers از شاخه‌ی main نیاز داشت؛ با نسخه‌ی PyPI فعلی دیگر لازم نشد (🔬).

## آزمون A14B روی molab 🔬 (۲۰۲۶-۱۰-۲۸)
🔬 مدل `Wan-AI/Wan2.2-T2V-A14B-Diffusers` با diffusers 0.42.1 و `WanPipeline` روی [molab](molab.md) (RTX PRO 6000 Blackwell، ۹۶ گیگ)، bf16، VAE در fp32، `guidance_scale=4.0`، `guidance_scale_2=3.0`، ۸۱ فریم با ۱۶ فریم در ثانیه (۵ ثانیه)، بذر ۴۲. صحنه‌ی محصولی از خودمان: جعبه‌ی هندزفری مشکی روی میز چوبی که درش باز می‌شود.

| تنظیم | زمان ساخت | بیشترین VRAM | نتیجه |
|---|---|---|---|
| ۴۸۰p (۸۳۲×۴۸۰)، ۲۰ گام، همه روی GPU | **۴ دقیقه** (۲۳۸ ثانیه) | ۷۵ گیگ | صحنه درست؛ در باز می‌شود؛ یک هندزفری سفید اضافه روی میز |
| ۷۲۰p (۱۲۸۰×۷۲۰)، ۴۰ گام، همه روی GPU | ۴۱ ثانیه در هر گام | ⛔ کمبود حافظه در **مرحله‌ی آخر** (رمزگشایی VAE) بعد از ۲۷ دقیقه | — |
| ۷۲۰p، ۴۰ گام، `enable_model_cpu_offload()` | ۲۹ دقیقه (۱۷۱۹ ثانیه) | ۳۵ گیگ | تمیزتر، بدون شیء اضافه، پس‌زمینه‌ی پنجره |

- 🔬 **دانلود اول** حدود ۷۰ گیگ و ۴ تا ۵ دقیقه در molab؛ اجرای بعدی در همان جلسه ۲۱ ثانیه بارگذاری. هر نوت‌بوک (حتی کلون) از نو دانلود می‌کند.
- 🔬 **عدد ۸۰ گیگ سازنده برای ۷۲۰p کامل روی GPU کافی نبود** وقتی ۸ گیگ دیگر هم گرفته بود. offload حافظه را به ۳۵ گیگ رساند و تقریباً همان سرعت ماند؛ برای ۷۲۰p از اول offload بزن.
- 🔬 **حکم بیننده (۲۰۲۶-۱۰-۲۸):** هر دو کلیپ را دید؛ **۴۸۰p با فریم بالاتر بهتر است** از ۷۲۰p با ۱۶ فریم در ثانیه. یعنی روانی حرکت از وضوح مهم‌تر است، و ۴۸۰p هفت برابر سریع‌تر هم هست.
- 🧭 روند کار: ۴۸۰p، و فریم در ثانیه را بالا ببر. ❓ هنوز آزموده نشده؛ دو راه: (۱) فریم بیشتر بساز و با ۲۴ فریم در ثانیه خروجی بگیر (برای ۵ ثانیه `num_frames=121`؛ تعداد فریم باید ۴k+1 باشد؛ زمان ساخت حدود ۱.۵ برابر می‌شود و ❓ کیفیت حرکت در طول بیشتر از آموزش مدل)، یا (۲) همان ۸۱ فریم با ۱۶ فریم در ثانیه، و بعد میان‌یابی فریم به ۳۲ فریم در ثانیه. ۷۲۰p با offload (۲۹ دقیقه) فقط وقتی وضوح واقعاً لازم شد.

## دام مهم: متن نادیده گرفته می‌شود 🔬
🔬 با **transformers 5.0.0**، لاگ بارگذاری `encoder.embed_tokens.weight | MISSING` می‌گوید و این لایه‌ی رمزگذار متن (UMT5) **صفر** می‌ماند (انحراف معیار ۰)، در حالی که `shared` درست بار شده (انحراف معیار حدود ۹.۷). ✅ پیکربندی رمزگذار متن مدل‌های Wan `tie_word_embeddings: false` دارد، پس transformers 5 این دو را به هم وصل نمی‌کند. نتیجه: **ویدیو کاملاً بی‌ربط به متن** ساخته می‌شود (به‌جای جعبه‌ی هندزفری، ورزش یک زن در باشگاه) و هیچ خطایی نمی‌دهد. راه‌حل آزموده: بعد از بارگذاری
`pipe.text_encoder.encoder.embed_tokens.weight = pipe.text_encoder.shared.weight`
و یک بررسی که انحراف معیارش صفر نباشد. ❓ گزارش رسمی این باگ در diffusers یا transformers پیدا نشد. همیشه پیش از استفاده یک فریم را با متن مقایسه کن.

## کی استفاده کنیم
🧪 کلیپ کوتاه بی‌صدای واقعی‌نما (محصول، b-roll) وقتی هزینه‌ی API نمی‌خواهیم و مجوز تجاری لازم است. صدا جدا: گوینده با [MOSS-TTS](moss-tts.md) ۸B و موسیقی جدا. فقط متن و تصویر عمومی در molab (نوت‌بوک عمومی ولی فهرست‌نشده است). ❓ روی RTX 4060 آزموده نشده؛ یک وبلاگ ۱۸۱ ثانیه برای ۵ ثانیه‌ی ۴۸۰p با 5B گزارش کرده.

## مرتبط
[GPU ابری molab](../domains/claude-code/cloud-gpu-molab.md) · [ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [مدل‌های تولید ویدیو](../domains/social-media/ai-video-models.md) · [S136](../sources/README.md#s136) · [S187](../sources/README.md#s187) · دفتر پروژه‌ها

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
