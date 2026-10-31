---
name: SkillSpector (NVIDIA)
slug: skillspector
category: claude-code-tooling
domains: [claude-code, security]
verdict: trial
status: researched
summary: اسکنر امنیتی skill عامل‌ها: تزریق دستور، نشت داده، زنجیره‌ی تأمین
use_when: "before installing any community skill"
how: "Trial first on a small task: uv tool install git+https://github.com/NVIDIA/skillspector.git, then skillspector scan ./my-skill/ --no-llm (no API key, offline-capable); Apache-2.0; a score is a signal, not proof of safety either way"
url: https://github.com/NVIDIA/SkillSpector
repo: "https://github.com/NVIDIA/SkillSpector"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S162]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# SkillSpector (NVIDIA)

## چیست
✅ ابزار NVIDIA (Apache-2.0، حدود ۲۲ هزار ستاره؛ آخرین نسخه v2.13.1 در ۲۰۲۶-۱۰-۲۳). ✅ README: نیاز به Python 3.12+؛ ۷۱ الگوی آسیب‌پذیری؛ حالت --no-llm فقط تحلیل ایستا.

✅ نصب و اجرا (https://github.com/NVIDIA/SkillSpector، ۲۰۲۶-۱۰-۲۷): uv tool install git+https://github.com/NVIDIA/skillspector.git ؛ skillspector scan ./my-skill/ --no-llm

## کی استفاده کنیم
🧭 پیش از نصب هر skill جامعه؛ امتیاز پایین اثبات امنیت نیست ([حوزه‌ی امنیت](../domains/security/README.md)).
