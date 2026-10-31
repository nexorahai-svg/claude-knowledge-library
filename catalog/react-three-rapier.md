---
name: React Three Rapier
slug: react-three-rapier
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: موتور فیزیک Rapier (WASM) برای React Three Fiber
use_when: "a 3D scene needs real physics (collisions, falling)"
how: "npm install @react-three/rapier (2.2.0, MIT) only if real physics is needed; wrap the scene in Physics inside Suspense and meshes in RigidBody; mind WASM size and CPU; maintenance has slowed"
url: https://github.com/pmndrs/react-three-rapier
repo: "https://github.com/pmndrs/react-three-rapier"
license: "MIT"
pricing: free
risk: low
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-25"
---

# React Three Rapier

## چیست
✅ فیزیک واقعی (برخورد، سقوط). نسخه‌ی 2.2.0 (۲۰۲۵-۱۱-۰۳)؛ حدود ۱۱ ماه بدون انتشار جدید؛ ولی مخزن هنوز commit دارد (آخرین push در ۲۰۲۶-۱۰-۱۲).
✅ نصب و اجرا (https://github.com/pmndrs/react-three-rapier، ۲۰۲۶-۱۰-۲۷): npm install @react-three/rapier

## دستور سریع

**نصب** (✅ README و متادیتای npm؛ peer: `react ^19`، `@react-three/fiber ^9.0.4`):
```bash
npm install @react-three/rapier@2.2.0      # با React 18 باید نسخه‌ی 1 و fiber 8 بگیری
```
**حداقل اجرا** (✅ الگوی README، کوتاه‌شده):
```jsx
import { Suspense } from 'react'
import { Canvas } from '@react-three/fiber'
import { Physics, RigidBody, CuboidCollider } from '@react-three/rapier'
export default () => (
  <Canvas><Suspense>
    <Physics debug>
      <RigidBody colliders="hull" restitution={1}><mesh><torusGeometry /><meshNormalMaterial /></mesh></RigidBody>
      <CuboidCollider position={[0, -2, 0]} args={[20, 0.5, 20]} />
    </Physics>
  </Suspense></Canvas>
)
```
**تنظیم‌های مهم**
- ✅ `timeStep` پیش‌فرض `1/60` است؛ `1/30` هزینه‌ی CPU را نصف می‌کند، `"vary"` ناپایدار و غیرقطعی می‌شود (خود README هشدار می‌دهد).
- ✅ `colliders`: `"cuboid"`، `"ball"`، `"hull"` و `"trimesh"`؛ 🧭 تا جای ممکن cuboid یا ball بگذار و trimesh را برای اجسام ساکن نگه دار.
- ✅ با `<Canvas frameloop="demand">` از `<Physics updateLoop="independent">` استفاده کن تا فقط وقتی جسمی حرکت می‌کند رندر شود.

**خطاهای رایج**
- ✅ `Physics` باید داخل `Suspense` باشد (Rapier تنبل بارگذاری می‌شود).
- ✅ `debug` را فقط در توسعه بگذار؛ و snapshot فقط وقتی کار می‌کند که جهان فیزیک دقیقاً همان باشد.
- ✅ از انتشار 2.2.0 (۲۰۲۵-۱۱-۰۳) نسخه‌ی تازه نیامده → قبل از وابسته شدن، سازگاری با نسخه‌ی R3F پروژه را بسنج؛ وزن WASM را در بسته‌ی اصلی نگذار.

## کی استفاده کنیم
🧭 فقط وقتی فیزیک واقعی لازم است؛ برای انیمیشن ساده نه.

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
وزن WASM و مصرف CPU؛ نگهداری کند شده.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
