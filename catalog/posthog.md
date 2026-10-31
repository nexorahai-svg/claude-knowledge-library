---
name: PostHog
slug: posthog
category: research-tools
domains: [apps, website]
verdict: trial
status: researched
summary: تحلیل محصول با حالت کاملاً ناشناس و ابر اروپا
use_when: "app or site analytics without cross-app tracking and without an ATT prompt ; session replay and error tracking"
how: "Trial first on a small task: PostHog Flutter SDK with personProfiles: never for anonymous events and disable() for opt-out; US or EU cloud (none in UAE); turn session recording and autocapture OFF on ID-document pages"
url: https://posthog.com
repo: "https://github.com/PostHog/posthog"
license: "MIT (بیشتر کد)"
pricing: freemium
risk: medium
sources: [S99]
found_in: []
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# PostHog

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) معیار درست نسخه بسته‌های SDK است، نه برچسب `desktop-v…` یا `agent-skills-v…`: posthog_flutter 5.58.3 (۲۰۲۶-۱۰-۳۰، https://pub.dev/packages/posthog_flutter) و posthog-js 1.444.0 (https://www.npmjs.com/package/posthog-js).
✅ (جاروی ۲۰۲۶-۱۰-۲۸) برچسب desktop-v0.61.851 (۲۰۲۶-۱۰-۲۷) مال اپ دسکتاپ است، نه انتشار محصول؛ 🧭 جریان برچسب‌های مخزن معیار نسخه نیست؛ مجوز بی‌تغییر.
✅ رایگان ماهانه: ۱ میلیون رویداد، ۵ هزار ضبط جلسه، ۱۰۰ هزار خطا. ابر آمریکا یا اروپا (فرانکفورت). SDK Flutter با `personProfiles: never` برای رویداد ناشناس و `disable()` برای انصراف.

## کی استفاده کنیم
🧭 تحلیل بدون ردیابی، بدون نیاز به پنجره‌ی ATT.

## قیمت و مجوز
✅ بالا. ✅ مجوز مخزن: MIT Expat، جز پوشه‌ی `ee/` که مجوز جدا دارد (https://github.com/PostHog/posthog/blob/master/LICENSE).

## ریسک و هشدار
⚠️ روی صفحه‌های مدرک ضبط جلسه و ثبت خودکار خاموش؛ سرور در امارات ندارد.

## مرتبط
[عملیات پس از انتشار](../domains/apps/app-operations.md) · [S99](../sources/README.md#s99)
