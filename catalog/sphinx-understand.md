---
name: Sphinx (pre-push comprehension quiz)
slug: sphinx-understand
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: هوک Git (MIT) که پیش از push به main از تو درباره‌ی تغییر عامل می‌پرسد؛ هوک سراسری Git و تنظیمات Claude Code را عوض می‌کند و کد به مدل داور می‌رود
use_when: "forcing yourself to understand an agent-written change before pushing to main ; practicing review of AI-written code on a personal project"
how: "Do not install without the user's yes; npm install -g sphinx-understand only prints a hint, but sphinx install rewrites global git core.hooksPath and Claude Code settings, so use sphinx install --repo on a throwaway repo and a local or own endpoint for client code"
url: https://sphinx-six-theta.vercel.app/
repo: "https://github.com/parthh01/sphinx"
license: "MIT"
pricing: free
risk: high
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# Sphinx (pre-push comprehension quiz)

## چیست
- ✅ مخزن MIT («Sphinx contributors»)، حدود ۴۶۰ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۶. بسته‌ی npm با نام `sphinx-understand` نسخه‌ی ۰٫۱٫۱۹ در ۲۰۲۶-۱۰-۲۵، مجوز MIT. release در GitHub ندارد: https://github.com/parthh01/sphinx
- ✅ README: پیش از push (به‌طور پیش‌فرض به `main`/`master`) یک پرسش‌نامه درباره‌ی رفتار، حالت‌های خطا و ناوردایی‌های تغییر می‌پرسد؛ باز-کتاب است. تا ۲۵ دقیقه Git را نگه می‌دارد.
- ✅ مدل داور: Claude Code یا Codex وارد‌شده (اشتراک خودت)، OpenRouter (کلید لازم) یا هر endpoint سازگار با OpenAI (مثل Ollama محلی). سرویس میزبانی‌شده‌ی خودش را ندارد.
- ✅ `sphinx yolo` بررسی را خاموش می‌کند و هر رد شدن ثبت می‌شود. README صریح می‌گوید «تمرین است، نه دروازه‌ی امنیتی» و داور ممکن است اشتباه کند.
- ✅ اسکریپت postinstall فقط یک راهنما چاپ می‌کند و چیزی تغییر نمی‌دهد: https://github.com/parthh01/sphinx/blob/main/scripts/postinstall.js
- ✅ نیازمندی‌ها: Node 22.19 به بالا، Git؛ macOS، لینوکس یا WSL (ویندوز بومی پشتیبانی نمی‌شود).

## کی استفاده کنیم
- 🧭 برای تمرین بازبینی کد عامل روی پروژه‌ی شخصی؛ ایده‌ی «دروازه‌ی فهم انسانی» که [بررسی خودکار](../domains/claude-code/verification.md) ما ندارد. برای کد مشتری فقط با مدل محلی.

## قیمت و مجوز
- ✅ رایگان، MIT: https://github.com/parthh01/sphinx/blob/main/LICENSE . هزینه‌ی مدل جدا؛ برای OpenRouter و ارائه‌دهنده‌های پولی سقف خرج بگذار (README: سقف پیش‌فرض تعداد فراخوانی وجود ندارد؛ هر بررسی حدود ۵ تا ۸ درخواست).

## ریسک و هشدار
- ✅ `sphinx install` گزینه‌ی سراسری Git یعنی `core.hooksPath` را برای همه‌ی مخزن‌های این رایانه تنظیم می‌کند (هوک‌های قبلی زنجیر می‌شوند) و هوک‌های بومی پرسش‌نامه و یک سرور MCP را به تنظیمات Claude Code اضافه می‌کند. برگشت: `sphinx uninstall`، محدودکردن: `sphinx install --repo`.
- ✅ کد تغییرکرده و فایل‌های مرتبط (به‌جز فایل‌های نادیده‌گرفته‌شده؛ `.env` و کلید خصوصی به‌طور پیش‌فرض کنار گذاشته می‌شوند) به ارائه‌دهنده‌ی مدل می‌رود. سر مشتری: `.sphinxignore` را پیش از بررسی اول بنویس. قاعده‌ها مسیر را می‌سنجند، پس رازِ چسبیده در کد را نمی‌گیرند.
- ✅ ممکن است push را تا ۲۵ دقیقه ببندد؛ شل عامل زودتر time-out می‌شود.

## مرتبط
[S191](../sources/README.md#s191) · [بررسی خودکار](../domains/claude-code/verification.md) · صفحه‌ی محصول: https://sphinx-six-theta.vercel.app/

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ کد install، hook و MCP خوانده شد (SHA `4e43537`). postinstall فقط پیام چاپ می‌کند. ⚠️ `sphinx install` تنظیم `core.hooksPath` در git را عوض می‌کند و hookهای SessionStart و PostToolUse را در `~/.claude/settings.json` و سرور MCP را در `~/.claude.json` می‌افزاید. `sphinx uninstall` همه را برمی‌گرداند.
- ⚠️ دیف کد به ارائه‌دهنده‌ی مدلی که خودت انتخاب کرده‌ای (OpenRouter یا endpoint سازگار با OpenAI) فرستاده می‌شود. تله‌متری ندارد. فقط بررسی نسخه‌ی npm دارد که با `SPHINX_UPDATE_CHECK=0` خاموش می‌شود.
