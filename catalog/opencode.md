---
name: OpenCode
slug: opencode
category: claude-code-tooling
domains: [claude-code]
verdict: trial
status: researched
summary: عامل کدنویسی متن‌باز ترمینالی با ارائه‌دهنده‌های مختلف و مدل محلی
use_when: "want an alternative or complement to Claude Code with a local or cheap model"
how: "Trial first on a small task: install with curl -fsSL https://opencode.ai/v2/install | bash (or brew install opencode), then for a local model add an ollama provider (@ai-sdk/openai-compatible, baseURL http://localhost:11434/v1) in opencode.json; only local models keep data on the computer (MIT)"
url: https://opencode.ai
repo: "https://github.com/anomalyco/opencode"
license: "MIT"
pricing: free
risk: medium
sources: [S159]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# OpenCode

## چیست
✅ عامل کدنویسی (MIT، حدود ۲۲۱ هزار ستاره، فعال؛ آخرین انتشار v1.19.4 در ۲۰۲۶-۱۰-۲۲؛ مخزن اکنون anomalyco/opencode است؛ README نصب با curl و brew را تأیید می‌کند و برای مدل محلی از بسته‌ی @ai-sdk/openai-compatible استفاده می‌شود)، با Ollama و ده‌ها ارائه‌دهنده.
✅ نصب و اجرا (https://opencode.ai/docs/providers/، ۲۰۲۶-۱۰-۲۷): curl -fsSL https://opencode.ai/v2/install | bash

## کی استفاده کنیم
🧭 جایگزین یا مکمل Claude Code برای مدل محلی یا ارزان. «چیزی از رایانه بیرون نمی‌رود» فقط با مدل محلی درست است.
