---
name: drawDB
slug: drawdb
category: database-backend
domains: [website, apps]
verdict: trial
status: researched
summary: ویرایشگر نمودار پایگاه داده در مرورگر و خروجی SQL
use_when: "designing database tables before building the backend ; showing a schema diagram to a client"
how: "Trial first on a small task: open https://drawdb.app, draw tables and export SQL; to self-host run npm install then npm run dev, or docker build -t drawdb . then docker run -p 3000:80 drawdb; AGPL-3.0, so do not embed or modify it in a product"
url: https://drawdb.app
repo: "https://github.com/drawdb-io/drawdb"
license: "AGPL-3.0"
pricing: free
risk: low
sources: [S160]
last_checked: 2026-10-27
next_check: "2027-01-25"
---

# drawDB

## چیست
✅ (AGPL-3.0، حدود ۴۰ هزار ستاره، فعال؛ آخرین تغییر ۲۰۲۶-۱۰-۲۴). ✅ README: بدون حساب در مرورگر کار می‌کند؛ اشتراک‌گذاری فایل به سرور جدا (drawdb-server) نیاز دارد.

✅ نصب و اجرا (https://github.com/drawdb-io/drawdb، ۲۰۲۶-۱۰-۲۷): npm install ؛ npm run dev (یا docker build -t drawdb . ؛ docker run -p 3000:80 drawdb)

## کی استفاده کنیم
🧭 برای طراحی جدول‌ها پیش از ساخت بک‌اند و نشان دادن به مشتری.
