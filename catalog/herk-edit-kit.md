---
name: Herk Edit Kit
slug: herk-edit-kit
category: video
domains: [social-media]
verdict: assess
status: researched
summary: کیت تدوین با Claude Code و Codex بر پایه‌ی HyperFrames: تدوین از روی متن گفتار، حذف مکث و کلیپ کوتاه؛ برخی کارها کلید پولی می‌خواهد
use_when: "cutting a talking-head video by editing its transcript ; removing pauses ; turning a long video into short clips"
how: "Works with local Whisper instead of paid Scribe; it pins hyperframes 0.7.109, far behind our version; read AGENTS.md and CLAUDE.md before opening the repo in a session"
url: https://github.com/nateherkai/herk-edit-kit
repo: "https://github.com/nateherkai/herk-edit-kit"
license: "MIT"
pricing: freemium
risk: medium
sources: [S214]
found_in: [x-yarad-ai-2026-10-30]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Herk Edit Kit

## چیست
- ✅ مخزن با متن مجوز MIT در فایل LICENSE (API گیت‌هاب NOASSERTION نشان می‌دهد؛ پوشه‌ی `licenses/` هم دارد ❓)، حدود ۲٫۴ هزار ستاره، آخرین push در ۲۰۲۶-۱۰-۱۴.
- ✅ README: نویسنده از ElevenLabs Scribe و Kie.ai استفاده می‌کند، ولی Whisper محلی جایگزین است و نمونه‌ی محلی کلید پولی نمی‌خواهد.
- 👀 آزموده نشده. ما خودمان [faster-whisper](faster-whisper.md) و HyperFrames را داریم.

## ریسک و هشدار
- ⚠️ `hyperframes 0.7.109` در `package.json` پین است و با نسخه‌ی ما خیلی فاصله دارد.
- ⚠️ کلیدهای چند سرویس را می‌پذیرد؛ کلید را در مخزن نگذار. کلمه‌ی telemetry در یک اسکیل هست و بررسی نشد ❓.

## مرتبط
[سبک‌های موشن](../domains/social-media/motion-design-styles.md) · [S214](../sources/README.md#s214)
