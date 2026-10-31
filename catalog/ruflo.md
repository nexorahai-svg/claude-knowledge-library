---
name: Ruflo (claude-flow سابق)
slug: ruflo
category: agents-memory
domains: [claude-code, security]
verdict: assess
status: researched
summary: لایه‌ی بزرگ هماهنگی گروه عامل برای Claude Code؛ دسترسی پوسته و حافظه
url: https://github.com/ruvnet/ruflo
repo: "https://github.com/ruvnet/ruflo"
license: "MIT"
pricing: free
risk: high
sources: [S159]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Ruflo (claude-flow سابق)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v3.66.0 (۲۰۲۶-۱۰-۳۱). ⚠️ v3.65.1 (۲۰۲۶-۱۰-۳۰) وصله‌ی امنیتی است: ابزار MCP به نام `http_fetch` فقط متن نام میزبان را می‌سنجید، پس نامی که به loopback، نشانی خصوصی یا 169.254.169.254 حل می‌شد رد می‌شد (SSRF، CWE-918). حالا هر اتصال و هر redirect بعد از DNS سنجیده می‌شود. نسخه‌های پایین‌تر از 3.65.1 را به کار نبر: https://github.com/ruvnet/ruflo/releases/tag/v3.65.1
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v3.63.6 (۲۰۲۶-۱۰-۲۷؛ پنج وصله در دو روز، عادی این مخزن)؛ MIT بی‌تغییر.
✅ (MIT، حدود ۷۹ هزار ستاره، فعال). «تیم ۶۰ عامل» ادعای سازنده است.

## کی استفاده کنیم
🧭 مثل Oh My Claude Code: سنگین و پرمصرف؛ کار موازی را با ابزار رسمی پیش ببر ([کار موازی](../domains/claude-code/parallel-agents.md)).

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v3.64.0 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
