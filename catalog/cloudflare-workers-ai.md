---
name: Cloudflare Workers AI
slug: cloudflare-workers-ai
category: local-ai
domains: [website, apps]
verdict: trial
status: researched
summary: مدل‌های باز (gpt-oss، Llama 4، Kimi، GLM، Qwen، Gemma، bge-m3) روی GPUهای Cloudflare؛ برای پاسخ چندزبانه با زمینه‌ی بلند از Claude Haiku 5.5 ارزان‌تر نیست
use_when: "a simple site assistant or FAQ bot on the free daily quota ; a cheap fallback model behind an OpenAI-compatible endpoint ; embeddings (bge-m3) next to a Cloudflare-hosted site"
how: "Call https://api.cloudflare.com/client/v4/accounts/<id>/ai/v1 (OpenAI-compatible) with a scoped API token; start with Gemma 4 26B (thinking off); for long-context multilingual answers compare cost with Claude Haiku 5.5 first, it was cheaper; judge answers for fabrication before going live"
url: https://developers.cloudflare.com/workers-ai/
repo: ""
license: "سرویس تجاری؛ هر مدل مجوز خودش را دارد"
pricing: freemium
risk: medium
sources: [S183]
found_in: [project/client]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Cloudflare Workers AI

## چیست
✅ ([S183](../sources/README.md#s183)) اجرای **مدل‌های باز** روی GPUهای Cloudflare از راه Workers یا REST، با نشانی سازگار با OpenAI (`api.cloudflare.com/client/v4/accounts/<id>/ai/v1`). مدل‌های اختصاصی Claude یا GPT روی آن نیستند (آن‌ها فقط از راه AI Gateway، که دروازه است نه اجراکننده).
- مدل‌های متنی شاخص: gpt-oss-120b/20b، Llama 4 Scout (بینایی)، Kimi K2.6، GLM-5.3 و GLM-4.7-flash، DeepSeek V4، Qwen3/3.8، Gemma 4 26B، Mistral Small 3.1. Embedding: bge-m3، qwen3-embedding و embeddinggemma.
- ✅ قیمت (۲۰۲۶-۱۰-۲۰): روزانه ۱۰٬۰۰۰ نورون رایگان (حدود ۰٫۱۱ دلار)، بعد ۰٫۰۱۱ دلار برای هر هزار نورون. به دلار برای هر میلیون توکن ورودی/خروجی: Qwen3-30B-A3B ۰٫۰۵۱/۰٫۳۳۵، GLM-4.7-flash ۰٫۰۶/۰٫۴۰، Gemma 4 26B ۰٫۱۰/۰٫۳۰، Llama 4 Scout ۰٫۲۷/۰٫۸۵، gpt-oss-120b ۰٫۳۵/۰٫۷۵، Kimi K2.6 ۰٫۹۵/۴٫۰۰، GLM-5.3 ۱٫۴۰/۴٫۴۰، bge-m3 ۰٫۰۱۲.
- ✅ سقف: مدل‌های متنی ۳۰۰ درخواست در دقیقه؛ مدل‌های پولیِ قوی (Kimi، GLM-5.x، DeepSeek V4) فقط ۲۰ (با اعتبار AI Gateway ۵۰).
- ✅ داده: برای آموزش استفاده نمی‌شود و بعد از پاسخ نگه داشته نمی‌شود (مگر کش یا لاگ AI Gateway). ⚠️ در جدول Data Localization، Workers AI با **Regional Services سازگار نیست**؛ منطقه‌های نام‌برده فقط آمریکا و اروپا؛ محل پردازش قابل تعیین نیست.
- ✅ JSON Mode فقط برای چند مدل قدیمی فهرست شده، رعایت schema تضمین ندارد و با پخش زنده کار نمی‌کند؛ Kimi و GLM-5.3 و DeepSeek V4 «structured outputs» دارند.
- ✅ AI Gateway جلوی هر سرویس (از جمله Anthropic): کش، آمار، سقف، جایگزین، DLP رایگان؛ DLP فقط علامت می‌زند یا رد می‌کند و **پنهان نمی‌کند**؛ Unified Billing کارمزد ۵٪ دارد.

## کی استفاده کنیم
- 🔬 (پروژه‌ای در [Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md)) دستیار ساده‌ی یک سایت ایستا با Qwen3-30B روی سهمیه‌ی رایگان: کار کرد.
- 🔬 (یک فروشگاه واقعی، ۲۰۲۶-۱۰-۲۷، ارزیابی روی کاغذ با مصرف واقعی) برای پاسخ سه‌زبانه با دانش بلند همراه پرسش (میانگین ۸٬۷۰۰ توکن ورودی، ۳۲۰ خروجی)، قیمت **ورودی** تعیین‌کننده است. Claude Haiku 5.5 (۰٫۱۰/۰٫۵۰) از همه‌ی مدل‌های قوی Workers AI ارزان‌تر بود: در ۳۰۰ پاسخ روزانه، Haiku حدود ۱۰ دلار در ماه، gpt-oss-120b حدود ۳۱، Llama 4 Scout حدود ۲۵ و Kimi K2.6 حدود ۹۲. فقط مدل‌های کوچک (Qwen3-30B-A3B، GLM-4.7-flash) چند دلار ارزان‌ترند، با کیفیت فارسی ثابت‌نشده (همان پروژه با Qwen و Gemma محلی حروف چینی در فارسی و MRZ ضعیف دیده بود). تصمیم: Claude ماند (آزمون واقعی پایین تأییدش کرد).
- 🔬 (همان پروژه، همان روز، **آزمون واقعی** با کلید مالک، از راه نشانی سازگار با OpenAI و موتور خود پروژه)
  - **۴۵ پرسش سه‌زبانه با داور Claude Sonnet** (درستی و کامل بودن از ۲، جواب ساختگی):

    | مدل | درستی | کامل بودن | ساختگی | زمان |
    |---|---|---|---|---|
    | Claude Haiku 5.5 | ۱٫۶۰ | ۱٫۶۹ | ۸ | ۳٫۲ ثانیه |
    | Gemma 4 26B (فکر خاموش) | ۱٫۶۱ | ۱٫۵۲ | ۷ | ۵٫۱ ثانیه |
    | Llama 4 Scout | ۱٫۴۸ | ۱٫۵۹ | ۹ | — |
    | gpt-oss-120b | ۱٫۱۳ | ۱٫۴۹ | ۱۸ | ۱۱٫۳ ثانیه |
    | Qwen3-30B | ۰٫۸۴ | ۱٫۲۹ | ۱۹ | — |

  - **۷ مدرک هویتی:**

    | مدل | فیلدها | زمان هر مدرک |
    |---|---|---|
    | Claude Sonnet 5.5 | ۳۱/۳۱ | ۱۲٫۷ ثانیه |
    | Qwen3.8-27B (با سقف توکن بیشتر) | ۳۱/۳۱ | ۱۵۲ ثانیه |
    | DeepSeek V4.1 flash | ۳۰/۳۱ | ۴۵ ثانیه |
    | Llama 4 Scout | ۲۵/۳۱ | — |
    | Mistral Small 3.1 | ۲۴/۳۱ | — |
    | Kimi K2.6 | — | تا ۵۹۱ ثانیه |

  - ⚠️ **تله‌ی فکر کردن:** مدل‌های فکرکننده‌ی Workers AI (Gemma 4، Kimi، Qwen3.8، DeepSeek V4، gpt-oss) کل `max_completion_tokens` را در `reasoning_content` خرج می‌کنند و `content` خالی برمی‌گردد.
    - برای Gemma 4: `chat_template_kwargs: {enable_thinking: false}` جواب داد.
    - `reasoning_effort: "none"` کار نکرد.
    - Kimi با هیچ‌کدام فکر را خاموش نکرد.
  - Llama 3.2 Vision پیش از استفاده باید با ارسال `agree` مجوز Meta را بپذیرد.
- 🧭 گزینه‌ی واقعی: embedding (bge-m3 همان مدل محلی است، ۰٫۰۱۲ دلار) برای سروری که نمی‌خواهد Ollama نصب کند؛ کارهای حجیم و ساده با مدل کوچک وقتی کیفیت با آزمون خود پروژه ثابت شد.
- ⛔ برای مدارک هویتی و MRZ بدون آزمون دقیق روی نمونه‌های واقعی نه؛ و هر جا داده‌ی شخصی می‌رود، افزودن Cloudflare یعنی پردازشگر تازه در متن رضایت و سیاست حریم خصوصی.

## ارتقا به trial (۲۰۲۶-۱۰-۳۰) 🔬
دو استفاده‌ی واقعی دارد (بخش «کی استفاده کنیم»): دستیار ساده روی سهمیه‌ی رایگان کار کرد و در آزمون ۴۵ پرسشی Gemma 4 26B در درستی هم‌پای Claude Haiku 5.5 بود. پس امیدوارکننده است، با این مرز: برای پاسخ با دانش بلند از Haiku ارزان‌تر نیست و ساختگی‌گویی مدل‌های کوچک بیشتر است. برای adopt یک پروژه‌ی دوم با استفاده‌ی واقعی در محصول لازم است.

## قیمت و مجوز
✅ بالا؛ هر مدل باز مجوز یا سیاست استفاده‌ی خودش را دارد (به گفته‌ی خود Cloudflare).
