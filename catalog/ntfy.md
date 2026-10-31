---
name: ntfy
slug: ntfy
category: claude-code-tooling
domains: [claude-code, apps, security]
verdict: trial
status: researched
summary: فرستادن اعلان به گوشی و دسکتاپ با یک درخواست HTTP؛ سرور عمومی ntfy.sh یا سرور خودت با Docker
use_when: "phone alert when a long job (sweep, app build, backup, video render) finishes or fails ; server down or disk full alert"
how: "Trial first on a small task: end the script with curl -d msg ntfy.sh/<long-random-topic>; on public server the topic name is the password so use a long random one and never send secrets; self-host with Docker and auth-default-access deny-all for private; use Firebase for customer app notifications"
url: https://ntfy.sh
repo: "https://github.com/binwiederhier/ntfy"
license: "Apache-2.0 یا GPLv2 (دوگانه)"
pricing: freemium
risk: medium
sources: [S118]
found_in: [batch-12]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# ntfy

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v2.35.0 (۲۰۲۶-۱۰-۳۰) با یک رفع امنیتی: درگاه push ماتریکس می‌توانست با کلید دارای بایت NUL پیامی را زیر موضوع محافظت‌شده ذخیره کند (فقط SQLite). رفع سهمیه و خطاهای 403 گاه‌به‌گاه؛ Apache-2.0 بی‌تغییر: https://github.com/binwiederhier/ntfy/releases/tag/v2.35.0
✅ سرویس «انتشار و اشتراک» برای اعلان: با یک درخواست POST یا PUT به آدرس یک «موضوع» (topic)، روی گوشی (Android و iOS) یا دسکتاپ اعلان می‌آید. سرور را می‌توانی خودت با Docker اجرا کنی. حدود ۳۵ هزار ستاره؛ نسخه‌ی v2.32.0 در ۲۰۲۶-۱۰-۱۸؛ فعال.

## کی استفاده کنیم
🧪 اول روی یک کار کوچک امتحان کن:
- 🧭 خبر دادن به گوشی وقتی یک کار طولانی یا زمان‌بندی‌شده تمام شد یا خطا داد (جاروی دو‌روزه، ساخت اپ، پشتیبان‌گیری، رندر ویدیو). یک خط `curl` در آخر اسکریپت کافی است ([دستیار شخصی](../domains/claude-code/personal-assistant.md)).
- 🧭 هشدار سرورهای پروژه‌ها، مثلاً قطع شدن سرویس یا تمام شدن فضا.
- برای اعلان داخل اپ‌های مشتری از سرویس رسمی Firebase استفاده کن ([کارت Firebase](firebase.md))؛ ntfy برای اعلان‌های خودمان است.

## قیمت و مجوز
✅ کد رایگان، با مجوز دوگانه Apache-2.0 و GPLv2 (README). ✅ سرور میزبانی‌شده بدون ثبت‌نام قابل استفاده است. طرح‌های پولی ماهانه ۵، ۱۰ و ۲۰ دلار هستند و موضوع رزروشده، پیام بیشتر، ایمیل و تماس تلفنی می‌دهند.

## ریسک و هشدار
⚠️ روی سرور عمومی بدون حساب، **نام موضوع حکم رمز را دارد**: هر کس نام را بداند، پیام‌ها را می‌خواند و می‌تواند پیام بفرستد. نام طولانی و تصادفی بساز و چیز محرمانه (رمز، اطلاعات مشتری) نفرست.
⚠️ مستندات رمزگذاری سرتاسری را نمی‌گوید ❓. پیام روی سرور ntfy.sh یا سرور خودت باز است.
✅ سرور خودت: برای سرور خصوصی `auth-default-access: deny-all` با کاربر و ACL. توکن‌های دسترسی فعلاً **دسترسی کامل به حساب** می‌دهند و توکن محدود هنوز نیامده.
✅ اعلان فوری iOS با سرور خودت: سرور تو شناسه‌ی پیام و هش آدرس موضوع را به ntfy.sh می‌فرستد، نه متن پیام. بدون این تنظیم، رسیدن اعلان ممکن است ساعت‌ها طول بکشد.

## مرتبط
[دستیار شخصی](../domains/claude-code/personal-assistant.md) · [S118](../sources/README.md#s118) · غربال دسته‌ی ۱۲
