---
name: faster-whisper
slug: faster-whisper
category: audio-voice
domains: [social-media, apps]
verdict: adopt
status: researched
summary: اجرای محلی و سریع Whisper برای تبدیل گفتار به متن
use_when: "Persian subtitles or transcripts without sending audio out ; local speech-to-text ; long or many Persian files that are slow on our CPU (run on a molab GPU, public audio only)"
how: "pip/uv install faster-whisper, use large-v3-turbo (same Persian accuracy as large-v3, 3x faster) with int8 on CPU or float16 on GPU; GPU needs CUDA 12 cuBLAS + cuDNN 9: on a CUDA 13 host pip install nvidia-cublas-cu12 nvidia-cudnn-cu12 and preload their lib*.so with ctypes RTLD_GLOBAL before transcribing; pass a 16 kHz float32 numpy array to avoid the PyAV metadata_errors TypeError"
url: https://github.com/SYSTRAN/faster-whisper
repo: "https://github.com/SYSTRAN/faster-whisper"
license: "MIT"
pricing: free
risk: low
sources: [S45, S151, S185]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-26"
---

# faster-whisper

## چیست
✅ تا ۴ برابر سریع‌تر با همان دقت (ادعای سازنده)، کوانتیزه‌ی ۸ بیتی روی CPU و GPU. همان مدل Whisper که `fa` دارد.

## دستور سریع

**نصب** (✅ [README](https://github.com/SYSTRAN/faster-whisper)؛ `1.2.1`؛ ffmpeg لازم نیست چون PyAV همراه است):
```bash
pip install faster-whisper==1.2.1
# فقط GPU (CUDA 12 + cuDNN 9)؛ LD_LIBRARY_PATH باید پیش از شروع پایتون ست شود:
pip install nvidia-cublas-cu12 "nvidia-cudnn-cu12==9.*"
```
**حداقل اجرا** (✅ README؛ `segments` یک generator است و تا نخوانی اجرا نمی‌شود):
```python
from faster_whisper import WhisperModel
model = WhisperModel("turbo", device="cpu", compute_type="int8")   # GPU: device="cuda", compute_type="float16"
segments, info = model.transcribe("voice16k.wav", language="fa", beam_size=5, word_timestamps=True)
for s in list(segments): print(f"[{s.start:.2f}-{s.end:.2f}] {s.text}")
```
**تنظیم‌های مهم**
- 🔬 `turbo` (large-v3-turbo): روی ۱۰۰ نمونه‌ی FLEURS فارسی WER ‏`20.2%` در برابر `20.0%` برای large-v3 ولی سه برابر سریع‌تر.
- ✅ حافظه‌ی GPU (README، RTX 3070 Ti ۸ گیگ، large-v2، ۱۳ دقیقه): fp16 ‏`4525 MB`، int8 ‏`2926 MB`؛ با `BatchedInferencePipeline(batch_size=8)` ‏`6090 MB` ولی حدود ۳٫۷ برابر سریع‌تر (`17s` در برابر `1m03s`). ❓ روی RTX 4060 اندازه نگرفتیم؛ برای ۸ گیگ از `batch_size` کوچک شروع کن.
- 🔬 CPU ضعیف (Xeon E5-2630 v3، int8) برای turbo `0.61×` زمان واقعی بود؛ برای فایل بلند GPU لازم است (✅ `vad_filter=True` سکوت‌های بیش از ۲ ثانیه را حذف می‌کند).

**خطاهای رایج**
- 🔬 `TypeError: open() got an unexpected keyword argument 'metadata_errors'` (ناسازگاری PyAV) ← صدا را با ffmpeg به WAV ۱۶k ببر و آرایه‌ی float32 بده.
- ✅ CUDA 13 با `libcublas.so.12 is not found` شکست می‌خورد؛ بسته‌های `-cu12` را نصب کن و (در نوت‌بوک زنده) 🔬 همه‌ی `lib*.so` آنها را پیش از `transcribe` با `ctypes.CDLL(..., RTLD_GLOBAL)` بار کن.
- 🔬 فارسی خوانده‌شده‌ی تمیز خوب است؛ پشتو بی‌معنی داد. خطاها بیشتر املایی‌اند و عدد را گاهی رقمی می‌نویسد → برای زیرنویس منتشرشدنی بازخوانی انسانی.

## کی استفاده کنیم
🧭 پیش‌فرض زیرنویس فارسی؛ داده بیرون نمی‌رود.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
GPU به کتابخانه‌های NVIDIA برای CUDA 12 نیاز دارد (دام CUDA 13 پایین). 🔬 دقت فارسی روی صدای خوانده‌شده‌ی تمیز (FLEURS) سنجیده شد؛ ❓ روی صدای خودمان (لهجه، موسیقی پس‌زمینه، چند گوینده) هنوز عدد نداریم.

🔬 در یک پروژه‌ی واقعی (۲۰۲۶-۱۰-۲۳): مدل large-v3 با int8 روی CPU یک پیام صوتی واتساپ فارسی را درست پیاده کرد. یک ویدیوی **پشتو** خروجی بی‌معنی داد (زبان «ps» با احتمال ۰.۲۸ تشخیص داده شد) → پشتو قابل استفاده نیست.

🔬 دام: با `uv run --with faster-whisper` نسخه‌ی PyAV نصب‌شده خطای `TypeError: open() got an unexpected keyword argument 'metadata_errors'` داد. راه‌حل: صدا را با ffmpeg به WAV ۱۶ کیلوهرتز ببر و آرایه‌ی numpy از نوع float32 را به `transcribe()` بده.

## هم‌ترازی زیرنویس با متن نوشته‌شده 🔬
- 🔬 روی رایانه‌ی آزمون large-v3 با CPU و int8 اجرا شد؛ CUDA نیامد (`libcublas.so.12` نبود). خطای `metadata_errors` در `av.open` (TypeError) ← اول صدا را به wav با ۱۶ کیلوهرتز برگردان.
- 🔬 تطبیق «اولین کلمه‌ی هر خط» با لغزش‌های Whisper می‌شکند (اخم→احم، غصه→قصه، ولی→بلی، کلمه‌ی شکسته). روش پایدار: متن و رونویسی را نرمال کن (حذف ZWNJ، اعراب و نشانه؛ یکی‌کردن حرف‌های هم‌صدا: غ→ق، خ→ح، ذ ظ ض→ز، ص ث→س، ط→ت، ع→ا) و **کل متن را با کل رونویسی نویسه‌به‌نویسه** با `difflib.SequenceMatcher(autojunk=False)` هم‌تراز کن؛ اولین نویسه‌ی تطبیق‌یافته‌ی هر خط = زمان شروع آن. [S151](../sources/README.md#s151)

## فارسی روی GPU: دقت و سرعت 🔬 (۲۰۲۶-۱۰-۲۸)
- 🔬 **دقت فارسی سنجیده شد:** ۱۰۰ نمونه‌ی اول FLEURS فارسی (۲۶.۵ دقیقه، متن مرجع، CC-BY-4.0) روی GPU ابری [molab](molab.md)، `language="fa"`، `beam_size=5`، بعد از یکسان‌سازی حروف و ارقام و حذف نشانه‌ها:

  | مدل | WER | CER | سرعت روی RTX PRO 6000 Blackwell (float16) |
  |---|---|---|---|
  | large-v3 | ۲۰.۰٪ | ۶.۶٪ | ۵۶ ثانیه، ۲۸ برابر زمان واقعی |
  | large-v3-turbo | ۲۰.۲٪ | ۶.۲٪ | ۱۸ ثانیه، ۹۰ برابر زمان واقعی |

  → **turbo پیش‌فرض است:** همان دقت، سه برابر سریع‌تر. خطاها بیشتر املایی‌اند (سند→سنت، گسترده→گزدرده، مؤثر→معسر) و عدد را گاهی رقمی می‌نویسد؛ برای زیرنویس منتشرشدنی بازخوانی انسانی لازم است.
- 🔬 **CPU این رایانه** (Xeon E5-2630 v3، ۳۲ رشته، int8): turbo روی ۱۰ نمونه‌ی اول ۰.۶۱ برابر زمان واقعی بود، یعنی کندتر از خود صدا. GPU molab حدود **۱۵۰ برابر** سریع‌تر بود (نمونه‌ها کمی فرق دارند، پس عدد تقریبی است). کارت این رایانه (Quadro M4000، Maxwell) برای این کار امتحان نشد.
- 🔬 **دام CUDA 13:** ✅ faster-whisper فقط cuBLAS و cuDNN 9 **برای CUDA 12** را می‌شناسد ([README](https://github.com/SYSTRAN/faster-whisper)). محیط molab با torch cu130 (CUDA 13) آمد و اجرا با `libcublas.so.12 is not found` شکست. ✅ README می‌گوید `nvidia-cublas-cu12` و `nvidia-cudnn-cu12` را با pip نصب کن و `LD_LIBRARY_PATH` را **پیش از شروع پایتون** بگذار؛ در نوت‌بوکی که از قبل در حال اجراست این ممکن نیست. 🔬 راه جایگزین: پیش از اولین `transcribe` همه‌ی `lib*.so.*` داخل پوشه‌ی `lib` آن دو بسته را با `ctypes.CDLL(path, mode=ctypes.RTLD_GLOBAL)` بار کن. جواب داد.
- 🔬 روی GPU صدا را مستقیم از بایت‌های WAV با `soundfile` به آرایه‌ی float32 بده؛ PyAV و ffmpeg لازم نشد. [S185](../sources/README.md#s185)

## مرتبط
[زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [S45](../sources/README.md#s45)

🔬 (۲۰۲۶-۱۰-۳۱، large-v3-turbo با int8 روی CPU، ریل ۱۱۷ ثانیه‌ای، ۵۳ قطعه در ۲۷ ثانیه) فارسی محاوره‌ای حدود ۷۰ تا ۸۰٪ درست بود و نام خاص و اصطلاح را غلط نوشت؛ اگر زیرنویس تصویری هست، آن مرجع بهتری است. نسخه‌ی 1.2.1 با PyAV جدید خطای `metadata_errors` داد؛ صدا را جدا بخوان و آرایه‌ی numpy به `transcribe` بده (مثلاً `ffmpeg -ac 1 -ar 16000 -f f32le` و بعد `numpy.fromfile`). این دام در دو محیط جدا دیده شد.
