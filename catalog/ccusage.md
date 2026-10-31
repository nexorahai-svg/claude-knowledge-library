---
name: ccusage
slug: ccusage
category: cost-tokens
domains: [claude-code]
verdict: adopt
status: researched
summary: گزارش مصرف توکن و هزینه‌ی تخمینی Claude Code از لاگ‌های محلی، بر اساس روز، جلسه و بازه‌ی ۵ ساعته
use_when: "measuring where Claude Code tokens and cost go ; before and after any cost-saving change"
how: "npx ccusage@latest daily (also weekly, monthly, session, blocks, statusline); add --offline to avoid fetching prices; measure first, change, then measure again"
url: https://github.com/ccusage/ccusage
repo: "https://github.com/ccusage/ccusage"
license: "MIT"
pricing: free
risk: low
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# ccusage

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v20.0.46 (۲۰۲۶-۱۰-۳۰): رفع خواندن پایگاه‌های ناخوانا و قیمت‌گذاری Ultrafast در بخش‌های غیر Claude؛ برای ما وصله‌ی جزئی؛ MIT بی‌تغییر: https://github.com/ccusage/ccusage/releases
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v20.0.45 (۲۰۲۶-۱۰-۲۶؛ npm همان)؛ MIT بی‌تغییر (فایل مجوز در apps/ccusage/LICENSE است، به همین دلیل GitHub API «NOASSERTION» می‌گوید).
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
کم؛ فقط لاگ محلی را می‌خواند. ✅ کد قیمت (https://github.com/ryoppippi/ccusage/blob/main/rust/crates/ccusage-core/src/pricing.rs): بدون `--offline` فایل قیمت LiteLLM را از `raw.githubusercontent.com/BerriAI/litellm/.../model_prices_and_context_window.json` می‌گیرد و برای مدل‌های ناشناخته `https://models.dev/api.json` را؛ در صورت خطا قیمت درون‌ساخت را به‌کار می‌برد و با `--offline` شبکه را نمی‌زند. (فقط این فایل خوانده شد، کل کد نه.) `npx …@latest` هر بار آخرین نسخه را اجرا می‌کند.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
