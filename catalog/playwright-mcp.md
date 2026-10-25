---
name: Playwright MCP
slug: playwright-mcp
category: browser-testing
domains: [website, claude-code]
verdict: trial
status: researched
summary: خودکارسازی مرورگر برای Claude با درخت دسترسی‌پذیری؛ چند مرورگر
url: https://github.com/microsoft/playwright-mcp
repo: "https://github.com/microsoft/playwright-mcp"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S21]
found_in: [batch-01/P19]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Playwright MCP

## چیست
✅ سرور MCP مایکروسافت (Apache-2.0، حدود ۳۸ هزار ستاره، نسخه‌ی 0.0.83). به‌جای اسکرین‌شات از **درخت دسترسی‌پذیری** صفحه استفاده می‌کند، پس مدل بینایی لازم نیست. Chrome، Firefox، WebKit و Edge. شبیه‌سازی موبایل، بارگذاری کوکی ذخیره‌شده (`--storage-state`).

## کی استفاده کنیم
🧭 تست جریان‌ها: پر کردن فرم تماس، ورود، خرید، در چند مرورگر. برای سرعت و Lighthouse از [Chrome DevTools MCP](chrome-devtools-mcp.md) استفاده کن.

## نصب
✅ دستور رسمی:
```bash
claude mcp add playwright npx @playwright/mcp@latest
```
نیازمندی: Node.js ۱۸ به بالا. ✅ خود README می‌گوید برای عامل‌های کدنویسی، CLI همراه skill از MCP کم‌مصرف‌تر است.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
✅ README صریح می‌گوید Playwright MCP «**مرز امنیتی نیست**»؛ گزینه‌های مجاز و ممنوع کردن دامنه‌ها هم مرز امنیتی نیستند. پیش‌فرض پروفایل ماندگار است؛ 🧭 با `--isolated` اجرا کن.

✅ نسخه‌ی 0.0.83 روی رایانه‌ی اصلی در سطح کاربر نصب شد و وصل شد (۲۰۲۶-۱۰-۲۱):
```bash
claude mcp add playwright --scope user -- npx @playwright/mcp@latest --isolated
```

## مرتبط
[امنیت MCP](../domains/claude-code/mcp-safety.md) · [S21](../sources/README.md#s21)
