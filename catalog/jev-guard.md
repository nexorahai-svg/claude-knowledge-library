---
name: Jev / jev-guard
slug: jev-guard
category: claude-code-tooling
domains: [claude-code]
verdict: hold
status: researched
summary: hook شخص ثالث که هر دستور و خروجی ابزار را برای امتیازدهی به سرویس بیرونی می‌فرستد؛ پیش‌فرض باز در خطا
url: https://github.com/leepokai/jev-guard
repo: "https://github.com/leepokai/jev-guard"
license: "MIT"
pricing: paid
risk: high
sources: [S36, S93]
found_in: [batch-01/P02, batch-01/P13, batch-01/P19]
last_checked: 2026-10-19
next_check: "2026-11-16"
---

# Jev / jev-guard

## چیست
✅ (کد خوانده شد) `jev-guard install claude` فایل **`~/.claude/settings.json` سراسری** را ویرایش می‌کند و hook با matcher `.*` روی PreToolUse، PostToolUse، UserPromptSubmit، SessionStart و InstructionsLoaded می‌گذارد. ✅ مخزن شخصی (leepokai، ۷۹ ستاره، ۳ نسخه در یک روز ۲۰۲۶-۰۹-۱۷)؛ **رسمی TypeSafe نیست**. Jev واقعاً مدل تصمیم‌گیری TypeSafe AI است (کارت مدل در Vercel AI Gateway).

## کی استفاده کنیم
⛔ نه. Claude Code خودش حالت auto (طبقه‌بند) و قواعد deny دارد ([امنیت MCP](../domains/claude-code/mcp-safety.md)).

## قیمت و مجوز
✅ کد MIT؛ نیاز به کلید API پولی. ✅ «۴ سنت برای ۱۰۰۰ بررسی» محاسبه‌ی خود README است (۰.۰۴۲ دلار برای هر میلیون توکن ورودی، با فرض ۱۰۰۰ توکن برای هر بررسی).

## ریسک و هشدار
⚠️ **چه چیزی بیرون می‌رود:** متن کامل هر دستور، پرامپت‌های اخیر تو، و بعد از هر ابزار **خروجی آن** (محتوای فایل، صفحه‌ی وب، خروجی دستور، تا حدود ۶۰ هزار کاراکتر)، به‌علاوه‌ی CLAUDE.md و skillها؛ به `api.typesafe.ai`، OpenRouter یا Vercel. یعنی رمزها و کد خصوصی ممکن است بیرون بروند. ⚠️ **پیش‌فرض باز در خطا:** اگر API در دسترس نباشد، همه‌چیز مجاز می‌شود (مگر `JEV_GUARD_FAIL_CLOSED=1`). کلید API به‌صورت متن ساده در `~/.jev-guard/config.json`. خود README: «حفاظ است، نه sandbox». در سه پست جدا با لحن مشابه تبلیغ شده بود.

## کمپین ادامه دارد (۲۰۲۶-۱۰-۱۹)
✅ پست @beaver_0x (https://x.com/beaver_0x/status/2111870631382008234) با تیتر دروغ «BlackRock چهار مخزن را لو داد» چهار پروژه‌ی معاملاتی عمومی (TradingAgents، OpenBB، freqtrade، QuantDinger) را معرفی و در پایان Jev را به‌عنوان «تصمیم خرید و فروش» تبلیغ کرد. ✅ QuantDinger واقعاً Jev را به‌عنوان دروازه‌ی پیش از معامله دارد (README). ⚠️ لینک QuantDinger در پست به freqtrade می‌رود. حالا چهار حساب با لحن مشابه Jev را تبلیغ کرده‌اند ([حساب‌های X](../research/x-accounts.md)). 🧭 «سریع» یعنی «درست» نیست؛ هر ادعای سود را با [سنجش ادعاهای عددی](../research/claim-testing.md) بسنج. این توصیه‌ی معامله نیست.

## مرتبط
[دستیار شخصی](../domains/claude-code/personal-assistant.md) · [امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S36](../sources/README.md#s36)
