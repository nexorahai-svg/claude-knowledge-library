---
name: uv (نصب Python خصوصی)
slug: uv
category: app-publishing
domains: [apps]
verdict: adopt
status: researched
summary: مدیر بسته و نسخه‌ی Python از Astral؛ بدون دسترسی ادمین یک Python کامل در پوشه‌ی برنامه نصب می‌کند
use_when: "installing Python without sudo or a system Python ; creating isolated venvs ; self-installing starter for a desktop app on Linux/Mac"
how: "save astral.sh/uv/install.sh to a file, read it, run with UV_UNMANAGED_INSTALL=<dir>; then UV_PYTHON_INSTALL_DIR=<dir> uv python install 3.13; needs internet for the GitHub download"
url: https://docs.astral.sh/uv/
repo: "https://github.com/astral-sh/uv"
license: "MIT یا Apache-2.0"
pricing: free
risk: medium
sources: [S71]
found_in: []
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# uv (نصب Python خصوصی)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 0.13.6 (۲۰۲۶-۱۰-۲۷): بیلدهای CPython 3.11.18 تا 3.15.2؛ مجوز دوگانه‌ی MIT/Apache-2.0 بی‌تغییر.
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

## ارتقا به adopt (۲۰۲۶-۱۰-۳۰) 🔬
در سه پروژه‌ی واقعی بدون مشکل جدی کار کرد (دفتر پروژه‌ها): یک سایت (بررسی خودکار)، یک اپ دسکتاپ (Python خصوصی بی‌sudo) و یک پروژه‌ی بلاک‌چین (ساخت PDF با `uv run --no-project --with markdown`). طبق قاعده‌ی «دو پروژه بدون مشکل جدی» به adopt رسید. ⚠️ نگهبان همان است: نصب‌کننده را اول در فایل ذخیره و بخوان. ⚠️ `uv pip install` مثل pip وابستگی‌ها را ارتقا می‌دهد؛ در محیط آماده‌ی torch نسخه‌ها را پین کن ([MOSS-TTS](moss-tts.md)).

## مرتبط
[اپ دسکتاپ](../domains/apps/desktop-apps.md) · منبع [S71](../sources/README.md#s71)
