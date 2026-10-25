---
name: Blender
slug: blender
category: 3d
domains: [website, social-media]
verdict: adopt
status: researched
summary: نرم‌افزار سه‌بعدی رایگان و کاملاً اسکریپت‌پذیر با پایتون؛ مدل پارامتری و رندر برای وب، شبکه‌های اجتماعی و بازسازی معماری
url: https://www.blender.org/
repo: ""
license: "GPL-3.0-or-later"
pricing: free
risk: low
sources: [S142]
found_in: []
last_checked: 2026-10-23
next_check: "2027-01-21"
---

# Blender

## چیست
✅ نرم‌افزار سه‌بعدی رایگان. نسخه‌ی LTS فعلی **5.2.2** (پوشه‌ی رسمی دانلود، با فایل sha256؛ نسخه‌ی 5.2.3 در ۲۰۲۶-۱۰-۲۲ آمده بود ولی هنوز sha256 نداشت). `blender --version` خروجی «Blender 5.2.2 LTS».

🔬 نصب در سطح کاربر بدون sudo: بسته را در `~/.local/opt/blender-5.2.2-linux-x64` باز کن و پیوند نمادین در `~/.local/bin/blender` بگذار.

## کی استفاده کنیم
🔬 جایگزین رایگان 3ds Max برای نمایش معماری (پارگولا، کارپورت): کل مدل با یک اسکریپت پایتون ساخته می‌شود (`blender -b -P script.py`)، پس ابعاد پارامتری‌اند. همچنین لوگوی سه‌بعدی ([پروژه‌ی Nexorah](scenario-blender.md)) و خروجی glTF برای [Three.js](threejs.md). روش جاسازی طرح در عکس مشتری: [تطبیق عکس](../domains/website/03-motion-3d/3d-webgl.md).

## قیمت و مجوز
✅ رایگان، GPL-3.0-or-later.

## ریسک و هشدار
کم. اندازه‌گیری روی RTX 4060 با درایور 550.163.01 و Ryzen 9 7900X (🔬 یک پروژه):
- **OptiX شروع نمی‌شود** («OptiX initialization failed with error code 7804») → CUDA بگذار.
- Cycles، ۱۹۲۰×۱۰۸۰ و ۶۴ نمونه: حدود ۲۰ ثانیه برای هر فریم. EEVEE (ردیابی پرتو روشن، ۶۴ نمونه TAA): حدود ۱ ثانیه برای هر فریم پس از کامپایل شیدر → برای انیمیشن EEVEE، برای عکس ثابت Cycles.
- در Blender 5.x جسم مقیاس‌شده مختصات «Object» رویه‌ای را در فضای محلی بدون مقیاس نگه می‌دارد؛ کاشی و تخته غول‌آسا دیده می‌شوند مگر مقیاس در خود مش پخته شود.
- نام ورودی‌های Principled BSDF: «Emission Color» و «Specular IOR Level». گره‌ی آسمان `MULTIPLE_SCATTERING` (جایگزین `NISHITA`). شناسه‌ی موتور: `BLENDER_EEVEE`.
- خروجی glTF بافت‌های رویه‌ای را از دست می‌دهد؛ در Three.js با نام متریال دوباره بساز.
- Shadow catcher سیکلز با `film_transparent` برای ترکیب با عکس ناپایدار بود؛ روش نسبت و پاس‌ها کار کرد.

## مرتبط
[سه‌بعدی و WebGL](../domains/website/03-motion-3d/3d-webgl.md) · دفتر پروژه‌ها · [Scenario برای Blender](scenario-blender.md) · [S142](../sources/README.md#s142)
