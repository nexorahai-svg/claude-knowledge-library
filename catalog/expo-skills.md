---
name: Expo Skills
slug: expo-skills
category: claude-code-tooling
domains: [apps, claude-code]
verdict: trial
status: researched
summary: مخزن رسمی skillها و پلاگین Claude Code از Expo برای ساخت، بیلد و انتشار اپ‌های Expo
use_when: "React Native or Expo app work where the agent needs official Expo guidance ; EAS build or simulator tasks driven by an agent"
how: "claude plugin install expo@claude-plugins-official (or npx skills@latest add expo/skills --skill '*'); read each SKILL.md first; never run the feedback command that calls @expo/agent-cli"
url: https://github.com/expo/skills
repo: "https://github.com/expo/skills"
license: "MIT"
pricing: free
risk: medium
sources: [S205]
found_in: [watch-2026-10-29]
last_checked: 2026-10-31
next_check: "2027-01-28"
---

# Expo Skills

## چیست
✅ (۲۰۲۶-۱۰-۳۰، README و ساختار مخزن) مخزن `expo/skills` از 650 Industries (Expo)، مجوز MIT، ۳٬۷۵۵ ستاره، ساخته‌شده ۲۰۲۵-۱۱-۳۰، آخرین push ۲۰۲۶-۱۰-۲۹. دو پلاگین: `expo` (حدود ۲۰ skill) و `expo-experiments`. فایل `.mcp.json` فقط https://mcp.expo.dev/mcp را ثبت می‌کند. نصب: `claude plugin install expo@claude-plugins-official` یا `npx skills@latest add expo/skills --skill '*'`.
❓ همه‌ی SKILL.mdها خوانده نشد.

## کی استفاده کنیم
🧭 پروژه‌های Expo/React Native؛ اگر پروژه‌ی Flutter است لازم نیست. پیش از فعال‌کردن فایل‌ها را بخوان.

## قیمت و مجوز
مجوز MIT، رایگان. اجرای EAS هزینه دارد (طرح Expo).

## ریسک و هشدار
⚠️ skill مربوط به eas-simulator با npx نسخه‌ی `agent-device@latest` و `eas-cli@latest` را می‌گیرد و فایل `.env.eas-simulator` با توکن نشست می‌نویسد. بسیاری از skillها در پایان `npx --yes @expo/agent-cli@latest feedback ...` دارند؛ هرگز اجرا نشود چون داده بیرون می‌فرستد. اجرای EAS پولی است.

## مرتبط
- [expo](expo.md)
- [expo-mcp](expo-mcp.md)
- https://github.com/expo/skills

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
