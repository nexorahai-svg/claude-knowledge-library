---
name: Grim Prompter
slug: grim-prompter
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: skill مدل‌سازی تهدید برای عامل‌های کدنویسی که با symlink در پوشه‌ی skills نصب می‌شود
use_when: "Threat-modeling a new feature or app before building ; security review prompts for a coding agent"
how: "Symlink skills/threat-model into ~/.claude/skills after reading the files; verify output yourself"
url: https://github.com/jmanico/grim-prompter
repo: "https://github.com/jmanico/grim-prompter"
license: "MIT"
pricing: free
risk: low
sources: [S205]
found_in: [watch-2026-10-29]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Grim Prompter

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README) skill مدل‌سازی تهدید برای عامل‌های کدنویسی؛ نصب با symlink پوشه‌ی `skills/threat-model` به `~/.claude/skills`. MIT، ۱۵۲ ستاره، آخرین push ۲۰۲۶-۱۰-۲۹.
❓ کد خوانده نشد.

## کی استفاده کنیم
🧭 پیش از ساخت قابلیت‌های حساس (ورود، پرداخت، API) برای فهرست تهدید اولیه؛ جایگزین بررسی انسانی نیست.

## قیمت و مجوز
MIT، رایگان.

## ریسک و هشدار
ریسک پایین. خروجی مدل‌سازی تهدید را راستی‌آزمایی کن 🧭.

## مرتبط
- https://github.com/jmanico/grim-prompter
