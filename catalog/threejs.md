---
name: Three.js
slug: threejs
category: 3d
domains: [website, social-media]
verdict: adopt
status: researched
summary: کتابخانه‌ی استاندارد سه‌بعدی و WebGL در مرورگر
use_when: "interactive 3D scene, product viewer, map-to-reality on a website"
how: "npm install three (r187 latest; our projects pin r186; MIT) or vendor the ES modules; in React use React Three Fiber; call dispose() on geometry, material, texture; always add a photo/video fallback for weak devices; record vendored version"
url: https://threejs.org/
repo: "https://github.com/mrdoob/three.js"
license: "MIT"
pricing: free
risk: low
sources: [S11, S63, S208]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Three.js

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) یادداشت r187: کد منسوخ‌شده از r177 و `getSharedDataFromNode()` حذف شد؛ پیش از ارتقا بخش ۱۸۶ به ۱۸۷ راهنمای مهاجرت را بخوان (❓ کامل خوانده نشد): https://github.com/mrdoob/three.js/releases/tag/r187 · https://github.com/mrdoob/three.js/wiki/Migration-Guide#186--187
✅ استاندارد صنعت برای سه‌بعدی در وب، MIT. Casa Serra با three@0.160.1 ساخته شده.

✅ آخرین نسخه‌ی پایدار: **r187** (GitHub releases و npm 0.187.0، هر دو ۲۰۲۶-۱۰-۳۰؛ [S208](../sources/README.md#s208)). قبلی r186 بود (۲۴ سپتامبر ۲۰۲۶؛ npm 0.186.1). پروژه‌های ما روی r186 ثابت‌اند و ارتقا فقط پس از خواندن آن‌ها.

🔬 یک فروشگاه واقعی همین r186 را **بدون npm** استفاده می‌کند: فایل‌های ES module (`three.module.js` و `three.core.js`) با فایل مجوز در پوشه‌ی vendor پروژه، با `import()` پویا و CSP سخت ([مطالعه‌ی موردی ۴](../domains/website/03-motion-3d/3d-webgl.md)، دفتر پروژه‌ها).

🔬 یک پروژه‌ی واقعی (۲۰۲۶-۱۰-۲۳): r186 (three@0.186.1 از jsDelivr با importmap) برای نمایشگر GLB با OrbitControls، برچسب ابعاد با CSS2DRenderer و Sky. خروجی glTF از Blender بافت‌های رویه‌ای را از دست می‌دهد؛ در نمایشگر با نام متریال، بافت canvas و UV مسطح از مختصات جهانی دوباره ساخته شد ([کارت Blender](blender.md)، دفتر پروژه‌ها).

## دستور سریع

**نصب** (✅ [manual](https://threejs.org/manual/) و npm؛ آخرین `0.187.0`، پین پروژه‌های ما `0.186.1`):
```bash
npm install --save-exact three@0.186.1      # r187 با postprocessing@6.39.5 (peer: three <0.187) ERESOLVE می‌دهد
npm install --save-dev @types/three          # فقط با TypeScript
```
**حداقل اجرا** (✅ الگوی README مخزن، کوتاه‌شده):
```js
import * as THREE from 'three';
const scene = new THREE.Scene(), camera = new THREE.PerspectiveCamera(70, innerWidth / innerHeight, 0.01, 10);
camera.position.z = 1;
const mesh = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.2, 0.2), new THREE.MeshNormalMaterial());
scene.add(mesh);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight); document.body.appendChild(renderer.domElement);
renderer.setAnimationLoop((t) => { mesh.rotation.y = t / 1000; renderer.render(scene, camera); });
```
**تنظیم‌های مهم**
- ✅ بدون npm: importmap با نسخه‌ی ثابت، مثلاً `"three": "https://cdn.jsdelivr.net/npm/three@0.186.1/build/three.module.js"`؛ 🔬 با CSP سخت فایل‌ها را در پوشه‌ی vendor بگذار.
- 🧭 `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`: بیشتر از ۲ هزینه‌ی GPU را بالا می‌برد و فرق دیده نمی‌شود. `antialias: true` را روی دستگاه ضعیف خاموش کن.
- ✅ `setAnimationLoop` به‌جای `requestAnimationFrame` دستی (در WebXR هم کار می‌کند).

**خطاهای رایج**
- ✅ هندسه، متریال و تکسچر خودکار آزاد نمی‌شوند: `dispose()` بزن ([راهنمای رسمی](https://threejs.org/manual/#en/how-to-dispose-of-objects)).
- ✅ بسته‌های دیگر نسخه‌ی three را قفل می‌کنند: `@google/model-viewer@4.4.0` می‌خواهد `^0.183.0` و `postprocessing@6.39.5` می‌خواهد `<0.187.0` (متادیتای npm). پیش از ارتقا به r187 این دو را ببین.
- 🧭 نسخه‌ی vendor‌شده را `npm outdated` نمی‌بیند؛ شماره را در `STATE.md` بنویس. بافت‌های رویه‌ای Blender در glTF نمی‌آیند ([کارت Blender](blender.md)).

## کی استفاده کنیم
صحنه‌ی سه‌بعدی، محصول تعاملی، «نقشه به واقعیت». در React: React Three Fiber.

## قیمت و مجوز
✅ رایگان (MIT).

## ریسک و هشدار
کم. همیشه نسخه‌ی جایگزین (عکس یا ویدیو) برای دستگاه ضعیف بساز.

✅ حافظه‌ی GPU خودکار آزاد نمی‌شود: هندسه، متریال و تکسچر هر کدام `dispose()` می‌خواهند (راهنمای رسمی، [S63](../sources/README.md#s63)). 🧭 نسخه‌ی vendor‌شده را `npm outdated` نمی‌بیند؛ شماره‌ی نسخه را جایی ثبت کن.

## مرتبط
[سه‌بعدی و WebGL](../domains/website/03-motion-3d/3d-webgl.md) · [S11](../sources/README.md#s11) · [S63](../sources/README.md#s63)
