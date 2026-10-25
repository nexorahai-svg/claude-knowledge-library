---
name: Context Mode
slug: context-mode
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: سرور MCP و hook که خروجی بزرگ ابزارها را در پروسه‌ی جدا نگه می‌دارد و فقط نتیجه را به Claude می‌دهد
url: https://github.com/mksglu/context-mode
repo: "https://github.com/mksglu/context-mode"
license: "Elastic License 2.0 (منبع‌دسترس، نه متن‌باز)"
pricing: free
risk: high
sources: [S122]
found_in: [batch-15]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Context Mode

## چیست
✅ v1.0.169؛ حدود ۳۱ هزار ستاره. یک سرور MCP با ۱۱ ابزار: اجرای کد در یک زیرپروسه (۱۲ زبان) که فقط خروجی چاپ‌شده وارد گفتگو می‌شود، و فهرست‌سازی و جستجوی محلی با SQLite (FTS5). چند hook دستورهای خام را به این ابزارها هدایت می‌کنند.

## کی استفاده کنیم
🧪 روی یک پروژه‌ی کوچک، وقتی خروجی ابزارها (لاگ، فایل بزرگ، صفحه‌ی وب) گفتگو را پر می‌کند ([هزینه و کارایی](../domains/claude-code/cost-efficiency.md)). ✅ عدد «۹۸٪» یک مثال است؛ BENCHMARK خود سازنده روی ۲۱ سناریو ۹۶٪ کاهش نشان می‌دهد، در یک سناریو فقط ۱۳٪. بدون hookها خود README حدود ۶۰٪ پیروی می‌گوید.

## قیمت و مجوز
✅ رایگان. ⚠️ مجوز Elastic 2.0: ارائه به‌عنوان سرویس میزبانی‌شده ممنوع.

## ریسک و هشدار
⚠️ ریسک بالا: کد دلخواه را با دسترسی کاربر خودت اجرا می‌کند و URL می‌گیرد. «sandbox» در این ابزار یعنی پروسه‌ی جدا، نه جداسازی امنیتی سیستم‌عامل ❓. hookها و کد را پیش از نصب بخوان ([امنیت MCP](../domains/claude-code/mcp-safety.md)). ادعای «بدون تله‌متری» فقط ادعای README است.

## مرتبط
[S122](../sources/README.md#s122) · غربال دسته‌ی ۱۵
