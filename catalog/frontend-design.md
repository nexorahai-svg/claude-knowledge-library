---
name: Frontend Design (افزونه‌ی رسمی Anthropic)
slug: frontend-design
category: claude-code-tooling
domains: [website, apps]
verdict: adopt
status: researched
summary: مهارت رسمی Anthropic برای رابط وب متمایز و باکیفیت، به‌جای ظاهر کلیشه‌ای هوش مصنوعی
use_when: "building a landing page, web page or web app UI that must not look like generic AI output ; any frontend design task"
how: "claude plugin marketplace add anthropics/claude-plugins-official then claude plugin install frontend-design@claude-plugins-official --scope user; it is a text-only skill (about 71 lines), combine it with our design-styles and RTL rules"
url: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design
repo: "https://github.com/anthropics/claude-plugins-official"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S126]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-21"
---

# Frontend Design (افزونه‌ی رسمی Anthropic)

## چیست
✅ افزونه‌ی Anthropic در بازار رسمی `claude-plugins-official` و در فهرست افزونه‌های Anthropic با سطح ناشر «anthropic». فقط یک مهارت متنی (حدود ۷۱ خط SKILL.md)؛ بدون hook، MCP یا اسکریپت (فایل‌ها خوانده شد).

## کی استفاده کنیم
🧭 هنگام ساختن صفحه، لندینگ یا رابط اپ وب، کنار راهنمای [سبک‌های طراحی](../domains/website/02-design/design-styles.md) و قواعد RTL کتابخانه.

## نصب
```bash
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install frontend-design@claude-plugins-official --scope user
```
✅ روی Linux نصب و آزموده شد، ۲۰۲۶-۱۰-۲۱.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
کم؛ فقط متن. سلیقه‌ی پیش‌فرضش جای پرسیدن سلیقه‌ی مشتری را نمی‌گیرد.

## مرتبط
[سبک‌های طراحی](../domains/website/02-design/design-styles.md) · [امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S126](../sources/README.md#s126)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
