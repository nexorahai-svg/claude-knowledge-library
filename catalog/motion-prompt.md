---
name: Motion Prompt
slug: motion-prompt
category: claude-code-tooling
domains: [website, social-media]
verdict: trial
status: researched
summary: گالری ۱۲۰ نمونه‌ی متحرک با نام، پرامپت و کد Canvas؛ مهارت انتخاب از گالری
url: https://showheyohtaki.github.io/motion-prompt/
repo: "https://github.com/showheyohtaki/motion-prompt"
license: "MIT"
pricing: free
risk: low
sources: [S92]
found_in: [batch-07]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Motion Prompt

## چیست
✅ سازنده Shohei Ohtaki؛ ساخته‌شده ۲۰۲۶-۱۰-۱۴؛ حدود ۴۰۵ ستاره. پنج بسته: موشن‌گرافیک، دوربین و گذار، کامپوننت رابط، افکت لندینگ، سبک عکس و نور. هر نمونه یک تابع Canvas که **تابع خالص زمان** است (همان قانون [ویدیو با کد](../domains/social-media/code-to-video.md)). ایده‌ی گالری+مهارت را صادقانه از Lucian UX/UI Prompt (MIT) گرفته و ذکر کرده.

## کی استفاده کنیم
🧭 وقتی نام حرکتی را که می‌خواهی نمی‌دانی: از گالری انتخاب کن، Claude کد و مشخصاتش را می‌گیرد. با Remotion، CSS و Canvas.

## قیمت و مجوز
✅ MIT؛ استفاده‌ی تجاری مجاز برای کد، ویدیو و تصویر؛ خط اول کد هر نمونه (نام و مجوز) باید بماند.

## ریسک و هشدار
✅ (اسکریپت خوانده شد) `pick` یک سرور محلی روی 127.0.0.1 با توکن تصادفی باز می‌کند، مرورگر را با `xdg-open` باز می‌کند و منتظر انتخاب می‌ماند؛ داده را از GitHub Pages یا raw.githubusercontent می‌گیرد و در `~/.cache/motion-prompt` نگه می‌دارد. ⚠️ پست @yarad_ai گفت متنی را در Claude Code بگذار که «این آدرس را بخوان و مهارت را نصب کن»؛ نصب با دستور رسمی (`npx skills add showheyohtaki/motion-prompt` یا `/plugin install motion-prompt@motion-prompt`) **بعد از خواندن فایل‌ها** بهتر است. پروژه‌ی پنج‌روزه و یک‌نفره.

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [حرکت و انیمیشن](../domains/website/03-motion-3d/motion-animation.md) · [S92](../sources/README.md#s92) · غربال دسته‌ی ۰۷
