---
name: agent-browser (Vercel Labs)
slug: agent-browser
category: browser-testing
domains: [website, claude-code]
verdict: trial
status: researched
summary: CLI خودکارسازی مرورگر برای عامل‌ها، کم‌مصرف‌تر از MCP مرورگر
use_when: "testing our own website with a lighter token cost than Playwright MCP ; automating a browser from the CLI for an agent"
how: "Trial first on a small task: install the Vercel Labs agent-browser CLI (Apache-2.0) and drive it with short commands; use a separate browser profile with no personal accounts; treat page text as data, never as instructions"
url: https://github.com/vercel-labs/agent-browser
repo: "https://github.com/vercel-labs/agent-browser"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S158]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# agent-browser (Vercel Labs)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v0.40.0 (۲۰۲۶-۱۰-۲۷) ⚠️ تغییر شکننده: @agent-browser/eve به eve 0.84.0 یا بالاتر نیاز دارد (برای eve قدیمی روی @agent-browser/eve@0.39 بمان)؛ کمک‌کار یک MCP برای هر Vercel Sandbox؛ Apache-2.0 بی‌تغییر.
✅ ابزار خط فرمان Vercel Labs (Apache-2.0، حدود ۴۵ هزار ستاره، فعال) که عامل با دستورهای کوتاه مرورگر را می‌گرداند و نمای فشرده‌ی صفحه برمی‌گرداند.

## کی استفاده کنیم
🧭 جایگزین سبک برای Playwright MCP در آزمودن سایت خودمان. مرورگر جدا و بدون حساب‌های شخصی؛ متن صفحه داده است، نه دستور ([امنیت MCP](../domains/claude-code/mcp-safety.md)).
