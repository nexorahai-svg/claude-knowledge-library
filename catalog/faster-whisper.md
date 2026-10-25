---
name: faster-whisper
slug: faster-whisper
category: audio-voice
domains: [social-media, apps]
verdict: adopt
status: researched
summary: اجرای محلی و سریع Whisper برای تبدیل گفتار به متن
url: https://github.com/SYSTRAN/faster-whisper
repo: "https://github.com/SYSTRAN/faster-whisper"
license: "MIT"
pricing: free
risk: low
sources: [S45, S151]
found_in: []
last_checked: 2026-10-24
next_check: "2027-01-15"
---

# faster-whisper

## چیست
✅ تا ۴ برابر سریع‌تر با همان دقت (ادعای سازنده)، کوانتیزه‌ی ۸ بیتی روی CPU و GPU. همان مدل Whisper که `fa` دارد.

## کی استفاده کنیم
🧭 پیش‌فرض زیرنویس فارسی؛ داده بیرون نمی‌رود.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
GPU به کتابخانه‌های NVIDIA نیاز دارد. ❓ کیفیت فارسی را روی صدای خودمان تست کن.

🔬 پروژه‌ی K25 (۲۰۲۶-۱۰-۲۳): مدل large-v3 با int8 روی CPU یک پیام صوتی واتساپ فارسی را درست پیاده کرد. یک ویدیوی **پشتو** خروجی بی‌معنی داد (زبان «ps» با احتمال ۰.۲۸ تشخیص داده شد) → پشتو قابل استفاده نیست.

🔬 دام: با `uv run --with faster-whisper` نسخه‌ی PyAV نصب‌شده خطای `TypeError: open() got an unexpected keyword argument 'metadata_errors'` داد. راه‌حل: صدا را با ffmpeg به WAV ۱۶ کیلوهرتز ببر و آرایه‌ی numpy از نوع float32 را به `transcribe()` بده.

## هم‌ترازی زیرنویس با متن نوشته‌شده 🔬
- 🔬 روی این رایانه large-v3 با CPU و int8 اجرا شد؛ CUDA نیامد (`libcublas.so.12` نبود). خطای `metadata_errors` در `av.open` (TypeError) ← اول صدا را به wav با ۱۶ کیلوهرتز برگردان.
- 🔬 تطبیق «اولین کلمه‌ی هر خط» با لغزش‌های Whisper می‌شکند (اخم→احم، غصه→قصه، ولی→بلی، کلمه‌ی شکسته). روش پایدار: متن و رونویسی را نرمال کن (حذف ZWNJ، اعراب و نشانه؛ یکی‌کردن حرف‌های هم‌صدا: غ→ق، خ→ح، ذ ظ ض→ز، ص ث→س، ط→ت، ع→ا) و **کل متن را با کل رونویسی نویسه‌به‌نویسه** با `difflib.SequenceMatcher(autojunk=False)` هم‌تراز کن؛ اولین نویسه‌ی تطبیق‌یافته‌ی هر خط = زمان شروع آن. [S151](../sources/README.md#s151) · دفتر پروژه‌ها (یک پروژه‌ی مشتری / Nexorah AI social، personal family videos)

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [S45](../sources/README.md#s45) · دفتر پروژه‌ها
