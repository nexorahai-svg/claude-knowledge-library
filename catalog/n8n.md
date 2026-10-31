---
name: n8n
slug: n8n
category: agents-memory
domains: [website, social-media]
verdict: trial
status: researched
summary: خودکارسازی جریان کار و عامل هوش مصنوعی بدون کدنویسی سنگین؛ خودمیزبان
use_when: "connecting website forms, email, social platforms and AI without code ; building automation workflows"
how: "Trial first on a small task: self-host n8n (Sustainable Use licence: internal use free, reselling restricted); run 2.45.5 or newer (Oct 2026 advisories, three high) and keep it updated and give credentials least privilege"
url: https://n8n.io
repo: "https://github.com/n8n-io/n8n"
license: "Sustainable Use (fair-code، متن‌باز OSI نیست)"
pricing: freemium
risk: medium
sources: [S158]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# n8n

## چیست
✅ (بررسی ۲۰۲۶-۱۰-۳۱) n8n@2.45.7 (۲۰۲۶-۱۰-۳۰): رفع اشکال؛ از جمله مسیرهای مخصوص گردش‌کار حالا برای خواندن داده‌ی اجرا مجوز `execution:read` می‌خواهند. حداقل نسخه‌ی امن همان 2.45.5 می‌ماند؛ Sustainable Use بی‌تغییر: https://github.com/n8n-io/n8n/releases
✅ (جاروی ۲۰۲۶-۱۰-۳۱) در ۲۰۲۶-۱۰-۲۸ حداقل ۱۲ هشدار امنیتی منتشر شد، از جمله سه مورد شدید: اجرای کد در پردازش اصلی با گره‌های Code منسوخ (GHSA-9p7v-45m2-wxgj)، پیکربندی ناامن GraphicsMagick (GHSA-f2cw-9483-7vcp) و جداسازی ناکافی در ارزیابی عبارت گردش‌کار (GHSA-gx3v-3x3v-f8r5). رفع در 2.45.5 و 2.46.1 و 1.123.89 و 3.0.1 است، پس نسخه‌ی پایدار فعلی 2.45.7 وصله‌شده است و هر نسخه‌ی پایین‌تر از 2.45.5 باید ارتقا یابد: https://github.com/n8n-io/n8n/security/advisories
✅ (جاروی ۲۰۲۶-۱۰-۲۸) n8n@2.45.4 (۲۰۲۶-۱۰-۲۶؛ رفع اشکال sandbox و زیرگردش‌کار؛ امنیتی نیست)؛ مجوز Sustainable Use بی‌تغییر.
✅ ابزار workflow (حدود ۲۰۹ هزار ستاره، فعال). مجوز Sustainable Use: استفاده‌ی داخلی آزاد، ولی فروش آن به‌عنوان سرویس محدود است.

## کی استفاده کنیم
🧭 برای اتصال فرم سایت، ایمیل، شبکه‌های اجتماعی و هوش مصنوعی بدون کد. ⚠️ نسخه‌ی خودمیزبان را به‌روز نگه دار (هشدار اکتبر ۲۰۲۶ در گره Supabase: [هشدارها](../domains/security/advisories-2026-10.md))؛ کلیدها با کمترین دسترسی.

✅ (بررسی نسخه، ۲۰۲۶-۱۰-۳۰) آخرین release در GitHub: n8n@2.45.6 (۲۰۲۶-۱۰-۲۹)؛ مجوز مخزن بی‌تغییر. یادداشت انتشار یک نسخه‌ی وصله‌ای است و حکم کارت عوض نمی‌شود.
