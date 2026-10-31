---
name: mirroir-mcp
slug: mirroir-mcp
category: app-testing
domains: [apps, security]
verdict: assess
status: researched
summary: سرور MCP که آیفون واقعی را از راه iPhone Mirroring در macOS 15+ کنترل می‌کند؛ پیش‌فرض فقط ابزارهای خواندنی، ۳۸ ابزار در کل؛ Apache-2.0
use_when: "running an agent test on a real iPhone when no device farm or simulator is enough ; checking a flow that only works on a physical device"
how: "Do not install without the user's yes and never on a personal phone; claude mcp add --transport stdio mirroir -- npx -y mirroir-mcp; keep the default read-only tools and set blockedApps in permissions.json"
url: https://github.com/jfarcand/mirroir-mcp
repo: "https://github.com/jfarcand/mirroir-mcp"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# mirroir-mcp

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی واقعی v0.42.0 (۲۰۲۶-۱۰-۳۰): بازپخش کامپایل‌شده هر گام را می‌سنجد و `record_step` ضربه‌ی بی‌اثر روی آیکن را رد می‌کند؛ Apache-2.0 بی‌تغییر. 🧭 مخزن دو جریان برچسب دارد (`runner-v…` و `v…`)؛ فقط `v…` معیار است: https://github.com/jfarcand/mirroir-mcp/releases/tag/v0.42.0
✅ MCP برای دیدن و لمس آیفون واقعی از راه iPhone Mirroring ([README](https://github.com/jfarcand/mirroir-mcp)). نیاز: macOS 15 به بالا و آیفون وصل‌شده به Mirroring؛ مجوزهای Screen Recording و Accessibility.
- ✅ ۳۸ ابزار ([ابزارها](https://github.com/jfarcand/mirroir-mcp/blob/main/docs/tools.md)). بدون فایل پیکربندی فقط ابزارهای خواندنی دیده می‌شوند (screenshot، describe_screen، ضبط و غیره)؛ ابزارهای تغییردهنده (tap، type_text، launch_app و ...) پنهان‌اند تا در `~/.mirroir-mcp/permissions.json` مجاز شوند ([مجوزها](https://github.com/jfarcand/mirroir-mcp/blob/main/docs/permissions.md)). `blockedApps` اجرای اپ‌هایی مثل Wallet را رد می‌کند.
- ✅ تشخیص متن پیش‌فرض محلی است (Apple Vision OCR). حالت «AI vision» اختیاری است و فریم صفحه را از راه ابزارهای وارد‌شده (Copilot یا Claude Code) به مدل می‌فرستد؛ README هر فریم را حدود ۲۴ هزار توکن می‌گوید.
- ✅ نسخه v0.41.0 (۲۰۲۶-۱۰-۲۷) در https://github.com/jfarcand/mirroir-mcp/releases؛ حدود ۲۷۰ ستاره؛ فعال؛ آرشیو نشده؛ ۴ مشارکت‌کننده، یعنی عملاً نگهدارنده‌ی تک‌نفره. نصب: curl-bash، npx یا Homebrew.

## قیمت و مجوز
✅ Apache-2.0 (https://github.com/jfarcand/mirroir-mcp/blob/main/LICENSE)، رایگان، استفاده‌ی تجاری آزاد. مک لازم است.

## ریسک و هشدار
- ✅ کل صفحه‌ی گوشی واقعی را می‌بیند؛ در حالت vision تصویر صفحه به سرویس مدل می‌رود. پیام و اپ بانکی هم دیده می‌شود.
- 🧭 فقط گوشی آزمایشی با حساب‌های ساختگی، هرگز گوشی شخصی. نصب با `curl | bash` را بدون خواندن اسکریپت اجرا نکن.
- 🧭 نیاز به مک؛ ما اکنون ماشین لینوکس داریم، پس فعلاً قابل استفاده نیست.

## کی استفاده کنیم
🧭 فقط وقتی آزمون روی آیفون واقعی لازم شد و شبیه‌ساز کافی نبود. [ios-simulator-mcp](ios-simulator-mcp.md) در کتابخانه ⛔ است؛ جایگزین‌های کم‌ریسک‌تر [agent-device](agent-device.md) و [Maestro](maestro.md) هستند. ارتقا پیشنهاد نمی‌شود.

## مرتبط
[S191](../sources/README.md#s191) · [آزمون اپ](../domains/apps/app-testing.md) · [امنیت MCP](../domains/claude-code/mcp-safety.md)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ `get-mirroir.sh`، `mirroir.sh` و `npm/install.js` خوانده شد (SHA `317dc15`). کارشان فقط clone یا pull، `swift build`، symlink و پیکربندی است. sudo ندارند. باینری npm با SHA256SUMS همان release سنجیده می‌شود (چکسام و باینری از یک منبع‌اند). تله‌متری دیده نشد.
- ⚠️ دستور `curl … | bash` از دامنه‌ی mirroir.dev می‌آید، نه GitHub. پس اسکریپت را از خود مخزن بخوان و اجرا کن. ❓ بیشتر کد Swift خوانده نشد.
