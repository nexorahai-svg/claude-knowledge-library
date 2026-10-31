---
name: Scenario MCP
slug: scenario-mcp
category: 3d
domains: [social-media, website]
verdict: assess
status: researched
summary: سرور MCP رسمی Scenario که از داخل Claude تصویر، ویدیو، صدا و مدل سه‌بعدی می‌سازد؛ مدل تازه‌ی Anthropic نیست؛ رایگان فقط برای ارزیابی، خروجی تجاری با پلن پولی از ۱۵ دلار
use_when: "a 3D object or product model (GLB/FBX) for a reel, ad or Three.js page, from one photo or text ; trying many media models from one connection inside Claude ; splitting or rigging a mesh inside Blender with the Scenario extension"
how: "claude mcp add --transport http scenario https://mcp.scenario.com/mcp then OAuth in the browser; the plan prices every run before spending; use a paid plan for client work because free outputs are personal and evaluation only; never send client data unless you accept the non-Enterprise data terms; read the export and OFAC clause first"
url: https://mcp.scenario.com/
repo: "https://github.com/scenario-labs/skills"
license: "سرویس پولی؛ اسکیل‌ها MIT"
pricing: freemium
risk: medium
sources: [S210]
found_in: [reel-farshad-shariatpoor-2026-10-30]
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Scenario MCP

## چیست
- ✅ سرور میزبانی‌شده‌ی [mcp.scenario.com](https://mcp.scenario.com/) با ۹۹ ابزار و بیش از ۷۵۰ مدل برای تصویر، ویدیو، سه‌بعدی و صدا (ادعای صفحه‌ی رسمی). با Claude Code، Claude Desktop، claude.ai، Cursor و VS Code کار می‌کند.
- ✅ سه‌بعدی از متن، یک عکس یا چند نما، با مدل‌های سازنده‌های دیگر مثل Meshy و Rodin. خروجی GLB و FBX، و ویرایش مش: remesh، retexture، UV، rig و انیمیشن ([اسکیل‌ها](https://github.com/scenario-labs/skills)، MIT، حدود ۱٬۲۰۰ ستاره).
- ✅ [افزونه‌ی Blender](scenario-blender.md) این کارها را داخل صحنه می‌آورد و مدل را با GLB، glTF، FBX، OBJ یا PLY تا ۲۵۶ مگابایت وارد می‌کند؛ مش را هم می‌تواند به قطعه‌ها تقسیم کند.

## ریسک و هشدار
- ⚠️ روی پلن‌های غیر Enterprise، طبق [شرایط](https://www.scenario.com/terms-of-service) داده به‌صورت بینش ناشناس برای بهبود سرویس و AI استفاده می‌شود. تضمین قراردادی عدم آموزش فقط با Enterprise است. عکس و داده‌ی محرمانه‌ی مشتری را نفرست.
- ⚠️ بند انطباق صادراتی شرایط، نیز EAR و OFAC است: کاربر نباید مقیم یا تابع کشور تحت تحریم باشد. ❓ پیش از کار مشتری موقعیت حقوقی را روشن کن ([LTX-2.5](ltx-2-5.md) هم بند مشابه دارد).
- ⚠️ MCP پولی است و اعتبار مصرف می‌کند؛ پیش از هر اجرا قیمت را ببین.

## کی استفاده کنیم
👀 آزموده نشده. مناسب شیء سه‌بعدی برای ریل و صفحه‌ی محصول. ❓ کیفیت مش، کیفیت رندر نهایی و برش‌پذیری واقعی روی نمونه‌ی ما سنجیده نشده است.

## قیمت و مجوز
✅ ([قیمت](https://www.scenario.com/pricing)، ۲۰۲۶-۱۰-۳۰) ۵۰ اعتبار رایگان روزانه بدون کارت. Starter ۱۵ دلار با ۱٬۵۰۰ اعتبار، Pro ۴۵ دلار با ۵٬۰۰۰ اعتبار، Max ۷۵ دلار با ۱۰٬۰۰۰ اعتبار در ماه. ✅ پلن پولی مجوز تجاری کامل دارد؛ خروجی پلن رایگان فقط برای استفاده‌ی شخصی و ارزیابی است. اعتبار استفاده‌نشده به ماه بعد نمی‌رود.

## ادعاهای ریل (۲۰۲۶-۱۰-۳۰)
ریل @farshad_shariatpoor ([S210](../sources/README.md#s210)) می‌گوید «Anthropic هوش مصنوعی Claude Opus 5.5 3D را معرفی کرد». ❌ در [فهرست رسمی مدل‌ها](https://platform.claude.com/docs/en/about-claude/models/overview) چنین مدلی نیست؛ Opus 5.5 است و Scenario MCP به آن وصل شده. لینک خود پست هم mcp.scenario.com است. ❌ «در کسری از ثانیه» نادرست است. ❓ ساخت هر قطعه به‌صورت جدا و خروجی `.blend` و dae در مستندات خوانده‌شده پیدا نشد؛ خروجی `.blend` با افزونه‌ی Blender و ذخیره‌ی صحنه منطقی است (🧭). «بی‌نقص» هم ادعای بی‌پشتوانه است.

## مرتبط
[Scenario برای Blender](scenario-blender.md) · [Blender](blender.md) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md)
