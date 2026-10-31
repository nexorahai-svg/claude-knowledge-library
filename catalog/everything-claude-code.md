---
name: Everything Claude Code (ECC)
slug: everything-claude-code
category: claude-code-tooling
domains: [claude-code]
verdict: assess
status: researched
summary: مجموعه‌ی بزرگ ۳۱۱ skill، ۷۱ عامل، ۹۷ دستور و ۲۷ hook برای Claude Code و ابزارهای دیگر؛ فقط برای ایده گرفتن، نصب نشود
url: https://github.com/affaan-m/ECC
repo: "https://github.com/affaan-m/ECC"
license: "MIT"
pricing: free
risk: medium
sources: [S157]
last_checked: 2026-10-25
next_check: "2027-01-23"
---

# Everything Claude Code (ECC)

## چیست
✅ مخزن `affaan-m/ECC` (نام قدیمی everything-claude-code)، مجوز MIT، حدود ۲۸۸ هزار ستاره، آخرین تغییر ۲۰۲۶-۱۰-۲۰. ۳۱۱ skill، ۷۱ عامل، ۹۷ دستور، پیکربندی MCP و ۲۷ hook؛ برای Claude Code، Codex، Cursor و چند ابزار دیگر. در شبکه‌های اجتماعی با ترفند «کامنت بگذار تا بفرستم» پخش می‌شود، در حالی که رایگان و عمومی روی GitHub است.

## چرا نصب نشود
- ✅ **۲۷ hook** روی تقریباً هر رخداد اجرا می‌شود (پیش و پس از هر ابزار، هر پیام کاربر، شروع و پایان جلسه)؛ هر کدام کد Node است که خودکار روی رایانه اجرا می‌شود. جلسه کندتر و پرهزینه‌تر می‌شود و با hookهای دیگر تداخل دارد.
- 🧭 صدها skill انتخاب Claude را شلوغ می‌کند؛ بیشتر بودن skill یعنی کیفیت بیشتر نیست.
- ✅ هر نسخه‌ی تازه کد جدید وارد رایانه می‌کند (ریسک زنجیره‌ی تأمین؛ [حوزه‌ی امنیت](../domains/security/README.md)).

## کی استفاده کنیم
🧭 فقط برای ایده: یک skill یا عامل خاص را کامل بخوان و نسخه‌ی خودت را بساز. سند `the-security-guide.md` آن خواندنی است.
