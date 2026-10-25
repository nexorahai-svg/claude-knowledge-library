---
name: Supabase
slug: supabase
category: database-backend
domains: [website]
verdict: trial
status: researched
summary: پایگاه داده‌ی Postgres، ورود کاربر، ذخیره‌ی فایل و API به‌صورت سرویس؛ با MCP رسمی برای Claude
url: https://supabase.com/
repo: "https://github.com/supabase/supabase"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S19, S95, S125]
found_in: [batch-01/P00]
last_checked: 2026-10-19
next_check: "2026-11-16"
---

# Supabase

## چیست
✅ سرویس مدیریت‌شده‌ی Postgres: هر پروژه یک پایگاه داده‌ی اختصاصی دارد، به‌همراه ورود کاربر (auth)، ذخیره‌ی فایل، Edge Functions، realtime و API خودکار. کد اصلی متن‌باز است (Apache-2.0، حدود ۱۱۲ هزار ستاره) و با Docker Compose می‌شود خودت میزبانی کنی، ولی نسخه‌ی خودمیزبان «پشتیبانی جامعه» است و پشتیبان‌گیری و امنیتش با خودت است.

## کی استفاده کنیم
🧭 وقتی سایت **داده‌ی ماندگار** لازم دارد: فرم تماس که پیام‌ها را ذخیره می‌کند، پنل مشتری با ورود، وبلاگ یا CMS کوچک، قابلیت‌های زنده.
🧭 برای یک سایت معرفی ساده **زیادی است**؛ سرویس «فرم به ایمیل» یا فرم داخلی میزبان ساده‌تر است.

## قیمت و مجوز
✅ (https://supabase.com/pricing، ۲۰۲۶-۱۰-۱۷)

| | رایگان | Pro (از ۲۵ دلار در ماه) |
|---|---|---|
| پایگاه داده | ۵۰۰ مگابایت در هر پروژه | ۸ گیگابایت دیسک در هر پروژه |
| کاربر فعال ماهانه | ۵۰ هزار | ۱۰۰ هزار |
| ترافیک خروجی | ۵ گیگابایت (+۵ گیگ کش) | ۲۵۰ گیگابایت (+۲۵۰ گیگ کش) |
| فایل | ۱ گیگابایت، حداکثر ۵۰ مگ برای هر فایل | ۱۰۰ گیگابایت |
| تعداد پروژه | ۲ پروژه‌ی فعال | — |
| توقف خودکار | **بعد از ۱ هفته بی‌فعالیتی متوقف می‌شود** | متوقف نمی‌شود |

⚠️ توقف بعد از یک هفته یعنی فرم سایتِ کم‌بازدید ممکن است از کار بیفتد؛ برای سایت مشتری از Pro استفاده کن. در Pro سقف هزینه به‌طور پیش‌فرض روشن است.

## منطقه و محل داده
✅ (https://supabase.com/docs/guides/platform/regions) هیچ منطقه‌ای در خاورمیانه یا امارات فهرست نشده. 🧭 نزدیک‌ترین گزینه‌ی جغرافیایی بمبئی (`ap-south-1`) یا فرانکفورت است. خود صفحه می‌گوید انتخاب منطقه کنترل محل داده است، نه اثبات رعایت قوانین.

## ریسک و هشدار
✅ از مستندات امنیت (https://supabase.com/docs/guides/database/postgres/row-level-security):
- جدولی که **RLS** (امنیت سطح ردیف) ندارد، برای هر نقشی که دسترسی دارد قابل خواندن و نوشتن است. روشن کردن RLS به‌تنهایی کافی نیست؛ سیاست‌ها (policy) و دسترسی‌ها (grant) را هم درست کن.
- **View**ها به‌طور پیش‌فرض RLS را دور می‌زنند.
- کلید **secret / service_role** همه‌ی RLSها را دور می‌زند: **هرگز در کد مرورگر**. فقط کلید publishable (anon) در مرورگر، و فقط با RLS درست.
- برای فرم تماس: فقط سیاست «درج» برای بازدیدکننده‌ی ناشناس، بدون خواندن.

✅ **MCP رسمی** (https://github.com/supabase/mcp، Apache-2.0): با دسترسی حساب خودت کار می‌کند (SQL، migration، لاگ، و بدون محدودیت حتی ساخت و توقف پروژه). توصیه‌ی رسمی: حالت `read_only=true`، محدود کردن به یک پروژه با `project_ref`، تأیید دستی هر عمل، و حواست به prompt injection باشد (به گفته‌ی خودشان «اصلی‌ترین حمله‌ی مخصوص مدل‌های زبانی»). فقط روی پروژه‌ی توسعه، نه داده‌ی واقعی مشتری. قواعد کلی: [امنیت MCP](../domains/claude-code/mcp-safety.md).

## بازبینی ۲۰۲۶-۱۰-۱۹
✅ منطقه‌ی خاورمیانه ندارد (نزدیک‌ترین: بمبئی، فرانکفورت)؛ برای داده‌ای که باید در امارات بماند مناسب نیست. AES-256، SOC 2 Type 2، ISO 27001. جدول بدون RLS برای همه باز است و view از RLS می‌گذرد. Passkey آزمایشی. ([بک‌اند اپ](../domains/apps/app-backend.md))

## بازبینی ورود کاربر ۲۰۲۶-۱۰-۱۹
✅ فهرست منطقه‌ها (https://supabase.com/docs/guides/platform/regions) دوباره خوانده شد: ۱۷ منطقه، **هیچ‌کدام در خاورمیانه، امارات، عربستان یا بحرین نیست**. ✅ صفحه‌ی MFA فقط دو عامل دوم دارد: TOTP و پیامک؛ WebAuthn و passkey آنجا نیامده. سطح `aal1`/`aal2` در JWT هست و با سیاست RLS از نوع `as restrictive` می‌شود aal2 را اجبار کرد (https://supabase.com/docs/guides/auth/auth-mfa). ✅ الگوی رسمی نقش: جدول `user_roles` و `role_permissions`، «custom access token hook» که نقش را در JWT می‌گذارد، و تابع `authorize()` در سیاست RLS (https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac). ✅ کد سرور ورود (`supabase/auth`) مجوز MIT دارد، نسخه‌ی `v2.197.0`. روش کامل: [ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md).

## مرتبط
[تکنولوژی](../domains/website/04-tech/tech-stack.md) · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S19](../sources/README.md#s19) · [S125](../sources/README.md#s125)
