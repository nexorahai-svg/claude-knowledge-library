---
name: T3 Code
slug: t3code
category: claude-code-tooling
domains: [claude-code]
verdict: hold
status: researched
summary: اپ وب و دسکتاپ و موبایل متن‌باز (MIT) از Ping/T3 برای کنترل عامل‌های کدنویسی روی رایانه‌ی خودت: Claude Code، Codex، Cursor، OpenCode و…
use_when: "comparing agent control surfaces with Orca, cc-switch and Claude Desktop ; watching or steering agents on the dev machine from a phone"
how: "Do not install without the user's yes: README offers curl install.sh | sh (avoid) and a desktop release; prefer npx t3@latest once on a throwaway profile after reading the code, pin versions, never expose the server beyond localhost"
url: https://github.com/pingdotgg/t3code
repo: "https://github.com/pingdotgg/t3code"
license: "MIT"
pricing: free
risk: medium
sources: [S216]
found_in: [watch-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# T3 Code

## چیست
✅ (GitHub API و README، ۲۰۲۶-۱۰-۳۱) سازمان pingdotgg؛ ساخته ۲۰۲۶-۰۲-۰۸، push امروز، حدود ۳۳٬۴۰۰ ستاره، MIT، آخرین release نسخه‌ی v0.1.6 (۲۰۲۶-۱۰-۳۱) یعنی هنوز 0.x. README: «سطح کنترل برای harness عامل»؛ با اشتراک‌های Claude Code، Codex، Cursor، Grok Build، OpenCode و Antigravity که روی همان رایانه راه‌اندازی شده‌اند کار می‌کند، اپ موبایل (iOS و Android) برای کنترل از راه دور دارد و می‌گوید چیزی نمی‌فروشد. ❓ ستاره‌ی زیاد معیار کیفیت نیست؛ کد و پیام‌های شبکه خوانده نشد.

## کی استفاده کنیم
🧭 اگر بخواهیم چند عامل را از یک پنل یا گوشی کنترل کنیم؛ با [Orca](orca-stably.md) و [cc-switch](cc-switch.md) مقایسه شود. هنوز در هیچ پروژه‌ای آزموده نشده. قانون منابع: یک کار سنگین در هر زمان.

## قیمت و مجوز
✅ MIT و رایگان؛ هزینه‌ی مدل‌ها همان اشتراک خودت است. ❓ سرویس ابری یا relay پولی بررسی نشد.

## ریسک و هشدار
⚠️ به عامل‌هایی که به فایل و فرمان دسترسی دارند وصل می‌شود و سرور محلی/ریموت باز می‌کند؛ نصب پیشنهادی `curl | sh` است (ممنوع بی‌خواندن). نحوه‌ی احراز هویت موبایل و relay و تله‌متری آن را بخوان ❓. اینکه کنترل اشتراک Claude از ابزار سوم با شرایط Anthropic می‌خواند را بررسی نکرده‌ایم ❓.

## مرتبط
[S216](../sources/README.md#s216)

🧭 (۲۰۲۶-۱۰-۳۱: 👀 به ⛔) تصمیم مالک: ابزاری که کدش خوانده نشده استفاده نمی‌شود.
