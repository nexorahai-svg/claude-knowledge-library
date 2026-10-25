---
name: Google Workspace CLI (gws)
slug: google-workspace-cli
category: agents-memory
domains: [claude-code]
verdict: trial
status: researched
summary: CLI سازمان googleworkspace برای دسترسی عامل به Gmail، تقویم و Drive؛ رسماً پشتیبانی نمی‌شود
url: https://github.com/googleworkspace/cli
repo: "https://github.com/googleworkspace/cli"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S36]
found_in: [batch-01/P15, batch-01/P19]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Google Workspace CLI (gws)

## چیست
✅ ابزار Rust در سازمان googleworkspace (کپی‌رایت Google LLC)، حدود ۳۱.۶ هزار ستاره. ✅ README صریح: «این محصول **رسماً پشتیبانی‌شده‌ی Google نیست**» و قبل از ۱.۰ تغییرات ناسازگار انتظار می‌رود. بیش از ۱۰۰ فایل SKILL.md برای عامل‌ها؛ MCP ندارد. بسته‌ی npm `@googleworkspace/cli` اصل است (نگهدارنده‌ی حساب Google).

## کی استفاده کنیم
🧭 فقط با **دسترسی فقط‌خواندنی**، در پروژه‌ی Google Cloud خودت:
```bash
gws auth login --readonly -s gmail,calendar,drive
```
✅ پرچم `--readonly` در کد منبع هست (README نامی از آن نمی‌برد).

## قیمت و مجوز
✅ Apache-2.0، رایگان. نیاز به کلاینت OAuth در پروژه‌ی Google Cloud خودت.

## ریسک و هشدار
⚠️ **دستور `gws auth setup` که پست‌ها گفته بودند فقط‌خواندنی نیست:** فهرست پیش‌فرض دسترسی‌ها شامل `gmail.modify` است. با دسترسی نوشتن، عامل می‌تواند به اسم تو ایمیل بفرستد. ✅ توکن‌ها با AES-256-GCM رمز می‌شوند (کلید در keyring سیستم). ⚠️ محتوای ایمیل و Drive متن غیرقابل‌اعتماد است (prompt injection). نصب npm یک فایل اجرایی از GitHub دانلود می‌کند؛ دانلود مستقیم از Releases امن‌تر است. آخرین نسخه 0.22.5 (۲۰۲۶-۰۳-۳۱) با وجود commitهای تازه‌تر.

## مرتبط
[دستیار شخصی](../domains/claude-code/personal-assistant.md) · [امنیت MCP و افزونه‌ها](../domains/claude-code/mcp-safety.md) · [S36](../sources/README.md#s36)
