---
name: Promptfoo
slug: promptfoo
category: app-testing
domains: [website, claude-code]
verdict: trial
status: researched
summary: آزمون و ارزیابی پرامپت و عامل هوش مصنوعی در CI، با red-team
use_when: "changing a prompt or model in an AI product and needing a fixed test to compare ; regression testing of AI features"
how: "Trial first on a small task: npx promptfoo@latest init --example getting-started, set your provider API key, npx promptfoo@latest eval then npx promptfoo@latest view; set PROMPTFOO_DISABLE_TELEMETRY=1; keep a fixed test set and rerun on each prompt or model change; MIT"
url: https://github.com/promptfoo/promptfoo
repo: "https://github.com/promptfoo/promptfoo"
license: "MIT"
pricing: free
risk: low
sources: [S159]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# Promptfoo

## چیست
✅ ابزار ارزیابی (MIT، حدود ۲۶ هزار ستاره، فعال؛ آخرین نسخه 0.125.1 در ۲۰۲۶-۱۰-۲۵). ✅ تله‌متری با `PROMPTFOO_DISABLE_TELEMETRY=1` خاموش می‌شود (https://www.promptfoo.dev/docs/configuration/telemetry/، ۲۰۲۶-۱۰-۲۷).

✅ نصب و اجرا (https://www.promptfoo.dev/docs/getting-started/، ۲۰۲۶-۱۰-۲۷): npx promptfoo@latest init --example getting-started ؛ npx promptfoo@latest eval ؛ npx promptfoo@latest view

## کی استفاده کنیم
🧭 برای محصولی که هوش مصنوعی دارد: هر تغییر پرامپت یا مدل با آزمون ثابت سنجیده شود ([هوش مصنوعی در محصول](../domains/website/04-tech/ai-in-product.md)).
