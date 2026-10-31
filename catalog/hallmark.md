---
name: Hallmark (skill طراحی)
slug: hallmark
category: design-inspiration
domains: [website, security]
verdict: assess
status: researched
summary: skill طراحی MIT از Together AI برای Claude Code، Codex، Cursor و OpenCode با ۵۰ تم، lint طراحی در مرورگر و hook اختیاری؛ بدون آزمون ما
use_when: "a generated landing page looks generic and needs a stricter anti-AI-slop visual system ; comparing design skills next to the official frontend-design skill"
how: "Do not install without the user's yes; npx skills add nutlope/hallmark -g runs a third-party installer, so first read skills/hallmark/SKILL.md and every scripts/*.mjs, never run install-hook.mjs or set TOGETHER_API_KEY"
url: https://github.com/Nutlope/hallmark
repo: "https://github.com/Nutlope/hallmark"
license: "MIT"
pricing: free
risk: high
sources: [S190]
found_in: [watch-2026-10-28]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Hallmark (skill طراحی)

## چیست
- ✅ مخزن MIT، حدود ۴۰٬۵۰۰ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۸. نسخه‌ی skill: ۲٫۰٫۰ (فیلد `version` در SKILL.md). release ثبت‌شده در GitHub ندارد (GitHub API): https://github.com/Nutlope/hallmark
- ✅ README: «ساخته‌ی Together AI». skill برای Claude Code، Codex، Cursor و OpenCode؛ از ۵۰ تم سه تا پیشنهاد می‌دهد، بر پایه‌ی کار بازدیدکننده صفحه می‌سازد، سپس با `sloplint.mjs --render` صفحه را در مرورگر واقعی در هشت عرض می‌سنجد و یک مرورگر تازه‌زمینه بازبینی می‌کند. دستورهای `/hallmark redesign` و `/hallmark audit` هم دارد.
- ✅ حالت «custom» تم را کنار می‌گذارد. ۷۵۵ عکس با مجوز آزاد را فقط به‌صورت پیوند (Wikimedia Commons) نگه می‌دارد و منبع را در صفحه ذکر می‌کند.
- ✅ فایل‌های اجرایی: `scripts/` شامل `capture.mjs`، `imagegen.mjs`، `install.mjs`، `install-hook.mjs`، `lint-hook.mjs`، `sloplint*.mjs`، `theme.mjs`. نصب: `npx skills add nutlope/hallmark -g` یا افزونه‌ی Claude Code با `/plugin marketplace add nutlope/hallmark`.
- ❓ اینکه خروجی از skill رسمی `frontend-design` بهتر باشد آزموده نشده؛ ستاره معیار نیست. خروجی صفحه‌ی HTML/CSS مستقل است، نه کد اپ موبایل.

## کی استفاده کنیم
- 🧭 فقط پس از بازبینی کد و فقط برای وب‌سایت: یک آزمون کوچک روی صفحه‌ی نمونه کنار [frontend-design](frontend-design.md). برای اپ موبایل و محتوای شبکه‌ی اجتماعی مناسب نیست.

## قیمت و مجوز
- ✅ رایگان، MIT: https://github.com/Nutlope/hallmark/blob/main/LICENSE
- ✅ مرحله‌ی «comp» (تصویر پیش‌طرح) فقط وقتی `TOGETHER_API_KEY` تنظیم شده باشد فعال می‌شود و پولی است (Together AI)؛ بدون کلید کار می‌کند (SKILL.md و flow.md).

## ریسک و هشدار
- ✅ SKILL.md دستیار را به اجرای اسکریپت‌های Node وامی‌دارد؛ lint رندر `puppeteer-core` و Chrome می‌خواهد (`npm i -g puppeteer-core`)، `capture.mjs` از URL یا سرور dev عکس می‌گیرد، و `imagegen.mjs` در صورت وجود کلید به Together AI درخواست می‌فرستد.
- ✅ `install-hook.mjs` یک hook PostToolUse به Claude Code اضافه می‌کند که با هر نوشتن فایل اجرا می‌شود؛ آن را نصب نکن مگر پس از خواندن کد.
- ✅ `allowed-tools` تعریف نشده. 🧭 طبق قانون ۴ پیش از نصب SKILL.md، `references/flow.md` و همه‌ی `scripts/*.mjs` را بخوان.
- ✅ نصب‌کننده `npx skills` بسته‌ی شخص ثالث است.

## مرتبط
[سبک‌های طراحی](../domains/website/02-design/design-styles.md) · [S190](../sources/README.md#s190) · https://www.usehallmark.com
