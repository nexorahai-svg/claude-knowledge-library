---
name: Ollama
slug: ollama
category: local-ai
domains: [apps, website]
verdict: adopt
status: researched
summary: اجراکننده‌ی محلی مدل‌های زبانی باز با API ساده، خروجی ساختاریافته با JSON Schema و فراخوانی ابزار
use_when: "a service on our own server needs a local model with a simple API ; daily analysis from computed numbers ; structured JSON output from a local model"
how: "Ollama (MIT) /api/chat; always set num_ctx explicitly, keep JSON Schema simple (no $ref/anyOf), validate output with Pydantic, never accept numbers not in the input, pin version and model digest, watch prompt_eval_count"
url: https://ollama.com
repo: "https://github.com/ollama/ollama"
license: "MIT"
pricing: free
risk: medium
sources: [S81]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-26"
---

# Ollama

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی v0.40.12 (۲۰۲۶-۱۰-۲۷): مدل‌های Liquid AI LFM3 (lfm3، -vl، -audio، -omni) و مدل‌های d1؛ MIT بی‌تغییر.
✅ سرور محلی برای اجرای مدل‌های باز. API `/api/chat` این‌ها را می‌گیرد: `format` (رشته‌ی `"json"` یا یک JSON Schema)، `tools`، `think`، `keep_alive` و `options` (`seed`، `temperature`، `num_ctx`، `num_predict` و…). آخرین نسخه‌ی دیده‌شده v0.40.6 است (۱۶ اکتبر ۲۰۲۶) ([S81](../sources/README.md#s81)).

✅ چند پیش‌فرض:
- طول زمینه ۴۰۹۶ توکن است (`OLLAMA_CONTEXT_LENGTH` یا `num_ctx`).
- مدل ۵ دقیقه در حافظه می‌ماند (`keep_alive`).
- `OLLAMA_NUM_PARALLEL` برابر ۱ است. حافظه با «تعداد درخواست همزمان × طول زمینه» بالا می‌رود.
- `ollama ps` نشان می‌دهد مدل کاملاً روی کارت گرافیک است یا نه.

## کی استفاده کنیم
🧭 وقتی سرویس روی سرور خودمان مدل محلی لازم دارد و API ساده‌تر از [llama.cpp](llama-cpp.md) می‌خواهیم (مثلاً تحلیل روزانه از روی عددهای حساب‌شده).

🧭 قاعده‌ها:
- `num_ctx` را همیشه صریح بده.
- schema را ساده نگه دار: بدون `$ref` و `anyOf`.
- خروجی را بعد از تولید با Pydantic بسنج.
- عدد را از متن مدل نپذیر مگر در داده‌ی ورودی باشد ([محافظ عدد](llama-cpp.md)).

## قیمت و مجوز
✅ رایگان، MIT. مجوز هر مدل جداست.

## ریسک و هشدار
- ✅ مستندات نمی‌گویند `format` کدام کلیدواژه‌های JSON Schema را پشتیبانی می‌کند یا وقتی خروجی با schema نخواند چه می‌شود. خروجی را همیشه بسنج.
- ❓ `seed` همراه با `temperature: 0` روی همان دستگاه و نسخه تکرارپذیر گزارش شده، ولی بین نسخه‌ها و دستگاه‌ها نه. نسخه‌ی Ollama و digest مدل را ثابت کن و ثبت کن.
- ❓ متنی که از `num_ctx` بلندتر باشد ممکن است بی‌صدا بریده شود. `prompt_eval_count` را بپا.
- 🧭 نصب با نسخه و چک‌سام ثابت ([سرور شخصی](../domains/website/04-tech/self-hosted-server.md)).

## در پروژه امتحان شد

🔬 پروژه‌ی معامله‌گر هوش مصنوعی (۲۰۲۶-۱۰-۱۸، دفتر پروژه‌ها) با `qwen3:8b` روی RTX 4060 هشت‌گیگی:
- با `num_ctx` برابر ۱۶۳۸۴ مدل حدود ۷٫۸ گیگ شد و بخشی به پردازنده ریخت، پس هر فراخوانی چند دقیقه طول کشید.
- در اولین آزمون، مدل برخلاف دستور عددها را خودش نوشت و یکی را هم اشتباه نوشت (‎−۰٫۰۰۲۶٪ به‌جای ‎−۰٫۲۷٪). نگهبان «فقط جای‌نگهدار کلید»، یعنی حذف هر رقم نوشته‌شده توسط مدل، همه را گرفت. بعد از یک مثال درست و نادرست در دستور، مدل جای‌نگهدار نوشت.
- با `temperature 0.7` یک فراخوانی وارد تکرار بی‌پایان شد و ۱۵ دقیقه ماند. `num_predict` (مثلاً ۳۰۰۰) و timeout برای هر فراخوانی لازم است.
- 🧭 برای این سخت‌افزار، پژوهش `qwen3.5:9b` (۶٫۶ گیگ، حافظه‌ی KV بسیار کم: حدود ۱ گیگ برای ۳۲K) و `gemma4:12b-it-qat` (۷٫۲ گیگ، سابقه‌ی بهتر فارسی) را پیشنهاد کرد. ❓ هنوز روی کار واقعی سنجیده نشده‌اند.

## مرتبط
[llama.cpp](llama-cpp.md) · [S81](../sources/README.md#s81)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.

🔬 (۲۰۲۶-۱۰-۳۱) `install.sh` رسمی checksum را نمی‌سنجد؛ در نصب‌کننده‌ی محصول فایل را خودت با هش بررسی کن.
