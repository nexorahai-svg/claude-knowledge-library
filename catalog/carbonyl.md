---
name: Carbonyl
slug: carbonyl
category: browser-testing
domains: [claude-code, website, security]
verdict: hold
status: researched
summary: مرورگر Chromium که صفحه را داخل ترمینال نقاشی می‌کند؛ از ۲۰۲۳ رها شده و روی Chromium 111 مانده
url: https://github.com/fathyb/carbonyl
repo: "https://github.com/fathyb/carbonyl"
license: "BSD-3-Clause"
pricing: free
risk: high
sources: [S109]
found_in: [batch-11]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Carbonyl

## چیست
✅ نسخه‌ی تغییر داده‌شده‌ی Chromium headless که صفحه را با کاراکترهای رنگی در ترمینال نشان می‌دهد، حتی از راه SSH و بدون محیط گرافیکی. README این ادعاها را دارد: WebGL، WebGPU، صدا و ویدیو، شروع زیر یک ثانیه، ۶۰ فریم در ثانیه. ❓ این عددها را نیازمودیم.

✅ حدود ۱۹٬۶۰۰ ستاره. ولی **آخرین commit در ۲۰۲۳-۰۲-۲۶** است و آخرین نسخه v0.0.3 در ۲۰۲۳-۰۲-۱۸. نسخه‌ی npm هم از ۲۰۲۳ عوض نشده. موتور آن روی **Chromium 111.0.5511.1** ثابت مانده است (فایل `chromium/.gclient` در مخزن).

## کی استفاده کنیم
⛔ برای کار ما نه:
- 🧭 عامل هوش مصنوعی صفحه را از راه درخت دسترس‌پذیری، DOM و عکس صفحه می‌فهمد، نه از تصویر کاراکتری ترمینال. README هیچ API خودکارسازی معرفی نمی‌کند ✅.
- برای کار عامل با وب، این‌ها را داریم: مرورگر داخلی Claude، [Playwright](playwright.md)، [Playwright MCP](playwright-mcp.md) و [Chrome DevTools MCP](chrome-devtools-mcp.md). همه روی Chromium به‌روز کار می‌کنند و در سرور بدون صفحه‌نمایش هم اجرا می‌شوند.
- 🧭 برای دیدن یک صفحه روی سرور از راه SSH، عکس صفحه با Playwright امن‌تر است.

## قیمت و مجوز
✅ رایگان، BSD-3-Clause.

## ریسک و هشدار
⚠️ Chromium 111 مال فوریه‌ی ۲۰۲۳ است. از آن زمان صدها وصله‌ی امنیتی Chromium را ندارد. باز کردن سایت‌های ناشناس با آن خطرناک است.
⚠️ issueهای ۲۰۲۶ نشان می‌دهند ورودی چندبایتی خراب می‌شود (UTF-8 حرف‌به‌حرف فرستاده می‌شود؛ issue #223). 🧭 برای تایپ فارسی هم احتمالاً همین مشکل هست ❓.
⚠️ پست معرفی، تاریخ رها شدن پروژه را نگفت.

## مرتبط
[بررسی خودکار](../domains/claude-code/verification.md) · [امنیت MCP](../domains/claude-code/mcp-safety.md) · [S109](../sources/README.md#s109) · غربال دسته‌ی ۱۱
