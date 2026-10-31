---
name: GitHub MCP Server
slug: github-mcp-server
category: claude-code-tooling
domains: [claude-code]
verdict: trial
status: researched
summary: سرور MCP رسمی GitHub برای issue، PR و مخزن
use_when: "needing GitHub issues, PRs or repo access from an agent ; MCP-based GitHub automation"
how: "Trial first on a small task: prefer the gh CLI; if MCP is needed run claude mcp add-json github with type http, url https://api.githubcopilot.com/mcp and an Authorization Bearer header holding a fine-grained PAT with minimum scopes (never commit the token)"
url: https://github.com/github/github-mcp-server
repo: "https://github.com/github/github-mcp-server"
license: "MIT"
pricing: free
risk: medium
sources: [S159]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# GitHub MCP Server

## چیست
✅ رسمی GitHub (MIT، حدود ۳۴ هزار ستاره؛ آخرین نسخه v2.0.3 در ۲۰۲۶-۱۰-۲۱، فعال).

✅ نصب و اجرا (https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md، ۲۰۲۶-۱۰-۲۷): claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer YOUR_GITHUB_PAT"}}'

## کی استفاده کنیم
🧭 فقط با توکن دانه‌ریز و کمترین دسترسی؛ در Claude Code معمولاً `gh` کافی است ([امنیت MCP](../domains/claude-code/mcp-safety.md)).
