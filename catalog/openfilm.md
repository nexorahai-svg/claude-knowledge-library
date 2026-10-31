---
name: OpenFilm
slug: openfilm
category: video
domains: [social-media, website]
verdict: assess
status: researched
summary: عامل ویدیوی متن‌باز: هر عامل کدنویس فیلم را به‌صورت یک فایل HTML می‌نویسد و ویرایشگر محلی Studio آن را نشان می‌دهد
use_when: "an AI coding agent should write a whole video as web pages and a human wants a real timeline editor to change it ; compare with HyperFrames and Remotion before choosing a video route"
how: "Read the repo first (rule 4); install is `npx skills add openfilm/openfilm` and the first run downloads a headless Chromium; needs Node 22.2+ and ffmpeg; generated voice, music and video need your own provider keys, so try only the no-key path on a small test"
url: https://github.com/openfilm/openfilm
repo: "https://github.com/openfilm/openfilm"
license: "MIT"
pricing: free
risk: medium
sources: [S208]
found_in: [watch-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# OpenFilm

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و `gh api`) مخزن `openfilm/openfilm`، MIT (فایل LICENSE خوانده شد)، حدود ۳٬۶۵۰ ستاره، ساخته‌شده ۲۰۲۶-۱۰-۰۴، آخرین push همان روز. فیلم یک پوشه با `film.html` است: هر `<section>` یک ترک و هر کلیپ یک صفحه، ویدیو، تصویر یا صدا. هر صفحه تابع `frame(t)` دارد و با هر چیزی که مرورگر بکشد (three.js، canvas، SVG، CSS، GSAP) تصویر آن لحظه را می‌سازد؛ قانونش: یک `t` همیشه یک تصویر بدهد. Studio ویرایشگر محلی در مرورگر Chromium است و خروجی MP4، GIF، صدا، زیرنویس و نیز تایم‌لاین برای Final Cut، Premiere و DaVinci دارد. دستورها: `openfilm open`، `look`، `render` (با `--4k`، `--alpha`)، `get`، `doctor`.
✅ README می‌گوید ساخت، ویرایش و رندر حساب نمی‌خواهد؛ برای صدا، موسیقی، تصویر و ویدیوی تولیدی باید با کلید خودت به سرویس‌ها (ElevenLabs، OpenAI، Google، fal و غیره) وصل شوی. نیاز: Node 22.2 به بالا، ffmpeg و بار اول حدود ۱۰۰ مگابایت Chromium.
❓ کد و تماس‌های شبکه‌ی بسته خوانده نشد. ❓ فونت فارسی و راست‌به‌چپ آزموده نشد. ❓ تفاوت کیفیت با HyperFrames آزموده نشد.

## کی استفاده کنیم
🧭 وقتی می‌خواهیم عامل کدنویس کل ویدیو را بنویسد و انسان با ویرایشگر واقعی روی تایم‌لاین دست ببرد. مقایسه با [HyperFrames](hyperframes.md) و [Remotion](remotion.md) و [OpenMontage](openmontage.md): OpenFilm چارچوب ندارد (یک تابع `frame(t)` کافی است).

## قیمت و مجوز
MIT، رایگان. هزینه فقط از کلیدهای سرویس‌های تولیدی خودت می‌آید.

## ریسک و هشدار
ریسک متوسط: بسته‌ی تازه (چند هفته‌ای)، `npx` آخرین نسخه را می‌گیرد (نسخه را در پروژه ثابت کن)، Chromium دانلود می‌کند و کلید سرویس‌ها را در تنظیمات نگه می‌دارد. پیش از نصب فایل‌ها و تماس‌های شبکه را بخوان؛ کلیدها را فقط با حساب جداگانه و سقف هزینه بده.

## مرتبط
- https://github.com/openfilm/openfilm · https://openfilm.dev
- [S208](../sources/README.md#s208)
