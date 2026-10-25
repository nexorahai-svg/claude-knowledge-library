---
name: Venice (venice.ai)
slug: venice-ai
category: local-ai
domains: [claude-code]
verdict: assess
status: researched
summary: سرویس گفتگو و API با مدل‌های باز و «بی‌سانسور»؛ ادعای عدم ذخیره‌ی پرامپت با چهار حالت حریم خصوصی
url: https://venice.ai
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S130]
found_in: [batch-16]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# Venice

## چیست
✅ (docs.venice.ai/overview/privacy) اپ و API گفتگو، تصویر، ویدیو و صدا با مدل‌های باز. درخواست‌ها از پراکسی Venice می‌گذرند و طبق ادعای خودش «محتوای پرامپت و پاسخ ذخیره یا لاگ نمی‌شود». چهار حالت: Anonymous (هویت از سازنده‌ی مدل پنهان، ولی **متن را سازنده‌ی مدل می‌بیند**)، Private (نگه‌نداشتن داده با قرارداد)، TEE و E2EE. MCP، CLI و راهنمای Claude Code هم دارد.
❓ پست معرفی گفت DeepSeek V4.1 Flash «بی‌سانسور» در اپ رایگان و بی‌محدودیت است؛ سایت اصلی venice.ai از این شبکه باز نشد (timeout) و قیمت و سقف رایگان بررسی نشد. عدد بنچمارک DeepSeek ادعای خود Venice است.

## کی استفاده کنیم
👀 کاری در پروژه‌های ما ندارد. «بی‌سانسور» یعنی محافظ‌های ایمنی مدل برداشته شده؛ برای محصول مشتری مناسب نیست.

## قیمت و مجوز
❓ بررسی نشد.

## ریسک و هشدار
⚠️ داده‌ی مشتری را به آن نده؛ ادعای حریم خصوصی را مستقل نسنجیده‌ایم و در حالت Anonymous متن به سازنده‌ی مدل می‌رسد.

## مرتبط
[هوش مصنوعی در محصول](../domains/website/04-tech/ai-in-product.md) · [S130](../sources/README.md#s130) · دسته‌ی ۱۶
