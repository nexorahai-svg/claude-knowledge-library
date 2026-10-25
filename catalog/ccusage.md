---
name: ccusage
slug: ccusage
category: cost-tokens
domains: [claude-code]
verdict: adopt
status: researched
summary: گزارش مصرف توکن و هزینه‌ی تخمینی Claude Code از لاگ‌های محلی، بر اساس روز، جلسه و بازه‌ی ۵ ساعته
url: https://github.com/ccusage/ccusage
repo: "https://github.com/ccusage/ccusage"
license: "MIT"
pricing: free
risk: low
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# ccusage

## چیست
✅ یک CLI که لاگ‌های محلی Claude Code را می‌خواند و توکن و هزینه‌ی تخمینی را بر اساس روز، هفته، ماه، جلسه یا بازه‌ی ۵ ساعته جمع می‌زند. دستور `statusline` هم برای نوار وضعیت Claude Code دارد. حدود ۱۹ هزار ستاره، نسخه‌ی 20.0.34. ابزار اندازه‌گیری است، نه صرفه‌جویی.

## کی استفاده کنیم
🧭 **قدم اول هر کاهش هزینه:** قبل از هر تغییری ببین توکن‌ها کجا می‌روند. بعد از هر تغییر دوباره اندازه بگیر.
```bash
npx ccusage@latest daily
```
زیردستورها: `daily`، `weekly`، `monthly`، `session`، `blocks`، `statusline`. پرچم `--offline` برای اینکه قیمت‌ها را از اینترنت نگیرد.

## قیمت و مجوز
✅ رایگان، MIT (فایل مجوز در `apps/ccusage/LICENSE`؛ گیت‌هاب آن را تشخیص نمی‌دهد چون فایل ریشه فقط اشاره‌گر است).

## ریسک و هشدار
کم؛ فقط لاگ محلی را می‌خواند. ❓ اینکه دقیقاً چه چیزی از اینترنت می‌گیرد (قیمت‌ها) در کد بررسی نشد؛ با `--offline` مطمئن‌تر است. `npx …@latest` هر بار آخرین نسخه را اجرا می‌کند.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
