---
name: anthropics/skills (skillهای رسمی)
slug: anthropic-skills
category: claude-code-tooling
domains: [claude-code]
verdict: adopt
status: researched
summary: مخزن رسمی Agent Skills از Anthropic؛ مرجع ساخت skill و skillهای سند (docx، pdf، pptx، xlsx)
use_when: "learning the correct structure of a Claude skill ; working with docx, pdf, pptx or xlsx files"
how: "In Claude Code run /plugin marketplace add anthropics/skills, then /plugin install document-skills@anthropic-agent-skills for docx/pdf/pptx/xlsx (or example-skills@anthropic-agent-skills); read the repo as the SKILL.md reference (the Agent Skills standard itself now belongs to AAIF, this repo stays Anthropic's); document skills are source-available"
url: https://github.com/anthropics/skills
repo: "https://github.com/anthropics/skills"
license: "هر skill مجوز خودش (بیشتر Apache-2.0؛ skillهای سند source-available)"
pricing: free
risk: low
sources: [S158, S189]
last_checked: 2026-10-28
next_check: "2027-01-25"
---

# anthropics/skills (skillهای رسمی)

## چیست
✅ مخزن رسمی Anthropic (حدود ۱۸۴ هزار ستاره؛ مجوز ریپو در GitHub یکپارچه ثبت نشده و README می‌گوید بیشتر skillها Apache-2.0 و skillهای docx/pdf/pptx/xlsx فقط source-available هستند ✅ با skillهای نمونه و skillهای سند که در Claude.ai هم استفاده می‌شوند، به‌علاوه‌ی الگوی ساخت skill.

✅ نصب و اجرا (https://github.com/anthropics/skills، ۲۰۲۶-۱۰-۲۷): /plugin marketplace add anthropics/skills ؛ /plugin install document-skills@anthropic-agent-skills

✅ (اعلام Anthropic، ۲۰۲۶-۱۰-۲۲) استاندارد باز Agent Skills (نام، لوگو، سازمان GitHub، دامنه‌ی agentskills.io) به Agentic AI Foundation زیر Linux Foundation اهدا شد؛ مالک استاندارد حالا AAIF است. این مخزن رسمی Anthropic جداست و همچنان مال Anthropic می‌ماند ([S189](../sources/README.md#s189)).

## کی استفاده کنیم
🧭 اول از همه برای یاد گرفتن ساختار درست skill و برای کار با فایل‌های Office و PDF؛ از بازارچه‌ی رسمی پلاگین نصب شود، نه کپی دستی.
