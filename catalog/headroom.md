---
name: headroom
slug: headroom
category: cost-tokens
domains: [claude-code]
verdict: trial
status: researched
summary: فشرده‌سازی محلی خروجی ابزار، لاگ و JSON قبل از رسیدن به مدل؛ با امکان برگرداندن اصل
url: https://github.com/headroomlabs-ai/headroom
repo: "https://github.com/headroomlabs-ai/headroom"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S24]
found_in: [batch-01/P05]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# headroom

## چیست
✅ لایه‌ی فشرده‌سازی برای خروجی ابزارها، لاگ، فایل و JSON. به چند شکل: کتابخانه‌ی Python/TS، پراکسی محلی HTTP، پوشاننده‌ی CLI (`headroom wrap claude`) و سرور MCP. فشرده‌سازی محلی است (فشرده‌ساز کد بر اساس AST، فشرده‌ساز JSON، یک مدل کوچک Hugging Face). نسخه‌ی اصلی محلی ذخیره می‌شود و مدل می‌تواند آن را پس بگیرد. حدود ۷۵ هزار ستاره. نسخه‌ی تیمی و سازمانی پولی دارد.

## ادعا در مقابل واقعیت
✅ ادعا: حدود ۲۰٪ توکن کمتر برای عامل‌های کدنویسی، ۶۰ تا ۹۵٪ برای JSON. جدول README: جستجوی کد ۲۱٪، دیباگ ۵۷٪، کاوش کد ۴۲٪.
✅ **بنچمارک قابل تکرار دارد** (`benchmarks/index_proof_table.py` و مجموعه‌ی ارزیابی دقت). 🧭 سناریوها مصنوعی‌اند؛ صرفه‌جویی واقعی روی کار سایت فرق دارد.

## کی استفاده کنیم
🧭 فقط اگر اندازه‌گیری نشان داد خروجی‌های بلند (لاگ، خروجی تست، JSON) بخش بزرگ هزینه‌اند. اول روی پروژه‌ی آزمایشی. ❓ اینکه `wrap claude` دقیقاً چطور Claude Code را هدایت می‌کند و آیا با اشتراک Pro/Max کار می‌کند، بررسی نشد.

## قیمت و مجوز
✅ هسته رایگان، Apache-2.0.

## ریسک و هشدار
✅ **تله‌متری به‌طور پیش‌فرض روشن است** (آمار فشرده‌سازی، شناسه‌ی مدل، سیستم‌عامل؛ طبق README نه پرامپت، نه کد، نه مسیر). خاموش کردن: `HEADROOM_TELEMETRY=off` یا `DO_NOT_TRACK=1` یا `HEADROOM_OFFLINE=1`. بررسی به‌روزرسانی: `HEADROOM_UPDATE_CHECK=off`.
در مسیر درخواست‌ها قرار می‌گیرد؛ وابستگی‌های سنگین (مدل یادگیری ماشین). فشرده‌سازی ممکن است اطلاعات حذف کند (هرچند برگشت‌پذیر است).

## مرتبط
[هزینه و کارایی Claude Code](../domains/claude-code/cost-efficiency.md) · [S24](../sources/README.md#s24)
