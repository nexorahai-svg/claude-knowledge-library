---
name: Repomix
slug: repomix
category: claude-code-tooling
domains: [claude-code]
verdict: adopt
status: researched
summary: کل مخزن را در یک فایل مناسب مدل زبانی بسته‌بندی می‌کند؛ محلی و امن
use_when: "giving a whole small project to a model without file access (web chat, another model)"
how: "npx repomix@latest --style markdown packs the project into one file and drops secrets via Secretlint; not needed inside Claude Code which reads files directly"
url: https://repomix.com
repo: "https://github.com/yamadashy/repomix"
license: "MIT"
pricing: free
risk: low
sources: [S158]
last_checked: 2026-10-25
next_check: "2027-01-23"
---

# Repomix

## چیست
✅ CLI متن‌باز (MIT، حدود ۲۹ هزار ستاره، فعال در ۲۰۲۶-۱۰-۲۵) که فایل‌های یک پروژه را با ساختار پوشه در یک فایل Markdown/XML جمع می‌کند و رازها را با Secretlint کنار می‌گذارد.

## کی استفاده کنیم
🧭 وقتی می‌خواهی کل یک پروژه‌ی کوچک را به مدلی بدهی که به فایل‌ها دسترسی ندارد (چت وب، مدل دیگر). در خود Claude Code لازم نیست، چون مستقیم فایل می‌خواند و یک فایل بزرگ فقط توکن هدر می‌دهد.
```bash
npx repomix@latest --style markdown
```
