---
name: Motion Graphics Skill Pack (Charlie Hills)
slug: motion-graphics-skills
category: video
domains: [social-media]
verdict: trial
status: researched
summary: بسته‌ی رایگان MIT با ۱۵ اسکیل Claude Code برای موشن‌گرافیک با کد (ویدیوی معرفی، نمودار متحرک، تیتراژ سه‌بعدی، ریل)؛ رندر MP4 با HyperFrames؛ بدون پشتیبانی فارسی یا راست‌به‌چپ
use_when: "a launch film, animated chart, 3D title or reel export where a ready brief and scene structure saves time ; learning how to write a motion brief before building with HyperFrames ; a template for packaging each effect as its own skill"
how: "Read the SKILL.md first; copy only the skills you need into the project's .claude/skills instead of the global folder; pin HyperFrames in the project because the skills call npx hyperframes render unpinned; brand-intake adds a block to CLAUDE.md, so review it; test Persian text yourself, the pack has no RTL guidance"
url: https://github.com/charlie947/motion-graphics-skills
repo: "https://github.com/charlie947/motion-graphics-skills"
license: "MIT"
pricing: free
risk: low
sources: [S209]
found_in: [reel-visualflow-ai-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Motion Graphics Skill Pack (Charlie Hills)

## چیست
- ✅ مخزن [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills): مجوز MIT، حدود ۴۸۵ ستاره، ساخت ۲۰۲۶-۰۹-۲۶، آخرین push در ۲۰۲۶-۱۰-۱۱، کار یک نفر. توضیح مخزن هنوز «۱۳ اسکیل» می‌گوید، README «۱۵» و جدول آن «چهارده»؛ پوشه‌ی `skills/` واقعاً ۱۵ اسکیل دارد.
- ✅ اسکیل‌ها: `brand-intake`، `motion-brief-writer`، `reference-to-motion`، `motion-prompt-writer`، `launch-video`، `apple-launch-film`، `vox-explainer`، `animated-chart`، `milestone-reveal`، `motion-effects`، `title-sequence-3d`، `model-showdown`، `newsletter-promo`، `loop-cover` و `reel-export`.
- ✅ خود اسکیل‌ها بیشتر دستورالعمل و پرامپت‌اند. انیمیشن را Claude با کد می‌نویسد و خروجی MP4 با [HyperFrames](hyperframes.md) ساخته می‌شود: `npx skills add heygen-com/hyperframes`، بعد `npx hyperframes render`.
- ✅ در اسکیل‌ها و پرامپت‌ها هیچ اشاره‌ای به فارسی، عربی یا راست‌به‌چپ نیست (جست‌وجو در متن).
- 🔬 (۲۰۲۶-۱۰-۳۱، یک آزمون ۶ ثانیه‌ای، دفتر پروژه‌ها) دستور `motion-effects` برای تایپ فارسی و عربی به‌عنوان بریف جواب داد: حروف با `clip-path` روی کل کلمه چسبیده ماندند و ماسک راست‌به‌چپ درست بود. ریل کامل آزموده نشد.

## ریسک و هشدار
- ✅ کد خوانده شد (`229022e`): ۲۲ فایل متنی، یک اسکریپت بررسی ساختار (`validate-skills.sh`) و دو zip که هر کدام فقط یک `SKILL.md` دارند. hook، MCP، ردیاب، کلید API و `curl | bash` ندارد. نشانی‌های بیرونی فقط خبرنامه‌ی نویسنده، GitHub، 21st.dev و LinkedIn‌اند.
- ⚠️ `npx hyperframes render` پین نیست؛ در هر پروژه نسخه را ثابت کن (قانون کاربر).
- ⚠️ `brand-intake` یک بلوک به `CLAUDE.md` پروژه اضافه می‌کند. پیش از اجرا متن آن را بخوان.
- ⚠️ `apple-launch-film` ظاهر اپل و `vox-explainer` سبک Vox را تقلید می‌کنند؛ برای کار تجاری مشتری، نام و نشان برند دیگری را به‌کار نبر (🧭).
- یک اسکیل دیگر پیشنهاد می‌کند `emilkowalski/skills` را نصب کنی که شخص ثالث است و اینجا خوانده نشد ❓.

## کی استفاده کنیم
👀 هنوز آزموده نشده. کاربردش بیشتر ساختار بریف و صحنه است. HyperFrames که خودش اسکیل‌های رسمی `motion-graphics`، `product-launch-video` و `faceless-explainer` دارد، از قبل روی رایانه نصب است. برای الگوی «هر افکت یک اسکیل» هم نمونه‌ی خوبی است ([سبک‌های موشن](../domains/social-media/motion-design-styles.md)).

## قیمت و مجوز
✅ رایگان، MIT. هزینه‌ی مصرف Claude جداست.

## ادعاهای ریل (۲۰۲۶-۱۰-۳۰)
ریل @visualflow_ai ([S209](../sources/README.md#s209)) می‌گوید «۱۳ اسکیل رایگان؛ موشن‌دیزاینر حرفه‌ای بی‌نیاز از After Effects». ✅ رایگان و کدنویسی و رندر MP4 درست است. نام پک، نویسنده و مخزن در پست نیامده و لینک پشت کامنت است، ولی مخزن عمومی است و نیازی به کامنت نیست. «فقط بگو چی می‌خوای» اغراق است؛ کیفیت به بریف و بازبینی شما بستگی دارد (🧭).

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
