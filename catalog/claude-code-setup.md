---
name: claude-code-setup (پلاگین رسمی)
slug: claude-code-setup
category: claude-code-tooling
domains: [claude-code]
verdict: adopt
status: researched
summary: پلاگین رسمی فقط‌خواندنی که برای هر پروژه hook، skill، MCP و زیرعامل پیشنهاد می‌دهد
use_when: "starting a new project and wanting hook, skill, MCP and subagent suggestions ; auditing a project setup for Claude Code"
how: "/plugin install claude-code-setup@claude-plugins-official (read-only, installs nothing); then judge each suggestion against the library rules"
url: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup
repo: "https://github.com/anthropics/claude-plugins-official"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S159]
last_checked: 2026-10-31
next_check: "2027-01-23"
---

# claude-code-setup (پلاگین رسمی)

## چیست
✅ پلاگین رسمی Anthropic در فهرست claude-plugins-official؛ کد را فقط می‌خواند و پیشنهاد می‌دهد، چیزی نصب نمی‌کند.

## کی استفاده کنیم
🧭 در شروع یک پروژه‌ی تازه، کنار [جعبه‌ابزار Claude](../domains/claude-code/claude-toolkit.md)؛ پیشنهادها را با قانون‌های کتابخانه بسنج.
```
/plugin install claude-code-setup@claude-plugins-official
```

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
