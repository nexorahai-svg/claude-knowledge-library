---
name: AI YouTube Shorts Generator
slug: ai-youtube-shorts-generator
category: video
domains: [social-media]
verdict: assess
status: researched
summary: بریدن ویدیوی بلند یوتیوب به کلیپ ۹:۱۶ با انتخاب مدل زبانی؛ کلید پولی لازم، و ابزار تبلیغ MuAPI
url: https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator
repo: "https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator"
license: "MIT"
pricing: freemium
risk: medium
sources: [S130]
found_in: [batch-16]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# AI YouTube Shorts Generator

## چیست
✅ (README) جایگزین متن‌باز Opus Clip: لینک یوتیوب ← رونویسی Whisper ← انتخاب بخش‌های جذاب با مدل زبانی ← برش عمودی ۹:۱۶. حدود ۵٫۵ هزار ستاره، MIT. دو حالت: `api` (پیش‌فرض، همه‌چیز از راه سرویس پولی MuAPI) و `local` (yt-dlp، faster-whisper، OpenCV روی دستگاه، فقط مرحله‌ی مدل زبانی با کلید OpenAI یا Gemini).

## کی استفاده کنیم
👀 فقط برای ویدیوی بلند **خود ما** که حق بریدنش را داریم، در حالت `local`. اجرا نشد: کلید پولی لازم است.

## قیمت و مجوز
✅ کد MIT. ⚠️ حالت پیش‌فرض به MuAPI وابسته است و README پر از پیوند تبلیغی همان سرویس است.

## ریسک و هشدار
⚠️ دانلود ویدیوی یوتیوب دیگران با yt-dlp با قوانین YouTube و حق نشر جور نیست. ⚠️ متن رونویسی به سرویس مدل زبانی فرستاده می‌شود. برای برش محلی بی‌کلید، [faster-whisper](faster-whisper.md) و [FFmpeg](ffmpeg.md) خودمان کافی است.

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S130](../sources/README.md#s130) · دسته‌ی ۱۶
