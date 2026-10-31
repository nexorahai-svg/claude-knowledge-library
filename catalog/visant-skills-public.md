---
name: Visant Skills
slug: visant-skills-public
category: claude-code-tooling
domains: [claude-code, website]
verdict: assess
status: researched
summary: مجموعه‌ی skill برای ممیزی رابط «ضد slop»، موشن، فرانت‌اند، کپی و تدوین، با آشکارسازهای اجراشدنی و آزمون
use_when: "auditing a built screen for generic AI-looking UI before a PR ; comparing detector-based design gates with impeccable"
how: "Read the SKILL.md files and scripts/*.mjs first (rule 4); install with `npx skills add pedrojaques99/visant-skills-public --skill visant-killer` only on request; run detectors on a throwaway copy, they are plain Node scripts"
url: https://github.com/pedrojaques99/visant-skills-public
repo: "https://github.com/pedrojaques99/visant-skills-public"
license: "MIT"
pricing: free
risk: low
sources: [S208]
found_in: [watch-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Visant Skills

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و `gh api`) مخزن `pedrojaques99/visant-skills-public`، MIT (فایل LICENSE خوانده شد)، حدود ۷۲ ستاره، ساخته‌شده ۲۰۲۶-۱۰-۲۸، push ۲۰۲۶-۱۰-۲۹. README پرتغالی-انگلیسی. skillها هر کدام اول می‌بینند مخزن هدف چه دارد (gateها، توکن‌ها) و بعد عمل می‌کنند. «killer» اسکریپت `killer-scan.mjs` را روی کد اجرا می‌کند و چند آشکارساز دارد: نشانه‌های ساخت AI (impeccable)، دور زدن توکن (رنگ Tailwind خام)، تیک‌های کپی (em-dash و غیره) و «نویز» (مثل پله‌ی شفافیت). `npm test` هر قانون را با فیکسچر از دو طرف آزمایش می‌کند؛ ادعای README: روی سه مخزن عمومی Next.js سنجیده و کالیبره شده.
❓ کد آشکارسازها و skillهای موشن و تدوین خوانده یا اجرا نشد. ❓ قانون‌ها برای سایت فارسی و راست‌به‌چپ سنجیده نشده‌اند. ❓ مخزن چند روزه است؛ پایداری معلوم نیست.

## کی استفاده کنیم
🧭 مقایسه با [impeccable](impeccable.md) برای دروازه‌ی کیفیت طراحی پیش از تحویل سایت. فقط ایده و آشکارسازها را بیاموز، متن skillها را کپی نکن.

## قیمت و مجوز
MIT، رایگان.

## ریسک و هشدار
ریسک پایین؛ اسکریپت Node را فقط روی نسخه‌ی دورریختنی پروژه اجرا کن.

## مرتبط
- https://github.com/pedrojaques99/visant-skills-public · [S208](../sources/README.md#s208)
