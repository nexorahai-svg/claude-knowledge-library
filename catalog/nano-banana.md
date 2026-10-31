---
name: Google Nano Banana (Gemini Image)
slug: nano-banana
category: image-generation
domains: [social-media, website]
verdict: adopt
status: researched
summary: مدل تولید تصویر Google در Gemini API؛ ارزان، با واترمارک SynthID
use_when: "generating text-free background images for posts ; character face consistency in Google Flow"
how: "Nano Banana 2.1 API (1K 0.0336, 2K 0.0504, 4K 0.113 USD, batch about half); put text via code templates not the model; send client data only on a paid plan; Persian text not guaranteed; outputs carry SynthID"
url: https://ai.google.dev/gemini-api/docs/image-generation
repo: ""
license: "شرایط Gemini API"
pricing: paid
risk: medium
sources: [S44, S151, S155]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-24"
---

# Google Nano Banana (Gemini Image)

## چیست
✅ Nano Banana 2.1: ۱K ۰.۰۳۳۶، ۲K ۰.۰۵۰۴، ۴K ۰.۱۱۳ دلار؛ Pro تا ۰.۲۴. دسته‌ای حدود نصف. همه‌ی خروجی‌ها SynthID دارند.

## دستور سریع

**نصب** (✅ [مستند تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation) و PyPI؛ پایتون ≥ 3.11):
```bash
pip install google-genai==2.34.0
export GEMINI_API_KEY="..."        # کلید پولی؛ طرح رایگان داده را برای آموزش به‌کار می‌برد
```
**حداقل اجرا** (✅ نمونه‌ی رسمی، با `interactions` و شناسه‌ی `gemini-nano-banana-2.1`):
```python
import base64
from google import genai
client = genai.Client()
it = client.interactions.create(model="gemini-nano-banana-2.1", input="clean pastel gradient background, no text",
        response_format={"type": "image", "mime_type": "image/jpeg", "aspect_ratio": "9:16", "image_size": "1K"})
open("bg.jpg", "wb").write(base64.b64decode(it.output_image.data))
```
**تنظیم‌های مهم**
- ✅ `image_size`: `1K` (`$0.0336`)، `2K` (`$0.0504`)، `4K` (`$0.113`) برای هر تصویر؛ پست شبکه‌ی اجتماعی معمولاً با `1K` یا `2K` بس است (🧭).
- ✅ حالت batch حدود نصف قیمت است (`$0.0168` / `$0.0252` / `$0.0567`)؛ برای دسته‌ی بزرگ غیرفوری.
- ✅ تا ۱۴ تصویر مرجع می‌گیرد؛ نسخه‌های ارزان‌تر: `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite).

**خطاهای رایج**
- ✅ فارسی در فهرست زبان‌های «بهترین عملکرد» مستند نیست (عربی مصری هست)؛ متن را با قالب کد روی تصویر بگذار، نه با مدل.
- ✅ همه‌ی خروجی‌ها SynthID دارند؛ ✅ نسخه‌ی 2.1 در سطح رایگان API «Not available» است و داده‌ی طرح رایگان برای بهبود محصول به‌کار می‌رود → داده‌ی مشتری فقط با کلید پولی.
- ⚠️ اصلاح کارت: `gemini-2.5-flash-image` در صفحه‌ی قیمت فعلاً «deprecated» است و **۲۰۲۷-۰۳-۱۵ بسته می‌شود** (هنوز بسته نشده)؛ مسیر مهاجرت پیشنهادی Nano Banana 2 Lite است.

**هزینه** (✅ [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing)، ۲۰۲۶-۱۰-۳۱): ارقام بالا برای `gemini-nano-banana-2.1` (ورودی `$1.50` و خروجی تصویر `$30` به‌ازای هر ۱ میلیون توکن). محافظ: هشدار بودجه روی حساب پولی (🧭) و یک تصویر آزمایشی پیش از هر دسته.

## کی استفاده کنیم
🧭 پس‌زمینه‌ی بدون متن برای پست؛ متن با قالب کد.

## قیمت و مجوز
✅ طرح پولی داده را برای آموزش استفاده نمی‌کند؛ طرح رایگان می‌کند. ❓ بند مالکیت.

## ریسک و هشدار
⚠️ داده‌ی مشتری را فقط در طرح پولی بفرست. متن فارسی تضمین نشده.

## در بخش Characters فلو 🔬
🔬 در Flow چهره‌ی شخصیت با Nano Banana 2.1 رایگان (بدون اعتبار) ساخته می‌شود و در ۱۲ صحنه ثابت ماند؛ شرح در [Google Flow](google-flow.md). [S151](../sources/README.md#s151)


## به‌روزرسانی 2026-10-25 ([S155](../sources/README.md#s155))
✅ قیمت (هر تصویر): 2.1 ‏۰٫۰۳۳۶ (1K)، ۰٫۰۵۰۴ (2K)، ۰٫۱۱۳ (4K)؛ 2 ‏۰٫۰۶۷؛ 2 Lite ‏۰٫۰۳۳۶؛ **Pro ‏۰٫۱۳۴ (1K/2K)، ۰٫۲۴ (4K)**؛ batch حدود نصف. تا ۱۴ مرجع؛ Pro ‏۵ شخصیت و ۶ شیء و ۳ سبک، 2.1 ‏۴ شخصیت و ۱۰ شیء. گوگل ادعای «متن دقیق‌تر عربی» برای Pro دارد ✅؛ آزمون مستقل و فارسی ❓. Nano Banana اصلی (2.5 flash image) و Imagen در Gemini API بسته شدند.

## مرتبط
[تصویر و گرافیک](../domains/social-media/images-and-graphics.md) · [S44](../sources/README.md#s44)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.

🔬 **تصویر بزرگ صفحه‌ی اصلی سایت (۲۰۲۶-۱۰-۳۱، از راه fal در 4K):** ۳ نمونه‌ی ۱۶:۹ هر سه بار اول قابل‌استفاده بود، 5504×3072، چهره و دست درست، WebP با عرض 2560 حدود ۱۲۶ کیلوبایت، هزینه‌ی تخمینی حدود ۰٫۹۰ دلار (از صورت‌حساب خوانده نشد). نیمه‌ی خالی برای متن را در پرامپت نام ببر، متن را ممنوع کن و گوشی را پشت به دوربین بخواه تا صفحه‌ی ساختگی نیاید؛ بعد می‌شود تصویر را برای راست‌به‌چپ آینه کرد. ❓ قیمت fal برای Pro از صفحه‌ی مدل خوانده نشد.

🔬 **نسخه‌ی رایگان در Google Flow (۲۰۲۶-۱۰-۳۱):** Nano Banana 2.1، ۱۶:۹، خروجی 1376×768، هر اجرا ۴۰ تا ۸۰ ثانیه؛ پیام اعتبار نیامد، ولی مصرف از صورت‌حساب خوانده نشد ❓. نوشتن `f/11`، deep focus و no background blur حالت نیمه‌تار را برداشت؛ نام بردن قفسه‌های پشت سوژه جزئیات مغازه را نگه داشت و حذفشان اتاق خالی داد. در اتوماسیون مرورگر فقط کلیک واقعی روی Start generation کار کرد.
