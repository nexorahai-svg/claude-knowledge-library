---
name: Auth.js (NextAuth.js)
slug: authjs
category: database-backend
domains: [website]
verdict: hold
status: researched
summary: کتابخانه‌ی قدیمی ورود برای Next.js؛ از ۲۰۲۵-۰۹ بخشی از Better Auth و فقط وصله‌ی امنیتی می‌گیرد؛ برای پروژه‌ی تازه نه
url: https://authjs.dev/
repo: "https://github.com/nextauthjs/next-auth"
license: "ISC"
pricing: free
risk: medium
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2027-01-17"
---

# Auth.js (NextAuth.js)

## چیست
✅ کتابخانه‌ی ورود برای وب با OAuth، ورود ایمیلی و passkey؛ با یا بدون پایگاه داده (نشست بی‌حالت). مجوز ISC، حدود ۲۸ هزار ستاره.
✅ نسخه‌ی پایدار `next-auth@4.24.15`؛ نسخه‌ی ۵ هنوز `5.0.0-beta.32` است (npm، ۲۰۲۶-۱۰-۱۹). آخرین push مخزن ۲۰۲۶-۰۷-۲۲.
✅ README مخزن: «Auth.js اکنون بخشی از Better Auth است» و برای پروژه‌ی تازه Better Auth را توصیه می‌کند، مگر برای نشست بی‌حالت بدون پایگاه داده. اعلام ۲۰۲۵-۰۹-۲۲: وصله‌ی امنیتی و مشکل فوری ادامه دارد؛ قابلیت تازه وعده داده نشده (https://better-auth.com/blog/authjs-joins-better-auth).
✅ آگهی‌های امنیتی ۱۲ ماه گذشته: ۵ (۲ زیاد، ۲ متوسط، ۱ کم)، از جمله دور زدن بررسی ایمیل با نویسه‌ی شبیه `@` (https://github.com/nextauthjs/next-auth/security/advisories).

## کی استفاده کنیم
🧭 پروژه‌ی تازه: نه؛ [Better Auth](better-auth.md) 🧪. پروژه‌ی موجود که Auth.js دارد: نگه دار، به‌روز کن، و مهاجرت را برنامه‌ریزی کن.

## قیمت و مجوز
✅ رایگان، ISC.

## ریسک و هشدار
⚠️ نقش و سازمان داخلی ندارد؛ باید خودت بسازی. ⚠️ نسخه‌ی ۵ بعد از سال‌ها هنوز beta است.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125)
