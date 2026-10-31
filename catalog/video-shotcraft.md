---
name: Video Shotcraft
slug: video-shotcraft
category: claude-code-tooling
domains: [social-media, website]
verdict: trial
status: researched
summary: مهارت Claude Code برای ویدیوی محصول سینمایی با Remotion: ۱۵۲ کارت نما، قالب آماده، صدا و موسیقی؛ رندر محلی آزموده شد
use_when: "making a launch or intro video of a client web/desktop product from real screenshots with Remotion"
how: "Trial first on a small task: install the Claude Code plugin (Apache-2.0), copy template/ separately, npm ci --ignore-scripts, REMOTION_DISABLE_TELEMETRY=1 to render; ask for the co-build mode not auto mode for client work; 7 audio files have unknown sources; Remotion licence applies"
url: https://vincentwei1021.github.io/video-shotcraft/
repo: "https://github.com/Vincentwei1021/video-shotcraft"
license: "Apache-2.0 (کد)؛ صداها بیشتر Mixkit؛ Remotion مجوز خودش"
pricing: free
risk: medium
sources: [S130]
found_in: [batch-16]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# Video Shotcraft

## چیست
✅ مهارت و افزونه‌ی Claude Code و Codex (حدود ۱۲٫۷ هزار ستاره، Apache-2.0، ساخته‌شده ۲۰۲۶-۰۷-۱۹، فعال). برای ساختن ویدیوی معرفی محصول وب یا دسکتاپ با [Remotion](remotion.md): کارت‌های «دستور نما» (SKILL.md می‌گوید ۱۲۴، README ۱۵۲)، گالری پیش‌نمایش حرکت، یک قالب کامل آزموده (Ink Press)، ۱۴۹ افکت صوتی و ۵ موسیقی، و خروجی پیش‌نویس برای Jianying. سه حالت: قالب، ساخت آزاد خودکار، ساخت مشترک با تأیید مرحله‌به‌مرحله.
✅ (کد خوانده شد، commit `43bd349`) hook و MCP ندارد؛ اسکریپت‌ها فقط FFmpeg و ffprobe محلی را صدا می‌زنند؛ تماس شبکه‌ای جز پیوندهای مستند نیست.

## آزمون روی رایانه‌ی آزمون (۲۰۲۶-۱۰-۲۱)
✅ قالب (`template/`) را جدا کپی کردیم، `npm ci --ignore-scripts` (۱۸۷ بسته، ۵ ثانیه)، و با `REMOTION_DISABLE_TELEMETRY=1` رندر: ویدیوی ۳۶ ثانیه‌ای ۱۹۲۰×۱۰۸۰، h264 با صدای aac، در ۳۳ ثانیه روی CPU ۲۴ هسته‌ای. فریم‌ها درست بودند (متن، صفحه‌ی محصول، حرکت دوربین ۲٫۵بعدی).

## کی استفاده کنیم
🧭 ویدیوی لانچ یا معرفی سایت و اپ مشتری از روی تصویر واقعی صفحه‌ها. کنار [ویدیو با کد](../domains/social-media/code-to-video.md).

## قیمت و مجوز
✅ کد Apache-2.0. ⚠️ Remotion 4.0.484 قفل شده و [مجوز Remotion](remotion.md) (رایگان تا ۳ نفر) جدا صدق می‌کند. ⚠️ (assets/audio/ATTRIBUTION.md) بیشتر صداها Mixkit Free License (تجاری بی‌نیاز به ذکر نام)، ولی **۷ فایل منبع نامعلوم دارند** و خود فایل می‌گوید «پیش از استفاده‌ی تجاری تأیید شود»: `keyboard`، `pop`، `riser-cine`، `sparkle`، `whoosh-big`، یک افکت دیگر و موسیقی `bgm-tech-house`. این‌ها را در کار مشتری نگذار.

## ریسک و هشدار
⚠️ حالت «ساخت آزاد خودکار» بی‌توقف تا ویدیوی نهایی جلو می‌رود؛ برای کار مشتری حالت «ساخت مشترک» را بخواه. ⚠️ متن‌ها و توضیحات بیشتر چینی است. ⚠️ پوشه‌ی کامل ۱۱۹ مگابایت است.

## مرتبط
[Remotion](remotion.md) · [ویدیو با کد](../domains/social-media/code-to-video.md) · [کتابخانه‌ی صدا](../domains/social-media/sound-library.md) · [S130](../sources/README.md#s130) · دسته‌ی ۱۶
