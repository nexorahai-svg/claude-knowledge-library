---
name: llama.cpp (llama-server)
slug: llama-cpp
category: local-ai
domains: [apps, website]
verdict: adopt
status: researched
summary: موتور اجرای محلی مدل زبانی (فایل GGUF) روی پردازنده یا کارت گرافیک، با سرور HTTP سازگار با OpenAI
use_when: "a product must answer on the customer's own machine offline without cloud cost ; sensitive replies where cloud AI is not acceptable ; local assistant, summary or classification"
how: "ship a pinned llama.cpp build with sha256 manifest; run llama-server on 127.0.0.1, random port, random --api-key, --no-webui, --offline; add a number guard on replies; ship the MIT LICENSE file"
url: https://github.com/ggml-org/llama.cpp
repo: "https://github.com/ggml-org/llama.cpp"
license: "MIT"
pricing: free
risk: medium
sources: [S76]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# llama.cpp (llama-server)

## چیست
✅ موتور C و C++ برای اجرای مدل‌های زبانی باز (قالب GGUF) بدون اینترنت. برنامه‌ی `llama-server` یک سرور HTTP محلی می‌دهد. نسخه‌های آماده‌ی ویندوز (پردازنده و Vulkan) در صفحه‌ی Releases است. مجوز MIT، با نام «The ggml authors» ([S76](../sources/README.md#s76)).

## کی استفاده کنیم
🧭 وقتی محصول باید روی رایانه‌ی خود مشتری و بدون هزینه‌ی ابری جواب بدهد (دستیار پیام، خلاصه، دسته‌بندی). برای جواب‌های حساس، کنار [هوش مصنوعی ابری در محصول](../domains/website/04-tech/ai-in-product.md) به‌عنوان موتور جایگزین.

🔬 یک پروژه‌ی واقعی نسخه‌ی b11408 را همراه برنامه‌ی ویندوزی می‌فرستد. الگوهایی که پروژه ساخته:
- فایل zip موتور با هش sha256 ثابت در یک manifest؛ پیش از باز کردن بررسی می‌شود.
- سرور فقط روی 127.0.0.1، در درگاه تصادفی، با `--api-key` تصادفی برای هر اجرا، `--no-webui` و `--offline`.
- پاسخ مدل با «محافظ عدد»: هر عددی در پاسخ (ساعت، قیمت) باید در اطلاعات کسب‌وکار یا پیام خود مشتری باشد؛ وگرنه پاسخ فرستاده نمی‌شود و گفتگو به همکار می‌رسد.
- سنجش خود پروژه (۲۰۲۶-۱۰-۰۶، ۶ صنف × ۳ زبان، روی پردازنده): Qwen3.5 0.8B، 2B و 4B همه ۱۰۰٪ پاسخ درست روی ساعت، آدرس و قیمت؛ سرعت به ترتیب حدود ۳۱، ۱۶ و ۸ توکن در ثانیه. ❓ مجموعه‌ی آزمون کوچک است و پیش از اجرا ثبت نشده بود ([سنجش ادعاها](../research/claim-testing.md)).

## قیمت و مجوز
✅ رایگان، MIT. ⚠️ ✅ MIT می‌گوید متن مجوز و نام صاحب حق «در همه‌ی نسخه‌ها» بیاید: اگر موتور را همراه برنامه می‌فرستی، فایل LICENSE را هم بفرست؛ فقط نام بردن در EULA کافی نیست ([اپ دسکتاپ](../domains/apps/desktop-apps.md#ابزار-همراه-برنامه-و-کلید-امضا)). مجوز هر مدل جداست (Qwen3.5 و Gemma 4: Apache-2.0 ✅).

## ریسک و هشدار
- 🧭 درگاه تصادفی را پیش از استفاده بررسی کن؛ برخورد درگاه موتور را تا اجرای بعدی خاموش می‌گذارد (در یک پروژه‌ی واقعی دیده شد).
- 🧭 نسخه‌ها خیلی تند عوض می‌شوند (شماره‌ی build روزانه)؛ یک نسخه را با هش ثابت کن و با مجموعه‌ی آزمون خودت به‌روز کن.
- ❓ مدل کوچک ممکن است عدد درستِ موردی دیگر را بنویسد (قیمت خدمت دیگر)؛ محافظ عدد این را نمی‌گیرد.

## مرتبط
[هوش مصنوعی ابری در محصول](../domains/website/04-tech/ai-in-product.md) · [اپ دسکتاپ](../domains/apps/desktop-apps.md) · [whisper.cpp](whisper-cpp.md) · [S76](../sources/README.md#s76)

🔬 (۲۰۲۶-۱۰-۳۱، b12019) نسخه‌های رسمی ubuntu به glibc 2.38 و GLIBCXX 3.4.32 نیاز دارند: روی Ubuntu 22.04 و Debian 12 اجرا نمی‌شوند، روی Ubuntu 24.04 و Debian 13 می‌شوند.
