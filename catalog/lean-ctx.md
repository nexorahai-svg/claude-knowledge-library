---
name: lean-ctx
slug: lean-ctx
category: cost-tokens
domains: [claude-code]
verdict: assess
status: researched
summary: لایه‌ی محلی فشرده‌سازی خواندن فایل و خروجی شل؛ گسترده، بدون عدد تأییدشده‌ی فعلی
url: https://github.com/yvgude/lean-ctx
repo: "https://github.com/yvgude/lean-ctx"
license: "Apache-2.0 + بخش‌های تجاری"
pricing: freemium
risk: medium
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# lean-ctx

## چیست
✅ یک برنامه‌ی Rust با چند لایه: سرور MCP با ابزارهای خواندن فایل کش‌شده و فشرده، hookهای شل برای کوتاه کردن خروجی دستورها، پراکسی اختیاری، و حافظه‌ی محلی جلسه. حدود ۳.۹ هزار ستاره، خیلی فعال.

## ادعا در مقابل واقعیت
✅ پست منبع می‌گفت فایلی که قبلاً خوانده شده «حدود ۱۳ توکن» هزینه دارد. README فعلی **هیچ عدد اصلی ادعا نمی‌کند و می‌گوید عددهای قبلی پس گرفته شده‌اند.** ابزار بنچمارک روی پروژه‌ی خودت دارد (`lean-ctx benchmark report .`).

## کی استفاده کنیم
🧭 فعلاً نه. با headroom و OpenWolf هم‌پوشانی دارد و بیشترین ردپا را دارد.

## قیمت و مجوز
✅ فایل LICENSE: Apache-2.0؛ ولی `LICENSE.md` می‌گوید بخش‌های تجاری خصوصی جدا هستند (مجوز «مختلط»). نسخه‌ی سازمانی پولی.

## ریسک و هشدار
⚠️ روش نصب اصلی `curl … | sh` است (اجرای مستقیم اسکریپت از اینترنت). hook، MCP و پراکسی نصب می‌کند. ✅ برای اشتراک Pro/Max پراکسی فعال نمی‌شود؛ فشرده‌سازی کامل کلید API می‌خواهد. ❓ وضعیت پیش‌فرض تله‌متری بررسی نشد (`lean-ctx telemetry status`).

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
