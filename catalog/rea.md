---
name: REA (Reverse Engineer Anything)
slug: rea
category: reverse-engineering
domains: [apps, claude-code]
verdict: assess
status: researched
summary: MCP و CLI که به عامل دیس‌اسمبلر و دیکامپایلر می‌دهد
url: https://github.com/morluto/rea
repo: "https://github.com/morluto/rea"
license: "MIT"
pricing: free
risk: high
sources: [S90, S120]
found_in: [batch-01/P14, batch-01/P16, batch-01/P17, batch-07, batch-13]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# REA (Reverse Engineer Anything)

## چیست
✅ (تحقیق کامل ۲۰۲۶-۱۰-۱۹) CLI و سرور MCP (`npx rea-agents mcp`، نسخه‌ی 6.7.0) با حدود ۱۸۷ ابزار که Hopper، Ghidra یا IDA را می‌راند؛ برای Electron، وب، HAR، .NET، APK، Flutter، WASM و… هم ابزار دارد. Ghidra و IDA را دانلود نمی‌کند؛ فقط Hopper را با امضای PGP و هش.
✅ حدود **۳۲۱ هزار ستاره** برای پروژه‌ای که حدود سه ماه است عمومی شده؛ زمان ستاره‌ها قابل بررسی نبود، پس عدد ستاره بی‌معناست. استفاده‌ی واقعی دارد: ۳۰۷ هزار دانلود npm در هفته‌ی ۱۰ تا ۱۶ اکتبر. بیشتر کار یک نفر (۱٬۹۱۳ commit).

## کی استفاده کنیم
🧭 فقط روی خروجی خودمان (APK، Flutter، Electron) یا دیدن اینکه یک SDK چه می‌فرستد، در ماشین مجازی، با ابزارهای ایستا و تأیید Claude روشن. برای سایت و شبکه‌های اجتماعی به کار نمی‌آید. ۲۰۲۶-۱۰-۱۹ به‌خاطر نیاز «آزمون مهاجم روی اپ خودمان» از بایگانی به کاتالوگ برگشت ([محافظت از اپ](../domains/apps/app-protection.md)).

## قیمت و مجوز
✅ MIT، رایگان؛ ابزارهای تجاری (IDA، Hopper، JEB) مجوز خودشان را می‌خواهند.

## ریسک و هشدار
✅ تله‌متری ندارد؛ نصب برنامه را نشان می‌دهد و تأیید می‌گیرد؛ به‌روزرسانی فقط با دستور.
⚠️ بعضی ابزارها برنامه‌ی هدف را اجرا می‌کنند و مستندات می‌گوید «تأیید جداگانه ندارد».
⚠️ تبلیغ اصلی README («قابلیتی در اپ دیگران دیدی؟ نسخه‌اش را برای پروژه‌ات بساز») با قانون «کپی نمی‌کنیم» نمی‌خواند.
⚠️ راه دوم نصب `curl … | bash` است؛ نصب Hopper روی لینوکس دسترسی root می‌خواهد.

## مرتبط
غربال دسته‌ی ۰۱ · غربال دسته‌ی ۰۷ · [S90](../sources/README.md#s90)
