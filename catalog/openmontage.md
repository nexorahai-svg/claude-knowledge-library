---
name: OpenMontage
slug: openmontage
category: video
domains: [social-media]
verdict: assess
status: researched
summary: سامانه‌ی تولید ویدیو با عامل: ۱۲ مسیر، کد و مدل‌های تولیدی
url: https://github.com/calesthio/OpenMontage
repo: "https://github.com/calesthio/OpenMontage"
license: "AGPL-3.0"
pricing: free
risk: medium
sources: [S83, S202]
found_in: [batch-05]
last_checked: 2026-10-29
next_check: "2027-01-27"
use_when: "an AI coding agent should plan, gather, voice, caption and render a whole video from one brief ; faceless explainers or stock-footage edits at volume after the simple HyperFrames route works"
how: "git clone calesthio/OpenMontage && make setup, then open the folder in Claude Code; first pin hyperframes in the Makefile (it runs npx --yes hyperframes unpinned) and skip the HeyGen curl|bash line in .agents/skills/media-use; AI clips need paid keys (fal, Veo), free path is stock footage + Piper"
---

# OpenMontage

## چیست
✅ حدود ۶۹.۴ هزار ستاره، ساخته‌شده ۲۰۲۶-۰۳-۲۹، فعال. بدون کلید فقط با کد و فیلم آماده کار می‌کند؛ با کلید اختیاری مدل‌های تولیدی (Kling از fal) و TTS را صدا می‌زند.

## کی استفاده کنیم
🧭 بعد از اینکه مسیر ساده (HyperFrames) کار کرد، برای تولید انبوه‌تر.

## قیمت و مجوز
✅ رایگان؛ کلیدهای API پولی. AGPL فقط اگر آن را به‌صورت سرویس برای دیگران میزبانی کنی مهم است.

## ریسک و هشدار
⚠️ رشد ستاره‌ی خیلی سریع برای سنش؛ کد خوانده نشد ❓.

## بررسی دوباره و خواندن کد (۲۰۲۶-۱۰-۲۹)
از یک ریل فارسی ([S202](../sources/README.md#s202)) که می‌گوید «با یک ریپو و یک پرامپت کل ویدیو را می‌سازد».
- ✅ حدود ۷۲.۹ هزار ستاره، آخرین push ۲۰۲۶-۱۰-۲۸، بی‌نسخه‌ی رسمی (release ندارد)، AGPL-3.0، حجم کلون حدود ۱۶۰ مگابایت.
- ✅ رندر نهایی هم با Remotion (پوشه‌ی `remotion-composer`) و هم با HyperFrames است؛ صدای رایگان محلی Piper ([سند صدا](../domains/social-media/ai-voice.md)).
- ✅ «یک پرامپت» اغراق است: README می‌گوید هر تصمیم خلاقانه تأیید تو را می‌خواهد. کلیپ هوش مصنوعی (Kling، Veo از fal و Google) کلید پولی می‌خواهد؛ مسیر رایگان فوتیج آماده‌ی Pexels و Pixabay (کلید رایگان) + Piper است. هزینه‌ی نمونه‌های README حدود ۱.۳ تا ۴ دلار.
- ⚠️ `make setup` نسخه‌ی HyperFrames را قفل نمی‌کند (`npx --yes hyperframes`)؛ برای ما باید نسخه پین شود.
- ⚠️ اسکیل همراه `.agents/skills/media-use` نصب HeyGen CLI را با `curl … | bash` پیشنهاد می‌دهد؛ اجرا نشود.
- ✅ ردیابی شبکه‌ای (PostHog، Sentry و مانند آن) در کد Python و JS پیدا نشد؛ «telemetry» در `tools/base_tool.py` فقط امتیازدهی داخلی است. کد به سرویس‌های زیادی وصل می‌شود (fal، HeyGen، ElevenLabs، xAI، MiniMax، DashScope و …) فقط اگر کلیدشان را بدهی.
- ❓ اجرا نشد؛ کیفیت خروجی فارسی (راست‌به‌چپ، زیرنویس) آزموده نشده است.
- 🧭 یک پروژه‌ی ویدیوی چهره‌دار آن را کنار گذاشت: برای ویدیوی «خود صاحب کسب‌وکار» با صدای کلون‌شده نمی‌خورد (Piper جای صدای کلون را نمی‌گیرد و زیرنویس و موسیقی را HyperFrames پوشش می‌دهد). جای درستش ویدیوی بی‌چهره (faceless) و توضیحی با فوتیج آماده است؛ همان وقت یک کلیپ کوتاه با زیرنویس فارسی آزموده شود.

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S83](../sources/README.md#s83)
