---
name: MCP for Blender
slug: mcp-for-blender
category: 3d
domains: [social-media, website]
verdict: trial
status: researched
summary: اتصال شخص ثالث Claude به Blender (نام قبلی blender-mcp) که صحنه را با پایتون می‌سازد؛ سه‌بعدی از روی عکس را به سرویس‌های دیگر می‌سپارد؛ کد دلخواه اجرا می‌کند
use_when: "building or editing a Blender scene by prompt ; a rough room or product scene from a floor plan and measurements ; placing Poly Haven or Sketchfab assets in a scene"
how: "Do not install without the user's yes; pypi mcp-for-blender plus the Blender add-on, then Start MCP Server; save the scene first because execute_blender_code runs arbitrary Python; turn Poly Haven off if not needed; basic anonymous usage record is on by default"
url: https://github.com/ahujasid/mcp-for-blender
repo: "https://github.com/ahujasid/mcp-for-blender"
license: "MIT"
pricing: freemium
risk: medium
sources: [S213]
found_in: [video-property-tour-2026-10-31]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# MCP for Blender

## چیست
- ✅ مخزن [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender): مجوز MIT، حدود ۳۲٫۸ هزار ستاره، ساخت ۲۰۲۵-۰۳-۰۷، آخرین push در ۲۰۲۶-۱۰-۲۹. نام قبلی `blender-mcp` بود. README می‌گوید شخص ثالث است و ساخت Blender نیست.
- ✅ ابزار `execute_blender_code` پایتون را در Blender باز اجرا می‌کند و ابزار `look` نتیجه را از دید دوربین می‌بیند.
- ✅ دارایی از Poly Haven، Sketchfab و Poly Pizza. مدل سه‌بعدی ساخته‌شده با AI از Meshy، Tripo، Hyper3D Rodin و Hunyuan3D می‌آید و بسته‌ی Premium هم دارد ❓ قیمت خوانده نشد.

## دستور سریع

**نصب** (✅ [README](https://github.com/ahujasid/mcp-for-blender)؛ طبق قاعده‌ی کتابخانه بدون اجازه‌ی کاربر نصب نکن؛ Blender نسخه‌ی ۳٫۰ به بالا، `uv` با نصب‌کننده‌ی رسمی، نه `pip install uv`):
```bash
claude mcp add blender -e DISABLE_TELEMETRY=true -e BLENDER_MCP_SAFE_MODE=1 -- uvx mcp-for-blender@2.2.6
uvx mcp-for-blender@2.2.6 install-addon     # بعد در Blender: Edit → Preferences → Add-ons → «MCP for Blender»
```
**حداقل اجرا:** صحنه را ذخیره کن؛ در Blender کلید `N` → تب «MCP for Blender» → «Start MCP Server»؛ در Claude بخواه: «یک مکعب قرمز بساز و با `look` نشانم بده» (✅ ابزارهای `execute_blender_code` و `look`).

**تنظیم‌های مهم**
- ✅ `BLENDER_MCP_SAFE_MODE=1` هر اسکریپت را پیش از اجرا بررسی می‌کند و نوشتن/خواندن فایل، اجرای برنامه و شبکه را می‌بندد؛ مدل‌سازی، متریال، رندر و ذخیره کار می‌کند.
- ✅ `DISABLE_TELEMETRY=true` رکورد ناشناس استفاده (شناسه‌ی نصب، نام ابزار، نسخه، سیستم‌عامل) را هم خاموش می‌کند.
- ✅ اگر uv پایتون ناسازگار برداشت: `uvx --python 3.11 mcp-for-blender` با `UV_PYTHON_PREFERENCE=only-managed`. پورت پیش‌فرض `9876` (`--port` برای نمونه‌ی دوم).

**خطاهای رایج**
- ✅ کلاینت‌های گرافیکی `PATH` ترمینال را نمی‌بینند و `spawn uvx ENOENT` می‌دهند → مسیر کامل `which uvx` را بنویس.
- ✅ سوکت افزونه احراز هویت و رمزنگاری ندارد: هر که به پورت برسد در Blender پایتون اجرا می‌کند؛ فقط `localhost`.
- ⚠️ `execute_blender_code` کد دلخواه اجرا می‌کند؛ صحنه‌ی ناشناس باز نکن و Poly Haven را اگر لازم نیست خاموش کن. هنوز در پروژه‌ی واقعی آزموده نشده (👀).

## کی استفاده کنیم
👀 آزموده نشده. برای ساختن صحنه از روی نقشه و اندازه مناسب است. ❓ ساخت یک ملک کامل و دقیق از چند عکس را README ادعا نمی‌کند و ما هم آن را نسنجیدیم.

## قیمت و مجوز
✅ کد MIT. سرویس‌های تولید مدل و Premium هزینه‌ی جدا دارند.

## ریسک و هشدار
- ⚠️ README هشدار می‌دهد `execute_blender_code` کد دلخواه اجرا می‌کند؛ پیش از آن صحنه را ذخیره کن و صحنه‌ی ناشناس باز نکن.
- ✅ تله‌متری: محتوا (پرامپت، کد، تصویر، صحنه) فقط با رضایت. ولی یک رکورد ناشناس استفاده پیش‌فرض می‌رود: شناسه‌ی نصب، نام ابزار، نسخه و سیستم‌عامل.
- ⚠️ عکس ملک مشتری اگر به سرویس تولید مدل برود، از رایانه خارج می‌شود.

## ادعای ویدیو (۲۰۲۶-۱۰-۳۱)
ویدیوی فارسی «تور سه‌بعدی ملک با Claude فقط با چند عکس» ([S213](../sources/README.md#s213)). ✅ ساخت صحنه در Blender با Claude و صفحه‌ی `furniture-planner.html` شدنی است. ❓ «فقط چند عکس» ثابت نشد. 🧭 بخش بازی‌مانند با برچسب پرتغالی `E_ Apagar Plafon da sala` و کلید `[E] Open the door` ساخت یک موتور بازی است و خروجی خود Blender نیست؛ سازنده‌اش پیدا نشد.

## مرتبط
[Blender](blender.md) · [Three.js](threejs.md) · [Scenario MCP](scenario-mcp.md)

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 👀 به 🧪) امیدوارکننده و مناسب آزمون کوچک. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
