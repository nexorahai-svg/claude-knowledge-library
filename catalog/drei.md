---
name: Drei
slug: drei
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: مجموعه‌ی کمکی React Three Fiber: کنترل، بارگذاری، محیط، متن
use_when: "any React Three Fiber 3D scene needing controls, loaders, environment or text ; building a 3D web hero"
how: "npm install @react-three/drei (10.x, MIT) next to R3F and import only the helpers needed"
url: https://github.com/pmndrs/drei
repo: "https://github.com/pmndrs/drei"
license: "MIT"
pricing: free
risk: low
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# Drei

## چیست
✅ کامپوننت‌های آماده برای R3F. نسخه‌ی 10.7.9 (۲۰۲۶-۰۹-۲۵).

## دستور سریع

**نصب** (✅ README و متادیتای npm؛ peer: `react ^19`، `@react-three/fiber ^9`، `three >=0.159`):
```bash
npm install @react-three/drei@10.7.9
```
**حداقل اجرا** (✅ [مستند useGLTF](https://pmndrs.github.io/drei/loaders/gltf-use-gltf) و Environment):
```jsx
import { Suspense } from 'react'
import { Canvas } from '@react-three/fiber'
import { OrbitControls, useGLTF, Environment } from '@react-three/drei'
function Model() { const { scene } = useGLTF('/model.glb'); return <primitive object={scene} /> }
useGLTF.preload('/model.glb')
export default () => <Canvas><Suspense fallback={null}><Model /><Environment files="/env.hdr" /></Suspense><OrbitControls /></Canvas>
```
**تنظیم‌های مهم**
- ✅ `Environment`: برای تولید از `files` استفاده کن (`.hdr`، `.exr` یا gainmap که کوچک‌ترین است)؛ `preset` روی CDN است و مستند می‌گوید برای تولید نیست.
- ✅ `useGLTF(url, '/draco-gltf')` یا `useGLTF.setDecoderPath(path)` دیکودر Draco را از پوشه‌ی خودت می‌خواند.
- ✅ برای محیط سفارشی، `resolution` پیش‌فرض `256` و `frames` فقط وقتی لازم است که محیط انیمیشن داشته باشد.

**خطاهای رایج**
- ✅ Draco به‌طور پیش‌فرض از `gstatic.com` بارگذاری می‌شود؛ با CSP سخت، آفلاین یا اینترنت محدود شکست می‌خورد → دیکودر را خودت میزبانی کن.
- ✅ `Environment preset="city"` هم از CDN می‌خواند و ممکن است در تولید خطا بدهد.
- 🧭 فقط ابزارهای لازم را ایمپورت کن؛ کل بسته را نکش.

## کی استفاده کنیم
🧭 همیشه همراه R3F؛ فقط بخش‌های لازم را ایمپورت کن.

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
کم.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)
