---
name: colibri (JustVugg)
slug: colibri
category: local-ai
domains: [apps]
verdict: assess
status: researched
summary: موتور C بی‌وابستگی که مدل‌های MoE خیلی بزرگ را با خواندن expertها از دیسک روی رایانه‌ی معمولی اجرا می‌کند
use_when: "running a local MoE model larger than RAM when speed does not matter ; overnight local inference without a GPU"
how: "Trial first on a small task: clone github.com/JustVugg/colibri, start with qwen36-35b (23 GB, ~6 tok/s CPU) not GLM-5.2 (429 GB, ~0.1 tok/s); run resource_guard.py check first; heavy SSD reads"
url: https://justvugg.github.io/colibri
repo: https://github.com/JustVugg/colibri
license: Apache-2.0
pricing: free
risk: medium
sources: [S180, S159]
found_in: [instagram]
last_checked: 2026-10-27
next_check: 2027-01-25
---

# colibri (JustVugg)

## چیست
✅ (README مخزن، ۲۰۲۶-۱۰-۲۷) موتور اجرای مدل محلی به زبان C، بدون وابستگی و بدون نیاز به GPU. در مدل‌های mixture-of-experts هر توکن فقط بخش کوچکی از مدل را لازم دارد؛ colibri همان بخش را در RAM نگه می‌دارد و expertها را هنگام نیاز از SSD می‌خواند. ۱۳ موتور: GLM-5.2/5.3، Kimi K3، DeepSeek V4 Flash، Qwen3.6 (و Qwen3-Coder)، MiMo-V2.6، Qwen-Image-2.1 و چند مدل دیگر. نسخه‌ی v2.0.0 (۲۰۲۶-۱۰-۰۶)، حدود ۴۴ هزار ستاره، فعال.
✅ ادعای پست («مدل ۷۴۴ میلیاردی روی کامپیوتر معمولی») درست ولی گمراه‌کننده است. جدول خود README برای GLM-5.2: ۴۲۹ گیگابایت دیسک، و روی لپ‌تاپ ۲۵ گیگابایتی **۰٫۰۵ تا ۰٫۱ توکن در ثانیه** (یعنی چند دقیقه برای یک جمله)؛ ۱٫۸۳ روی رایانه‌ی ۱۲۸ گیگابایتی و ۹ با شش کارت RTX 5090.
✅ مدل‌های میانه کاربردی‌ترند: Qwen3.6-35B-A3B (۲۳ گیگابایت) حدود ۶ توکن در ثانیه روی CPU و ۳۰ با CUDA؛ Qwen3-Coder-30B حدود ۸ تا ۹.

## کی استفاده کنیم
🧭 وقتی مدل محلی بزرگ‌تر از RAM لازم است و سرعت مهم نیست (کار شبانه، آزمایش). برای چت روزمره و کدنویسی محلی، مدل‌های کوچک‌تر با [Ollama](ollama.md) یا [llama.cpp](llama-cpp.md) سریع‌ترند. پیش از هر اجرا قانون منابع (`resource_guard.py check`) را بسنج.

## قیمت و مجوز
✅ رایگان، Apache-2.0 (فایل LICENSE مخزن). وزن هر مدل مجوز خودش را دارد؛ پیش از کار تجاری مجوز همان مدل را بخوان.

## ریسک و هشدار
متوسط: صدها گیگابایت دانلود و خواندن سنگین و مداوم از SSD (فرسودگی دیسک)؛ RAM و swap را پر می‌کند. اسکریپت راه‌انداز ویندوز (`START-HERE.bat`) پایتون نصب می‌کند؛ اجرا نشده و آزموده نشد ❓. پست منبع لینک را فقط با «کامنت بده» می‌دهد؛ آدرس رسمی همین مخزن است.

## مرتبط
[S180](../sources/README.md#s180) · [S159](../sources/README.md#s159) · [Ollama](ollama.md) · [llama.cpp](llama-cpp.md)
