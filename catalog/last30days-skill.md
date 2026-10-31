---
name: last30days-skill
slug: last30days-skill
category: research-tools
domains: [social-media, claude-code, security]
verdict: assess
status: researched
summary: مهارت پژوهش چندمنبعی (Reddit، X، YouTube، HN، تیک‌تاک، ریلز) با ورودی کوکی مرورگر که فقط با رضایت صریح فعال می‌شود
use_when: "need a fresh multi-source brief on what people said about a topic, trend or competitor in the last 30 days ; Reddit, Hacker News, Polymarket and GitHub research without any key"
how: "Do not install without the user's yes; /plugin marketplace add mvanhorn/last30days-skill then /plugin install last30days; answer NO to the browser-cookie question and never use the main X login; run the --preflight command first"
url: https://github.com/mvanhorn/last30days-skill
repo: "https://github.com/mvanhorn/last30days-skill"
license: "MIT"
pricing: free
risk: high
sources: [S165]
found_in: [inbox/2026-10-25-instagram-skills]
last_checked: 2026-10-29
next_check: "2027-01-27"
---

# last30days-skill

## چیست
- ✅ مخزن https://github.com/mvanhorn/last30days-skill؛ مجوز MIT؛ نسخه‌ی v3.31.0 (۲۰۲۶-۱۰-۲۷)؛ آخرین push ۲۰۲۶-۱۰-۲۸؛ حدود ۶۵٬۷۰۰ ستاره؛ بایگانی نشده (API گیت‌هاب).
- ✅ README: یک موتور پژوهش که Reddit، HN، Polymarket و GitHub را بدون تنظیم می‌خواند و با کلید یا ورود، X و YouTube و تیک‌تاک و ریلز اینستاگرام را هم اضافه می‌کند؛ نتیجه را امتیازدهی و خلاصه می‌کند.
- ✅ اینستاگرام، تیک‌تاک، Threads و LinkedIn از راه کلید ScrapeCreators می‌آیند (README: ۱۰٬۰۰۰ تماس رایگان، بعد پرداخت به‌ازای مصرف). مخصوص اینستاگرام نیست.
- ✅ داده به‌طور پیش‌فرض روی دستگاه می‌ماند؛ فقط به APIهایی می‌رود که صدا می‌زنی. اگر کلید مدل (OpenAI، xAI، Gemini...) بدهی، موضوع و متن‌ها برای رتبه‌بندی به آن می‌رود؛ وگرنه مدل محلی.
- 🧭 ستاره‌ها بسیار زیادند و بخشی تبلیغ است؛ ارزش واقعی را باید با یک آزمایش کوچک سنجید.

## ریسک و هشدار
- ✅ کد خواندن کوکی دارد (`chrome_cookies.py`، `safari_cookies.py`، `cookie_extract.py`). SKILL.md می‌گوید فقط با رضایت صریح (`FROM_BROWSER` یا `--allow-browser-cookies`) فعال می‌شود و پیش از خواندن باید پرسید؛ بی‌پاسخی یعنی نه.
- ✅ برای X می‌توان توکن رسمی API داد؛ مسیر کوکی «رایگان» است ولی نشست واردشده را به ابزار می‌دهد.
- 🧭 خواندن X و اینستاگرام با نشست کاربر ممکن است شرایط پلتفرم را نقض کند و حساب را محدود کند؛ هرگز با حساب اصلی.
- ✅ منابع اختیاری دیگر (مثل Amazon با Bright Data) اعتبار پولی مصرف می‌کنند.

## کی استفاده کنیم
🧭 پژوهش موضوع و رقبا از منابع عمومی (Reddit، HN، GitHub) بدون کوکی. اگر دیدگاه اینستاگرام لازم شد، API رسمی یا ScrapeCreators با کلید جدا بهتر از کوکی مرورگر است. بدون اجازه‌ی کاربر نصب نشود.

## قیمت و مجوز
✅ کد رایگان MIT. منابع پولی اختیاری (ScrapeCreators، X API، مدل رتبه‌بندی) هزینه‌ی جدا دارند.

## مرتبط
غربال · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S165](../sources/README.md#s165) · https://github.com/mvanhorn/last30days-skill/blob/main/README.md

## بازبینی کد (۲۰۲۶-۱۰-۲۹)
- ✅ بخش کوکی مرورگر خوانده شد (SHA `7efc0ef`). پیش‌فرض خاموش است. ⚠️ اگر در ویزارد راه‌اندازی رضایت بدهی، کوکی‌های x.com و truthsocial.com را از مرورگرها می‌خواند (روی مک با کلید Keychain). 🧭 `FROM_BROWSER=off` بگذار و کلید API رسمی به کار ببر. تله‌متری دیده نشد. ❓ همه‌ی ۸۰ ماژول خوانده نشد.
