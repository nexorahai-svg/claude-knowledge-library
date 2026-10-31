---
name: Claude Agent SDK
slug: claude-agent-sdk
category: claude-code-tooling
domains: [apps, claude-code]
verdict: trial
status: researched
summary: کتابخانه‌ی رسمی Anthropic برای ساخت عامل مستقل داخل محصول خودمان با همان موتور Claude Code
use_when: "Build an autonomous agent or AI feature inside a product ; run Claude Code style agent loops from your own backend code"
how: "npm install @anthropic-ai/claude-agent-sdk; billing is Claude API pricing; license is Anthropic Commercial Terms (not open source); see playbooks/ai-feature-agent.md"
url: https://docs.claude.com/en/api/agent-sdk/overview
repo: "https://github.com/anthropics/claude-agent-sdk-typescript"
license: "SEE LICENSE IN README.md (شرایط تجاری Anthropic؛ متن‌باز نیست)"
pricing: paid
risk: low
sources: [S205, S208]
found_in: [watch-2026-10-29]
last_checked: 2026-10-31
next_check: "2026-11-29"
---

# Claude Agent SDK

## چیست
✅ (۲۰۲۶-۱۰-۳۱، npm) بسته‌ی npm با نام `@anthropic-ai/claude-agent-sdk` نسخه‌ی 0.3.316 (هم‌شماره با Claude Code 2.1.316؛ ۲۰۲۶-۱۰-۳۰ 0.3.314 بود؛ [S216](../sources/README.md#s216)).  ✅ (۲۰۲۶-۱۰-۳۰) بسته‌ی npm با نام `@anthropic-ai/claude-agent-sdk` نسخه‌ی 0.3.314 (هم‌شماره با Claude Code 2.1.314؛ [S208](../sources/README.md#s208)). مجوز در بسته «SEE LICENSE IN README.md» است، یعنی شرایط تجاری Anthropic، نه متن‌باز. نصب: `npm install @anthropic-ai/claude-agent-sdk`.

## کی استفاده کنیم
🧭 وقتی می‌خواهیم عامل مستقل یا قابلیت هوشمند داخل محصول بسازیم؛ راهنمای مرحله‌به‌مرحله در [ai-feature-agent](../playbooks/ai-feature-agent.md).

## قیمت و مجوز
هزینه طبق قیمت API Claude است. مجوز: شرایط تجاری Anthropic.

## ریسک و هشدار
ریسک پایین. کلید API فقط سمت سرور نگه‌داری و سقف هزینه تنظیم شود 🧭.

## مرتبط
- [playbook عامل داخل محصول](../playbooks/ai-feature-agent.md)
- https://docs.claude.com/en/api/agent-sdk/overview
- https://github.com/anthropics/claude-agent-sdk-typescript

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
