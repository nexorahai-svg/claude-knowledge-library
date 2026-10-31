---
name: Open Generative AI (Anil-matcha)
slug: open-generative-ai
category: video
domains: [social-media, security]
verdict: hold
status: researched
summary: اپ رومیزی MIT شبیه «Cinema Studio» هیگزفیلد که در عمل ظاهری برای API پولی MuAPI است؛ «بی‌فیلتر»، نصب‌کننده‌ی بی‌امضا؛ اجرای محلی فقط عکس با sd.cpp و ویدیو با Wan2GP جدا
use_when: "only to read how a multi-studio UI over many models is laid out ; not for production: use fal, Replicate or the vendor's own API instead"
how: "Do not install; if ever tried, only in a VM, never with a real MuAPI key on the main machine; installers are unsigned (xattr -cr / SmartScreen bypass) and the app advertises no content filters"
url: https://github.com/Anil-matcha/Open-Generative-AI
repo: "https://github.com/Anil-matcha/Open-Generative-AI"
license: "MIT (کد اپ)؛ مدل‌ها از راه MuAPI با شرایط خودش"
pricing: freemium
risk: high
sources: [S204]
found_in: [reel-alirezayazdanii-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Open Generative AI (Anil-matcha)

## چیست
- ✅ مخزن [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI): مجوز MIT، حدود ۳۱٫۸ هزار ستاره، آخرین push در ۲۰۲۶-۱۰-۲۹، نسخه‌ی v2.0.0 در ۲۰۲۶-۰۵-۲۳ برای ویندوز، مک و لینوکس (Electron و Next.js).
- ✅ ادعای README: «۶۰۰+ مدل در ۱۴ استودیو» (Image، Video، Lip Sync، Cinema و غیره) و «بدون فیلتر محتوا».
- ✅ **در عمل:** کد مدل‌ها را با `x-api-key` از `api.muapi.ai` صدا می‌زند (`src/lib/muapi.js`). یعنی Kling، Veo، Sora و Midjourney از راه سرویس پولی [MuAPI](https://muapi.ai/pricing) اجرا می‌شوند، نه روی رایانه‌ی تو. MuAPI هزینه را برای هر بار ساخت یا هر ثانیه می‌گیرد. README بسته‌ی «White Label» از ۴۹ دلار در ماه را هم تبلیغ می‌کند.
- ✅ **اجرای محلی (فقط اپ رومیزی):** sd.cpp داخل اپ است ولی فقط عکس می‌سازد. برای ویدیو باید [Wan2GP](https://github.com/deepbeepmeep/Wan2GP) را خودت جدا نصب کنی؛ سبک‌ترین مدلش Wan 2.1 1.3B است که 480p و حدود ۸ گیگ VRAM می‌خواهد. نسخه‌ی وب همیشه API ابری است.
- ✅ در کد ردیاب تحلیلی (PostHog، Sentry، GA و مانند آن) پیدا نشد. نشانی‌های بیرونی بیشتر `muapi.ai` و یک CloudFront است. سه submodule از همین نویسنده دارد که خوانده نشد (❓).

## ریسک و هشدار
- ⚠️ نصب‌کننده‌ها امضا ندارند. README برای مک `xattr -cr` و برای ویندوز رد کردن هشدار SmartScreen را آموزش می‌دهد.
- ⚠️ «بدون فیلتر» یعنی خروجی ممکن است شرایط استفاده‌ی سازنده‌ی مدل را نقض کند. MuAPI ابزار «حذف واترمارک ویدیو» و «جابه‌جایی چهره» هم می‌فروشد. هر دو با AUP مدل‌هایی مثل [LTX-2.5](ltx-2-5.md) و قانون برچسب AI در تضادند.
- ⚠️ نام «Cinema Studio» محصول Higgsfield است. این اپ ربطی به Higgsfield ندارد.
- 🧭 Midjourney API رسمی ندارد، پس دسترسی از راه واسطه احتمالاً غیررسمی است (❓ شرایط MuAPI خوانده نشد).

## کی استفاده کنیم
👀 استفاده نکن. برای ویدیوی پولی از [fal](fal-ai.md) یا API خود سازنده استفاده کن ([ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md)). برای اجرای محلی Wan مستقیم سراغ [Wan 2.2](wan-2-2.md) برو.

## قیمت و مجوز
✅ کد MIT است. تولید با کلید MuAPI پولی است، مثلاً ۰٫۰۱ تا ۰٫۲۵ دلار برای هر ابزار ([جدول قیمت](https://muapi.ai/pricing)). مدل‌ها شرایط خود را دارند.

## ادعاهای ریل (۲۰۲۶-۱۰-۳۰)
- ریل @alirezayazdanii ([S204](../sources/README.md#s204)) گفته «نسخه‌ی اوپن‌سورس Cinema Studio که مستقیم روی کامپیوتر اجرا می‌شود و بی‌هزینه است». ✅ متن‌باز درست است. ❌ «بی‌هزینه و محلی» برای ویدیوی سینمایی درست نیست، چون از API پولی می‌گذرد. نام مخزن در پست نیامده و برای گرفتنش باید کامنت «راه اندازی» گذاشت (قیف کامنت). نام مخزن از فریم ویدیو خوانده شد.
