---
name: ffmpeg-skill
slug: ffmpeg-skill
category: video
domains: [social-media, claude-code]
verdict: trial
status: researched
summary: مهارت و سرور MCP برای ویرایش ویدیو با FFmpeg محلی: برش، حذف سکوت، زیرنویس، تناسب ۹:۱۶
use_when: "cutting, captioning and reformatting short videos (reels/shorts) locally with an agent"
how: "npx ffmpeg-skill (inspect bin/install.js first) or copy SKILL.md; needs ffmpeg + python3 on PATH"
url: https://github.com/kajisho5/ffmpeg-skill
repo: "https://github.com/kajisho5/ffmpeg-skill"
license: "MIT"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# ffmpeg-skill

## چیست
✅ مهارت عامل و سرور MCP برای ویرایش ویدیو با FFmpeg/ffprobe محلی (برش، حذف سکوت، کپشن، تناسب ۹:۱۶، لودنس، HDR به SDR)؛ MIT. ✅ زیرنویس عربی و راست‌به‌چپ تأیید شد (libass و fribidi)؛ ❓ فارسی و نیم‌فاصله (ZWNJ) در مستندات نیامده. ❓ ادعای «۴۲ ابزار» و «بدون شبکه» تأیید نشد.

## دستور سریع

**نصب** (✅ [README](https://github.com/kajisho5/ffmpeg-skill)؛ npm `2.22.1`؛ ⚠️ `npx` فایل `bin/install.js` را اجرا می‌کند، اول بخوانش؛ هنوز trial و نیازموده):
```bash
sudo apt install ffmpeg                         # FFmpeg ≥ 6.1 و Python ≥ 3.10 توصیه شده
npx ffmpeg-skill@2.22.1 --project               # فقط همین پروژه: ./.claude/skills/ffmpeg-skill
npx ffmpeg-skill@2.22.1 doctor
```
**حداقل اجرا** (✅ README؛ `--dry-run` فقط برنامه را چاپ می‌کند):
```bash
S=./.claude/skills/ffmpeg-skill/scripts
python3 $S/probe.py in.mp4 --compact
python3 $S/fit.py in.mp4 --duration 60 --aspect 9:16 --dry-run
python3 $S/export.py in.mp4 --preset reels --json
```
**تنظیم‌های مهم**
- ✅ `render.py FILE --template reels|tiktok|shorts` یک ویرایش را برای هر مقصد با ناحیه‌ی امن تحویل می‌دهد (مثلاً الگوی `tiktok`: ۹:۱۶ و `-14 LUFS`)؛ اول `--dry-run`.
- ✅ `export.py --fast`: در جدول README برای یک بخش ۱۰ دقیقه‌ای حدود `3.7×` زمان واقعی در برابر `1.2×` برای `medium` (دستگاه آنها، نه ما).
- ✅ `--timeout` پیش‌فرض `1800` ثانیه است؛ ویدیوی یک‌ساعته‌ی کامل با آن کشته شد. MCP به‌طور پیش‌فرض ۱۲ ابزار هسته را نشان می‌دهد؛ `FFMPEG_SKILL_MCP_FULL=1` همه را (README می‌گوید ۴۲، شمارش مستقل نکردیم).

**خطاهای رایج**
- ✅ `doctor` اگر یک فیلتر (مثل `subtitles` / libass) نباشد `ok=false` می‌دهد حتی وقتی بیشتر ابزارها کار می‌کنند؛ فیلد `tools` را بخوان.
- ✅ زیرنویس از گفتار موتور محلی جدا می‌خواهد (`pip install faster-whisper`، بار اول مدل دانلود می‌شود). ❓ فارسی و نیم‌فاصله در README نیامده؛ پیش از تحویل چشمی ببین.
- ✅ فایل خروجی موجود بدون `--overwrite` رد می‌شود؛ اسکریپت‌ها ffmpeg را با subprocess اجرا می‌کنند (شبکه در مسیرهای خوانده‌شده پیدا نشد، کد کامل خوانده نشد).

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: cutting, captioning and reformatting short videos (reels/shorts) locally with an agent. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۴,۰۶۲ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ❓ ۴.۱ هزار ستاره در ۲ ماه؛ رشد سریع مستقل بررسی نشد.
- ⚠ نصب با npx فایل bin/install.js را اجرا می‌کند؛ ابتدا بخوانید.
- اسکریپت‌ها subprocess برای ffmpeg اجرا می‌کنند؛ در مسیرهای scripts/mcp/bin کدی برای شبکه پیدا نشد (خوانش کامل نبود).
- اسکریپت‌ها subprocess برای ffmpeg اجرا می‌کنند؛ در scripts/mcp/bin مورد urllib/socket پیدا نشد؛ نصب npx اسکریپت اجرا می‌کند.
- ❓ bin/install.js و ابزارها خط‌به‌خط خوانده نشد؛ ادعای ۴۲ ابزار شمارش نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/kajisho5/ffmpeg-skill

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
