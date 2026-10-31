---
name: Motion AI Kit (رسمی)
slug: motion-ai-kit
category: claude-code-tooling
domains: [website, claude-code]
verdict: assess
status: researched
summary: مهارت و MCP رسمی Motion؛ به سرورهای Motion وصل می‌شود و بخشی پولی است
url: https://github.com/motiondivision/ai-kit
repo: "https://github.com/motiondivision/ai-kit"
license: "MIT (طبق package.json)"
pricing: freemium
risk: medium
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Motion AI Kit (رسمی)

## چیست
✅ از سازنده‌ی Motion. یک مهارت با راهنماهای بهترین روش، جستجوی مستندات، ساخت فنر CSS، ممیزی عملکرد و تنظیم انتقال؛ یک عامل بازبین.

## کی استفاده کنیم
🧭 راهنماهایش را بخوان؛ نصب فقط وقتی MCP میزبانی‌شده و Motion+ را می‌خواهی.

## قیمت و مجوز
✅ بهترین روش‌ها، جستجوی مستندات و فنر رایگان. ممیزی MotionScore، مستندات و کد نمونه‌ی Motion+ و ویرایشگر بصری نیاز به **Motion+** دارد (پولی).

## ریسک و هشدار
✅ فایل `plugins/motion/mcp.json` به دو سرور میزبانی‌شده وصل می‌شود: `https://mcp.motion.dev` و `https://mcp.motion.dev/plus`. یعنی پرسش‌ها به سرور Motion می‌رود و محتوای راهنما از راه دور می‌آید. نصب‌کننده (`npx motion-ai`) فایل‌های تنظیمات عامل را می‌نویسد. ([امنیت MCP](../domains/claude-code/mcp-safety.md))

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)
