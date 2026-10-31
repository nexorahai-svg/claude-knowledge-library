---
name: Ponytail
slug: ponytail
category: claude-code-tooling
domains: [claude-code, website, apps]
verdict: trial
status: researched
summary: افزونه‌ی Claude Code که عامل را به ساده‌ترین راه‌حل لازم وادار می‌کند؛ به‌اضافه‌ی بازبینی، ممیزی و تابلوی هزینه
use_when: "Claude over-builds (libraries, classes, layers for simple work) ; reviewing a change or repo for bugs, security, load and tests"
how: "Trial first on a test project: /plugin marketplace add DietrichGebert/ponytail then /plugin install ponytail@ponytail; use /ponytail, /ponytail-review, /ponytail-audit; read hooks/ before updating; keep webhook off or sendNames off; say in project CLAUDE.md which rule wins"
url: https://ponytail.dev
repo: "https://github.com/DietrichGebert/ponytail"
license: "MIT"
pricing: free
risk: medium
sources: [S79]
found_in: [batch-04]
last_checked: 2026-10-18
next_check: "2027-01-16"
---

# Ponytail

## چیست
✅ یک پرامپت (`skills/ponytail/SKILL.md`) که در هر جلسه با hook بار می‌شود: «فقط کدی که کار لازم دارد»، اول کتابخانه‌ی استاندارد و کد موجود، بدون انتزاع اضافه. **اعتبارسنجی، امنیت، مدیریت خطا و دسترسی‌پذیری حذف نمی‌شوند** و هر منطق پرخطر یک تست کوچک می‌گیرد. هر پاسخ با «چه چیزی چک نشد» تمام می‌شود.
✅ فرمان‌ها: `/ponytail` (lite، full، ultra، off)، `/ponytail-review` (بازبینی تغییر: باگ، امنیت، بار، تست)، `/ponytail-audit` (همان برای کل مخزن)، `/ponytail-debt`. از نسخه‌ی 5.3 یک نوار بالای پرامپت هزینه، توکن، زمان و وضعیت تست کار را نشان می‌دهد (Claude Code 2.1.290 به بعد) و یک تابلوی محلی دارد.
✅ نسخه‌ی 5.3.2 (۲۰۲۶-۱۰-۱۶)، حدود ۱۶۶ هزار ستاره، ۱۲۰۰ PR، چند مشارکت‌کننده؛ برای Codex، Cursor، Copilot و چند عامل دیگر هم هست.

## کی استفاده کنیم
🧭 پروژه‌هایی که Claude در آن‌ها بیش از لازم می‌سازد (کتابخانه برای کار ساده، کلاس و لایه‌ی اضافه). `/ponytail-review` کنار [بررسی خودکار](../domains/claude-code/verification.md)، نه جای آن. اول روی یک پروژه‌ی آزمایشی با [روش اثبات صرفه‌جویی](../domains/claude-code/cost-efficiency.md#روش-اثبات-صرفهجویی).

## قیمت و مجوز
✅ رایگان، MIT. نصب: `/plugin marketplace add DietrichGebert/ponytail` و بعد `/plugin install ponytail@ponytail`. سازنده می‌گوید فقط از همین مخزن یا `@dietrichgebert/ponytail` در npm نصب کنید و هیچ‌وقت فایل exe نمی‌دهد.

## ادعا در مقابل شواهد
✅ ادعای README: ۵۳٪ کد کمتر، ۴۱٪ زمان کمتر، ۲۶٪ هزینه‌ی کمتر، ۴۵٪ توکن کمتر؛ تست برای منطق پرخطر ۹۸٪ در مقابل ۶۸٪.
✅ روش (`benchmarks/results/2026-10-07-agentic.md`): خود سازنده اجرا کرده؛ ۳۹ کار (۱۲ تیکت در یک مخزن واقعی FastAPI و React، ۱۸ کار با چک پنهان)، Opus 5.5، ۵ بار برای هر کار، ۵۸۵ جلسه، میانگین هندسی با بازه‌ی اطمینان ۹۵٪. روش جدی‌تر از بیشتر ادعاهای مشابه است.
⚠️ محدودیت‌ها: **Bash برای همه خاموش بود** (کار واقعی Claude Code با شل فرق دارد)؛ جلسه‌ها بدون CLAUDE.md؛ داور کیفیت هم یک مدل Claude بود؛ پوشه‌ی داده‌ی خام (`runs/`) در مخزن نیست، پس عددها از بیرون دوباره محاسبه نمی‌شوند. خود گزارش می‌گوید کد کمتر **درستی یا امنیت اضافه نکرد**؛ فقط کم هم نکرد. ❓ روی پروژه‌های ما آزموده نشد.

## ریسک و هشدار
✅ (کد خوانده شد، ۲۰۲۶-۱۰-۱۸) سه hook دارد: شروع جلسه، شروع زیرعامل و ارسال پرامپت. با `git ls-files` یک نقشه‌ی کوتاه پروژه (حدود ۲۰۰۰ نویسه) به context می‌افزاید.
✅ پیش‌فرض هیچ داده‌ای بیرون نمی‌رود. نوار هر کار را در `~/.config/ponytail/band/<project>.csv` می‌نویسد. `/ponytail band import` رونوشت‌های جلسه‌ها در `~/.claude/projects` را می‌خواند تا هزینه حساب کند (فقط محلی).
⚠️ گزینه‌ی اختیاری **webhook** بعد از هر نوبت ردیف کار را می‌فرستد و نام کار هم پیش‌فرض روشن است (`sendNames`). اگر webhook می‌گذاری، `sendNames` را خاموش کن.
⚠️ هر hook با هر پرامپت اجرا می‌شود؛ پیش از به‌روزرسانی نسخه، تغییرات `hooks/` را بخوان (قانون ۴ [CLAUDE.md](../CLAUDE.md)).
🧭 «تنبل» بودن ممکن است با قانون‌های پروژه‌ی ما (مثلاً «بررسی خودکار از جلسه‌ی اول») برخورد کند. در `CLAUDE.md` پروژه بنویس کدام قانون مقدم است.

## مرتبط
[هزینه و کارایی](../domains/claude-code/cost-efficiency.md#ابزارهای-جانبی) · [سنجش ادعاهای عددی](../research/claim-testing.md) · [S79](../sources/README.md#s79) · غربال دسته‌ی ۰۴
