---
name: bg0
slug: bg0
category: assets-media
domains: [website, social-media]
verdict: assess
status: researched
summary: حذف پس‌زمینه‌ی تصویر کاملاً در مرورگر با BiRefNet و WebGPU
use_when: "remove image background privately in browser ; add background removal to a website"
how: "bun install --frozen-lockfile && bun run dev; check BiRefNet weights licence for commercial use."
url: https://github.com/opencoredev/bg0
repo: "https://github.com/opencoredev/bg0"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S212]
found_in: [github-scan-2026-10-30]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# bg0

## چیست
✅ حذف پس‌زمینه کاملاً در مرورگر با BiRefNet (ONNX) و WebGPU/WASM، بدون آپلود و حساب؛ Apache-2.0؛ بسته‌ی @bg0/browser برای افزودن به سایت. وزن BiRefNet از جای دیگر دانلود و کش می‌شود (مجوزش جدا).

## کی استفاده کنیم
🧭 نمونه‌ی کاربرد: remove image background privately in browser؛ add background removal to a website. وضعیت: 👀 فعلاً زیر نظر؛ بعد از بررسی بیشتر تصمیم می‌گیریم.

## قیمت و مجوز
- مجوز: Apache-2.0 (✅ از LICENSE مخزن؛ ستاره‌ها ۴۸۲ در تاریخ بررسی).
- قیمت: رایگان.

## ریسک و هشدار
- سطح ریسک: low.
- ❓ مجوز وزن مدل (THIRD_PARTY_NOTICES.md) تأیید نشد. «بدون آپلود» ادعای README است. مدل در اولین استفاده دانلود می‌شود.
- همه محلی در مرورگر؛ مجوز وزن BiRefNet خوانده نشد.
- ❓ مجوز وزن، کیفیت روی موی ریز، صفحهٔ privacy.
- 👀 این ابزار در پروژه‌ی واقعی آزمایش نشد؛ فقط مخزن و مستندات خوانده شد (هیچ کاری اجرا یا نصب نشد).

## مرتبط
- منبع: [S212](../sources/S212.md)
- ساخته‌ی اسکن GitHub در ۲۰۲۶-۱۰-۳۰
- لینک اصلی: https://github.com/opencoredev/bg0
