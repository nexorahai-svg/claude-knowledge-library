---
name: video-use (browser-use)
slug: video-use
category: video
domains: [social-media]
verdict: trial
status: researched
summary: مهارت Claude Code برای تدوین فیلم خام: حذف مکث و «اِ»، رنگ، زیرنویس، انیمیشن با HyperFrames/Remotion؛ ولی متن‌برداری فقط با ElevenLabs Scribe پولی و زیرنویس پیش‌فرض لاتین
use_when: "editing raw talking-head footage (product intro, tutorial, interview) into reels"
how: "Trial first on a small task: put raw clips in a folder, run claude there and describe the edit (output edit/final.mp4); needs an ElevenLabs key and sends audio to ElevenLabs so get client permission; default captions are Latin caps so use our own Persian RTL pipeline; test one short English clip first"
url: https://video-use.com
repo: "https://github.com/browser-use/video-use"
license: "MIT"
pricing: freemium
risk: medium
sources: [S143]
found_in: [x-yarad_ai-2026-10-23]
last_checked: 2026-11-01
next_check: "2027-01-30"
---

# video-use (browser-use)

## چیست
✅ (README، `helpers/`، ۲۰۲۶-۱۰-۲۳) یک **مهارت** (فایل SKILL.md و چند اسکریپت پایتون)، نه برنامه یا پلاگین. فیلم‌های خام را در یک پوشه می‌گذاری، در همان پوشه `claude` را باز می‌کنی و می‌گویی چه می‌خواهی. خروجی `edit/final.mp4` است. شرکت browser-use آن را ساخته؛ حدود ۲۹٬۶۰۰ ستاره؛ آخرین تغییر ۲۰۲۶-۱۰-۰۸.

**روش کار:** مدل فیلم را نمی‌بیند، **می‌خواند**. صدای هر فایل یک بار به ElevenLabs Scribe فرستاده می‌شود و برمی‌گردد: زمان هر کلمه، گوینده‌ها و رویدادهایی مثل خنده. همه در یک متن حدود ۱۲ کیلوبایتی جمع می‌شود. فقط سر تصمیم‌ها یک تصویر نوار فیلم و موج صدا ساخته می‌شود. Claude فهرست برش (EDL) می‌نویسد، FFmpeg می‌سازد، و بعد خودش خروجی را سر هر برش بررسی می‌کند (حداکثر ۳ بار اصلاح). پیش از برش، روش کار را از کاربر تأیید می‌گیرد. حافظه‌ی پروژه در `project.md` می‌ماند.

## ادعاهای پست در برابر منبع
- ⚠️ پست آن را «رایگان» گفته. کد MIT و رایگان است، ولی **متن‌برداری فقط با کلید ElevenLabs** کار می‌کند (`helpers/transcribe.py`، مدل `scribe_v1`)؛ هزینه‌ی هر دقیقه و **فرستادن صدای فیلم به سرور ElevenLabs** را در نظر بگیر. برای فیلم مشتری اجازه لازم است.
- ⚠️ زیرنویس پیش‌فرض: دو کلمه‌ی **حروف بزرگ** با فونت Helvetica (`render.py`). برای فارسی و عربی مناسب نیست؛ شیوه‌ی زیرنویس [خط تولید ویدیوی ما](../domains/social-media/multilang-video-pipeline.md) (Vazirmatn، راست‌به‌چپ، libass) باید جایش بیاید.
- ✅ HyperFrames و Remotion برای انیمیشن روی فیلم استفاده می‌شوند، و هر انیمیشن در یک زیرعامل موازی ساخته می‌شود.

## کی استفاده کنیم
🧪 برای **فیلم خام گوینده** (معرفی محصول، آموزش، مصاحبه) به ریلز. مکمل خط تولید خودمان است: آن یکی از یک پرامپت ویدیو **می‌سازد**، این یکی فیلم واقعی را **تدوین** می‌کند. آزمون اول: یک فیلم انگلیسی کوتاه. برای فارسی دو چیز باید جدا آزموده شود: دقت Scribe روی فارسی ❓، و اینکه بشود متن‌برداری را با faster-whisper محلی عوض کرد. نصب از روی `install.md` (clone، `uv sync`، symlink در `~/.claude/skills/`)؛ ⚠️ پیش از نصب SKILL.md و helpers را بخوان. پرامپت نصب README نصب Homebrew را فرض می‌کند؛ روی لینوکس FFmpeg از apt.

## قیمت و مجوز
✅ کد MIT. هزینه: Scribe در ElevenLabs (طبق طرح ElevenLabs) و سهمیه‌ی Claude. نسخه‌ی ابری (video-use.com) هنوز فهرست انتظار است.

## مرتبط
[خط تولید ویدیوی چندزبانه](../domains/social-media/multilang-video-pipeline.md) · [HyperFrames](hyperframes.md) · [ElevenLabs](elevenlabs-tts.md)
