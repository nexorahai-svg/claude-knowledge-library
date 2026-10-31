---
name: WhisperX
slug: whisperx
category: audio-voice
domains: [social-media]
verdict: trial
status: researched
summary: Whisper با هم‌ترازی دقیق زمان کلمه و تشخیص گوینده
use_when: "need accurate word-by-word subtitles ; transcription plus alignment"
how: "Trial first on a small task: use WhisperX (fa uses jonatasgrosman persian wav2vec2 aligner; its licence unread); it always runs Whisper first so for known text use wav2vec2-xlsr-aligner; speaker detection needs a Hugging Face token and pyannote terms"
url: https://github.com/m-bain/whisperX
repo: "https://github.com/m-bain/whisperX"
license: "BSD-2-Clause"
pricing: free
risk: low
sources: [S45, S136]
found_in: []
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# WhisperX

## چیست
✅ برای `fa` مدل wav2vec2 فارسی را برای هم‌ترازی استفاده می‌کند.

## کی استفاده کنیم
🧭 وقتی زیرنویس کلمه‌به‌کلمه دقیق لازم است.

## قیمت و مجوز
✅ رایگان. ✅ مجوز مدل هم‌ترازی فارسی (`jonatasgrosman/wav2vec2-large-xlsr-53-persian`): Apache-2.0 (https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-persian).

## ریسک و هشدار
⚠️ تشخیص گوینده توکن Hugging Face و قرارداد pyannote می‌خواهد.

## به‌روزرسانی ۲۰۲۶-۱۰-۲۲
✅ `alignment.py`: ۵ زبان با مدل torchaudio (en، fr، de، es، it) و ۳۸ زبان از Hugging Face؛ fa ← `jonatasgrosman/wav2vec2-large-xlsr-53-persian`، ar ← `...-arabic`. README هم‌ترازی متن دلخواه کاربر را توضیح نمی‌دهد و همیشه اول Whisper را اجرا می‌کند؛ برای متن معلوم مستقیم [هم‌ترازی wav2vec2](wav2vec2-xlsr-aligner.md). [S136](../sources/README.md#s136)

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [S45](../sources/README.md#s45)
