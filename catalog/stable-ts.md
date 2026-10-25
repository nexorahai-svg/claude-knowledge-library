---
name: stable-ts
slug: stable-ts
category: audio-voice
domains: [social-media]
verdict: hold
status: researched
summary: هم‌ترازی و زیرنویس کلمه‌به‌کلمه بر پایه‌ی Whisper؛ بایگانی شده از ۲۰۲۶-۰۵-۳۰
url: https://github.com/jianfch/stable-ts
repo: "https://github.com/jianfch/stable-ts"
license: "MIT"
pricing: free
risk: medium
sources: [S136]
found_in: []
last_checked: 2026-10-22
next_check: "2027-04-22"
---

# stable-ts

## چیست
✅ MIT؛ `model.align(audio, text, language=)` متن معلوم را هم‌تراز می‌کند و `to_ass(karaoke=True)` زیرنویس کلمه‌به‌کلمه می‌سازد. ✅ مخزن از ۲۰۲۶-۰۵-۳۰ بایگانی شده و سازنده توسعه را بی‌زمان متوقف کرده است.

## کی استفاده کنیم
⛔ برای کار تازه نه؛ نگهداری نمی‌شود. به‌جایش [هم‌ترازی wav2vec2](wav2vec2-xlsr-aligner.md). ⚠️ خودش هشدار می‌دهد که `reverse_text` مشکل راست‌به‌چپ بعضی پخش‌کننده‌ها را حل نمی‌کند.

## مرتبط
[ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [S136](../sources/README.md#s136)
