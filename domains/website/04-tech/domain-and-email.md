# دامنه، ایمیل شرکتی و ارسال ایمیل از سایت

> **نوع سند:** دستورالعمل
> **هدف این سند:** یک ایمیل شرکتی رایگان روی دامنه‌ی خود کسب‌وکار، با رکوردهای ضد جعل درست، و ارسال امن پیام فرم سایت به آن.
> **موضوع تحقیق:** Zoho Mail رایگان و Mail Lite، SPF، DKIM، DMARC، CAA، قوانین فرستنده‌ی گوگل، IMAP در Zoho و Microsoft 365، EmailJS و جایگزین‌هایش.
> **منابع:** [S54 دامنه و ایمیل](../../../sources/README.md#s54) · [S53 Cloudflare](../../../sources/README.md#s53) · [S62 DNS، ایمیل و سئو برای سرور خودمان](../../../sources/README.md#s62)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۱۷
> **دفعه‌ی بعد چک شود:** شرایط طرح رایگان Zoho (تعداد کاربر، IMAP)؛ ❓ IMAP در Mail Lite و رکوردهای مرکز داده‌ی امارات؛ زمان بازنشستگی Basic auth برای SMTP AUTH در Microsoft 365؛ قیمت و سقف EmailJS؛ قوانین فرستنده‌ی گوگل و Yahoo.

روی سایت یک سایت مشتری اجرا شد (دفتر پروژه‌ها) 🔬: `info@` روی Zoho رایگان، DMARC با `p=reject`، پیام فرم سایت به همین صندوق.

---

## ۱. ایمیل شرکتی رایگان: Zoho Mail «Forever Free»

✅ از صفحه‌ی قیمت Zoho:
- تا **۵ کاربر**؛ از کاربر ششم همه پولی می‌شوند
- **۵ گیگابایت** برای هر کاربر
- **فقط یک دامنه**
- **بدون IMAP، POP و ActiveSync**: فقط وب و اپ موبایل خود Zoho (یعنی در Outlook یا اپ ایمیل گوشی اضافه نمی‌شود)
- هر پیام حداکثر ۱۰۰ گیرنده‌ی بیرونی
- فقط در بعضی مراکز داده موجود است
- ❓ سقف پیوست طرح رایگان در صفحه‌ی رسمی پیدا نشد

[کارت Zoho Mail](../../../catalog/zoho-mail.md)

🧭 برای یک شرکت کوچک که یک یا دو صندوق (`info@`) می‌خواهد کافی است. اگر کارمندان باید در Outlook یا Gmail گوشی ایمیل را ببینند، طرح پولی لازم است.

## ۲. رکوردهای ضد جعل

| رکورد | نمونه (Zoho) | معنی |
|---|---|---|
| MX | `mx.zoho.com` (۱۰)، `mx2.zoho.com` (۲۰)، `mx3.zoho.com` (۵۰)، برای حساب مرکز داده‌ی آمریکا | ایمیل دامنه کجا تحویل شود. ✅ پسوند نام سرور MX به **مرکز داده‌ی حساب** بستگی دارد؛ مقدار دقیق را از Admin Console بخش Tools & Configurations بردار |
| SPF (TXT روی `@`) | `v=spf1 include:zohomail.com -all` | فقط این سرورها حق ارسال دارند. `-all` یعنی بقیه رد؛ `~all` یعنی «مشکوک» وقتی سرور دیگری هم از طرف دامنه می‌فرستد |
| DKIM (TXT روی `<selector>._domainkey`) | کلیدی که Zoho می‌دهد | امضای هر ایمیل |
| DMARC (TXT روی `_dmarc`) | `v=DMARC1; p=reject; sp=reject; adkim=s; aspf=s` | اگر SPF و DKIM نخواند با ایمیل چه شود |

⚠️ ✅ **اصلاح ۲۰۲۶-۱۰-۱۷:** این‌جا قبلاً `include:zoho.com` نوشته شده بود. راهنمای رسمی SPF در Zoho مقدار `include:zohomail.com` را می‌دهد (و `include:one.zoho.com` برای کسی که چند سرویس Zoho را از طرف دامنه استفاده می‌کند). اگر دامنه‌ای با مقدار قدیمی ساخته‌ای، با «Verify SPF Record» در Admin Console چک کن. ❓ مقدار SPF و MX برای مرکز داده‌ی امارات در صفحه‌ی رسمی نیامده؛ از Admin Console همان حساب بردار.

✅ RFC 7489: `none` یعنی کاری نکن (فقط گزارش)، `quarantine` یعنی مشکوک (معمولاً اسپم)، `reject` یعنی رد در همان لحظه‌ی تحویل.
✅ گوگل: همه‌ی فرستنده‌ها SPF **یا** DKIM لازم دارند؛ فرستنده‌ی انبوه (بیش از ۵٬۰۰۰ در روز به Gmail) هر سه را لازم دارد و حداقل DMARC می‌تواند `none` باشد.

🧭 ترتیب امن: اول SPF و DKIM، بعد DMARC با `p=none` و چند روز بررسی، بعد `quarantine` و `reject`. 🔬 در یک سایت مشتری چون **هیچ سرویس دیگری از طرف دامنه ایمیل نمی‌فرستد**، مستقیم `reject` گذاشتیم و مشکلی نبود.
⚠️ 🧭 قبل از `reject` همه‌ی فرستنده‌های دامنه را فهرست کن (فرم سایت، خبرنامه، CRM، فاکتور). هر کدام که در SPF و DKIM نباشد، ایمیلش رد می‌شود.

🔬 دامنه‌ای که اصلاً ایمیل نمی‌فرستد: `v=spf1 -all` و DMARC با `p=reject` تا کسی به اسمش ایمیل جعل نکند.

### CAA: فقط صادرکننده‌ی گواهی خودمان

✅ (RFC 8659) رکورد CAA می‌گوید کدام مرجع صدور (CA) حق دارد برای دامنه گواهی بدهد. مرجع‌ها **باید** پیش از صدور آن را چک کنند. جستجو از همان نام شروع می‌شود و تا دامنه‌ی بالاتر می‌رود؛ پس رکورد روی `@` زیردامنه‌ها را هم پوشش می‌دهد مگر زیردامنه رکورد خودش را داشته باشد.

| رکورد | معنی |
|---|---|
| `0 issue "letsencrypt.org"` | ✅ فقط Let's Encrypt (نام شناسه‌ی رسمی‌اش در CAA `letsencrypt.org` است) |
| `0 issuewild ";"` | ✅ گواهی wildcard از هیچ مرجعی. وقتی `issuewild` هست، `issue` برای wildcard نادیده گرفته می‌شود |
| `0 iodef "mailto:security@example.com"` | ✅ اختیاری: نشانی گزارش تخلف؛ خودش چیزی را منع نمی‌کند |

- ⚠️ 🧭 اگر سرور (مثلاً Caddy) وقتی Let's Encrypt در دسترس نیست سراغ ZeroSSL می‌رود، یا آن را هم در CAA بگذار، یا بدان که با این رکورد فقط Let's Encrypt کار می‌کند.
- ✅ Let's Encrypt پارامترهای `accounturi` (فقط یک حساب ACME مشخص) و `validationmethods` (مثلاً فقط `tls-alpn-01`) را هم می‌شناسد. 🧭 سخت‌گیرانه‌تر است ولی جابه‌جایی سرور را هم سخت‌تر می‌کند.
- 🔬 MARIO E.G.S.H همین دو رکورد اول را در فهرست DNS پیش از انتشار گذاشته؛ هنوز روی دامنه‌ی زنده آزموده نشده (دفتر پروژه‌ها).

## ۳. خواندن صندوق از برنامه (IMAP و SMTP)

وقتی خود سایت باید ایمیل‌ها را بخواند یا از صندوق شرکت جواب بفرستد (مثلاً اتاق نامه‌ی پنل مدیریت):

| سرویس | واقعیت | برچسب |
|---|---|---|
| Zoho، **طرح رایگان** | IMAP، POP و ActiveSync ندارد | ✅ |
| Zoho، **طرح پولی سازمانی** | IMAP: `imappro.zoho.com` پورت ۹۹۳ (SSL)؛ SMTP: `smtppro.zoho.com` پورت ۴۶۵ (SSL) یا ۵۸۷ (TLS). حساب شخصی و سازمان رایگان: `imap.zoho.com` و `smtp.zoho.com` | ✅ |
| Zoho با تأیید دومرحله‌ای | برای برنامه‌ی بیرونی **رمز مخصوص برنامه** (app-specific password) لازم است | ✅ |
| Zoho Mail Lite | صفحه‌ی قیمت رسمی IMAP را برای Mail Lite صریح نمی‌نویسد؛ فروشنده‌ها می‌گویند دارد | ❓ قبل از خرید از Zoho بپرس یا یک ماه امتحان کن |
| Microsoft 365 | Basic auth برای IMAP و POP در **همه‌ی** tenantها خاموش است و دیگر روشن نمی‌شود؛ رمز برنامه هم کار نمی‌کند. برنامه‌ی خودت باید **OAuth 2.0** پیاده کند (یا Graph API). SMTP AUTH با Basic فعلاً هست ولی بازنشستگی‌اش اعلام شده | ✅ |

🔬 MARIO E.G.S.H: دو صندوق Zoho (`info@` عمومی، `services@` برای ادارات و پرونده‌ها)، با رمز مخصوص برنامه‌ی رمزشده در پایگاه داده. ❓ هنوز با سرور واقعی Zoho امتحان نشده. Microsoft 365 به‌خاطر نیاز به OAuth کنار گذاشته شد.

## ۴. ارسال پیام فرم سایت

| راه | کی | نکته |
|---|---|---|
| **EmailJS** (از مرورگر) | سایت ایستای بدون سرور | ✅ رایگان: ۲۰۰ درخواست در ماه، ۲ قالب. ⚠️ **محدود کردن دامنه‌های مجاز فقط در طرح پولی** (Personal، ماهی ۹ دلار، ۲٬۰۰۰ درخواست). کلید عمومی در مرورگر است، پس هر کسی می‌تواند از سایت دیگری با آن ایمیل بفرستد. ✅ گزینه‌های رایگان `blockHeadless` و `limitRate` در `emailjs.init` را روشن کن |
| **از Function سرور** (مثلاً Cloudflare Pages Functions با یک سرویس ارسال ایمیل) | وقتی سرور داری | 🧭 امن‌تر: کلید در سرور، ضد ربات (Turnstile) قبل از ارسال، ذخیره در پایگاه داده |

[کارت EmailJS](../../../catalog/emailjs.md)

🔬 در یک سایت مشتری: فرم اول در D1 ذخیره می‌شود (منبع اصلی و مطمئن) و EmailJS فقط اعلان می‌فرستد. گیرنده در **داشبورد EmailJS** تنظیم می‌شود، نه در کد سایت. بعد از عوض کردن ایمیل شرکت، قالب EmailJS را هم عوض کن؛ ما اول فراموش کردیم و پیام‌ها به ایمیل قدیمی رفت.
🧭 در قالب: «To» = ایمیل شرکت، «Reply-To» = ایمیل مشتری، «From Name» = «Website - نام مشتری».

---

## پرامپت

```text
Set up company email and form delivery following
~/Desktop/knowledge-library/domains/website/04-tech/domain-and-email.md.
List every service that sends mail as this domain first. Then give me the exact DNS
records (MX, SPF, DKIM, DMARC) for Cloudflare, starting DMARC at p=none unless the list
is only the mailbox provider. For the website form, store each lead server-side first,
verify Turnstile, and send only a notification email; never put a secret key in the
browser. If EmailJS is used, enable blockHeadless and limitRate and set Reply-To to the
customer's address.
```
