---
name: Vercel Skills (npx skills)
slug: vercel-skills
category: claude-code-tooling
domains: [claude-code]
verdict: trial
status: researched
summary: CLI نصب skill مشترک برای عامل‌های مختلف؛ skill یعنی کدی که با دسترسی عامل اجرا می‌شود
use_when: "installing the same skill across several agents or a team"
how: "Trial first on a small task: run npx skills add vercel-labs/agent-skills --skill NAME -a claude-code (Node 22.20+); read each skill first and pin a commit; set DISABLE_TELEMETRY=1 since the CLI sends anonymous usage data (MIT)"
url: https://github.com/vercel-labs/skills
repo: "https://github.com/vercel-labs/skills"
license: "MIT"
pricing: free
risk: medium
sources: [S159]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# Vercel Skills (npx skills)

## چیست
✅ CLI متن‌باز Vercel Labs (MIT، حدود ۳۶ هزار ستاره، آخرین انتشار v1.7.4 در ۲۰۲۶-۱۰-۱۹؛ README: Node.js 22.20 یا بالاتر، و با DISABLE_TELEMETRY=1 یا DO_NOT_TRACK=1 ارسال داده‌ی ناشناس خاموش می‌شود) با مجموعه‌ی `vercel-labs/agent-skills`.
✅ نصب و اجرا (https://github.com/vercel-labs/skills، ۲۰۲۶-۱۰-۲۷): npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code

## کی استفاده کنیم
🧭 برای نصب یکسان skill در چند عامل یا تیم. هر skill را پیش از نصب بخوان و روی commit ثابت پین کن.
