---
name: هم‌ترازی متن و صدا با wav2vec2 XLSR-53
slug: wav2vec2-xlsr-aligner
category: audio-voice
domains: [social-media]
verdict: adopt
status: researched
summary: زمان دقیق هر کلمه‌ی متنی که داریم، روی صدا؛ فارسی، عربی، انگلیسی و ۹ زبان دیگر، Apache-2.0
use_when: "aligning known text to audio for word-level subtitles in Persian, Arabic or other languages ; multilingual video pipeline"
how: "use jonatasgrosman/wav2vec2-large-xlsr-53-<lang> (Apache-2.0) with torchaudio.functional.forced_align (our tests used torchaudio 2.8; it is still in 2.11); snap word starts after pauses with FFmpeg silence detection; do NOT use PyPI ctc-forced-aligner (non-commercial MMS)"
url: https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-persian
repo: ""
license: "Apache-2.0 (مدل‌ها)؛ torchaudio BSD"
pricing: free
risk: low
sources: [S136]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-22"
---

# هم‌ترازی اجباری با wav2vec2 XLSR-53

## چیست
✅ مدل‌های CTC `jonatasgrosman/wav2vec2-large-xlsr-53-<زبان>` (فارسی، عربی، انگلیسی، آلمانی، فرانسوی، اسپانیایی، روسی، چینی، ژاپنی، ایتالیایی، پرتغالی، هلندی) همه با مجوز Apache-2.0 (کارت Hugging Face، ۲۰۲۶-۱۰-۲۲)، با حروف خود زبان. با `torchaudio.functional.forced_align` متن معلوم روی صدا هم‌تراز می‌شود. WhisperX هم برای fa و ar همین مدل‌ها را بار می‌کند ✅.

## دستور سریع

**نصب** (✅ [کارت مدل](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-persian)، Apache-2.0، وزن حدود `1.26 GB`؛ 🔬 آزمون ما روی torchaudio 2.8):
```bash
pip install torch==2.8.0 torchaudio==2.8.0 transformers
ffmpeg -i voice.mp3 -ar 16000 -ac 1 -f wav voice16k.wav       # ✅ مدل ورودی ۱۶ کیلوهرتز می‌خواهد
```
**حداقل اجرا** (✅ اسکلت از کارت مدل و [آموزش رسمی torchaudio](https://github.com/pytorch/audio/blob/main/examples/tutorials/ctc_forced_alignment_api_tutorial.py)؛ اینجا اجرا نشد):
```python
import torch, torchaudio.functional as F
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
mid = "jonatasgrosman/wav2vec2-large-xlsr-53-persian"
proc, model = Wav2Vec2Processor.from_pretrained(mid), Wav2Vec2ForCTC.from_pretrained(mid).eval()
with torch.inference_mode():                      # wav: float32 تک‌کانال ۱۶k
    emission = torch.log_softmax(model(proc(wav, sampling_rate=16000, return_tensors="pt").input_values).logits, -1)
ids = proc.tokenizer(text).input_ids              # فاصله‌ها به «|» می‌روند؛ blank = pad = 0
path, scores = F.forced_align(emission, torch.tensor([ids], dtype=torch.int32), blank=0)
spans = F.merge_tokens(path[0], scores[0].exp())  # زمان هر نویسه؛ نویسه‌ها را به کلمه (جداکننده «|») جمع کن
```
**تنظیم‌های مهم**
- ✅ ورودی باید ۱۶ کیلوهرتز باشد (کارت مدل)؛ تبدیل را خودت با ffmpeg انجام بده.
- 🔬 چسباندن آغاز کلمه‌ی کش‌آمده به آغاز گفتار بعد از مکث دست‌کم `0.2 s` با `silencedetect` ffmpeg دقت را بالا برد.
- 🧭 روی CPU برای صدای کوتاه (زیر چند دقیقه) کافی است؛ مدل را یک‌بار بار کن و برای همه‌ی خطوط به‌کار ببر.

**خطاهای رایج**
- ⛔ `ctc-forced-aligner` از PyPI را برای کار مشتری نیاور: مدل پیش‌فرضش MMS با مجوز غیرتجاری (CC-BY-NC) است.
- 🔬 رقم و کلمه‌ی لاتین در واژگان مدل نیستند (واژگان ۶۷ نویسه)؛ متن را پیش از هم‌ترازی نرمال کن یا زمانشان را از همسایه‌ها درون‌یابی کن.
- ⚠️ ادعای کارت «`forced_align` در 2.9 حذف می‌شود» با منبع نمی‌خواند: در درخت منبع `v2.9.0`، `v2.10.0` و `v2.11.1` هنوز هست و یادداشت 2.9 می‌گوید «در حال حفظ آن‌ایم». ما فقط روی 2.8 آزموده‌ایم؛ ارتقا را با آزمون دوباره بپذیر (`torchaudio.load` در 2.9 به TorchCodec رفته).

## تجربه 🔬
🔬 در [خط تولید ویدیوی چندزبانه](../domains/social-media/multilang-video-pipeline.md) (دفتر پروژه‌ها): حدود ۶۰ خط کد. وقتی صدا کلمه‌ای را کش می‌دهد، آغاز آن دیر می‌افتد؛ چسباندن به آغاز گفتار بعد از مکث دست‌کم ۰٫۲ ثانیه آن را با سکوت‌سنج FFmpeg یکی کرد. رقم و کلمه‌ی لاتین درون فارسی در واژگان مدل نیستند؛ زمانشان از همسایه‌ها درون‌یابی می‌شود.

## ریسک و هشدار
✅ (اصلاح ۲۰۲۶-۱۰-۳۱) `forced_align` در torchaudio حذف نشده و در `v2.9.0` و `v2.11.0` هم هست. ادعای قبلی این کارت نادرست بود. 🔬 آزمون ما روی 2.8 بوده است. ⛔ بسته‌ی PyPI `ctc-forced-aligner` 1.0.2 شاخه‌ای دیگر با مدل پیش‌فرض غیرتجاری (MMS، CC-BY-NC) است؛ آن را برای کار مشتری نیاور.

## مرتبط
[ویدیو از یک پرامپت به هر زبان](../domains/social-media/multilang-video-pipeline.md) · [زیرنویس و متن](../domains/social-media/captions-and-copy.md) · [WhisperX](whisperx.md) · [S136](../sources/README.md#s136)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
