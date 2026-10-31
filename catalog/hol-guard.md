---
name: HOL Guard
slug: hol-guard
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: «آنتی‌ویروس عامل» محلی: پیش از اجرا فرمان شل، دسترسی به فایل و راز، نصب بسته و فراخوانی ابزار MCP را بررسی می‌کند و اجازه، مسدود یا پرسش می‌دهد
use_when: "judging whether a runtime guard for agent shell, file, package-install and MCP calls is worth adding next to our own hooks ; auditing a third-party plugin, skill or MCP server before installing it"
how: "Do not install on the main machine yet (rule 4, it hooks into agents); read docs/guard/harness-support.md and local-vs-cloud.md first; then try `pipx install hol-guard` and `hol-guard init` only in a throwaway project, decline the cloud connect step"
url: https://github.com/hashgraph-online/hol-guard
repo: "https://github.com/hashgraph-online/hol-guard"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S208]
found_in: [watch-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# HOL Guard

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و `gh api`) مخزن `hashgraph-online/hol-guard`، Apache-2.0 (فایل LICENSE در مخزن هست)، حدود ۱٬۰۲۰ ستاره، ساخته‌شده ۲۰۲۶-۰۳-۲۸، push همان روز. بسته‌ی پایتون `hol-guard` (نیاز Python 3.10 به بالا و pipx). طبق README فرمان شل، دسترسی به فایل، نصب بسته و فراخوانی ابزار MCP را پیش از اجرا بررسی می‌کند، نشت راز و عملیات مخرب و تزریق پرامپت و ریسک زنجیره‌ی تأمین را تشخیص می‌دهد و طبق سیاست تو اجازه می‌دهد، مسدود می‌کند یا می‌پرسد. با hook بومی عامل‌ها، پروکسی MCP مدیریت‌شده و یکپارچه‌سازی راه‌اندازی وصل می‌شود؛ پوشش بسته به رویدادهایی است که هر عامل می‌دهد (جدول `docs/guard/harness-support.md`). `hol-guard plugin` منبع افزونه یا skill را پیش از بارگذاری وارسی می‌کند.
✅ بدون حساب محلی کار می‌کند؛ «Guard Cloud» (سابقه‌ی مشترک، سیاست تیمی) اختیاری است و `hol-guard connect` آن را وصل می‌کند.
❓ کد و رفتار واقعی hookها خوانده یا آزموده نشد؛ ❓ اینکه با hookهای خودِ ما و Claude Code تداخل ندارد؛ ❓ آیا چیزی بدون اجازه به سرویس بیرونی می‌فرستد.

## کی استفاده کنیم
🧭 مقایسه با نگهبان‌های داخلی [امنیت MCP](../domains/claude-code/mcp-safety.md) و hookهای خودمان؛ اگر نتیجه‌ی آزمایش در پروژه‌ی دورریختنی خوب بود، برای وارسی افزونه و skillهای شخص ثالث پیش از نصب.

## قیمت و مجوز
Apache-2.0؛ محلی رایگان. بخش Cloud (تیمی) اختیاری و احتمالاً پولی است ❓ (قیمتش خوانده نشد).

## ریسک و هشدار
ریسک متوسط: ابزاری که به hookهای عامل وصل می‌شود خودش سطح حمله است و می‌تواند فرمان‌ها را ببیند. «ستاره‌ی زیاد» اعتماد نیست؛ نصب نکن مگر کاربر بخواهد (قانون ۴). بخش cloud را وصل نکن.

## مرتبط
- https://github.com/hashgraph-online/hol-guard · https://hol.org/guard/activate
- [امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S208](../sources/README.md#s208)
