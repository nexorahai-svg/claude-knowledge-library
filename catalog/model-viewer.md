---
name: model-viewer (Google)
slug: model-viewer
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: نمایش مدل سه‌بعدی در صفحه و واقعیت افزوده در گوشی با یک تگ HTML
url: https://modelviewer.dev/
repo: "https://github.com/google/model-viewer"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S55]
found_in: [project/client]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# model-viewer (Google)

## چیست
✅ کامپوننت وب `<model-viewer>` گوگل: فایل glTF/GLB را با چرخش و زوم نشان می‌دهد و دکمه‌ی AR دارد. حالت‌های AR: `webxr`، `scene-viewer` (اندروید)، `quick-look` (آیفون، با فایل USDZ). آخرین نسخه ✅ **4.4.0**.

## کی استفاده کنیم
🔬 در طراح سه‌بعدی یک سایت مشتری برای دیدن پرگولا و سایه‌بان در فضای واقعی با گوشی. 🧭 برای پیکربندی‌کننده‌ی محصول، صحنه‌ی اصلی با three.js و خروجی GLB به model-viewer برای AR.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
🔬 وابستگی peer به نسخه‌ی خاص three.js باعث خطای `ERESOLVE` در build شد؛ راه‌حل `.npmrc` با `legacy-peer-deps=true`. 🧭 AR برای سازه‌های خیلی بزرگ (پرگولای چندمتری) در گوشی سخت قابل استفاده است؛ اندازه و نقطه‌ی شروع را راهنمایی کن.

## مرتبط
[سه‌بعدی](../domains/website/03-motion-3d/3d-webgl.md) · [Three.js](threejs.md) · [S55](../sources/README.md#s55)
