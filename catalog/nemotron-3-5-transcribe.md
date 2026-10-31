---
name: Nemotron 3.5 Transcribe
slug: nemotron-3-5-transcribe
category: local-ai
domains: [social-media]
verdict: hold
status: researched
summary: مدل رونویسی NVIDIA با تشخیص گوینده و زمان‌بندی کلمه؛ فارسی ندارد و به GPU دیتاسنتر نیاز دارد
use_when: "Comparing speech-to-text models for subtitles ; checking whether a new NVIDIA ASR model supports Persian"
how: "Not for Persian: keep faster-whisper large-v3 for Persian subtitles; model needs ~1x H100 80 GB"
url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
repo: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B"
license: "OpenMDW-1.1"
pricing: free
risk: low
sources: [S206]
found_in: [batch-25]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Nemotron 3.5 Transcribe

## چیست
✅ (۲۰۲۶-۱۰-۳۰، کارت Hugging Face) مدل رونویسی NVIDIA با مجوز OpenMDW-1.1 (https://openmdw.ai/license/1-1/)، معماری MoE ترکیبی Mamba-Transformer روی Nemotron-3.5 Lightning 30B-A3B با حدود ۴٫۳ میلیارد پارامتر فعال، فقط آفلاین، تا یک ساعت صدا، تشخیص گوینده، زمان‌بندی کلمه. نسخه‌های FP8، NVFP4 و DFlash2 هم هست. ۴۰ زبان طبق برچسب‌های کارت؛ فارسی (fa) نیست (عربی و عبری هست). هدف: یک H100 با ۸۰ گیگابایت؛ روی RTX 4060 با ۸ گیگابایت جا نمی‌شود.
✅ طبق https://the-decoder.com/nvidias-open-nemotron-3-5-transcribe-combines-transcription-translation-and-speaker-recognition/ تا ۸ گوینده را تشخیص می‌دهد.

## کی استفاده کنیم
⛔ برای زیرنویس فارسی نه؛ faster-whisper large-v3 را نگه دار.

## قیمت و مجوز
OpenMDW-1.1، رایگان.

## ریسک و هشدار
ریسک پایین؛ فقط نامناسب (بدون فارسی، GPU سنگین).

## مرتبط
- [nemotron-3-ultra](nemotron-3-ultra.md)
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
