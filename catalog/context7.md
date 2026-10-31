---
name: Context7
slug: context7
category: claude-code-tooling
domains: [claude-code, website, apps]
verdict: adopt
status: researched
summary: مستندات به‌روز کتابخانه‌ها برای عامل؛ پلاگین رسمی بیرونی Claude Code
use_when: "writing code against a library API and needing current docs ; avoiding outdated API usage"
how: "Install the Context7 plugin or MCP (Upstash, MIT) and query it before coding with a library; never put client code or secrets in the query"
url: https://context7.com
repo: "https://github.com/upstash/context7"
license: "MIT"
pricing: freemium
risk: low
sources: [S159]
last_checked: 2026-10-25
next_check: "2026-11-24"
---

# Context7

## چیست
✅ سرور MCP و پلاگین Upstash (MIT، حدود ۶۴ هزار ستاره، فعال) که مستندات نسخه‌ی فعلی هر کتابخانه را به عامل می‌دهد.

## کی استفاده کنیم
🧭 در هر پروژه‌ی کد، پیش از نوشتن با API یک کتابخانه؛ کد مشتری و راز را در پرسش نگذار ([جعبه‌ابزار Claude](../domains/claude-code/claude-toolkit.md)).
