---
name: whisper.cpp
slug: whisper-cpp
category: audio-voice
domains: [social-media, apps]
verdict: adopt
status: researched
summary: نسخه‌ی C و C++ از Whisper برای اجرای کاملاً آفلاین
use_when: "transcribing voice messages or audio on Mac/CPU or inside an on-device app ; making SRT/VTT subtitles"
how: "whisper.cpp with -osrt or -ovtt (-ml for line length); convert audio to 16 kHz WAV with FFmpeg; use large-v3-turbo for Persian (small gives 23 percent char error); about real-time speed on CPU"
url: https://github.com/ggml-org/whisper.cpp
repo: "https://github.com/ggml-org/whisper.cpp"
license: "MIT"
pricing: free
risk: low
sources: [S45, S76]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# whisper.cpp

## چیست
✅ خروجی مستقیم `-osrt` و `-ovtt`؛ `-ml` برای طول خط؛ پشتیبانی Metal و Core ML روی Apple Silicon.

## کی استفاده کنیم
🧭 مک و CPU؛ یا داخل اپ روی دستگاه.

🔬 یک پروژه‌ی واقعی نسخه‌ی b5130 ویندوز را برای خواندن پیام صوتی مشتری به کار می‌برد (FFmpeg صدا را به WAV ۱۶ کیلوهرتز تبدیل می‌کند، سقف ۳۰۰ ثانیه، یک اجرای `whisper-cli` برای هر پیام). سنجش خود پروژه (۲۰۲۶-۱۰-۰۶، ۶۰ ویس Opus، i5-13400F، ۴ رشته):

| مدل | خطای حرف کل | فارسی | عربی | انگلیسی | زمان نسبت به طول صدا |
|---|---|---|---|---|---|
| small | ۱۱٫۲٪ | ۲۲٫۹٪ | ۷٫۷٪ | ۳٪ | ۰٫۲۳× |
| medium | ۹٫۳٪ | ۲۲٫۳٪ | ۴٫۶٪ | ۱٪ | ۰٫۷۲× |
| large-v3-turbo | ۵٪ | ۱۱٫۳٪ | ۳٫۴٪ | ۰٫۴٪ | ۰٫۹۷× |

🧭 درس: فارسی با فاصله ضعیف‌ترین زبان است؛ برای فارسی مدل large-v3-turbo لازم است و حدود هم‌اندازه‌ی طول صدا روی پردازنده وقت می‌برد. ❓ نمونه‌ی هر زبان حدود ۲۰ ویس خوانده‌شده است، نه گفتار واقعی مشتری؛ این عددها را دوباره اجرا نکردیم ([S76](../sources/README.md#s76)).

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
—

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [llama.cpp](llama-cpp.md) · [S45](../sources/README.md#s45) · [S76](../sources/README.md#s76)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.

🔬 (۲۰۲۶-۱۰-۳۱) انتشار v1.9.5 هیچ فایل آماده‌ای ندارد. برای لینوکس خودت بساز؛ ساخت در `almalinux:8` (glibc 2.28) روی توزیع‌های قدیمی هم اجرا می‌شود.
