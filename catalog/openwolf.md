---
name: OpenWolf
slug: openwolf
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: hookهای محلی برای فهرست پروژه، یادداشت جلسه و هشدار خواندن تکراری؛ بدون فشرده‌سازی
url: https://github.com/cytostack/openwolf
repo: "https://github.com/cytostack/openwolf"
license: "AGPL-3.0"
pricing: free
risk: medium
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# OpenWolf

## چیست
✅ فشرده نمی‌کند. یک پوشه‌ی `.wolf/` در پروژه می‌سازد (فهرست فایل‌ها، یادداشت‌ها، لاگ باگ، وضعیت) و hookهای Claude Code (شروع جلسه، قبل از خواندن فایل، بعد از Bash، هنگام فشرده‌سازی، پایان) به خواندن تکراری هشدار می‌دهند، خروجی بزرگ Bash را کوتاه می‌کنند و بعد از compaction زمینه را برمی‌گردانند. گزارش مصرف توکن هم دارد. حدود ۲.۴ هزار ستاره.

## ادعا در مقابل واقعیت
✅ README فعلی هیچ درصدی ادعا نمی‌کند و صریح می‌گوید تخمین‌هایش «مقدار ثابتی صرفه‌جویی را ثابت نمی‌کنند». اسکریپت آزمون A/B دارد (`openwolf bench`، با هزینه‌ی واقعی مدل) ولی نتیجه‌ی منتشرشده‌ای پیدا نشد.

## کی استفاده کنیم
🧭 اگر بعد از اندازه‌گیری دیدی خواندن تکراری فایل‌ها یا از دست رفتن زمینه بعد از compaction مشکل اصلی است. اول روی یک پروژه‌ی آزمایشی.
```bash
npm install -g openwolf
```
بعد در پوشه‌ی پروژه: `openwolf init`.

## قیمت و مجوز
✅ رایگان، **AGPL-3.0**. 🧭 برای استفاده‌ی محلی به‌عنوان ابزار توسعه مشکلی ندارد؛ AGPL فقط وقتی مهم است که آن را تغییر دهی و به‌صورت سرویس شبکه‌ای ارائه کنی یا داخل کد توزیع‌شده بگذاری.

## ریسک و هشدار
متوسط: hook روی هر رویداد ابزار کد اجرا می‌کند ([امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md)). ✅ README می‌گوید فقط فایل محلی، بدون API و بدون تله‌متری؛ تنها اتصال، بررسی به‌روزرسانی از npm است. ❓ کد بررسی نشد. محتوای `.wolf/` را قبل از commit نگاه کن.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
