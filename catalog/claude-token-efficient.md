---
name: claude-token-efficient
slug: claude-token-efficient
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: یک CLAUDE.md کوتاه برای پاسخ‌های کوتاه‌تر؛ اثر واقعی کم و فقط روی خروجی
use_when: "trying to shorten Claude output in output-heavy tasks ; testing a concise-behaviour CLAUDE.md"
how: "Trial first on a small task: use only the default CLAUDE.md, measure before and after with ccusage; real output savings are about 2 to 11% (not 63%) and the file adds input tokens to every message so skip for short chats; avoid the compressed profile"
url: https://github.com/drona23/claude-token-efficient
repo: "https://github.com/drona23/claude-token-efficient"
license: "MIT"
pricing: free
risk: low
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# claude-token-efficient

## چیست
✅ فقط یک فایل CLAUDE.md با قواعد رفتاری: قبل از نوشتن بخوان و فایل تغییرنکرده را دوباره نخوان، فکر کامل ولی جواب کوتاه، بدون تعارف و ایموجی، و **هیچ API یا نسخه یا نام بسته‌ای را حدس نزن**. هیچ کدی اجرا نمی‌شود.

## ادعا در مقابل واقعیت
- پست منبع و README عدد **۶۳٪** کاهش را می‌گویند. ✅ این عدد از یک آزمون ۵ پرامپتی با شمارش کلمه آمده، بدون کنترل تغییرپذیری (خود README می‌گوید «جهت‌نما، نه اندازه‌گیری دقیق»).
- ✅ **بنچمارک خود مخزن می‌گوید ۶۳٪ روی فایل فعلی تکرار نمی‌شود.** کاهش واقعی توکن خروجی: Haiku حدود ۲٪، Sonnet حدود ۱۱٪، Opus حدود ۷٪.
- ✅ نسخه‌ی فشرده (`profiles/CLAUDE.compressed.md`) روی Opus تا ۶۲٪ کم می‌کند، ولی طبق README قواعد ضد حدس زدن و ضد خواندن تکراری را حذف کرده؛ **یعنی ممکن است کیفیت را پایین بیاورد.**
- ✅ خود README: فایل در هر پیام به ورودی اضافه می‌شود؛ برای پرسش‌های کوتاه **مصرف را زیاد می‌کند**.

## کی استفاده کنیم
🧭 آزمایشی، فقط نسخه‌ی پیش‌فرض، فقط در کارهای پرخروجی، و با اندازه‌گیری قبل و بعد با [ccusage](ccusage.md). ایده‌ی خوبش («حدس نزن، اول چک کن») را می‌شود در CLAUDE.md خودمان با کلمات خودمان نوشت.

## قیمت و مجوز
✅ رایگان، MIT.

## ریسک و هشدار
کم (فقط متن). به عدد ۶۳٪ اعتماد نکن. نسخه‌ی فشرده را استفاده نکن.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
