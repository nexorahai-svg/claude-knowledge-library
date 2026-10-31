---
name: Ootto content skills
slug: ootto-content-skills
category: claude-code-tooling
domains: [social-media, claude-code, security]
verdict: hold
status: researched
summary: مجموعه‌ی مهارت محتوا و ویرالیتی ریل اینستاگرام با «کارخانه‌ی محتوا» (روزی ۳ پست) و پاسخ خودکار کامنت و DM؛ استفاده نکن
use_when: "only to read the hook and virality checklists as study material, not to run the pipeline"
how: "Do not install or run content-factory or comment-responder; use ig-reel, ig-caption and ig-plan skills with manual posting instead"
url: https://github.com/Ootto-AI/claude-content-skills
repo: "https://github.com/Ootto-AI/claude-content-skills"
license: "MIT"
pricing: free
risk: high
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# Ootto content skills

## چیست
- ✅ مخزن https://github.com/Ootto-AI/claude-content-skills؛ MIT؛ حدود ۳۰۹ ستاره؛ آخرین push ۲۰۲۶-۱۰-۱۷؛ نسخه‌ی رسمی ندارد.
- ✅ README: حدود ۳۰ مهارت (Content Factory، Virality، AI Brain، Reel Analyzer، Hook، Caption، Calendar، Comment Responder، DM Script...). Content Factory کل خط را اجرا می‌کند و «۳ بار در روز» تکرار می‌کند.
- ✅ مهارت Agent Reach را از Panniantong/Agent-Reach همراه خود دارد (ریسک آن در [Agent-Reach](agent-reach.md) آمده).
- ✅ Comment Responder به هر کامنت پاسخ عمومی می‌دهد و منبع را در DM می‌فرستد، «۲۴ ساعته».
- ✅ README تبلیغ محصول پولی خودشان (Ootto autopilot) است. ❓ «۳٫۵ میلیون بازدید / ۲۶۲ پست» ادعای خود سازنده است و راستی‌آزمایی نشد.

## ریسک و هشدار
- ⚠️ 🧭 پاسخ و DM خودکار انبوه اینستاگرام خطر محدود شدن حساب و برچسب اسپم دارد.
- ⚠️ ✅ کار با اسکرپینگ و دانلود از اینترنت و `install.sh` و `mine_hooks.py` (کد اجرایی)، که خوانده نشد (❓).
- 🧭 محتوای تولیدشده‌ی انبوه بدون بازبینی انسانی با قواعد کتابخانه (بازبینی و لحن خودمان) نمی‌خواند.

## کی استفاده کنیم
⛔ نه. فقط چک‌لیست قلاب/virality را می‌شود برای مطالعه خواند (بدون کپی متن‌ها).

## قیمت و مجوز
✅ رایگان، MIT؛ هدف تجاری آن فروش سرویس Ootto است.

## مرتبط
غربال · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S165](../sources/README.md#s165)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ `install.sh` و `mine_hooks.py` کامل خوانده شد (SHA `c79c330`). `install.sh` فقط مهارت‌ها را در `~/.claude/skills` کپی می‌کند. `mine_hooks.py` فقط یک CSV محلی را پردازش می‌کند و شبکه ندارد.
- ⚠️ مهارت `agent-reach` می‌گوید دستور نصب را از مخزن شخص ثالث Panniantong/agent-reach بخوانی و دنبال کنی. آن را دنبال نکن (کارت [agent-reach](agent-reach.md)).
