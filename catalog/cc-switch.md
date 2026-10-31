---
name: CC Switch
slug: cc-switch
category: claude-code-tooling
domains: [claude-code, security]
verdict: hold
status: researched
summary: برنامه‌ی رومیزی برای جابه‌جایی ارائه‌دهنده‌ی API و مدیریت تنظیمات Claude Code، Codex و Gemini؛ نگه‌داشته شد به‌خاطر ریسک اشتراک و تبلیغ رله
use_when: "Evaluating tools that switch Claude Code API providers ; deciding whether to use a relay or subscription-sharing app"
how: "Do not install; official site is only https://ccswitch.io (fake copies exist); using a subscription outside the official client may violate vendor terms"
url: https://ccswitch.io
repo: "https://github.com/farion1231/cc-switch"
license: "MIT"
pricing: free
risk: high
sources: [S205]
found_in: [watch-2026-10-29]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# CC Switch

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و API گیت‌هاب) برنامه‌ی رومیزی؛ تنظیمات موجود Claude Code/Codex/Gemini را به‌عنوان ارائه‌دهنده‌ی `default` وارد می‌کند، ارائه‌دهنده‌ی API را عوض می‌کند، MCP/skill/prompt را مدیریت می‌کند، مسیریابی محلی، آمار مصرف و ورود چندحسابی دارد. MIT، حدود ۱۵۰ هزار ستاره، ساخته‌شده ۲۰۲۵-۰۸-۰۴، آخرین push ۲۰۲۶-۱۰-۲۹. تنها سایت رسمی https://ccswitch.io است؛ نسخه‌های جعلی وجود دارد.
✅ خود README هشدار می‌دهد استفاده از اشتراک بیرون از برنامه‌ی رسمی ممکن است شرایط ارائه‌دهنده را نقض کند و پر از تبلیغ سرویس‌های رله‌ی پولی است.
❓ تله‌متری و دقیق‌ترین تغییرات در `~/.claude` گفته نشده.

## کی استفاده کنیم
🧭 فعلاً استفاده نکن؛ هر سوئیچ ارائه‌دهنده را خودمان با متغیرهای محیطی انجام می‌دهیم.

## قیمت و مجوز
MIT، رایگان.

## ریسک و هشدار
⛔ به پوشه‌ی تنظیمات و کلیدهای API دسترسی و تغییر دارد؛ ریسک نقض شرایط اشتراک؛ رله‌ها می‌توانند پرامپت و کد را ببینند؛ نسخه‌ی جعلی.

## مرتبط
- https://github.com/farion1231/cc-switch
- https://ccswitch.io
