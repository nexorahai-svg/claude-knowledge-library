---
name: yt-dlp
slug: yt-dlp
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: دانلودگر خط فرمان ویدیو و فراداده از یوتیوب، اینستاگرام و صدها سایت؛ نسخه‌ی سیستمی کهنه برای اینستاگرام شکست می‌خورد و نسخه‌ی تازه در venv جواب داد
use_when: "read metadata or formats of a reference reel or video to study its structure ; download your own or licensed footage for editing ; extract frames from a reference clip with ffmpeg for style analysis"
how: "pip install -U yt-dlp inside a venv (never rely on the distro package, it goes stale); yt-dlp -J <url> for metadata; study only, never re-post other people's videos; Instagram may need --cookies-from-browser when it hits the login wall"
url: https://github.com/yt-dlp/yt-dlp
repo: "https://github.com/yt-dlp/yt-dlp"
license: "Unlicense"
pricing: free
risk: low
sources: [S205]
found_in: [batch-24]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# yt-dlp

## چیست
- ✅ دانلودگر متن‌باز ویدیو و فراداده ([مخزن](https://github.com/yt-dlp/yt-dlp)): مجوز Unlicense، حدود ۲۰۳ هزار ستاره، آخرین push در ۲۰۲۶-۱۰-۲۹.
- ✅ آخرین نسخه 2026.10.26 (۲۰۲۶-۱۰-۲۶). در این نسخه پشتیبانی Python 3.10 حذف شد (حداقل 3.11) و فایل‌های اجرایی رسمی ویندوز ۱۰ به بالا می‌خواهند. یادداشت انتشارش تغییری برای اینستاگرام ندارد ([releases](https://github.com/yt-dlp/yt-dlp/releases)).
- 🔬 در کار ریل‌های نمونه (۲۰۲۶-۱۰-۲۸، دسته‌ی ۲۴) نسخه‌ی سیستمی 2025.04.30 برای اینستاگرام خطای «Main webpage is locked behind the login page» داد. نسخه‌ی 2026.10.26 در venv فرمت‌ها را از صفحه‌ی embed گرفت. نتیجه از یک پروژه‌ی واقعی است.
- ✅ issue [#16327](https://github.com/yt-dlp/yt-dlp/issues/16327) با عنوان «Instagram downloads missing audio (music reels)» تا ۲۰۲۶-۱۰-۳۰ هنوز باز است (آخرین به‌روزرسانی ۲۰۲۶-۰۹-۱۲)؛ یعنی ریلزهای دارای موسیقی ممکن است بی‌صدا دانلود شوند. 🧭 اگر دیوار ورود برگشت، راه معمول `--cookies-from-browser` است.

## دستور سریع

**نصب** (✅ [README](https://github.com/yt-dlp/yt-dlp) و PyPI؛ `2026.10.26`، پایتون ≥ 3.11؛ بسته‌ی دیسترو کهنه می‌شود، پس venv):
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install "yt-dlp[default]==2026.10.26"        # extra «default» شامل yt-dlp-ejs است
# ffmpeg و ffprobe (باینری) و برای یوتیوب یک JS runtime مثل deno هم توصیه شده
```
**حداقل اجرا** (✅ README):
```bash
yt-dlp -J --no-playlist "<url>" > info.json                # فقط فراداده، دانلود نمی‌کند
yt-dlp -F "<url>"                                          # فهرست فرمت‌ها
yt-dlp -f "bv*+ba/b" -o "%(id)s.%(ext)s" "<url>"           # دانلود (فقط محتوای خودت یا مجاز)
```
**تنظیم‌های مهم**
- ✅ `-S "res:720,fps"` ترتیب فرمت را عوض می‌کند (هزینه‌ی دانلود و حجم)؛ `--download-sections "*10:15-inf"` فقط یک بازه.
- ✅ `-r 2M` سرعت را محدود می‌کند و `--sleep-interval 10` بین دانلودها مکث می‌دهد (کم‌فشار برای شبکه و سایت).
- ✅ `--cookies-from-browser firefox` فقط وقتی دیوار ورود برگشت (نشست حساب خودت؛ ⚠️ به حساب دسترسی می‌دهد).

**خطاهای رایج**
- 🔬 نسخه‌ی سیستمی کهنه (2025.04.30) برای اینستاگرام «Main webpage is locked behind the login page» داد؛ نسخه‌ی تازه در venv جواب داد.
- ✅ بدون `yt-dlp-ejs` و JS runtime پشتیبانی کامل یوتیوب نیست؛ extra `default` اولی را می‌آورد، دومی را خودت نصب کن.
- ✅ issue [#16327](https://github.com/yt-dlp/yt-dlp/issues/16327): ریلزهای موسیقی‌دار ممکن است بی‌صدا دانلود شوند (باز است). ✅ 2026.10.26 پایتون 3.10 را حذف کرد.

## کی استفاده کنیم
🧭 برای مطالعه‌ی ساختار یک ریل یا ویدیوی مرجع (فراداده، فرمت، فریم با ffmpeg) و دانلود ویدیوی خودت یا ویدیویی که مجوزش را داری. اسکریپت `scripts/fetch_post.py` کتابخانه برای خواندن پست همین کار را ساده‌تر می‌کند.

## ریسک و هشدار
- ⚠️ دانلود و انتشار دوباره‌ی ویدیوی دیگران قانون کپی‌رایت و شرایط پلتفرم‌ها را نقض می‌کند. فقط برای مطالعه.
- ⚠️ استفاده از کوکی مرورگر یعنی دسترسی به نشست حساب. فقط با حساب خودت و با اجازه‌ی صاحب حساب.

## قیمت و مجوز
✅ رایگان، Unlicense.

## مرتبط
[S205](../sources/README.md#s205) · [سبک‌های موشن](../domains/social-media/motion-design-styles.md)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
