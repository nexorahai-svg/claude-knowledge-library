---
name: Chrome DevTools MCP
slug: chrome-devtools-mcp
category: browser-testing
domains: [website, claude-code]
verdict: adopt
status: researched
summary: Claude را به Chrome وصل می‌کند: تست سرعت، Lighthouse، شبکه، کنسول، اسکرین‌شات
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
repo: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S21]
found_in: [batch-01/P00]
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Chrome DevTools MCP

## چیست
✅ سرور MCP رسمی سازمان ChromeDevTools در گیت‌هاب (Apache-2.0، حدود ۵۴ هزار ستاره، نسخه‌ی 1.11.0 در ۲۰۲۶-۱۰-۱۵). به Claude یک Chrome واقعی می‌دهد. گروه‌های ابزار: کلیک و پر کردن فرم، ناوبری، شبیه‌سازی دستگاه و اندازه‌ی صفحه، **ثبت و تحلیل عملکرد (performance trace)**، درخواست‌های شبکه، کنسول با stack trace، اسکرین‌شات، **ممیزی Lighthouse** (دسترسی‌پذیری، سئو، بهترین روش‌ها؛ عملکرد از طریق trace)، حافظه، و غیره. حالت `--slim` فقط ۳ ابزار دارد.

## کی استفاده کنیم
🧭 **بهترین ابزار برای تست سایت قبل از انتشار**: سرعت و Core Web Vitals، خطاهای کنسول، درخواست‌های شکسته، چیدمان در اندازه‌های مختلف. برای خودکارسازی جریان فرم در چند مرورگر، [Playwright MCP](playwright-mcp.md) مناسب‌تر است.

## نصب
✅ دستور رسمی برای Claude Code:
```bash
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```
نیازمندی: Node.js نسخه‌ی LTS و Chrome پایدار. فقط Chrome و Chrome for Testing رسماً پشتیبانی می‌شوند.

## قیمت و مجوز
✅ رایگان، Apache-2.0.

## ریسک و هشدار
✅ از README:
- «محتوای مرورگر را در اختیار MCP می‌گذارد و اجازه می‌دهد هر داده‌ای در مرورگر را بررسی و تغییر دهد.» اطلاعات شخصی یا حساس را در آن مرورگر باز نکن.
- **آمار استفاده به‌طور پیش‌فرض برای Google ارسال می‌شود.** خاموش کردن: `--no-usage-statistics`.
- ابزارهای عملکرد ممکن است آدرس صفحه را به API گوگل (CrUX) بفرستند. خاموش کردن: `--no-performance-crux`.
- 🧭 همیشه با `--isolated` اجرا کن (پروفایل موقت که بعد پاک می‌شود)، نه با پروفایل شخصی.

پیکربندی پیشنهادی ما:
```bash
claude mcp add chrome-devtools --scope user -- npx chrome-devtools-mcp@latest --isolated --no-usage-statistics --no-performance-crux
```
✅ این ترکیب پرچم‌ها نوشته‌ی ماست (پرچم‌ها هر کدام در مستندات رسمی هستند). روی Linux (Debian 13، Node 24، Chrome پایدار) در سطح کاربر نصب شد و `claude mcp list` آن را «Connected» نشان داد (۲۰۲۶-۱۰-۲۱).

## مرتبط
[چک‌لیست قبل از انتشار](../domains/website/07-quality/launch-checklist.md) · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S21](../sources/README.md#s21)
