---
name: skill-scanner
slug: cisco-skill-scanner
category: claude-code-tooling
domains: [claude-code, security]
verdict: trial
status: researched
summary: اسکنر امنیتی «بهترین تلاش» برای مهارت‌های عامل (تزریق پرامپت، نشت داده، کد مخرب)
use_when: "vetting a third-party Claude skill or plugin before installing it ; auditing skills in a repo"
how: "Trial first on a small task: pip/uv install cisco-ai-skill-scanner then run skill-scanner on a skill folder (use --lenient for .claude/commands); run on a copy, no LLM keys needed for static mode"
url: https://github.com/cisco-ai-defense/skill-scanner
repo: "https://github.com/cisco-ai-defense/skill-scanner"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# skill-scanner

## چیست
✅ اسکنر امنیتی «بهترین تلاش» برای مهارت‌های عامل (تزریق پرامپت، نشت داده، کد مخرب) با قواعد YAML/YARA-X، تحلیل AST و داوری اختیاری LLM. ✅ سازمان Cisco AI Defense؛ README صریحاً می‌گوید نبود یافته به معنی امن بودن نیست.

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: vetting a third-party Claude skill or plugin before installing it؛ auditing skills in a repo. وضعیت: 🧭 قبل از هر استفاده روی یک کار کوچک امتحان شود.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۲,۶۶۹ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ❓ نقل‌قول «بهترین تلاش» از README را خودم دوباره تطبیق ندادم. متن فایل LICENSE مخزن Apache-2.0 است (API گیت‌هاب NOASSERTION نشان می‌دهد).
- ابزار دفاعی؛ حالت LLM-judge ممکن است محتوا را به API بفرستد (اختیاری). SPDX در GitHub NOASSERTION است ولی متن LICENSE آپاچی است.
- ❓ موتورهای تشخیص و آزمون‌ها خوانده نشد. کد منبع به‌طور کامل خوانده نشد؛ اجرا یا نصب نشد.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/cisco-ai-defense/skill-scanner
