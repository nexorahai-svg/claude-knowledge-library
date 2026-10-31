---
name: Instatic
slug: instatic
category: site-generators
domains: [website]
verdict: trial
status: researched
summary: سازنده‌ی سایت و CMS بصری خودمیزبان با عامل هوش مصنوعی
use_when: "a site the client will edit content on later ; self-hosted visual CMS and site builder with an AI agent"
how: "Trial first on a small task: self-host with Bun 1.4.1+: bun install then bun run dev (SQLite, admin at localhost:3001/admin via bun run start), or Docker: docker compose -f compose.prod.yml -f compose.sqlite.yml up -d; MIT; test on a three-language RTL trial site"
url: https://github.com/CoreBunch/Instatic
repo: "https://github.com/CoreBunch/Instatic"
license: "MIT"
pricing: free
risk: low
sources: [S158]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# Instatic

## چیست
✅ CMS و سایت‌ساز بصری خودمیزبان با عامل (MIT، حدود ۹ هزار ستاره، آخرین تغییر ۲۰۲۶-۱۰-۱۳؛ آخرین نسخه v0.0.21، پس هنوز پیش از ۱.۰ است). ✅ README: عامل هوش مصنوعی با مدل خودت (Claude، OpenAI، OpenRouter یا Ollama محلی)، پایگاه SQLite یا Postgres.

✅ نصب و اجرا (https://github.com/CoreBunch/Instatic، ۲۰۲۶-۱۰-۲۷): bun install ؛ bun run dev (نیاز به Bun 1.4.1 یا بالاتر)

## کی استفاده کنیم
🧭 برای سایت‌هایی که مشتری بعداً خودش محتوا را ویرایش می‌کند؛ پیش از استفاده‌ی واقعی روی یک سایت آزمایشی سه‌زبانه با راست‌به‌چپ امتحان شود ❓.
