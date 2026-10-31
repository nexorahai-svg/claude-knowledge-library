---
name: Tencent Hunyuan Prism
slug: hunyuan-prism
category: video
domains: [social-media]
verdict: assess
status: researched
summary: چارچوب پژوهشی آموزش مدل‌های هم‌زمان ویدیو و صدا تا ۲K با توجه تُنُک؛ پیش‌نمایش آلفا و بتا، سنگین (حدود ۲۰۸ گیگ وزن)، برای تولید محتوای ما کاربردی نیست
use_when: "tracking research on native 2K joint video-audio generation ; only if training or fine-tuning a video-audio model on a rented multi-GPU cluster"
how: "Read-only watch item; do not install or download weights (about 208 GB, needs CUDA 12.4 and a flash-attn build) without the user's yes; for real clips use Wan, LTX or Kandinsky instead"
url: https://github.com/Tencent-Hunyuan/Prism
repo: "https://github.com/Tencent-Hunyuan/Prism"
license: "MIT (کد و وزن Prism) + Apache-2.0 برای مدل پایه‌ی MOVA-360p"
pricing: free
risk: low
sources: [S178]
found_in: [sweep-2026-10-26]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# Tencent Hunyuan Prism

## چیست
- ✅ مخزن رسمی [Tencent-Hunyuan/Prism](https://github.com/Tencent-Hunyuan/Prism): چارچوب «توجه تُنُک پویا» برای آموزش بومی مدل‌های هم‌زمان ویدیو و صدا در ۷۲۰p تا ۲K. مقاله: [arXiv 2610.05416](https://arxiv.org/abs/2610.05416). ساخته‌شده ۲۰۲۶-۰۹-۲۱، آخرین push ۲۰۲۶-۱۰-۱۵، ۱٫۴ هزار ستاره، بایگانی نشده، بدون release برچسب‌خورده.
- ✅ خروجی منتشرشده «پیش‌نمایش» است: Prism-preview-alpha (پایدار) و Prism-preview-beta (حرکت). فهرست کارهای README: Prism-pro هنوز منتشر نشده. وزن‌ها در [Hugging Face](https://huggingface.co/FrancisRing/Prism) (مجموع فایل‌ها حدود ۲۰۸ گیگابایت، شامل مدل پایه).
- ✅ ادعای اصلی مقاله: ۲٫۵ برابر آموزش سریع‌تر از توجه کامل با کیفیت بهتر. این ادعای سازنده است؛ آزمون مستقل ندیدم (❓).
- ✅ ساخته‌شده روی MOVA-360p؛ نیازها: پایتون ۳٫۱۰+، CUDA ۱۲٫۴+، flash-attn، ffmpeg؛ README برای آموزش خوشه‌ی چندگره را شرح می‌دهد. ✅ README (https://github.com/Tencent-Hunyuan/Prism) VRAM را می‌گوید: استنتاج ۷۲۰p روی یک GPU ‏۸۰ گیگ (با `--offload cpu`)؛ ۱۰۸۰p و 2K دست‌کم ۴ کارت ۸۰ گیگ؛ آموزش ۷۲۰p دست‌کم ۳۲ و ۱۰۸۰p/2K دست‌کم ۶۴ کارت ۸۰ گیگ. پس روی ۸ گیگ شدنی نیست.
- ✅ زبان: ورودی متن/تصویر؛ ❓ پشتیبانی فارسی در گفتار یا متن گفته نشده.

## ریسک و هشدار
- ✅ ریسک امنیتی پایین: کد پژوهشی باز، نصب از pip و Hugging Face. ریسک اصلی منابع است: دانلود بسیار حجیم و ساخت flash-attn.
- ⚠️ GitHub مجوز را NOASSERTION نشان می‌دهد؛ متن [LICENSE](https://github.com/Tencent-Hunyuan/Prism/blob/main/LICENSE) را کامل خواندم: Prism تحت MIT است (کد، پارامتر و وزن‌های Tencent)، و تنها مؤلفه‌ی ثالث فهرست‌شده MOVA-360p با Apache-2.0 است. محدودیت اضافه نیست.

## کی استفاده کنیم
👀 فقط پیگیری پژوهشی. برای تولید محتوا مدل‌های آماده‌ی [Kandinsky 6](kandinsky-6.md) و [LTX-2.5](ltx-2-5.md) و Wan به‌کارتر هستند. اگر Prism-pro منتشر شد دوباره بسنج.

## قیمت و مجوز
✅ رایگان، MIT (+ Apache-2.0 برای مدل پایه).

## مرتبط
[S178](../sources/README.md#s178) · [مدل‌های ویدیوی هوش مصنوعی](../domains/social-media/ai-video-models.md)
