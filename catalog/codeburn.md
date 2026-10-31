---
name: CodeBurn
slug: codeburn
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: ردیاب محلی مصرف توکن و هزینه برای ده‌ها عامل کدنویسی (README: ۴۲ یکپارچه‌سازی)
use_when: "tracking token cost across many coding agents ; comparing against ccusage"
how: "Trial first on a small task: read the code first, then run npx codeburn (Node 22.13+); optional Claude Code plugin /plugin install codeburn --marketplace getagentseal/codeburn; third-party code via npx, MIT; ccusage stays the baseline"
url: https://github.com/getagentseal/codeburn
repo: "https://github.com/getagentseal/codeburn"
license: "MIT"
pricing: free
risk: medium
sources: [S162]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# CodeBurn

## چیست
✅ (MIT، حدود ۱۲ هزار ستاره، فعال)؛ اجرا با `npx codeburn`. ✅ README (۲۰۲۶-۱۰-۲۷): نیاز به Node.js 22.13+؛ ۴۲ یکپارچه‌سازی (کارت قبلاً ۳۷ نوشته بود)؛ بدون حساب و بدون طرح پولی.

✅ نصب و اجرا (https://github.com/getagentseal/codeburn، ۲۰۲۶-۱۰-۲۷): npx codeburn

## کی استفاده کنیم
🧭 کنار [ccusage](ccusage.md)؛ `npx` کد شخص ثالث اجرا می‌کند، اول کد را بخوان.
