---
name: Zoho Mail
slug: zoho-mail
category: email-domain
domains: [website]
verdict: adopt
status: researched
summary: ایمیل شرکتی روی دامنه‌ی خود؛ طرح رایگان تا ۵ کاربر بدون IMAP، طرح پولی با IMAP و رمز مخصوص برنامه
url: https://www.zoho.com/mail/
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S54, S62]
found_in: [project/client, project/client]
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# Zoho Mail

## چیست
✅ میزبانی ایمیل روی دامنه‌ی خود کسب‌وکار (مثل `info@domain.com`).

## کی استفاده کنیم
🔬 ایمیل شرکتی یک سایت مشتری (`info@`) روی طرح رایگان، با SPF، DKIM و DMARC. 🧭 برای شرکت کوچکی که یک تا پنج صندوق می‌خواهد. راهنما: [دامنه و ایمیل شرکتی](../domains/website/04-tech/domain-and-email.md).

## قیمت و مجوز
✅ (https://www.zoho.com/mail/zohomail-pricing.html) Forever Free: تا ۵ کاربر، ۵ گیگابایت برای هر کاربر، یک دامنه، **بدون IMAP، POP و ActiveSync**، فقط در بعضی مراکز داده. ✅ (https://www.zoho.com/mail/help/adminconsole/rates-and-limits.html) حداکثر ۱۰۰ گیرنده‌ی بیرونی در هر پیام. ❓ سقف پیوست طرح رایگان در صفحه‌ی رسمی پیدا نشد.

✅ (https://www.zoho.com/mail/help/imap-access.html) **طرح پولی سازمانی:** IMAP `imappro.zoho.com:993` (SSL) و SMTP `smtppro.zoho.com:465` (SSL) یا `587` (TLS). حساب شخصی و سازمان رایگان: `imap.zoho.com` و `smtp.zoho.com`؛ ولی سازمان رایگانِ تازه IMAP ندارد. با تأیید دومرحله‌ای، برنامه‌ی بیرونی **رمز مخصوص برنامه** لازم دارد. ❓ صفحه‌ی قیمت رسمی IMAP را برای Mail Lite صریح نمی‌نویسد (فروشنده‌ها می‌گویند دارد)؛ قبل از خرید بپرس. 🔬 MARIO E.G.S.H دو صندوق (`info@` و `services@`) را برای خواندن و جواب دادن از پنل مدیریت آماده کرد؛ ❓ هنوز با سرور واقعی Zoho امتحان نشده.

✅ (https://www.zoho.com/mail/help/adminconsole/spf-configuration.html) SPF رسمی `v=spf1 include:zohomail.com -all` است، نه `include:zoho.com`. ✅ پسوند نام سرور MX به مرکز داده‌ی حساب بستگی دارد؛ مقدار دقیق را از Admin Console بردار. ❓ رکوردهای مرکز داده‌ی امارات در صفحه‌ی رسمی نیامده. راهنما: [دامنه و ایمیل](../domains/website/04-tech/domain-and-email.md).

## ریسک و هشدار
⚠️ ریسک متوسط: همه‌ی ایمیل شرکت نزد یک سرویس بیرونی است؛ تأیید دومرحله‌ای را روشن کن. 🔬 ایمیل‌های سیستمی (مثلاً کد ورود Cloudflare) ممکن است به پوشه‌ی «Notification» بروند، نه Inbox.

## مرتبط
[دامنه و ایمیل شرکتی](../domains/website/04-tech/domain-and-email.md) · [S54](../sources/README.md#s54) · [S62](../sources/README.md#s62)
