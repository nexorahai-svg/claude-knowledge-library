---
name: fal.ai
slug: fal-ai
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: پرداخت به‌ازای مصرف برای ده‌ها مدل ویدیو و تصویر در یک صورت‌حساب؛ ارزان‌ترین راه تأییدشده برای H3 و Kling
use_when: "generating video or images from many models on pay-per-use ; cheapest way to test video models"
how: "before a paid job read the balance: GET https://api.fal.ai/v1/account/billing?expand=credits (key needs billing:usage:read); an empty balance locks the account and even storage upload returns 403; create the API key inside the funded team; upload audio/images via rest.alpha.fal.ai/storage/upload/initiate (no data: URIs on OmniHuman/InfiniteTalk); use fal API pay-as-you-go (Kling 3.0 Pro 1080p about $0.11 per second); Seedance 2.5 on fal is the US version and 2x pricier, buy from BytePlus or Replicate; terms and UAE access unread"
url: https://fal.ai/pricing
repo: ""
license: "شرایط هر مدل جدا"
pricing: paid
risk: low
sources: [S155, S192, S194]
found_in: [paid-ai-media-research-2026-10-25]
last_checked: 2026-11-01
next_check: "2026-12-01"
---

# fal.ai

## چیست
✅ قیمت به‌ازای ثانیه یا توکن خروجی، بدون اشتراک. Kling 3.0 Pro 1080p ۰٫۱۱۲ دلار در ثانیه بی‌صدا و ۰٫۱۶۸ با صدا؛ Kling 4.0 ‏۰٫۱۵۷ (720p) و ۰٫۲۳۵ (1080p)؛ MiniMax H3 Max ‏1080p ‏۰٫۱۰۴ (تا ۲۰۲۶-۱۰-۳۱، بعد حدود ۰٫۱۶)، H3 Max Turbo ‏۰٫۰۵۲ (بعد حدود ۰٫۰۸)؛ Wan 3.0 ‏۰٫۰۵/۰٫۱۰/۰٫۲۰؛ Omni Flash 1.1 ‏۰٫۰۳ تا ۰٫۳۰.
⚠️ Seedance 2.5 در fal نسخه‌ی آمریکایی و دو برابر گران است (۰٫۴۷ دلار در 720p)؛ از BytePlus یا Replicate بخر. شرایط استفاده و دسترسی امارات خوانده نشد ❓. کارت جدا [fal MCP](fal-mcp.md) برای اتصال به Claude است.

🔬 **قفل حساب با تمام شدن اعتبار** (۲۰۲۶-۱۱-۰۱): وقتی اعتبار پیش‌پرداخت تمام شد، حتی اولین قدم، آپلود به `rest.alpha.fal.ai/storage/upload/initiate`، پاسخ 403 با `User is locked. Reason: Exhausted balance` داد؛ درخواستی ساخته نشد و هزینه‌ای نرفت. ✅ موجودی پیش از ارسال با `GET https://api.fal.ai/v1/account/billing?expand=credits` خوانده می‌شود (`credits.current_balance`؛ کلید با مجوز `billing:usage:read`، در پیش‌تنظیم‌های BILLING، READONLY و FULL): https://fal.ai/docs/platform-apis/v1/account/billing . ❓ این فراخوانی را خودمان اجرا نکرده‌ایم و آستانه‌ی قفل عدد مشخصی در این صفحه ندارد.

## دستور سریع

**نصب** (✅ [مستند fal](https://docs.fal.ai/model-apis/client) و PyPI/npm):
```bash
pip install fal-client==1.0.3          # یا: npm install --save @fal-ai/client   (1.10.1)
export FAL_KEY="..."                   # کلید را داخل همان تیمِ شارژشده بساز (🔬)، در لاگ چاپ نکن
```
**حداقل اجرا** (✅ README `fal-client` و صفحه‌ی مدل):
```python
import fal_client
url = fal_client.upload_file("start.png")                       # نه data: URI
r = fal_client.run("fal-ai/kling-video/v3/pro/image-to-video",
                   arguments={"start_image_url": url, "prompt": "slow push-in", "duration": "5"})
print(r["video"]["url"])
```
**تنظیم‌های مهم**
- ✅ `duration` رشته است (`"3"` تا `"15"`) و `generate_audio` بولی؛ هر دو مستقیم روی هزینه اثر دارند. اول ۳ تا ۵ ثانیه تست کن (🧭).
- ✅ برای کارهای چند‌دقیقه‌ای از صف استفاده کن (`submit` و شناسه‌ی درخواست) تا با قطع اتصال کار پولی گم نشود؛ 🔬 برای هر کار `try/except` جدا بگذار.
- ✅ مدل ارزان‌تر هم‌خانواده: `fal-ai/kling-video/v3/standard/image-to-video`.

**خطاهای رایج**
- 🔬 کلید به **یک تیم** تعلق دارد؛ کلید تیم دیگر حتی بعد از شارژ 403 «Exhausted balance» می‌دهد.
- 🔬 `omnihuman/v1.5` و `infinitalk` برای صدا `data:` URI را نمی‌پذیرند (422)؛ آپلود با `upload_file` یا `rest.alpha.fal.ai/storage/upload/initiate`، سپس `file_url`.
- 🔬 POST با بدنه‌ی خالی به `queue.fal.run/<endpoint>` کار واقعی و **پولی** صف می‌کند؛ وضعیت را با GET یا لغو (`PUT …/requests/<id>/cancel`) بسنج. 🔬 `sync-lipsync/v2/pro` روی کاراکتر انیمیشنی دهان را عوض نکرد.

**هزینه** (✅ [صفحه‌ی مدل](https://fal.ai/models/fal-ai/kling-video/v3/pro/image-to-video/api)، ۲۰۲۶-۱۰-۳۱): Kling 3.0 Pro `$0.112` بر ثانیه بی‌صدا، `$0.168` با صدا، `$0.196` با کنترل صدا (۵ ثانیه با صدا و کنترل ≈ `$0.98`). ⚠️ جدول کلی fal.ai/pricing همان مدل را `$0.14` نشان می‌دهد؛ صورت‌حساب واقعی را در داشبورد با یک کار ۳ ثانیه‌ای بسنج. محافظ: قبل از هر دسته، حداکثر تعداد و ثانیه را در کد بگذار. (🔬 ها: دفتر پروژه‌ها)

## درس‌های حساب و ورودی (۲۰۲۶-۱۰-۲۸) 🔬
- 🔬 کلید API به یک تیم تعلق دارد: حساب شارژشده «No API keys» نشان داد و کلید قدیمی تیم دیگر حتی پس از خرید ۱۰ دلار 403 «User is locked. Reason: Exhausted balance» داد. راه‌حل: کلید را داخل همان تیمِ شارژشده بساز.
- 🔬 POST با بدنه‌ی خالی به `queue.fal.run/<endpoint>` یک درخواست واقعی را به صف می‌گذارد (لغو: `PUT …/requests/<id>/cancel`). وضعیت حساب را فقط با GET وضعیت یا لغو بسنج.
- 🔬 `omnihuman/v1.5` و `infinitalk` برای صدا `data:` URI را نمی‌پذیرند (422 «Failed to download the file» / «URL too long»). آپلود: POST به `https://rest.alpha.fal.ai/storage/upload/initiate` با `{content_type,file_name}` ← PUT بایت‌ها به `upload_url` ← استفاده از `file_url`. Kling v1 ai-avatar data URI را پذیرفت.
- 🔬 (۲۰۲۶-۱۰-۲۸، یک پروژه‌ی واقعی قسمت ۱) `sync-lipsync/v2/pro` روی کاراکتر سه‌بعدی سبک انیمیشن **هیچ تغییری در دهان نداد** (تفاوت ناحیه‌ی دهان با ورودی بی‌صدا فقط در حد نویز فشرده‌سازی، حدود ۲٫۵ در هر ثانیه). در همان نما Kling 3.0 با `generate_audio: true` و صدای Kling ساخته‌شده از جمله‌ی ElevenLabs (`create-voice`، ۵ تا ۳۰ ثانیه) که با `voice_id` به element بسته شد، لب را با صدا حرکت داد. برای کاراکتر کارتونی و انیمیشنی اول ۲ ثانیه آزمون کن؛ پیش از تحویل، حرکت دهان را بسنج.
- 🔬 (۲۰۲۶-۱۰-۳۰) ۳ مدل آواتار هم‌زمان: OmniHuman 1.5 با `data:` URI پس از ۲۳ ثانیه 422 `file_download_error` داد؛ همان کار با آدرس ذخیره‌سازی fal در ۲۹۱ ثانیه تمام شد (۹ ثانیه، 1088×1920، 25 fps)؛ Kling v1 ai-avatar ۲۴۱ ثانیه؛ InfiniteTalk ۲۹۲ ثانیه در صف. دو POST خالی «پروب» هر دو **صف شدند و پول داشتند** و باید لغو می‌شدند. یک 422 اسکریپت را کشت در حالی که دو کار پولی بی‌نظارت ادامه داشت: برای هر کار `try/except` جدا بگذار و با شناسه‌ی درخواست دوباره وصل شو. `duration` در Kling v3 رشته است (`"12"`، بازه‌ی ۳ تا ۱۵). ✅ قیمت‌ها: Kling 3.0 Pro ‏۰٫۱۱۲ دلار بر ثانیه بی‌صدا، sync-lipsync v2 pro ‏۵ دلار بر دقیقه.
- روش و نتیجه‌ی مدل‌ها: [ویدیوی سخن‌گو و راه رفتن](../domains/social-media/ai-video-models.md). [S194](../sources/README.md#s194)

## مرتبط
[ابزارهای پولی تولید محتوا](../domains/social-media/paid-ai-tools.md) · [S155](../sources/README.md#s155)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
