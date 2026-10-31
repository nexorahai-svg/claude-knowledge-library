---
name: claude-mem
slug: claude-mem
category: agents-memory
domains: [claude-code, security]
verdict: assess
status: researched
summary: حافظه‌ی ماندگار بین جلسه‌ها که همه‌ی کار عامل را ضبط و دوباره تزریق می‌کند؛ ریسک حریم خصوصی
url: https://github.com/thedotmack/claude-mem
repo: "https://github.com/thedotmack/claude-mem"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S159, S198]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# claude-mem

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v15.7.0 (۲۰۲۶-۱۰-۳۰؛ Apache-2.0). ⚠️ یادداشت همین نسخه می‌گوید پیش از آن، وقتی پاسخ Claude Code رد می‌شد، به‌روزرسانی خودکار My Work سراغ عامل واردشده‌ی بعدی می‌رفت و روی رایانه‌ی دارای Codex، اجرای پنهان `codex exec` روی حساب ChatGPT صاحب رایانه می‌ساخت؛ در این نسخه رفع شد: https://github.com/thedotmack/claude-mem/releases/tag/v15.7.0 . ❓ گزارش زیرعامل: از v15.5.0 تله‌متری PostHog بازدید My Work را می‌شمارد؛ پیش از نصب بازبینی شود.
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v15.3.0 (۲۰۲۶-۱۰-۲۶)؛ Apache-2.0 بی‌تغییر.
✅ (Apache-2.0، حدود ۱۰۳ هزار ستاره). محل نگهداری داده در README روشن نیست.

## هشدار امنیتی
✅ CVE-2026-11330 (NVD، کم): ضعف هش در `computeObservationContentHash` تا نسخه‌ی 11.0.1؛ نسخه‌های 15.x اصلاح‌شده‌اند. نسخه‌ی قدیمی نگه ندار ([S198](../sources/README.md#s198)).

## کی استفاده کنیم
🧭 همه‌چیز، حتی راز و داده‌ی مشتری، ضبط می‌شود. حافظه‌ی داخلی Claude Code و `STATE.md` امن‌ترند.

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: v15.6.0 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
