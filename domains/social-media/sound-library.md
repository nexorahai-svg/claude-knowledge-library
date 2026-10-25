# کتابخانه‌ی صدا: افکت، صدای محیط و موسیقی

> **نوع سند:** دستورالعمل
> **هدف این سند:** پیدا کردن صدای رایگان و قانونی برای ویدیوهای سایت و تبلیغات، و وصل کردن Claude به آن.
> **موضوع تحقیق:** Openverse و API رایگانش: حجم، محدودیت‌ها، فیلتر مجوز و روش ذکر منبع.
> **منابع:** [S16 Openverse](../../sources/README.md#s16)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۴
> **دفعه‌ی بعد چک شود:** تعداد فایل‌ها (`/v1/audio/stats/`)، سقف درخواست بدون کلید (هدرهای `x-ratelimit`)، مقادیر مجاز `category`، و اینکه منابع جدیدی اضافه شده یا نه.

---

## Openverse چیست

✅ یک موتور جستجوی رسانه‌ی آزاد (تصویر و صدا) با مجوز Creative Commons یا مالکیت عمومی. بررسی مستقیم API در ۲۰۲۶-۱۰-۱۶:

| مورد | مقدار |
|---|---|
| تعداد کل فایل‌های صوتی | **۵٬۲۱۸٬۷۶۷** |
| منابع | Wikimedia (حدود ۳.۹۸ میلیون)، Jamendo (حدود ۶۴۵ هزار، بیشتر موسیقی)، Freesound (حدود ۵۹۲ هزار، بیشتر افکت) |
| سقف بدون کلید | **۲۰ درخواست در دقیقه** و **۲۰۰ درخواست در روز** |
| حداکثر نتیجه در هر صفحه بدون کلید | **۲۰** |
| حداکثر کل نتایج یک جستجو بدون کلید | ۲۴۰ |
| کلید رایگان | از طریق `POST /v1/auth_tokens/register/` (برای سقف بالاتر) |

## ⚠️ «رایگان» یعنی «مجاز برای تجاری» نیست

✅ هر فایل مجوز خودش را دارد. تست مستقیم نشان داد:
- فیلتر `license_type=commercial` فقط CC0 و CC BY برگرداند (CC BY یعنی **ذکر نام سازنده لازم است**)
- فیلتر `license_type=modification` به‌تنهایی فایل‌های **CC BY-NC (غیرتجاری)** هم برگرداند
- **برای ویدیوی تجاری که صدا را برش می‌دهی یا میکس می‌کنی:** هر دو را با هم بزن: `license_type=commercial,modification`. این ترکیب فایل‌های غیرتجاری (NC) و بدون‌تغییر (ND) را حذف می‌کند.

✅ هر نتیجه یک فیلد آماده‌ی `attribution` دارد (متن کامل ذکر منبع) و یک `foreign_landing_url` (صفحه‌ی اصلی فایل). برای CC BY همین متن را در توضیحات ویدیو یا صفحه‌ی «اعتبار» سایت بگذار.

❓ فیلتر `category=sound_effect` در تست برای «rain» هیچ نتیجه‌ای نداد؛ برچسب دسته‌بندی برای بسیاری از فایل‌ها پر نشده. بهتر است با کلمه‌ی کلیدی جستجو کنی، نه با دسته.

## نمونه‌ی درخواست

```bash
curl "https://api.openverse.org/v1/audio/?q=whoosh&license_type=commercial,modification&page_size=20"
```

فیلدهای مهم هر نتیجه: `title`، `creator`، `license`، `url` (فایل صوتی)، `duration` (میلی‌ثانیه)، `attribution`، `foreign_landing_url`.

## پرامپت برای Claude

(نسخه‌ی دقیق‌شده‌ی دستور پست منبع، با محدودیت‌های تست‌شده)

```text
When a video needs sound effects, ambience or music, search Openverse first:
GET https://api.openverse.org/v1/audio/?q=<keywords>&license_type=commercial,modification&page_size=20
No API key is needed (limit: 20 requests/minute, 200/day). Search by descriptive
keywords, not by category. For each candidate, check the license field and duration,
and listen before choosing. Keep a credits file listing title, creator, license and
foreign_landing_url for every sound used, and use the provided attribution text for
any CC BY file.
```

## موسیقی ساخته با کد (مالکیت کامل) 🔬

برای ویدیوی خانوادگی موسیقی با numpy ساخته شد: ambient مراقبه‌ای و موسیقی احساسی که با بخش‌های متن تغییر می‌کند. هیچ مجوز بیرونی لازم نیست. میکس زیر صدا با `sidechaincompress` و `loudnorm`؛ مقدارها در [FFmpeg](../../catalog/ffmpeg.md). [S151](../../sources/README.md#s151)
