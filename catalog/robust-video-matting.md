---
name: RobustVideoMatting (RVM)
slug: robust-video-matting
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: جداسازی سوژه از پس‌زمینه‌ی ویدیو به‌صورت محلی و رایگان؛ روی GPU هشت‌گیگی کار کرد؛ مجوز GPL-3.0؛ مخزن از ۲۰۲۴ تغییر نکرده است
use_when: "text behind the speaker in a talking-head reel ; a separate background or a smaller subject on black ; rim light around a silhouette ; matting a clip locally with no paid API"
how: "Run rvm_mobilenetv3 on an image sequence with downsample_ratio 0.25 in a venv with torch pinned; merge the alpha with ffmpeg alphamerge into VP9 yuva420p (-auto-alt-ref 0), because output_foreground has no alpha; two video layers in HyperFrames with text between them; matte only people who consented"
url: https://github.com/PeterL1n/RobustVideoMatting
repo: "https://github.com/PeterL1n/RobustVideoMatting"
license: "GPL-3.0"
pricing: free
risk: medium
sources: [S211]
found_in: [experience-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# RobustVideoMatting (RVM)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) مخزن از ۲۰۲۴-۰۴ بی‌تغییر، بایگانی نشده، GPL-3.0؛ هشدارهای کارت کافی است. ❓ شرط وزن‌های مدل جدا سنجیده نشد.
- ✅ مخزن [PeterL1n/RobustVideoMatting](https://github.com/PeterL1n/RobustVideoMatting): مجوز GPL-3.0، حدود ۹٫۶ هزار ستاره، آخرین push در ۲۰۲۴-۰۴-۰۲، بایگانی نشده.
- 🔬 (۲۰۲۶-۱۰-۳۰، RTX 4060 هشت‌گیگی، مدل mobilenetv3 با وزن ۱۵ مگابایت، دفتر پروژه‌ها) ۲۸۹ فریم 1080×1920 در ۱۴۳ ثانیه (۲ فریم در ثانیه) با `downsample_ratio 0.25` و `seq_chunk 4`، با لبه‌ی تمیز روی لباس سفید و کلیپ ساخته‌ی Kling.

## دستور سریع

**نصب** (✅ [README](https://github.com/PeterL1n/RobustVideoMatting) و 🔬 آزمون ما: commit `53d74c6`؛ `requirements_inference.txt` مخزن `torch==1.9.0` می‌خواهد که کهنه است، پس torch را خودت در venv پین کن):
```bash
git clone --depth 1 https://github.com/PeterL1n/RobustVideoMatting && cd RobustVideoMatting
python3 -m venv .venv && . .venv/bin/activate
pip install torch==2.8.0 torchvision==0.23.0 tqdm pillow   # 🔬 ترکیبی که کار کرد (cu128)
curl -LO https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3.pth   # حدود ۱۵ مگابایت
```
**حداقل اجرا** (✅ امضای تابع از مستند inference مخزن؛ اینجا اجرا نشد؛ `requirements_inference.txt` را نصب نکن، اگر ناچار شدی با `--no-deps`):
```python
import torch
from model import MattingNetwork
from inference import convert_video
m = MattingNetwork('mobilenetv3').eval().cuda()
m.load_state_dict(torch.load('rvm_mobilenetv3.pth'))
convert_video(m, input_source='frames_dir_or_in.mp4', output_type='png_sequence', output_composition='out/com',
              output_alpha='out/pha', output_foreground='out/fgr', downsample_ratio=0.25, seq_chunk=4)
```
**تنظیم‌های مهم**
- ✅ `downsample_ratio` را طوری بگذار که اندازه‌ی کوچک‌شده بین ۲۵۶ و ۵۱۲ بیفتد (۱۰۸۰×۱۹۲۰ با `0.25` ← ۲۷۰×۴۸۰ درست است)؛ بالاتر همیشه بهتر نیست.
- 🔬 روی RTX 4060 (۸ گیگ) `seq_chunk=4` با mobilenetv3: ۲۸۹ فریم ۱۰۸۰×۱۹۲۰ در ۱۴۳ ثانیه (حدود ۲ فریم در ثانیه)؛ README پیش‌فرض `12` را می‌گذارد، اگر حافظه کم آمد پایین بیاور.
- ✅ مدل بازگشتی است: فریم‌ها را **پشت‌سرهم** بده؛ پردازش جدا جدا کیفیت را می‌شکند.

**خطاهای رایج**
- ⚠️ `output_foreground` آلفا ندارد؛ کدر انکود می‌شود. 🔬 آلفا را با `ffmpeg alphamerge` ترکیب کن و به VP9 `yuva420p -auto-alt-ref 0` بده ([روش](../domains/social-media/motion-design-styles.md)).
- 🔬 `inference_utils` به `av` و `pims` وابسته است؛ برای دنباله‌ی تصویر با try/except رد شد.
- ⚠️ مخزن از ۲۰۲۴ تکان نخورده و GPL-3.0 است؛ فقط با رضایت صاحب چهره ماتینگ کن.

## کی استفاده کنیم
🧭 متن پشت سوژه، پس‌زمینه‌ی جدا و هاله‌ی دور سیلوئت در ریل چهره‌دار. روش کامل در [سبک‌های موشن](../domains/social-media/motion-design-styles.md).

## قیمت و مجوز
✅ رایگان، GPL-3.0. 🧭 اگر خود کد را داخل محصولی بگذاری که توزیع می‌شود، GPL شامل آن می‌شود. استفاده به‌عنوان ابزار جدا برای ساخت ویدیو این مشکل را ندارد.

## ریسک و هشدار
- ⚠️ مخزن نگهداری فعال ندارد؛ `torch` و `torchvision` را پین کن و بدون `--no-deps` نصب نکن.
- ⚠️ `output_foreground` آلفا ندارد؛ انکود مستقیم آن ویدیوی کاملاً کدر می‌دهد. آلفا را جدا با `alphamerge` ترکیب کن.
- 🔬 `inference_utils` به `av` و `pims` وابسته است؛ برای دنباله‌ی تصویر با try/except رد شد.
- ⚠️ جداسازی چهره‌ی افراد فقط با رضایت خودشان.

## مرتبط
[S211](../sources/README.md#s211) · [HyperFrames](hyperframes.md)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.

🔬 (۲۰۲۶-۱۰-۳۱) ۱۵۰ فریم 720×1280 در ۳۱ ثانیه (۴٫۸ فریم در ثانیه). سوژه یعنی کل جسم: پا با جوراب و کفش یک‌جا جدا می‌شود؛ برای فقط پوست، فیلتر رنگ کافی نیست: سه نسخه‌ی HSV شکست خورد، چون سایه‌ی پوست از جوراب سیاه با رنگ جدا نمی‌شود. برای زیرناحیه‌ی بدن از ماسک معنایی مثل SAM 2 با کلیک مثبت و منفی استفاده کن که در همان پروژه جواب داد ([Barty](barty-motion-graphics.md)). برگه‌ی زوم ۴۸۰ پیکسلی با روکش قرمز ایراد ماسک را فوری نشان می‌دهد؛ برگه‌ی ۳۶۰ پیکسلی آن را پنهان کرد.
