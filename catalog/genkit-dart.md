---
name: Genkit Dart
slug: genkit-dart
category: database-backend
domains: [apps]
verdict: trial
status: researched
summary: SDK رسمی Genkit (Firebase/گوگل) برای Dart و Flutter: فراخوانی مدل، خروجی ساخت‌یافته، ابزار و عامل با افزونه‌های Google AI، Anthropic، OpenAI و MCP؛ Apache-2.0
use_when: "adding an LLM feature inside a Flutter app or a Dart server without hand-written HTTP ; calling Claude or Gemini from Dart with structured output ; serving AI flows from a Dart backend"
how: "Trial first on a small task: dart pub add genkit (1.0.x) plus genkit_anthropic or genkit_google_genai; keep API keys on a server or behind Firebase App Check, never in the app binary"
url: https://pub.dev/packages/genkit
repo: "https://github.com/genkit-ai/genkit-dart"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Genkit Dart

## چیست
✅ چارچوب هوش مصنوعی برای Dart و Flutter ([README](https://github.com/genkit-ai/genkit-dart)): جریان‌ها (flows)، ابزارها، prompt، خروجی ساخت‌یافته، عامل‌ها.
- ✅ بسته‌ی `genkit` نسخه‌ی 1.0.1 (۲۰۲۶-۱۰-۲۱)، ناشر تأییدشده `genkit.dev`، ۱۶۰ از ۱۶۰ امتیاز و ۸۱ پسند در https://pub.dev/packages/genkit؛ پشتیبانی همه‌ی سکوها (iOS، Android، وب، دسکتاپ).
- ✅ افزونه‌ها: `genkit_google_genai`، `genkit_vertexai`، `genkit_anthropic`، `genkit_openai`، `genkit_firebase_ai`، `genkit_chrome`، `genkit_mcp`، `genkit_shelf` (سرو از راه HTTP)، `genkit_otel` و بسته‌ی schemantic.
- ✅ مخزن ۱۷۵ ستاره، فعال (push ۲۰۲۶-۱۰-۲۸)، آرشیو نشده. در GitHub release با برچسب `genkit-v1.0.1` هست.
- ✅ README یک skill رسمی برای عامل معرفی می‌کند (`npx skills add genkit-ai/skills --skill developing-genkit-dart`)؛ نصب نکردیم.
- ❓ پایداری واقعی API پس از ۱٫۰ و کیفیت افزونه‌ی Anthropic آزموده نشد. افزونه‌ی `genkit_a2ui` و `genkit_google_cloud` طبق README آزمایشی‌اند.

## قیمت و مجوز
✅ Apache-2.0 (فایل https://github.com/genkit-ai/genkit-dart/blob/main/packages/genkit/LICENSE و برچسب license در pub.dev؛ ریشه‌ی مخزن فایل LICENSE ندارد، پس GitHub مجوز را تشخیص نمی‌دهد). رایگان و استفاده‌ی تجاری آزاد؛ هزینه‌ی مدل جداست.

## ریسک و هشدار
- 🧭 اگر فراخوانی مدل داخل اپ موبایل انجام شود، کلید API در باینری لو می‌رود. از سرور (`genkit_shelf`) یا Firebase AI با App Check استفاده کن ([بک‌اند اپ](../domains/apps/app-backend.md)).
- 🧭 وابستگی به اکوسیستم گوگل؛ بسته‌های زیاد و جوان‌اند.

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: one small AI feature in a test branch. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
🧭 وقتی اپ Flutter یا بک‌اند Dart قابلیت LLM لازم دارد و نمی‌خواهی HTTP دستی بنویسی؛ مقایسه با فراخوانی مستقیم API در [هوش مصنوعی در محصول](../domains/website/04-tech/ai-in-product.md). پیشنهاد ارتقا به trial: بله، برای یک قابلیت کوچک، چون نسخه‌ی ۱٫۰ پایدار، مجوز روشن و ناشر رسمی دارد.

## مرتبط
[S191](../sources/README.md#s191) · [Flutter](flutter.md) · [بک‌اند اپ](../domains/apps/app-backend.md)
