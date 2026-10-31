---
name: infinite-canvas (بوم بی‌نهایت تولید تصویر و ویدیو)
slug: infinite-canvas
category: image-generation
domains: [social-media, security]
verdict: hold
status: researched
summary: بوم بی‌نهایت متن‌باز برای تولید تصویر و ویدیو با عامل، سازگار با API شبیه OpenAI؛ README راه‌های غیررسمی (chatgpt2api، grok2api، flow2api) و حامی تبلیغاتی را پیشنهاد می‌کند
use_when: "only as a reference for a canvas-style image and video workspace UI"
how: "Do not install: unofficial relay gateways that resell or bypass other services' accounts, an advertising sponsor in the README, and API keys stored in browser localStorage; read the code first if ever needed"
url: https://github.com/basketikun/infinite-canvas
repo: "https://github.com/basketikun/infinite-canvas"
license: "MIT"
pricing: free
risk: high
sources: [S198]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# infinite-canvas

## چیست
✅ (GitHub API و README، ۲۰۲۶-۱۰-۲۸) مجوز MIT، حدود ۹٬۳۲۰ ستاره، نسخه‌ی v0.20.0 (۲۰۲۶-۱۰-۱۰)، آخرین push ۲۰۲۶-۱۰-۲۵. README به چینی است. یک بوم بی‌نهایت برای ساخت تصویر و ویدیو با هوش مصنوعی است: ویرایش با تصویر مرجع، عامل دستیار، کتابخانه‌ی پرامپت و مدیریت فایل‌ها. با هر سرویسی که API شبیه OpenAI دارد کار می‌کند.

## کی استفاده کنیم
⛔ برای کار واقعی، نه. فقط می‌شود از رابط بوم آن ایده گرفت.

## قیمت و مجوز
✅ کد MIT است. هزینه‌ی تولید به سرویسی بستگی دارد که به آن وصل می‌شود.

## ریسک و هشدار
- ⚠️ **راه‌های غیررسمی:** README راه‌هایی مثل chatgpt2api، grok2api، flow2api و newapi را پیشنهاد می‌کند. این‌ها حساب سرویس‌های دیگر را دور می‌زنند یا دوباره می‌فروشند، که خطر بسته شدن حساب و نشت داده دارد.
- ⚠️ **حامی تبلیغاتی:** README حامی تبلیغاتی دارد (APIMart).
- ⚠️ **ذخیره‌ی کلید:** کلید API و Base URL در حافظه‌ی مرورگر ذخیره می‌شوند.
- 🧭 اگر فقط با کلید رسمی (OpenAI/Gemini خودمان) وصل شود ریسک کمتر است، ولی ابزار برای مسیرهای غیررسمی هم ترویج می‌شود؛ منبع: https://github.com/basketikun/infinite-canvas

## مرتبط
[S198](../sources/README.md#s198)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ `canvas-proxy` و `canvas-agent` خوانده شد (SHA `9cd3dea`). ⚠️ `canvas-proxy` یک پراکسی CORS باز با `*` است: هر URL را با هدرهایش، از جمله Authorization، فوروارد می‌کند و فهرست مجاز ندارد. پیش‌فرض فقط روی 127.0.0.1 است، ولی هر صفحه‌ی وب در مرورگر می‌تواند از آن به آدرس‌های داخلی برسد. روشنش نکن مگر لازم باشد، و بعد از کار ببندش.
- ✅ `canvas-agent` محلی و توکن‌دار است و `claude -p` را فقط با ابزار MCP خودش اجرا می‌کند. تله‌متری دیده نشد. ❓ فرانت‌اند خوانده نشد.
