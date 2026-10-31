---
name: React Postprocessing
slug: react-postprocessing
category: 3d
domains: [website]
verdict: adopt
status: researched
summary: افکت‌های پس‌پردازش (bloom، عمق میدان، نویز) برای R3F
use_when: "adding cinematic effects (bloom, depth of field) to a React Three Fiber scene"
how: "npm install @react-three/postprocessing (3.2.2, MIT) next to @react-three/fiber and wrap effects in EffectComposer; each effect costs GPU so test on mobile"
url: https://github.com/pmndrs/react-postprocessing
repo: "https://github.com/pmndrs/react-postprocessing"
license: "MIT"
pricing: free
risk: low
sources: [S28]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-25"
---

# React Postprocessing

## چیست
✅ نسخه‌ی 3.2.2 در npm (۲۰۲۶-۱۰-۲۱)؛ MIT.
✅ نصب و اجرا (https://github.com/pmndrs/react-postprocessing، ۲۰۲۶-۱۰-۲۷): npm install @react-three/postprocessing

## دستور سریع

**نصب** (✅ README و متادیتای npm؛ peer: `postprocessing ^6.36.0`، `@react-three/fiber >=9.7.0`):
```bash
npm install --save-exact three@0.186.1 @react-three/fiber@9.8.2 @react-three/postprocessing@3.2.2
```
**حداقل اجرا** (✅ الگوی README):
```jsx
import { Canvas } from '@react-three/fiber'
import { EffectComposer, Bloom, Vignette } from '@react-three/postprocessing'
export default () => (
  <Canvas>
    {/* صحنه */}
    <EffectComposer>
      <Bloom luminanceThreshold={1} mipmapBlur />
      <Vignette offset={0.1} darkness={1.1} />
    </EffectComposer>
  </Canvas>
)
```
**تنظیم‌های مهم**
- ✅ `EffectComposer multisampling` پیش‌فرض `4` است و `0` آن را خاموش می‌کند (مثلاً با SMAA یا FXAA)؛ روی GPU ضعیف اول همین را کم کن.
- ✅ `Bloom luminanceThreshold={1}` یعنی فقط ماده‌های روشن‌تر از ۱ می‌درخشند؛ `mipmapBlur` نرم‌تر است. `resolutionX/Y` را پایین بیاور تا ارزان‌تر شود.
- ✅ افکت‌های پشت‌سرهم در یک پاس ادغام می‌شوند (`mergeMode: 'auto'`)، ولی در هر پاس فقط یک افکت convolution مثل DepthOfField می‌ماند.

**خطاهای رایج**
- ✅ `postprocessing@6.39.5` (وابسته‌ی peer) `three <0.187.0` می‌خواهد → با `three@0.187.0` نصب ERESOLVE می‌دهد؛ روی r186 بمان.
- ✅ Bloom روی ماده‌ای که `toneMapped` روشن دارد نمی‌درخشد؛ برای درخشش `toneMapped={false}` و `emissiveIntensity` بالای ۱ بگذار.
- 🧭 هر افکت هزینه‌ی GPU دارد؛ روی یک موبایل واقعی تست کن و تعداد افکت‌ها را کم نگه دار.

## کی استفاده کنیم
🧭 ظاهر سینمایی صحنه‌ی سه‌بعدی؛ روی موبایل تست کن.

## قیمت و مجوز
✅ MIT، رایگان.

## ریسک و هشدار
هر افکت هزینه‌ی GPU دارد.

## مرتبط
[کتابخانه‌های کامپوننت و انیمیشن](../domains/website/04-tech/component-libraries.md) · [S28](../sources/README.md#s28)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) رسمی، کم‌ریسک و جزو پشته‌ی ما. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
