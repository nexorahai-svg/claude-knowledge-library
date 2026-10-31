---
name: Sentry
slug: sentry
category: browser-testing
domains: [apps, website, security]
verdict: trial
status: researched
summary: گزارش خطا و کارایی با منطقه‌ی داده‌ی اروپا
use_when: "app or site error monitoring where error data should stay in Europe"
how: "Trial first on a small task: Sentry EU (Frankfurt) region, chosen once and not changeable; keep sendDefaultPii and screenshots off and mask session replay; no UAE server so keep ID-document data out"
url: https://sentry.io
repo: "https://github.com/getsentry/sentry"
license: "FSL (کد سرور)؛ SDKها MIT"
pricing: freemium
risk: medium
sources: [S99]
found_in: []
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Sentry

## چیست
✅ رایگان: ۵ هزار خطا، ۱ کاربر، ۳۰ روز؛ Team ۲۹ دلار. منطقه: آمریکا یا اروپا (فرانکفورت)، بعداً عوض نمی‌شود. در React Native `sendDefaultPii`، عکس صفحه و ساختار نما پیش‌فرض خاموش؛ ضبط جلسه در Flutter متن و ورودی را می‌پوشاند. بارگذاری source map در EAS Build با متغیر حساس.

## کی استفاده کنیم
🧭 وقتی می‌خواهی داده‌ی خطا در اروپا بماند.

## قیمت و مجوز
✅ بالا. ✅ مجوز کد سرور: FSL-1.1-Apache-2.0 (Functional Source License؛ بعد از دو سال Apache-2.0) (https://github.com/getsentry/sentry/blob/master/LICENSE.md).

## ریسک و هشدار
⚠️ سرور در امارات ندارد؛ داده‌ی مدارک نباید به آن برسد.

## مرتبط
[عملیات پس از انتشار](../domains/apps/app-operations.md) · [S99](../sources/README.md#s99)
