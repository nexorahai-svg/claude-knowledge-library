---
name: uv (نصب Python خصوصی)
slug: uv
category: app-publishing
domains: [apps]
verdict: trial
status: researched
summary: مدیر بسته و نسخه‌ی Python از Astral؛ بدون دسترسی ادمین یک Python کامل در پوشه‌ی برنامه نصب می‌کند
url: https://docs.astral.sh/uv/
repo: "https://github.com/astral-sh/uv"
license: "MIT یا Apache-2.0"
pricing: free
risk: medium
sources: [S71]
found_in: []
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# uv (نصب Python خصوصی)

## چیست
ابزار خط فرمان Astral برای مدیریت Python و بسته‌ها. نسخه‌ی پایدار در این تاریخ: 0.13.1 ✅.
- متغیر `UV_UNMANAGED_INSTALL=<پوشه>` نصب‌کننده را وادار می‌کند خود uv را فقط در همان پوشه بگذارد و PATH و فایل‌های shell را دست نزند ✅.
- `UV_PYTHON_INSTALL_DIR=<پوشه> uv python install 3.13` یک Python کامل (با sqlite3) بدون sudo در همان پوشه نصب می‌کند ✅. 🔬 در پروژه‌ی پنل قرارداد روی لینوکس، بدون Python سیستمی و بدون sudo، Python 3.13.16 در `runtime/python/cpython-3.13.16-linux-x86_64-gnu/bin/python3` نصب شد و برنامه با آن اجرا شد.

## کی استفاده کنیم
راه دوم در برنامه‌ی استارت لینوکس و مک، وقتی مدیر بسته‌ی سیستم یا sudo در دسترس نیست. راه اول همچنان مدیر بسته‌ی سیستم است. الگوی کامل: [برنامه‌ی استارت خودنصب‌کن](../domains/apps/desktop-apps.md).

## قیمت و مجوز
رایگان، MIT یا Apache-2.0 ✅. استفاده‌ی تجاری آزاد.

## ریسک و هشدار
- نصب‌کننده یک اسکریپت از اینترنت است (`https://astral.sh/uv/install.sh`). اول در فایل ذخیره کنید، بعد اجرا کنید، نه `curl | sh` کورکورانه 🧭.
- Python را از GitHub (پروژه‌ی python-build-standalone) دانلود می‌کند؛ پس اینترنت لازم است.

## مرتبط
[اپ دسکتاپ](../domains/apps/desktop-apps.md) · منبع [S71](../sources/README.md#s71)
