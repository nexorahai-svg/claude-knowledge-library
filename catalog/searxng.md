---
name: SearXNG
slug: searxng
category: research-tools
domains: [claude-code, website, apps]
verdict: adopt
status: researched
summary: موتور فراجستجوی متن‌باز که خودت اجرا می‌کنی؛ جستجوی رایگان با خروجی JSON برای اسکریپت و عامل
use_when: "paid search (e.g. Firecrawl) has no credits ; a product or assistant must search the web without per-request cost"
how: "run SearXNG by container on 127.0.0.1 (AGPL-3.0), enable json under search.formats in settings.yml or you get 403, pin a commit; never expose publicly; no personal data in queries; add a health check"
url: https://docs.searxng.org
repo: https://github.com/searxng/searxng
license: AGPL-3.0
pricing: free
risk: medium
sources: [S69, S70]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# SearXNG

## چیست
✅ موتور فراجستجو: پرسش را به چند موتور جستجو می‌فرستد و نتیجه‌ها را یک‌جا برمی‌گرداند. طبق توضیح خود پروژه، کاربر ردیابی نمی‌شود. سه روش نصب در مستندات: کانتینر، اسکریپت نصب، و گام‌به‌گام.

✅ خروجی `json`، `csv` و `rss` باید در `settings.yml` زیر `search.formats` روشن شود؛ پیش‌فرض فقط `html` است و قالب روشن‌نشده خطای ۴۰۳ می‌دهد.

## کی استفاده کنیم
🧭 وقتی جستجوی پولی (مثل Firecrawl) اعتبار ندارد، یا محصول خودش باید روی اینترنت جستجو کند بی‌آنکه هزینه‌ی هر درخواست بدهد ([برنامه‌ی تحقیق](../research/x-research-plan.md)).

🔬 در یک فروشگاه واقعی (دفتر پروژه‌ها) دستیار سایت با آن جستجو می‌کند: فقط روی `127.0.0.1:8888`، با JSON روشن، نسخه‌ی قفل‌شده روی یک commit، کاربر سیستمی بدون شل، و سرویس systemd محدودشده. پرسش‌هایی که داده‌ی شخصی دارند رد می‌شوند و نشانی‌های رسمی اول می‌آیند. نصب از صفر در WSL حدود ۱ دقیقه و ۲۰ ثانیه.

## قیمت و مجوز
✅ رایگان. ✅ AGPL-3.0. 🧭 اجرای بی‌تغییر برای خودمان مشکلی ندارد؛ اگر کدش را تغییر دهی و به‌عنوان سرویس به دیگران بدهی، AGPL انتشار کد تغییرکرده را می‌خواهد (متن کامل مجوز را آن موقع بخوان).

## ریسک و هشدار
- ⚠️ پرسش‌ها به موتورهای بیرونی (گوگل، Bing و…) می‌روند؛ داده‌ی شخصی در پرسش ننویس.
- ⚠️ موتورها ممکن است درخواست خودکار را محدود یا مسدود کنند؛ نتیجه همیشه کامل نیست. 🧭 یک بررسی سلامت بگذار.
- ⚠️ 🧭 نمونه را عمومی نکن (روی `127.0.0.1` یا پشت VPN)؛ نمونه‌ی باز مورد سوءاستفاده قرار می‌گیرد.
- حکم 🧪: فقط در یک پروژه آزموده شد و نگهداری (به‌روزرسانی، موتورهای خراب) با خودمان است.

## مرتبط
[برنامه‌ی تحقیق X](../research/x-research-plan.md) · [S69](../sources/README.md#s69) · [S70](../sources/README.md#s70)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
