---
name: Light-X
slug: lightx
category: video
domains: [social-media]
verdict: assess
status: researched
summary: مدل تغییر نور و حرکت دوربین مجازی روی ویدیوی موجود، با API روی fal؛ مجوز کد منبع غیرتجاری است و نتیجه نزد ما آزموده نشده.
use_when: "relight an existing video ; add a virtual camera move to an existing clip"
how: "fal-ai/lightx/relight or fal-ai/lightx/recamera; for ic use relight_parameters.relight_prompt as a short lighting phrase with bg_source; $0.10 per output second on relight; clear the licence conflict before commercial use."
url: https://lightx-ai.github.io/
repo: "https://github.com/tqtqliu/Light-X"
license: "S-Lab License 1.0 (non-commercial source); fal page labels commercial"
pricing: paid
risk: medium
sources: [S220]
found_in: [project-2026-10-31]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Light-X

## چیست
✅ Light-X (مقاله‌ی ICLR 2026) ویدیو را با کنترل نور و دوربین دوباره می‌سازد. روی fal دو endpoint دارد: `fal-ai/lightx/relight` و `fal-ai/lightx/recamera` (تأییدشده از OpenAPI رسمی fal).

## کی استفاده کنیم
وقتی نور یا حرکت دوربین یک کلیپ موجود باید عوض شود. ❓ کیفیت هنوز نزد ما آزموده نشده است.

## پرامپت
✅ از README مخزن و schema در fal:

- حالت‌های نور: `ic` با متن، `ref` با تصویر مرجع، `hdr` با نقشه‌ی محیط، `bg` با تصویر زمینه.
- برای `ic` فیلد `relight_parameters` لازم است: `relight_prompt`، `bg_source` (Left، Right، Top، Bottom)، `cfg` با پیش‌فرض ۲، و `use_sky_mask`.
- نمونه‌های مخزن عبارت کوتاه نور هستند، مثل `sunlight`. جمله‌ی بلند صحنه نیست.
- `prompt` جدا اختیاری است و اگر خالی بماند مدل خودش کپشن می‌سازد.
- `ref`، `hdr` و `bg` به `relit_cond_img_url` نیاز دارند.
- دوربین: `mode` یکی از gradual، bullet، direct و dolly-zoom است و `camera` یکی از traj و target.
- ❓ راهنمای رسمی نوشتن پرامپت جدا پیدا نشد.

## قیمت و مجوز
✅ fal برای relight ۰٫۱۰ دلار برای هر ثانیه‌ی خروجی نوشته است. ❓ قیمت recamera را نخواندیم.

⚠️ ناهمخوانی: مجوز مخزن S-Lab License 1.0 است و استفاده‌ی تجاری را بدون اجازه نمی‌دهد، ولی صفحه‌ی fal برچسب Commercial use دارد. ❓ نمی‌دانیم fal اجازه‌ی جدا گرفته است یا نه. پیش از محتوای تجاری از fal بپرس.

## ریسک و هشدار
راهنمای پیش‌فرض ۴۹ فریم دارد؛ ❓ طول خروجی برای کلیپ بلند را پیش از ارسال بسنج.

## مرتبط
[نوشتن پرامپت](../domains/social-media/prompt-writing.md) · [مدل‌های ویدیو](../domains/social-media/ai-video-models.md) · [fal](fal-ai.md)
