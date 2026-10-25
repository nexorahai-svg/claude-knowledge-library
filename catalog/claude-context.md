---
name: claude-context
slug: claude-context
category: cost-tokens
domains: [claude-code]
verdict: assess
status: researched
summary: جستجوی معنایی کد با پایگاه داده‌ی برداری؛ در حالت پیش‌فرض کد را به OpenAI و Zilliz می‌فرستد
url: https://github.com/zilliztech/claude-context
repo: "https://github.com/zilliztech/claude-context"
license: "MIT"
pricing: freemium
risk: high
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# claude-context

## چیست
✅ سرور MCP از Zilliz که کد را به بردار (embedding) تبدیل و در پایگاه داده‌ی برداری ذخیره می‌کند، بعد فقط تکه‌های مرتبط را به Claude می‌دهد. حدود ۱۲.۶ هزار ستاره؛ آخرین فعالیت ۲۰۲۶-۰۷-۱۴.

## ادعا در مقابل واقعیت
✅ ادعا: حدود ۴۰٪ توکن کمتر با همان کیفیت بازیابی. ✅ ارزیابی منتشر شده، ولی روی ۳۰ نمونه‌ی SWE-bench، با GPT-4o-mini و LangGraph (**نه Claude Code**) و فقط برای بازیابی کد.

## کی استفاده کنیم
🧭 فقط برای کدبیس‌های بزرگ. یک پروژه‌ی سایت معمولی آن‌قدر کوچک است که سودی ندارد.

## قیمت و مجوز
✅ کد MIT. حالت پیش‌فرض به حساب Zilliz Cloud و کلید OpenAI نیاز دارد (پولی). حالت کاملاً محلی با Milvus و Ollama ممکن است.

## ریسک و هشدار
⚠️ **در حالت پیش‌فرض، تکه‌های کد تو به OpenAI (برای embedding) و Zilliz Cloud (برای ذخیره) فرستاده می‌شود.** دو حساب و دو کلید شخص ثالث. برای کد مشتری فقط حالت کاملاً محلی.

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
