---
name: flutter_animate
slug: flutter-animate
category: app-frameworks
domains: [apps]
verdict: adopt
status: researched
summary: بسته‌ی Flutter برای انیمیشن زنجیره‌ای کوتاه (fadeIn، slide، scale، تأخیر پلکانی) با یک خط
use_when: "staggered card entrances, like buttons or app bar effects in Flutter ; short chained animations in one line"
how: "flutter pub add flutter_animate (4.5.2, BSD-3); write widget.animate().fadeIn(delay: 90.ms).slideX(begin: 0.12); for complex motion use CustomPainter with our own AnimationController; avoid AnimatedSwitcher clearing the skeleton too early (white frames)"
url: https://pub.dev/packages/flutter_animate
repo: "https://github.com/gskinner/flutter_animate"
license: "BSD-3-Clause"
pricing: free
risk: low
sources: [S132]
found_in: [batch-17]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# flutter_animate

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) pub.dev آخرین نسخه 4.5.2 (۲۰۲۴-۱۱-۲۵)؛ بایگانی نشده؛ BSD-3. 🧭 پایدار است، نه رهاشده: https://pub.dev/packages/flutter_animate
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 4.5.2 همچنان آخرین (۲۰۲۴-۱۱-۲۵، pub.dev و GitHub)؛ ۴۸ issue باز، بایگانی نشده؛ پایدار است نه رها‌شده (❓ بیانیه‌ی نگهدارنده نیست).
✅ (pub.dev، ۲۰۲۶-۱۰-۲۱) نسخه‌ی 4.5.2، BSD-3، حدود ۴٫۳ هزار لایک، ۱۵۰ امتیاز. نوشتن انیمیشن به‌صورت زنجیره: `widget.animate().fadeIn(delay: 90.ms).slideX(begin: 0.12)`؛ `animate(target:)` برای حالت روشن/خاموش. ⚠️ آخرین انتشار ۲۰۲۴-۱۱-۲۵.

## دستور سریع
✅ ([pub.dev](https://pub.dev/packages/flutter_animate)، 4.5.2):
```bash
flutter pub add flutter_animate
```
```dart
import 'package:flutter_animate/flutter_animate.dart';
Text("Hello").animate().fadeIn(delay: 90.ms).slideX(begin: 0.12);       // زنجیره‌ی افکت
Text("Hi").animate(onPlay: (c) => c.repeat()).fadeIn();                  // حلقه
MyButton().animate(target: over ? 1 : 0).fade(end: 0.8).scaleXY(end: 1.1);  // روشن/خاموش با state
```
✅ تنظیم‌های مهم ([README](https://github.com/gskinner/flutter_animate)): افکت‌ها هم‌زمان اجرا می‌شوند، برای پشت‌سرهم از `delay` یا `.then(delay:)` استفاده کن؛ `delay` خود `animate()` فقط یک بار اول می‌آید ولی delay افکت در هر حلقه؛ `interval:` ورود پلکانی فهرست را می‌دهد؛ `Animate.restartOnHotReload = true` در توسعه.
خطاهای رایج: 🔬 اگر کارت با تأخیر وارد شود و `AnimatedSwitcher` اسکلت را زودتر پاک کند، چند فریم سفید دیده می‌شود (بخش «تجربه» پایین). ✅ دو افکت هم‌نوع روی یک ویجت نتیجه‌ی غیرمنتظره دارند. حرکت پیچیده (کشیدن خط) را با `CustomPainter` بنویس ([طراحی رابط اپ](../domains/apps/app-design.md)). آخرین انتشار ۲۰۲۴-۱۱-۲۵ است؛ با هر ارتقای اصلی Flutter یک build بگیر.

## کی استفاده کنیم
🧪 ورود پلکانی کارت‌ها، دکمه‌ی پسند، نوار بالا. برای حرکت پیچیده (کشیدن خط لوگو) `CustomPainter` با `AnimationController` خودمان بهتر است.

## تجربه ✅
✅ در یک اپ نمونه‌ی Flutter ورود پلکانی کارت‌ها و پرش قلب کار کرد. ⚠️ اگر کارت با تأخیر وارد شود و `AnimatedSwitcher` جای اسکلت را زودتر خالی کند، چند فریم سفید دیده می‌شود؛ مدت `AnimatedSwitcher` را از بیشترین تأخیر بیشتر بگذار.

## قیمت و مجوز
✅ رایگان، BSD-3.

✅ بازبینی ۲۰۲۶-۱۰-۲۶: pub.dev نسخه‌ی 4.5.2 (۲۰۲۴-۱۱-۲۵)، مخزن بایگانی نشده. ❓ سازگاری با آخرین Flutter پایدار آزموده نشد.

## مرتبط
[طراحی رابط اپ](../domains/apps/app-design.md) · [Flutter](flutter.md) · [S132](../sources/README.md#s132)

✅ (بررسی ۲۰۲۶-۱۰-۳۰) آخرین نسخه 4.5.2 (۲۰۲۴-۱۱-۲۴ در pub.dev) و آخرین push همان روز؛ آرشیو نشده. 🧭 بسته‌ی کوچک و پایداری است و کم‌تغییری به‌تنهایی دلیل کنار گذاشتن نیست؛ با هر ارتقای اصلی Flutter یک بار build بگیر.

🧭 (ارتقا ۲۰۲۶-۱۰-۳۱ با تصمیم کاربر: 🧪 به ✅) در پروژه‌ی واقعی نتیجه داد. نگهبان‌های ریسک همین کارت سر جایشان می‌مانند.
