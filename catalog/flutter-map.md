---
name: flutter_map
slug: flutter-map
category: app-frameworks
domains: [apps]
verdict: trial
status: researched
summary: نقشه‌ی متن‌باز Flutter با کاشی دلخواه، خط مسیر، نشانگر ویجتی؛ بدون کلید Google
url: https://pub.dev/packages/flutter_map
repo: "https://github.com/fleaflet/flutter_map"
license: "BSD-3-Clause"
pricing: free
risk: medium
sources: [S132]
found_in: [batch-17]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# flutter_map

## چیست
✅ (pub.dev، ۲۰۲۶-۱۰-۲۱) نسخه‌ی 8.3.2 (۲۰۲۶-۰۸-۲۷)، BSD-3، حدود ۲٫۲ هزار لایک. لایه‌ها: `TileLayer`، `PolylineLayer` (با `StrokePattern.dashed`)، `MarkerLayer` با هر ویجتی، `RichAttributionWidget`؛ `initialCameraFit: CameraFit.bounds(...)` برای جا دادن مسیر.

## کی استفاده کنیم
🧪 صفحه‌ی ردیابی سفارش، نقشه‌ی شعبه‌ها، منطقه‌ی تحویل؛ کنار [H3](h3.md).

## تجربه ✅
✅ در design-lab: مسیر طی‌شده و باقی‌مانده، موتور متحرک روی مسیر، هاله‌ی تپنده، کم‌رنگ کردن نقشه با `ColorFiltered` تا مسیر دیده شود، و `padding` پایین در `CameraFit` تا مسیر زیر برگه‌ی پایین نرود.

## ریسک و هشدار
⚠️ کاشی `tile.openstreetmap.org` فقط برای آزمایش؛ سیاست استفاده‌ی OSM اپ منتشرشده با کاربر زیاد را رد می‌کند. برای محصول، سرویس کاشی مجوزدار یا کاشی خودمان. نام بسته در `userAgentPackageName` و ذکر «OpenStreetMap contributors» لازم است.

## قیمت و مجوز
✅ بسته رایگان؛ هزینه‌ی کاشی جدا.

## مرتبط
[طراحی رابط اپ](../domains/apps/app-design.md) · [Flutter](flutter.md) · [S132](../sources/README.md#s132)
