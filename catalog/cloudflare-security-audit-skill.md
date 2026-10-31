---
name: Cloudflare Security Audit Skill
slug: cloudflare-security-audit-skill
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: skill رسمی Cloudflare برای ممیزی امنیتی چندمرحله‌ای یک مخزن با یافته‌های ماشین‌خوان و راستی‌آزمایی مستقل
use_when: "running a deep multi-agent security audit of one repository before launch ; comparing against our own security-review routine and past multi-agent audits"
how: "Read SKILL.md and the validate-*.cjs scripts first; install with `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` only on request; run target code only inside an OS sandbox with no network, otherwise findings stay needs_validation"
url: https://github.com/cloudflare/security-audit-skill
repo: "https://github.com/cloudflare/security-audit-skill"
license: "MIT"
pricing: free
risk: medium
sources: [S208]
found_in: [watch-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Cloudflare Security Audit Skill

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و `gh api`) مخزن `cloudflare/security-audit-skill` زیر سازمان Cloudflare، MIT، ساخته‌شده ۲۰۲۶-۰۶-۱۸، آخرین push ۲۰۲۶-۰۹-۱۴. README می‌گوید از همین skill ابزار کشف آسیب‌پذیری Cloudflare شروع شد (پست رسمی وبلاگ: https://blog.cloudflare.com/build-your-own-vulnerability-harness که باز می‌شود). شش فاز: شناسایی و نقشه‌ی پوشش، شکار با عامل‌های جدا، اعتبارسنجی هر نامزد با عامل تازه‌ای که می‌کوشد ردش کند، خروجی ساخت‌یافته (`findings.json` با طرحواره)، راستی‌آزمایی مستقل رکوردها و گزارش خنثی. سه حکم: `confirmed`، `needs_validation`، `rejected`. دو اعتبارسنج بدون وابستگی Node دارد. اجراهای پشت‌سرهم روی همان مخزن روی هم جمع می‌شوند.
✅ شرط README: مدلی با زیرعامل موازی، Node.js و sandbox در سطح سیستم‌عامل برای هر کدِ هدف (بدون شبکه، محیط پاک‌شده، محدودیت منابع)؛ بدون آن یافته «needs_validation» می‌ماند.
❓ شمار ستاره (حدود ۵۳ هزار برای مخزنی چهارماهه) غیرعادی است؛ سازمان رسمی است ولی عدد را مدرک اعتماد نگیر. ❓ کد اعتبارسنج‌ها و هزینه‌ی توکن یک اجرا خوانده یا اندازه‌گیری نشد.

## کی استفاده کنیم
🧭 پیش از انتشار یک پروژه‌ی مهم؛ با دستور `/security-review` خودمان و تجربه‌ی ممیزی چندعاملی پروژه‌های قبلی مقایسه شود. هزینه‌ی چندعاملی زیاد است؛ پیش از اجرا از کاربر تخمین بگیر (قانون بودجه).

## قیمت و مجوز
MIT، رایگان؛ هزینه فقط توکن مدل.

## ریسک و هشدار
ریسک متوسط: عامل‌ها کد هدف را می‌خوانند و ممکن است بسازند و اجرا کنند؛ فقط داخل sandbox. خروجی ممیزی خودش حساس است (آسیب‌پذیری‌های واقعی)؛ مسیر خروجی را بیرون مخزن بگذار.

## مرتبط
- https://github.com/cloudflare/security-audit-skill · [S208](../sources/README.md#s208)
