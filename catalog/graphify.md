---
name: Graphify
slug: graphify
category: agents-memory
domains: [claude-code]
verdict: assess
status: researched
summary: تبدیل پوشه به گراف دانش برای عامل؛ کد محلی، اسناد به مدل زبانی؛ نام بسته‌ی رسمی graphifyy
url: https://graphify.com
repo: "https://github.com/Graphify-Labs/graphify"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S36]
found_in: [batch-01/P15, batch-01/P19]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Graphify

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v0.9.99 (۲۰۲۶-۱۰-۳۰): مسیر محافظه‌کارانه‌تر در `graphify path`، رفع تحلیل Go و Python و محل نصب Gemini و OpenCode؛ Apache-2.0 بی‌تغییر: https://github.com/Graphify-Labs/graphify/releases
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v0.9.97 (۲۰۲۶-۱۰-۲۷)؛ Apache-2.0 بی‌تغییر.
✅ حدود ۱۲۷ هزار ستاره؛ ۲۶۰ نسخه از ۲۰۲۶-۰۴. کد با tree-sitter **محلی** تحلیل می‌شود (بدون مدل زبانی)؛ اسناد، PDF و تصویر برای استخراج معنا به **مدل زبانی** فرستاده می‌شوند (در Claude Code مدل خودت؛ در حالت بدون رابط، هر کلید API که در محیط باشد). ✅ README: بدون تله‌متری. ✅ صفحه‌ی Y Combinator تأیید می‌کند: Graphify Labs، دسته‌ی S26، **۱ کارمند**.

## کی استفاده کنیم
🧭 روی پروژه‌ی آزمایشی، با حالت فقط کد (`GRAPHIFY_BACKEND=none`) یا Ollama محلی، با نسخه‌ی ثابت.

## قیمت و مجوز
✅ Apache-2.0. نسخه‌ی ابری پولی (Graphify Cloud) هم تبلیغ می‌شود. ❓ ادعای «۸۰٪ کاهش توکن» تأیید نشد.

## ریسک و هشدار
⚠️ **نام بسته‌ی رسمی `graphifyy` (با دو y) است** (خود README)؛ README هشدار می‌دهد بسته‌های دیگر با نام graphify وابسته نیستند و نام تک‌y فعلاً ثبت نشده → ریسک بسته‌ی تقلبی؛ نام را دقیقاً کپی کن. ✅ `graphify install` مهارت در `~/.claude/skills/graphify` می‌گذارد؛ `graphify claude install` یک hook همیشه‌روشن اضافه می‌کند. ⚠️ اگر کلید API در محیط باشد، خودکار یک ارائه‌دهنده را انتخاب می‌کند (Kimi به سرورهای چین می‌رود).

## مرتبط
[دستیار شخصی](../domains/claude-code/personal-assistant.md) · [امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S36](../sources/README.md#s36)
