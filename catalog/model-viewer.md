---
name: model-viewer (Google)
slug: model-viewer
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: نمایش مدل سه‌بعدی در صفحه و واقعیت افزوده در گوشی با یک تگ HTML
use_when: "showing a glTF/GLB 3D model on a web page with rotate/zoom ; adding AR view on phones ; product configurator with AR"
how: "Use Google <model-viewer> 4.4.0 (Apache-2.0); AR modes webxr, scene-viewer (Android), quick-look (iPhone; a USDZ is generated on the fly); main scene in three.js and export GLB; if ERESOLVE peer error add legacy-peer-deps=true in .npmrc"
url: https://modelviewer.dev/
repo: "https://github.com/google/model-viewer"
license: "Apache-2.0"
pricing: free
risk: low
sources: [S55]
found_in: [project/client]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# model-viewer (Google)

## چیست
✅ کامپوننت وب `<model-viewer>` گوگل: فایل glTF/GLB را با چرخش و زوم نشان می‌دهد و دکمه‌ی AR دارد. حالت‌های AR: `webxr`، `scene-viewer` (اندروید)، `quick-look` (آیفون، با فایل USDZ). آخرین نسخه ✅ **4.4.0**.

## دستور سریع

**نصب** (✅ [README بسته](https://github.com/google/model-viewer/blob/master/packages/model-viewer/README.md) و متادیتای npm؛ `4.4.0` به `three ^0.183.0` وابسته است):
```bash
npm install three@0.183.2 @google/model-viewer@4.4.0    # three را با نسخه‌ی خود model-viewer هم‌قفل نگه دار
```
یا بدون npm و بدون دعوای peer (🧭): یک `<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@4.4.0/dist/model-viewer.min.js">`.

**حداقل اجرا** (✅ صفحه‌ی اصلی modelviewer.dev):
```html
<model-viewer src="model.glb" alt="توضیح مدل" camera-controls shadow-intensity="1"
  ar ar-modes="webxr scene-viewer quick-look" poster="poster.webp"></model-viewer>
```
**تنظیم‌های مهم**
- ✅ `loading` (`auto`، `lazy`، `eager`) و `reveal` (`auto`، `manual`): مدل سنگین را `lazy` بگذار و `poster` بده تا صفحه‌ی خالی سفید دیده نشود.
- ✅ `ar-modes` فهرست اولویت است؛ پیش‌فرض `webxr scene-viewer quick-look`.
- ✅ `environment-image` یک `.hdr` یا `.jpg` می‌گیرد (`neutral` پیش‌فرض)؛ فایل بزرگ حجم صفحه را بالا می‌برد.

**خطاهای رایج**
- ✅ README می‌گوید اگر ناچار از three دیگر شدی، `--legacy-peer-deps` راه دور زدن است ولی «issue نزن»؛ 🔬 در یک پروژه ERESOLVE همین‌طور حل شد (`legacy-peer-deps=true` در `.npmrc`).
- ✅ اصلاح بالا: `quick-look` در iOS دیگر **حتماً** `ios-src` (USDZ) نمی‌خواهد؛ بدون آن USDZ را در لحظه می‌سازد (مستند `ios-src` و `ar-modes`).
- 🧭 AR برای سازه‌ی چندمتری در گوشی سخت است؛ مقیاس (`ar-scale`) و نقطه‌ی شروع را راهنمایی کن. فقط glTF/GLB پشتیبانی می‌شود.

## کی استفاده کنیم
🔬 در طراح سه‌بعدی یک پروژه‌ی واقعی برای دیدن پرگولا و سایه‌بان در فضای واقعی با گوشی. 🧭 برای پیکربندی‌کننده‌ی محصول، صحنه‌ی اصلی با three.js و خروجی GLB به model-viewer برای AR.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
🔬 وابستگی peer به نسخه‌ی خاص three.js باعث خطای `ERESOLVE` در build شد؛ راه‌حل `.npmrc` با `legacy-peer-deps=true`. 🧭 AR برای سازه‌های خیلی بزرگ (پرگولای چندمتری) در گوشی سخت قابل استفاده است؛ اندازه و نقطه‌ی شروع را راهنمایی کن.

## مرتبط
[سه‌بعدی](../domains/website/03-motion-3d/3d-webgl.md) · [Three.js](threejs.md) · [S55](../sources/README.md#s55)
