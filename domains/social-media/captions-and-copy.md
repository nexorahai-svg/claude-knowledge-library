# زیرنویس و متن پست

> **نوع سند:** دستورالعمل
> **هدف این سند:** زیرنویس فارسی دقیق برای ویدیوی کوتاه بسازیم (فایل برای YouTube، سوخته در ویدیو برای TikTok و Instagram) و کپشن هر شبکه را در حد مجاز بنویسیم.
> **موضوع تحقیق:** Whisper و جایگزین‌ها (faster-whisper، WhisperX، whisper.cpp، OpenAI، Google Chirp، Deepgram، AssemblyAI، ElevenLabs Scribe)، قالب زیرنویس هر شبکه، و نمایش درست فارسی در FFmpeg.
> **منابع:** [S45 گفتار به متن و زیرنویس](../../sources/README.md#s45) · [S43 ابعاد شبکه‌ها](../../sources/README.md#s43) · [S78 مهارت‌های آماده](../../sources/README.md#s78)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۲
> **دفعه‌ی بعد چک شود:** نرخ خطای فارسی Whisper large-v3 و Scribe؛ قیمت و نگهداری داده‌ی سرویس‌های ابری؛ زبان‌های زیرنویس خودکار TikTok.

---

## وقتی متن را خودمان نوشته‌ایم ✅
اگر گفتار از متن خودمان ساخته شده (صدای هوش مصنوعی)، **رونویسی نکن؛ متن را با صدا هم‌تراز کن** ([هم‌ترازی wav2vec2](../../catalog/wav2vec2-xlsr-aligner.md) 🧪). رونویسی خطای خودش را می‌آورد. قواعد طول خط و سرعت خواندن (Netflix)، رندر راست‌به‌چپ آزموده و پذیرش فایل زیرنویس در هر شبکه: [ویدیو از یک پرامپت به هر زبان](multilang-video-pipeline.md). [S136](../../sources/README.md#s136)

## انتخاب ابزار

| ابزار | کجا اجرا می‌شود | فارسی | برچسب زمانی کلمه | مجوز یا قیمت | حکم |
|---|---|---|---|---|---|
| faster-whisper | محلی | همان مدل Whisper (`fa`) ✅ | بله 🧭 | MIT ✅ | ✅ |
| whisper.cpp | محلی، مک و CPU | همان مدل | خروجی مستقیم SRT و VTT ✅ | MIT ✅ | 🧪 |
| WhisperX | محلی | هم‌ترازی فارسی با مدل wav2vec2 ✅ | دقیق‌تر ✅ | BSD-2 ✅ | 🧪 |
| ElevenLabs Scribe | ابری | «Persian (fas)» در رده‌ی دقت بالا (خطا بین ۵ تا ۱۰٪) ✅ | بله ✅ | ساعتی ❓ | 🧪 |
| OpenAI whisper-1 | ابری | Whisper | فقط whisper-1 ✅ | ۰.۰۰۶ دلار هر دقیقه، فایل تا ۲۵ مگابایت ✅ | 👀 |
| Google Chirp | ابری | fa-IR در chirp و chirp_2 (منطقه‌ی asia-southeast1، با علامت‌گذاری خودکار) ✅ | ❓ | ❓ | 👀 |
| Deepgram nova-3 | ابری | `fa` در فهرست رسمی زبان‌ها ✅ | ❓ | طرح pay-as-you-go با ۲۰۰ دلار اعتبار رایگان؛ nova-3 تک‌زبانه حدود ۰.۰۰۷۷ دلار در دقیقه (قیمت فعلی صفحه ۰.۰۰۴۲ هم نشان داده شده) ✅ | 👀 |
| AssemblyAI Universal-2 | ابری | ۹۹ زبان ✅ (Universal-3.5 Pro فقط ۱۸ زبان) | ❓ | ۰.۱۵ دلار در ساعت (Pro: ۰.۲۱) ✅ | 👀 |

- 🧭 پیش‌فرض: **محلی با faster-whisper**؛ داده از کامپیوتر بیرون نمی‌رود. اگر کیفیت فارسی کافی نبود، Scribe را تست کن.
- ✅ README خود Whisper می‌گوید کیفیت بین زبان‌ها خیلی فرق دارد. ❓ عدد خطای فارسی خوانده نشد؛ روی صدای خودمان تست کن.
- ✅ OpenAI برای صدای ضبط‌شده `gpt-transcribe` (۰.۰۰۴۵ دلار هر دقیقه) را پیشنهاد می‌کند، ولی برچسب زمانی کلمه فقط در whisper-1 است.
- ⚠️ diarization در WhisperX توکن Hugging Face و پذیرفتن قرارداد pyannote می‌خواهد. برای ویدیوی تک‌گوینده لازم نیست.

## هر شبکه زیرنویس را چطور می‌گیرد

| شبکه | راه |
|---|---|
| YouTube | ✅ آپلود فایل: SRT، VTT، SBV، TTML و… (VTT جای‌گذاری دارد؛ سبک فقط `<b>`، `<i>`، `<u>`) |
| Instagram | ✅ زیرنویس خودکار Reels قابل روشن و خاموش؛ ❓ آپلود SRT برای پست معمولی پیدا نشد → **بسوزان** |
| TikTok | ✅ زیرنویس خودکار قابل ویرایش؛ ❓ آپلود SRT پیدا نشد و فارسی در فهرست دیده نشد → **بسوزان** |
| تبلیغ Meta | ✅ آپلود SRT با کد زبان در نام فایل (از خلاصه‌ی جستجو) |

## فارسی درست در FFmpeg

- ✅ فیلتر `subtitles` با libass کار می‌کند؛ FFmpeg باید با `--enable-libass` ساخته شده باشد. گزینه‌ی `fontsdir` پوشه‌ی فونت را می‌دهد.
- ✅ libass برای شکل‌دهی درست خط‌های پیچیده HarfBuzz و FriBidi لازم دارد.
- 🧭 دام‌ها:
  - FFmpeg بدون libass یا فونت فارسی پیدانشده → حروف جدا و برعکس.
  - عدد، کلمه‌ی لاتین و علامت در خط فارسی جابه‌جا می‌شوند؛ نمونه را ببین.
  - نیم‌فاصله (U+200C) را هیچ مرحله‌ی تمیزکاری نباید حذف کند.
  - «ی» و «ک» فارسی، نه «ي» و «ك» عربی.
  - فایل SRT با UTF-8.

## روش کار (خط لوله) 🧭

1. صدای تک‌کاناله‌ی ۱۶ کیلوهرتز با FFmpeg جدا کن.
2. با faster-whisper (مدل large-v3، زبان `fa`، برچسب زمانی کلمه) متن بگیر.
3. اختیاری: زمان کلمه‌ها را با WhisperX دقیق‌تر کن.
4. **بازبینی انسانی متن فارسی:** نام‌ها، نیم‌فاصله، ی و ک.
5. کلمه‌ها را در خط‌های ۲ تا ۴ کلمه‌ای گروه کن؛ SRT برای YouTube و ASS برای سوزاندن بساز.
6. با `subtitles` و `fontsdir` بسوزان؛ در منطقه‌ی امن ([ابعاد شبکه‌ها](platform-specs.md)).
7. یک کلیپ نمونه را با چشم چک کن، بعد بقیه.

```bash
ffmpeg -i in.mp4 -ac 1 -ar 16000 audio.wav
ffmpeg -i in.mp4 -vf "subtitles=subs.ass:fontsdir=./fonts" -c:a copy out.mp4
```

## کپشن و هشتگ

| شبکه | حد (✅ از مستندات) |
|---|---|
| Instagram | ۲٬۲۰۰ نویسه، ۳۰ هشتگ، ۲۰ منشن |
| TikTok | ۲٬۲۰۰ نویسه (🧭 از خلاصه‌ی جستجو) |
| YouTube Shorts | عنوان ۱۰۰ نویسه |
| Reels تبلیغاتی | متن اصلی ۴۴ نویسه |

🧭 کپشن را Claude بنویسد، ولی انتشار با تأیید انسان ([انتشار](publishing.md)). جمله‌ی اول قلاب باشد؛ هشتگ کم و مرتبط.

## مهارت آماده برای کپشن اینستاگرام

✅ [Instagram Agent Skill](../../catalog/instagram-agent-skill.md) (MIT، ۱۳ مهارت برای Claude Code): سناریوی ریلز با قلاب امتیازدار، کپشن با بررسی بریده شدن متن در فید، کاروسل، استوری، برنامه‌ی هفتگی، پیش‌نویس پاسخ و پیام. هیچ‌چیز را در Instagram منتشر نمی‌کند و اسکریپت‌هایش تماس شبکه‌ای ندارند.

⚠️ **برای فارسی:** مهارت `ig-human` («انسانی‌کننده») نیم‌فاصله، ZWJ و نشانه‌های جهت را از متن پاک می‌کند. روی متن فارسی اجرایش نکن، یا اول این نویسه‌ها را از فهرست حذفش (`slop.json`) بیرون بیاور. فهرست واژه‌ها و قلاب‌ها هم فقط انگلیسی است؛ برای فارسی فقط ساختار کار به درد می‌خورد.

## پرامپت

```text
Transcribe audio.wav locally with faster-whisper (large-v3, language fa, word timestamps).
Then: keep ZWNJ, convert Arabic ي/ك to Persian ی/ک, group words into lines of 2-4 words
(max 2 lines on screen), and write subs.srt and subs.ass (our Persian font, white text with
a dark outline, positioned above the bottom 35% safe zone). List any words you are unsure
about so I can review them before burning in.
```

## مرتبط

[صداگذاری با هوش مصنوعی](ai-voice.md) · [ویدیو با کد](code-to-video.md) · کارت‌ها: [faster-whisper](../../catalog/faster-whisper.md)، [WhisperX](../../catalog/whisperx.md)، [whisper.cpp](../../catalog/whisper-cpp.md)، [ElevenLabs Scribe](../../catalog/elevenlabs-scribe.md)، [FFmpeg](../../catalog/ffmpeg.md)
