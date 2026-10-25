---
name: هم‌ترازی متن و صدا با wav2vec2 XLSR-53
slug: wav2vec2-xlsr-aligner
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: زمان دقیق هر کلمه‌ی متنی که داریم، روی صدا؛ فارسی، عربی، انگلیسی و ۹ زبان دیگر، Apache-2.0
url: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-persian
repo: ""
license: "Apache-2.0 (مدل‌ها)؛ torchaudio BSD"
pricing: free
risk: low
sources: [S136]
found_in: []
last_checked: 2026-10-22
next_check: "2027-01-22"
---

# هم‌ترازی اجباری با wav2vec2 XLSR-53

## چیست
✅ مدل‌های CTC `jonatasgrosman/wav2vec2-large-xlsr-53-<زبان>` (فارسی، عربی، انگلیسی، آلمانی، فرانسوی، اسپانیایی، روسی، چینی، ژاپنی، ایتالیایی، پرتغالی، هلندی) همه با مجوز Apache-2.0 (کارت Hugging Face، ۲۰۲۶-۱۰-۲۲)، با حروف خود زبان. با `torchaudio.functional.forced_align` متن معلوم روی صدا هم‌تراز می‌شود. WhisperX هم برای fa و ar همین مدل‌ها را بار می‌کند ✅.

## تجربه 🔬
🔬 در [خط تولید ویدیوی چندزبانه](../domains/social-media/multilang-video-pipeline.md) (دفتر پروژه‌ها): حدود ۶۰ خط کد. وقتی صدا کلمه‌ای را کش می‌دهد، آغاز آن دیر می‌افتد؛ چسباندن به آغاز گفتار بعد از مکث دست‌کم ۰٫۲ ثانیه آن را با سکوت‌سنج FFmpeg یکی کرد. رقم و کلمه‌ی لاتین درون فارسی در واژگان مدل نیستند؛ زمانشان از همسایه‌ها درون‌یابی می‌شود.

## ریسک و هشدار
⚠️ `forced_align` در torchaudio 2.9 حذف می‌شود؛ روی 2.8 بمان یا جایگزین بیاور. ⛔ بسته‌ی PyPI `ctc-forced-aligner` 1.0.2 شاخه‌ای دیگر با مدل پیش‌فرض غیرتجاری (MMS، CC-BY-NC) است؛ آن را برای کار مشتری نیاور.

## مرتبط
[ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [WhisperX](whisperx.md) · [S136](../sources/README.md#s136)
