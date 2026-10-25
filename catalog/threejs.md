---
name: Three.js
slug: threejs
category: 3d
domains: [website, social-media]
verdict: adopt
status: researched
summary: کتابخانه‌ی استاندارد سه‌بعدی و WebGL در مرورگر
url: https://threejs.org/
repo: "https://github.com/mrdoob/three.js"
license: "MIT"
pricing: free
risk: low
sources: [S11, S63]
found_in: [batch-01/P24]
last_checked: 2026-10-23
next_check: "2027-01-15"
---

# Three.js

## چیست
✅ استاندارد صنعت برای سه‌بعدی در وب، MIT. Casa Serra با three@0.160.1 ساخته شده.

✅ آخرین نسخه‌ی پایدار: **r186** (GitHub releases، ۲۴ سپتامبر ۲۰۲۶؛ در npm نسخه‌ی 0.186.1).

🔬 پروژه‌ی MARIO E.G.S.H همین r186 را **بدون npm** استفاده می‌کند: فایل‌های ES module (`three.module.js` و `three.core.js`) با فایل مجوز در پوشه‌ی vendor پروژه، با `import()` پویا و CSP سخت ([مطالعه‌ی موردی ۴](../domains/website/03-motion-3d/3d-webgl.md)، دفتر پروژه‌ها).

🔬 پروژه‌ی K25 (۲۰۲۶-۱۰-۲۳): r186 (three@0.186.1 از jsDelivr با importmap) برای نمایشگر GLB با OrbitControls، برچسب ابعاد با CSS2DRenderer و Sky. خروجی glTF از Blender بافت‌های رویه‌ای را از دست می‌دهد؛ در نمایشگر با نام متریال، بافت canvas و UV مسطح از مختصات جهانی دوباره ساخته شد ([کارت Blender](blender.md)، دفتر پروژه‌ها).

## کی استفاده کنیم
صحنه‌ی سه‌بعدی، محصول تعاملی، «نقشه به واقعیت». در React: React Three Fiber.

## قیمت و مجوز
✅ رایگان (MIT).

## ریسک و هشدار
کم. همیشه نسخه‌ی جایگزین (عکس یا ویدیو) برای دستگاه ضعیف بساز.

✅ حافظه‌ی GPU خودکار آزاد نمی‌شود: هندسه، متریال و تکسچر هر کدام `dispose()` می‌خواهند (راهنمای رسمی، [S63](../sources/README.md#s63)). 🧭 نسخه‌ی vendor‌شده را `npm outdated` نمی‌بیند؛ شماره‌ی نسخه را جایی ثبت کن.

## مرتبط
[سه‌بعدی و WebGL](../domains/website/03-motion-3d/3d-webgl.md) · [S11](../sources/README.md#s11) · [S63](../sources/README.md#s63)
