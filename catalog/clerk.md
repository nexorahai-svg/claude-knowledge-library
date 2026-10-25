---
name: Clerk
slug: clerk
category: database-backend
domains: [website, apps]
verdict: assess
status: researched
summary: سرویس ورود آماده با صفحه‌های ساخته‌شده برای Next.js؛ داده فقط در آمریکا؛ passkey و ورود دومرحله‌ای فقط در طرح پولی
url: https://clerk.com/
repo: "https://github.com/clerk/javascript"
license: "سرویس تجاری (SDK با MIT)"
pricing: freemium
risk: medium
sources: [S125]
found_in: [gap-playbooks]
last_checked: 2026-10-19
next_check: "2026-11-18"
---

# Clerk

## چیست
✅ سرویس ورود میزبانی‌شده با کامپوننت‌های آماده (`@clerk/nextjs@7.9.17`، SDK با مجوز MIT). سازمان، نقش Admin و Member، دسترسی سفارشی و دعوت در همه‌ی طرح‌ها هست (https://clerk.com/pricing).

## کی استفاده کنیم
🧭 فقط برای نمونه‌ی سریع یا SaaS بدون داده‌ی حساس که مشتری‌اش با میزبانی داده در آمریکا مشکلی ندارد. برای امارات و داده‌ی حساس نه. پیش‌فرض ما [Better Auth](better-auth.md) 🧪 است.

## قیمت و مجوز
✅ (https://clerk.com/pricing، ۲۰۲۶-۱۰-۱۹)
- **Hobby (رایگان):** ۵۰ هزار «کاربر ماندگار ماهانه» (MRU) برای هر اپ، ۳ صندلی داشبورد. Clerk بر اساس کاربر ماندگار حساب می‌کند، نه کاربر فعال.
- **Pro:** ۲۵ دلار در ماه (سالانه ۲۰)؛ بعد از ۵۰ هزار، هر کاربر ۰٫۰۲ دلار تا ۱۰۰ هزار.
- ⚠️ **passkey، ورود دومرحله‌ای و حذف نشان Clerk فقط در Pro و بالاتر.**
- سازمان در طرح رایگان: ۱۰۰ سازمان، هر کدام تا ۲۰ عضو؛ نقش سفارشی با افزونه‌ی ۱۰۰ دلار در ماه.

## ریسک و هشدار
⚠️ ✅ **محل داده انتخاب‌شدنی نیست:** داده روی زیرساخت آمریکا (Google Cloud و Cloudflare) است و همه‌ی پردازشگرهای فرعی در آمریکا (https://clerk.com/security.md، «Regional data residency: Not offered»). ✅ SOC 2 Type 2 دارد؛ ISO 27001 خود Clerk ندارد.
🧭 قفل شدن به سرویس: کاربران و نشست‌ها بیرون از سرور ما هستند؛ انتقال بعدی کار دارد.

## مرتبط
[ورود مشتری و نقش‌ها](../domains/website/04-tech/customer-auth.md) · [S125](../sources/README.md#s125)
