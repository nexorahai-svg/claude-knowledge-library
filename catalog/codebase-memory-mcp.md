---
name: codebase-memory-mcp
slug: codebase-memory-mcp
category: agents-memory
domains: [claude-code]
verdict: assess
status: researched
summary: سرور MCP محلی که گراف دانش کد را برای جست‌وجوی ساختاری می‌سازد
use_when: "giving Claude Code a local code graph for large repos ; reducing file-reading tokens"
how: "install.sh (read first) or release binary with checksum; add as MCP server; index per project"
url: https://github.com/DeusData/codebase-memory-mcp
repo: "https://github.com/DeusData/codebase-memory-mcp"
license: "MIT"
pricing: free
risk: medium
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# codebase-memory-mcp

## چیست
✅ سرور MCP محلی نوشته‌شده با C که گراف دانش کد می‌سازد. ✅ شبکه: «بدون شبکه» نیست؛ یک بررسی به‌روزرسانی بهترین‌تلاش به api.github.com دارد و نصب/به‌روزرسانی از GitHub دانلود می‌کند؛ داده‌ی پروژه ارسال نمی‌شود. ✅ SLSA Build L3 فقط برای آرشیوهای release است، نه تأیید شخص ثالث. ❓ ادعای کارایی تأیید نشد.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: giving Claude Code a local code graph for large repos؛ reducing file-reading tokens. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: MIT (✅ از LICENSE مخزن؛ ستاره‌ها ۴۷,۸۳۷ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: medium.
- ⚠ مایکروسافت بعضی باینری‌ها را Wacatac.B!ml علامت می‌زند (پروژه می‌گوید هشدار کاذب است).
- ❓ تعداد ستاره (۴۷ هزار) غیرعادی است و تأیید نشد.
- باینری بومی (نصب‌کننده دانلود می‌کند)؛ ۵۹۲ issue باز؛ بک‌دور vendored دارد؛ ادعای ستاره ۴۷ هزار با یک نویسنده غیرعادی است.
- ❓ کد C، نصب‌کننده و ادعاهای نشت‌نکردن داده با ترافیک واقعی تست نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/DeusData/codebase-memory-mcp
