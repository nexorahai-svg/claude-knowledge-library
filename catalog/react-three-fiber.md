---
name: React Three Fiber
slug: react-three-fiber
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: نوشتن صحنه‌ی Three.js به‌صورت کامپوننت React
use_when: "adding a 3D scene to a React or Next.js site"
how: "npm install three @react-three/fiber (9.8.2, MIT) with Drei; lazy-load the 3D chunk and provide a fallback version"
url: https://r3f.docs.pmnd.rs
repo: "https://github.com/pmndrs/react-three-fiber"
license: "MIT"
pricing: free
risk: low
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-15"
---

# React Three Fiber

## چیست
✅ رندرکننده‌ی React برای Three.js. حدود ۳۳ هزار ستاره؛ نسخه‌ی 9.8.2 (۲۰۲۶-۱۰-۱۴).

## دستور سریع

**نصب** (✅ README رسمی و متادیتای npm؛ نسخه‌ی 9 فقط با React 19):
```bash
npm install --save-exact three@0.186.1 @react-three/fiber@9.8.2   # peer: react و react-dom >=19 <19.4
npm install --save-dev @types/three                                  # فقط با TypeScript
```
**حداقل اجرا** (✅ الگوی README، کوتاه‌شده):
```jsx
import { useRef } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
function Box() {
  const ref = useRef(null)
  useFrame((_, dt) => { ref.current.rotation.x += dt })
  return <mesh ref={ref}><boxGeometry /><meshStandardMaterial color="orange" /></mesh>
}
export default () => <Canvas dpr={[1, 2]}><ambientLight /><pointLight position={[10, 10, 10]} /><Box /></Canvas>
```
**تنظیم‌های مهم**
- ✅ `dpr` پیش‌فرض `[1, 2]` است؛ 🧭 روی موبایل و GPU ضعیف `[1, 1.5]` بگذار.
- ✅ `frameloop="demand"` فقط وقتی چیزی عوض شد رندر می‌کند (باتری و فن)؛ با `invalidate()` فریم می‌خواهی.
- ✅ در `useFrame` مقدار را روی `ref` تغییر بده، نه `setState` ([pitfalls رسمی](https://r3f.docs.pmnd.rs/advanced/pitfalls)).

**خطاهای رایج**
- ✅ پروژه‌ی React 18 باید R3F نسخه‌ی 8 بگیرد (README کتابخانه‌ی rapier هم همین را می‌گوید)؛ 9.x با 19 جور است.
- ✅ با `frameloop="demand"` کنترل‌هایی مثل OrbitControls که دوربین را مستقیم تغییر می‌دهند باید `invalidate` را به رویداد `change` وصل شوند، وگرنه تصویر کهنه می‌ماند.
- 🧭 Three.js حجم زیادی دارد: بخش سه‌بعدی را تنبل‌بار کن و نسخه‌ی جایگزین (عکس یا ویدیو) بگذار.

## کی استفاده کنیم
🧭 صحنه‌ی سه‌بعدی در سایت React یا Next.js. با [Drei](drei.md).

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
کم؛ Three.js حجم زیادی اضافه می‌کند: تنبل‌بار کن و نسخه‌ی جایگزین داشته باش.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)
