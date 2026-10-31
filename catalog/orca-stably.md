---
name: Orca (Stably)
slug: orca-stably
category: claude-code-tooling
domains: [claude-code, security]
verdict: assess
status: researched
summary: اپ دسکتاپ و موبایل MIT برای اجرای موازی چند عامل کدنویسی هرکدام در worktree جدا؛ تله‌متری پیش‌فرض روشن، Computer Use و relay موبایل؛ انتشار تقریباً روزانه
use_when: "running several coding agents (Claude Code, Codex, OpenCode) side by side in isolated git worktrees with one dashboard ; monitoring agents from a phone"
how: "Do not install without the user's yes; set DO_NOT_TRACK=1 before first launch, skip the mobile pairing and Computer Use, and respect the resource rule (one heavy agent job at a time)"
url: https://github.com/stablyai/orca
repo: "https://github.com/stablyai/orca"
license: "MIT"
pricing: free
risk: high
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Orca (Stably)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v1.4.245 (۲۰۲۶-۱۰-۳۰؛ MIT): کنترل پس‌زمینه‌ی اپ‌های مک هنگام کار عامل‌ها، حالت Chat، افزونه و پوسته، دیکته از گوشی: https://github.com/stablyai/orca/releases/tag/v1.4.245 . هشدار «Computer Use را نصب نکن» همچنان برقرار است.
- ✅ مخزن MIT (حق نشر Lovecast Inc.)، حدود ۱۰۸٬۸۷۰ ستاره (API و سایت مستندات تأیید کردند؛ شمار پیشتر مشکوک بود)، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۸. آخرین release: `v1.4.243` در ۲۰۲۶-۱۰-۲۸ (تقریباً روزانه): https://github.com/stablyai/orca
- ✅ README: «ارکستراتور AI»؛ Codex، Claude Code، OpenCode، Pi و عامل‌های دیگر را کنار هم اجرا می‌کند، هرکدام در worktree جدا؛ مرورگر داخلی و Design Mode؛ نمای diff؛ SSH؛ اتصال GitHub، Linear و Jira؛ همراه موبایل (iOS App Store و APK اندروید) و Computer Use که عامل‌ها را با رابط دسکتاپ کار می‌دهد.
- ✅ نصب: دانلود از https://onorca.dev/download ، یا `brew install --cask stablyai/orca/orca`، یا AppImage لینوکس. با اشتراک خودت از عامل‌ها کار می‌کند (README).
- ✅ relay که موبایل را با دسکتاپ جفت می‌کند در پوشه‌ی `cloud/` مخزن هم هست.
- 🧭 Claude Code خودش worktree و تیم عامل دارد؛ ارزش افزوده‌ی Orca بیشتر رابط تصویری و موبایل است.

## کی استفاده کنیم
- 🧭 اگر واقعاً چند عامل موازی با نمای یکجا لازم شد. دستگاه ما محدود است ([کار موازی](../domains/claude-code/parallel-agents.md)، قانون منابع): هر بار یک کار سنگین. فعلاً نیازی نیست.

## قیمت و مجوز
- ✅ رایگان، MIT: https://github.com/stablyai/orca/blob/main/LICENSE . هزینه‌ی مدل‌ها جدا و از اشتراک خود عامل‌ها است.

## ریسک و هشدار
- ✅ تله‌متری ناشناس در نسخه‌های بسته‌بندی‌شده روشن است (شناسه‌ی تصادفی محلی، رویدادهای چرخه‌ی عمر، افزودن مخزن، شروع عامل و...). سند رسمی می‌گوید محتوای فایل، prompt، خروجی عامل، نام مخزن/شاخه، URL و مسیر ارسال نمی‌شود. خاموش‌کردن: `DO_NOT_TRACK=1` یا `ORCA_TELEMETRY_DISABLED=1`: https://www.onorca.dev/docs/telemetry
- ✅ Computer Use (کنترل برنامه‌های دسکتاپ) و relay موبایل دسترسی گسترده می‌دهند؛ فقط در صورت نیاز، و هرگز روی حساب اصلی با کلیدهای حساس.
- ✅ شرکت و برنامه‌ی پرتحول (۲۴۰+ نسخه‌ی ۱٫۴)؛ نسخه را پین کن و بروزرسانی خودکار را کنترل کن.
- 🧭 چند عامل هم‌زمان حافظه و CPU زیادی می‌برد ⚠️ قانون منابع.

## مرتبط
[S191](../sources/README.md#s191) · [کار موازی](../domains/claude-code/parallel-agents.md)

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ تله‌متری PostHog (`us.i.posthog.com`) در کد هست (SHA `e5b45ac`). با `DO_NOT_TRACK=1` یا `ORCA_TELEMETRY_DISABLED=1` خاموش می‌شود. ⚠️ **بستن بنر رضایت، بی‌صدا یعنی «موافقم»** (کامنت خود کد در `src/main/telemetry/client.ts`: «Banner dismissal persists silent opt-in»). پس تله‌متری را در تنظیمات یا با متغیر محیطی خاموش کن.
- ✅ برنامه hookهای مدیریت‌شده و statusLine را در `settings.json` خود Claude Code می‌نویسد. اسکریپت‌هایش را در `~/.orca/agent-hooks` می‌گذارد و روی میزبان SSH ریموت هم با SFTP نصب می‌کند. ❓ ماژول relay و محتوای payload تله‌متری خوانده نشد.
