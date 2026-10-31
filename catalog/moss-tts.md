---
name: MOSS-TTS (OpenMOSS)
slug: moss-tts
category: audio-voice
domains: [social-media, website]
verdict: trial
status: researched
summary: تبدیل متن به گفتار محلی با مجوز تجاری (Apache-2.0)؛ فارسی و عربی بومی، شبیه‌سازی صدا؛ آزموده روی RTX 4060
use_when: "voice-over for videos in Persian, Arabic or English on our own machine, free and commercial-licensed ; multilingual video pipeline narration"
how: "Trial first on a small task: Apache-2.0 MOSS-TTS; for faithful Persian use the 8B v1.5 on a 24 GB+ GPU (molab works; Local v1.5 turns formal text colloquial); make each language voice with NO reference in that language (pick best seed, reuse as fixed reference); in an existing torch env install transformers==5.0.0 plus accelerate einops librosa tiktoken and pin torch/torchvision/torchaudio to 2.11/0.26/2.11; on 8 GB card put audio_tokenizer on CPU and use device_map=auto with max_memory; Nano for fast English only"
url: https://github.com/OpenMOSS/MOSS-TTS
repo: "https://github.com/OpenMOSS/MOSS-TTS"
license: "Apache-2.0 (کد و وزن‌ها؛ فایل LICENSE در مخزن و برچسب مدل در Hugging Face)"
pricing: free
risk: low
sources: [S135, S136, S151, S186]
found_in: [real-project]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# MOSS-TTS (OpenMOSS)

## چیست
✅ خانواده‌ی مدل‌های گفتار OpenMOSS با مجوز Apache-2.0 (هم کد، هم وزن‌ها): **MOSS-TTS v1.5** (۸B)، **MOSS-TTS-Local-Transformer v1.5** (۴٫۵B، خرداد ۲۰۲۶)، **MOSS-TTS-Nano** (۱۰۰M، روی CPU)، **MOSS-VoiceGenerator** (طراحی صدا از توصیف). فهرست رسمی زبان‌های v1.5: ۳۱ زبان، فارسی (`fa`) و عربی (`ar`) هم. شبیه‌سازی صدا با یک فایل مرجع؛ برچسب زبان (`language="Persian"`) کیفیت را بالا می‌برد.

## آزمون روی رایانه‌ی آزمون (۲۰۲۶-۱۰-۲۱)
🔬 RTX 4060 با ۸ گیگابایت. سنجش بی‌گوش: صدا با faster-whisper large-v3-turbo به متن برگشت و CER با متن سنجیده شد (رقم و حروف عدد یکی شد)، بعد با گوش هم سنجیده شد.

| روش | فارسی CER | عربی CER | نظر شنونده |
|---|---|---|---|
| Local v1.5، **بدون مرجع**، فقط برچسب زبان | ۲٫۴ تا ۱۳٪ (میانه حدود ۵٪) | ۱۸ تا ۳۳٪ (بیشترش رقم) | ✅ بومی؛ صدای ۱ فارسی و ۳ عربی انتخاب شد |
| Local v1.5، **مرجع انگلیسی** (صدای طراحی‌شده) | — | — | ⛔ «انگار یک انگلیسی‌زبان فارسی حرف می‌زند»: لهجه‌ی مرجع منتقل می‌شود |
| Nano (۱۰۰M) با مرجع | ۸ تا ۱۶٪ | ۱۸ تا ۲۹٪ | انگلیسی ۰ تا ۶٪ عالی؛ فارسی و عربی ضعیف |
| VoiceGenerator با متن فارسی/عربی | حدود ۵۰٪ | ۵۰ تا ۷۵٪ | ⛔ نامفهوم؛ طراحی صدا فقط برای انگلیسی خوب است |

🧭 **روش درست برای صدای اختصاصی چندزبانه:** برای هر زبان، صدا را با خود مدل و **بدون مرجع** در همان زبان بساز (چند بذر)، بهترین را انتخاب کن و همان فایل را مرجع ثابت آن زبان کن. مرجع یک زبان را برای زبان دیگر به کار نبر.

## اجرا روی کارت ۸ گیگی (درس‌ها)
- ⚠️ رمزگذار صدای MOSS (`processor.audio_tokenizer`) خودش ۱٫۸B پارامتر و در fp32 حدود ۷ گیگابایت است: آن را روی CPU بگذار (`.to("cpu")`).
- ⚠️ Local v1.5 در bf16 حدود ۹٫۱ گیگابایت است. bitsandbytes (۸ و ۴ بیت) با کد سفارشی مدل اثر نکرد. راه کارآمد: `device_map="auto", max_memory={0: "5GiB", "cpu": "26GiB"}`؛ حدود ۶ تا ۷ برابر کندتر از زمان صدا (۸ ثانیه صدا در ۵۳ ثانیه)، برای صدای یک‌باره کافی.
- ⚠️ Transformers 5: `torch_dtype` نادیده گرفته می‌شود و مدل fp32 بار می‌شود؛ `dtype=` بنویس.
- ⚠️ torchaudio 2.9 فایل را با torchcodec می‌خواند که نسخه‌ی CUDA آن NPP می‌خواهد؛ `torchaudio.load` را با soundfile جایگزین کن و خروجی را هم با soundfile بنویس.
- ⚠️ نصب: `pip install -e ".[torch-runtime]"` (بدون این extra، PyTorch نصب نمی‌شود). Nano: `--disable-wetext-processing` (وگرنه بسته‌ی `tn` چینی می‌خواهد).

## طول و استفاده در خط تولید ویدیو (۲۰۲۶-۱۰-۲۲) 🔬
✅ طول با شمار توکن: ۱۲٫۵ کد در ثانیه (`tokens=125` حدود ۱۰ ثانیه)؛ مکث با `[pause 3.2s]`؛ پارامتر سرعت ندارد. ✅ اندازه: GitHub می‌گوید Local v1.5 «۴B»، کارت Hugging Face حدود ۵B؛ عدد «۴٫۵B» بالا با هیچ‌کدام نمی‌خواند. ❓ GitHub می‌گوید مدل ۸B با llama.cpp در ۸ گیگابایت جا می‌شود؛ آزموده نشده.
🔬 در [خط تولید ویدیوی چندزبانه](../domains/social-media/multilang-video-pipeline.md) با ۳ گیگابایت کارت (چون Ollama بقیه را گرفته بود) حدود ۱۰ برابر زمان واقعی. بررسی خودکار با برگرداندن به متن و ساخت دوباره‌ی خط ضعیف: فارسی ≤۱۰٪، عربی یک خط ۱۰٫۲٪، انگلیسی ۰٪.

## مدل ۸B روی GPU ابری 🔬 (۲۰۲۶-۱۰-۲۸، molab)
🔬 روی [molab](molab.md) (RTX PRO 6000 Blackwell، bf16، `attn_implementation="sdpa"`، بدون مرجع، `language="Persian"`، یک بذر برای هر جمله). ۵ جمله‌ی فارسی فروشگاهی از خودمان، عدد با حروف. سنجش بی‌گوش مثل بالا: برگرداندن به متن با faster-whisper turbo و CER بعد از حذف فاصله و ZWNJ.

| مدل | CER فارسی (۵ جمله) | سرعت | حافظه‌ی GPU | خروجی |
|---|---|---|---|---|
| **MOSS-TTS v1.5 (۸B)** | ۱.۶ تا ۵.۷٪، میانگین ۳.۳٪ | حدود ۲.۵ برابر زمان واقعی | ۲۲.۶ گیگ | ۲۴ کیلوهرتز |
| Local v1.5 (۴B) | ۳.۸ تا ۸.۲٪، میانگین ۵.۴٪ | ۲.۴ برابر زمان واقعی | ۱۲ گیگ | ۴۸ کیلوهرتز استریو |

- 🔬 **۸B متن را وفادارتر می‌خواند.** Local متن رسمی را **محاوره‌ای** تلفظ کرد (آمدید→اومدید، دارد→داره، می‌کند→میکنه، یک→یه) و بخشی از CER بالاترش از همین است. برای گویندگی خودمانی شاید خوب باشد، ولی متن نوشته‌شده را دقیق نمی‌خواند. ۸B فقط «را» را «رو» گفت.
- 🔬 روی همین GPU، Local حدود **۱۶ برابر** سریع‌تر از اجرای نیمه‌روی‌CPU روی کارت ۸ گیگی بالا بود (۲.۴ در برابر حدود ۰.۱۵ برابر زمان واقعی).
- 🔬 **با گوش:** شنونده هر دو نمونه‌ی جمله‌ی ۱ را شنید (۲۰۲۶-۱۰-۲۸): ۸B «خوب» بود و Local دوباره «خیلی مصنوعی»، همان ایراد پایین. 🧭 برای گویندگی فارسی اول ۸B را امتحان کن و ElevenLabs را برای وقتی نگه دار که ۸B کافی نبود. ❓ یک جمله کافی نیست؛ روی متن بلند و چند بذر هنوز شنیده نشده.
- 🔬 **دام نصب:** پیش‌فرض‌های `uv pip install accelerate` در یک محیط آماده torch را از 2.11 به 2.14 برد. torchvision قدیمی با `operator torchvision::nms does not exist` شکست و **torchaudio بعد از 2.11 منتشر نشده** (کد مدل به آن نیاز دارد). راه‌حل: سه بسته را با هم پین کن (`torch==2.11.0 torchvision==0.26.0 torchaudio==2.11.0`). به‌جای `-e ".[torch-runtime]"` که torch 2.9 با cu128 نصب می‌کند، کافی بود `transformers==5.0.0 accelerate einops librosa tiktoken scipy orjson` را کنار torch موجود نصب کنی؛ کد مدل با `trust_remote_code` از Hugging Face می‌آید. [S186](../sources/README.md#s186) · دفتر پروژه‌ها

## کی استفاده کنیم
🧭 گویندگی ویدیوی آموزشی و تبلیغ به فارسی و عربی و انگلیسی، روی سیستم خود، بدون هزینه و با مجوز تجاری. برای انگلیسی سریع روی CPU: Nano. برای فارسی و عربی: Local v1.5 بدون مرجع یا با مرجع بومی.

## ریسک و هشدار
⚠️ شبیه‌سازی صدای شخص واقعی فقط با رضایت او. 🔬 مدل ۸B (۱۷ گیگابایت) روی GPU ابری آزموده شد و فارسی دقیق‌تری داد (بخش بالا)؛ روی کارت ۸ گیگی هنوز آزموده نشده.

## حکم آزمون واقعی ۲۰۲۶-۱۰-۲۴ 🔬
🔬 در یک پروژه‌ی واقعی فارسی MOSS-TTS «خیلی مصنوعی» ارزیابی شد؛ برای تحویل نهایی ElevenLabs v4 مناسب‌تر بود و MOSS برای پیش‌نویس و آزمون زمان‌بندی می‌ماند. [کارت ElevenLabs](elevenlabs-tts.md) · [S151](../sources/README.md#s151)

## مرتبط
[صداگذاری](../domains/social-media/ai-voice.md) · [OmniVoice](omnivoice.md) · [faster-whisper](faster-whisper.md) · [S135](../sources/README.md#s135)

🧭 (مرور ارتقا ۲۰۲۶-۱۰-۳۰) trial می‌ماند: در دو پروژه از نظر فنی کار کرد، ولی فارسی مدل Local با گوش «مصنوعی» بود و برای تحویل نهایی ElevenLabs انتخاب شد. فقط مدل ۸B روی GPU ابری «خوب» شنیده شد. برای پیش‌نویس و راوی آزمایشی مناسب است.
