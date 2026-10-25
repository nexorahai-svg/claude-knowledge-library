---
name: jcodemunch-mcp
slug: jcodemunch-mcp
category: cost-tokens
domains: [claude-code]
verdict: hold
status: researched
summary: فهرست کد با AST و خواندن فقط یک تابع؛ برای هر کار تجاری مجوز پولی لازم است
url: https://github.com/jgravelle/jcodemunch-mcp
repo: "https://github.com/jgravelle/jcodemunch-mcp"
license: "اختصاصی Dual-Use v1.1 (تجاری پولی)"
pricing: paid
risk: medium
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# jcodemunch-mcp

## چیست
✅ سرور MCP که کد را با tree-sitter به نمادها (تابع، کلاس) فهرست می‌کند تا عامل فقط یک تابع را بخواند، نه کل فایل. با `init` هم hook و هم بخشی در `~/.claude/CLAUDE.md` می‌نویسد. حدود ۲.۸ هزار ستاره، خیلی فعال.

## ادعا در مقابل واقعیت
✅ ادعا: ۸۶ تا ۹۹٪ کمتر (میانگین ۹۶.۶٪) — ولی فقط برای **خواندن کد** و در مقایسه با عاملی که grep می‌کند و همه را می‌خواند؛ خود مخزن رقم ۹۹.۶٪ را «سقف» می‌نامد. ✅ آزمون A/B خود README روی پروژه‌ی واقعی خیلی متواضع‌تر است: **۱۵ تا ۲۵٪** صرفه‌جویی در لایه‌ی ابزار.

## قیمت و مجوز
✅ متن کامل مجوز (v1.1): **رایگان فقط برای استفاده‌ی شخصی، آموزشی، پژوهشی یا غیرتجاری.** هر استفاده‌ی تجاری پولی است: داخل شرکت انتفاعی، ابزار داخلی که به کسب درآمد کمک می‌کند، و **کار مشاوره یا آژانس**. هیچ معافیت درآمدی ندارد. قیمت‌ها طبق مجوز: Builder ۷۹ دلار (یک نفر)، Studio ۳۴۹ دلار (تا ۵ نفر)، Platform ۱٬۹۹۹ دلار.

## کی استفاده کنیم
⛔ برای ساخت سایت مشتری یا شرکت، **بدون خرید مجوز استفاده نکن**. برای پروژه‌ی شخصی رایگان است.

## ریسک و هشدار
✅ به‌طور پیش‌فرض یک شمارنده‌ی ناشناس صرفه‌جویی به بیرون می‌فرستد (خاموش: `share_savings: false`). در `~/.claude/CLAUDE.md` و hookها می‌نویسد.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
