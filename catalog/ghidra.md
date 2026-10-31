---
name: Ghidra
slug: ghidra
category: reverse-engineering
domains: [apps, security]
verdict: trial
status: researched
summary: دیس‌اسمبلر و دیکامپایلر باینری بومی از NSA
use_when: "inspecting native parts of our own app (Rust in Tauri, .so libraries, desktop binary) ; testing how hard reverse engineering is for our build"
how: "Trial first on a small task: run Ghidra (Apache-2.0) only on OUR OWN binaries, inside a VM or container; using it to copy others' apps violates library rules and usually terms and copyright"
url: https://github.com/NationalSecurityAgency/ghidra
repo: "https://github.com/NationalSecurityAgency/ghidra"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S120]
found_in: [batch-13]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Ghidra

## چیست
✅ دیس‌اسمبلر و دیکامپایلر باینری بومی از NSA. مجوز Apache-2.0؛ ~۹۱ هزار ستاره، فعال (۲۰۲۶-۱۰-۱۹).

## کی استفاده کنیم
🧪 باز کردن بخش‌های بومی خودمان (Rust در Tauri، کتابخانه‌های .so، باینری دسکتاپ). فقط روی خروجی خودمان، داخل ماشین مجازی یا کانتینر ([محافظت از اپ](../domains/apps/app-protection.md)).

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
⚠️ ابزار مهندسی معکوس است: فقط روی نرم‌افزار خودمان. استفاده روی اپ دیگران برای کپی، قانون اول کتابخانه و معمولاً شرایط استفاده و قانون حق نشر را می‌شکند. طبق قانون کتابخانه بدون درخواست کاربر نصب نشود.

## مرتبط
[محافظت از اپ و آزمون خودمان](../domains/apps/app-protection.md) · [S120](../sources/README.md#s120) · غربال دسته‌ی ۱۳
