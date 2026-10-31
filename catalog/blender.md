---
name: Blender
slug: blender
category: 3d
domains: [website, social-media]
verdict: adopt
status: researched
summary: نرم‌افزار سه‌بعدی رایگان و کاملاً اسکریپت‌پذیر با پایتون؛ مدل پارامتری و رندر برای وب، شبکه‌های اجتماعی و بازسازی معماری
use_when: "generating parametric 3D models or renders for web, social or architecture visuals ; scripting 3D scenes with Python"
how: "Install the LTS tarball in ~/.local/opt without sudo and symlink to ~/.local/bin/blender; run headless `blender -b -P script.py`; on RTX 4060 use CUDA not OptiX; EEVEE for animation, Cycles for stills; bake scale into the mesh"
url: https://www.blender.org/
repo: ""
license: "GPL-3.0-or-later"
pricing: free
risk: low
sources: [S142]
found_in: []
last_checked: 2026-10-31
next_check: "2027-01-21"
---

# Blender

## چیست
✅ نرم‌افزار سه‌بعدی رایگان. نسخه‌ی LTS فعلی **5.2.2** (پوشه‌ی رسمی دانلود، با فایل sha256؛ نسخه‌ی 5.2.3 در ۲۰۲۶-۱۰-۲۲ آمده بود ولی هنوز sha256 نداشت). `blender --version` خروجی «Blender 5.2.2 LTS».

🔬 نصب در سطح کاربر بدون sudo: بسته را در `~/.local/opt/blender-5.2.2-linux-x64` باز کن و پیوند نمادین در `~/.local/bin/blender` بگذار.

## دستور سریع

**نصب** (✅ [پوشه‌ی رسمی](https://download.blender.org/release/Blender5.2/): LTS فعلی `5.2.3` حالا فایل sha256 دارد؛ اندازه‌گیری‌های این کارت روی `5.2.2` بود):
```bash
mkdir -p ~/.local/opt ~/.local/bin && cd ~/.local/opt
curl -LO https://download.blender.org/release/Blender5.2/blender-5.2.3-linux-x64.tar.xz
curl -s https://download.blender.org/release/Blender5.2/blender-5.2.3.sha256 | grep linux-x64 | sha256sum -c
tar xf blender-5.2.3-linux-x64.tar.xz && ln -sf ~/.local/opt/blender-5.2.3-linux-x64/blender ~/.local/bin/blender
```
**حداقل اجرا** (✅ [راهنمای رندر خط فرمان](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html)): اسکریپت صحنه را می‌سازد و یک فریم رندر می‌شود.
```bash
blender -b --factory-startup --python-exit-code 1 -P scene.py -E CYCLES -o ./renders/f_##### -F PNG -f 1 -- --cycles-device CUDA
```
**تنظیم‌های مهم**
- ✅ `--cycles-device` یکی از `CPU CUDA OPTIX HIP ONEAPI METAL` است. 🔬 روی RTX 4060 `CUDA` بگذار (OptiX خطای ۷۸۰۴ داد).
- 🔬 موتور: EEVEE حدود ۱ ثانیه برای هر فریم، Cycles حدود ۲۰ ثانیه (۱۹۲۰×۱۰۸۰، ۶۴ نمونه) → انیمیشن با EEVEE، عکس ثابت با Cycles.
- ✅ `-t 4` تعداد رشته‌ها را محدود می‌کند (عدد ۴ پیشنهاد ماست 🧭)؛ رندر چندفریمی را با محافظ منابع کتابخانه (`scripts/resource_guard.py run --mem 8G --`) اجرا کن.

**خطاهای رایج**
- ✅ آرگومان‌ها به ترتیب اجرا می‌شوند: `-f` و `-a` باید **آخرین** گزینه‌ها باشند، وگرنه خروجی و قالب بعد از رندر ست می‌شود.
- 🔬 مقیاس را در خود مش بپز و نام ورودی‌های Principled را نو بنویس؛ جزئیات و دام glTF در «ریسک و هشدار» همین کارت.
- ✅ `--python-exit-code 1` را بگذار تا خطای اسکریپت در خط فرمان کد خروج غیرصفر بدهد، نه رندر خالی.

## کی استفاده کنیم
🔬 جایگزین رایگان 3ds Max برای نمایش معماری (پارگولا، کارپورت): کل مدل با یک اسکریپت پایتون ساخته می‌شود (`blender -b -P script.py`)، پس ابعاد پارامتری‌اند. همچنین لوگوی سه‌بعدی ([نمونه‌ی برند](scenario-blender.md)) و خروجی glTF برای [Three.js](threejs.md). روش جاسازی طرح در عکس مشتری: [تطبیق عکس](../domains/website/03-motion-3d/3d-webgl.md).

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
[سه‌بعدی و WebGL](../domains/website/03-motion-3d/3d-webgl.md) · [Scenario برای Blender](scenario-blender.md) · [S142](../sources/README.md#s142)
