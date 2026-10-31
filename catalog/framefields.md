---
name: Framefields
slug: framefields
category: video
domains: [social-media, website]
verdict: assess
status: researched
summary: ویدیو و تصویر کدمحور با رندر بومی روی WebGPU (بدون مرورگر headless) و بسته‌ی npm که عامل کدنویس با TypeScript هدایتش می‌کند؛ بتا
use_when: "comparing code-to-video options with Remotion and HyperFrames ; a WebGPU/3D-heavy video scene driven by an agent on a machine with a GPU"
how: "Read the repo and docs first; try only on a throwaway project: npx framefields init my-film --install with a pinned version (beta, Node 22 or newer, needs a GPU or Mesa lavapipe on Linux); do not replace HyperFrames or Remotion until a real test"
url: https://github.com/gatewai-dev/framefields
repo: "https://github.com/gatewai-dev/framefields"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S215, S216]
found_in: [sweep-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Framefields

## چیست
✅ (GitHub API، README و npm، ۲۰۲۶-۱۰-۳۱) مخزن سازمان gatewai-dev؛ ساخته‌شده ۲۰۲۶-۱۰-۰۲، آخرین push ۲۰۲۶-۱۰-۳۱، حدود ۵۰۰ ستاره، Apache-2.0. بسته‌ی `framefields` در npm نسخه‌ی 2.9.2 (Apache-2.0). ادعای README: ترکیب‌بندی، موشن‌گرافیک و سه‌بعدی در یک بسته؛ رندر مستقیم روی GPU با Dawn/WebGPU بدون Chromium و Puppeteer؛ قطعی و فریم‌به‌فریم؛ خروجی MP4 با رمزگذار سخت‌افزاری؛ `npx skills add gatewai-dev/framefields` به عامل آموزش می‌دهد. وضعیت را خود README «beta» می‌نویسد. ❓ کیفیت خروجی و پایداری را نیازموده‌ایم.

## کی استفاده کنیم
🧭 مقایسه با [HyperFrames](hyperframes.md) و Remotion برای صحنه‌های سه‌بعدی و افکت سنگین؛ برای ویدیوی ساده‌ی متنی HyperFrames که آزموده‌ایم کافی است. هنوز در هیچ پروژه‌ای آزموده نشده.

## قیمت و مجوز
✅ Apache-2.0 و رایگان؛ ❓ طرح پولی یا ابری ندیدیم.

## ریسک و هشدار
⚠️ بتا؛ Node 22 و GPU لازم دارد (در رایانه‌ی بی‌GPU روی CPU با Mesa کند است 🧭). وابستگی‌های بومی (`webgpu`، `sharp`) باینری می‌آورند؛ نسخه را پین کن و روی پروژه‌ی آزمایشی نصب کن. ❓ تله‌متری بررسی نشد.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S215](../sources/README.md#s215) · [S216](../sources/README.md#s216)
