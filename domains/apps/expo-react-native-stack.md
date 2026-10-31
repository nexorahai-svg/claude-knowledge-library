# پشته‌ی Expo و React Native

> **نوع سند:** مرجع
> **هدف این سند:** اگر پروژه‌ای Expo یا React Native شد، برای هر نیاز بدانیم از کدام ابزار شروع کنیم و کدام دام را ببینیم.
> **موضوع تحقیق:** جستجوی GitHub و npm برای کتابخانه‌ها، قالب‌ها، اسکیل‌ها و MCPهای Expo و React Native.
> **منابع:** [S222 پشته‌ی Expo از GitHub](../../sources/README.md#s222)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۱
> **دفعه‌ی بعد چک شود:** نسخه‌ها و بازه‌ی RN؛ قیمت RevenueCat؛ آخرین push کتابخانه‌های کندشده.

---

⚠️ هیچ‌کدام از این‌ها هنوز در پروژه‌ی واقعی ما آزموده نشده‌اند. انتخاب‌ها 🧭 هستند و عددها از GitHub و npm در ۲۰۲۶-۱۰-۳۱ آمده‌اند. پیش‌فرض ما برای اپ چندسکویی همچنان [مقایسه‌ی فریم‌ورک‌ها](cross-platform-frameworks.md) است.

## انتخاب برای هر نیاز

| نیاز | شروع از | جایگزین | دام |
|---|---|---|---|
| شروع اپ | `create-expo-app` رسمی | [Create Expo Stack](../../catalog/create-expo-stack.md)، [Ignite](../../catalog/ignite.md) | Ignite از ژوئن push ندارد |
| انیمیشن | [Reanimated](../../catalog/react-native-reanimated.md) | `lottie-react-native` برای طرح آماده | نسخه به RN بسته است |
| لمس | [Gesture Handler](../../catalog/react-native-gesture-handler.md) | | |
| گرافیک | [React Native Skia](../../catalog/react-native-skia.md) | | نام بسته هنوز `@shopify` است |
| فهرست بلند | [FlashList](../../catalog/flash-list.md) | [Legend List](../../catalog/legend-list.md) | روی داده‌ی واقعی بسنج |
| سبک | [NativeWind](../../catalog/nativewind.md) | [Uniwind](../../catalog/uniwind.md)، [Tamagui](../../catalog/tamagui.md) | |
| کامپوننت | [React Native Reusables](../../catalog/react-native-reusables.md) | [HeroUI Native](../../catalog/heroui-native.md) | RTL را روی صفحه‌ی واقعی بسنج |
| برگه‌ی پایین | [Bottom Sheet](../../catalog/gorhom-bottom-sheet.md) | | آخرین push ۲۰۲۶-۰۵ |
| ذخیره‌ی محلی | [MMKV](../../catalog/react-native-mmkv.md) | | راز اینجا نه |
| دوربین | `expo-camera` | [VisionCamera](../../catalog/vision-camera.md) | به dev build نیاز دارد |
| خرید درون‌برنامه | [RevenueCat](../../catalog/revenuecat.md) | [OpenIAP](../../catalog/openiap.md) | مخزن قدیم بایگانی شد |
| هوش مصنوعی روی گوشی | [ExecuTorch](../../catalog/react-native-executorch.md) | | اندازه‌ی مدل |
| آزمون | [Maestro](../../catalog/maestro.md) | [Detox](../../catalog/detox.md) | iOS به Mac نیاز دارد |
| کارایی | [Flashlight](../../catalog/flashlight.md) | | فقط Android |

## اسکیل و ابزار عامل

- [Expo Skills](../../catalog/expo-skills.md) و [Expo MCP](../../catalog/expo-mcp.md): منبع رسمی و نقطه‌ی شروع.
- [Callstack Agent Skills](../../catalog/callstack-agent-skills.md): ارتقای React Native و کارایی.
- [Appllama Skills](../../catalog/appllama-skills.md): کیفیت صفحه و حرکت.
- [agent-device](../../catalog/agent-device.md): کنترل دستگاه برای عامل.
- [Software Mansion Skills](../../catalog/software-mansion-skills.md) و [Margelo Skills](../../catalog/margelo-skills.md): فایل مجوز ندارند؛ فقط بخوان.
- MCPهای کم‌ستاره‌ی جامعه‌ی React Native را کارت نکردم، چون نشانه‌ی کافی از نگه‌داری نداشتند.

## قاعده‌ها

- 🧭 کتابخانه‌ی بومی را با `npx expo install` نصب کن تا نسخه با SDK جفت شود.
- 🧭 ستاره و تاریخ به‌روزرسانی GitHub گمراه‌کننده است؛ `updatedAt` با هر ستاره عوض می‌شود. `pushed_at` را ببین.
- 🧭 پیش از نصب هر اسکیل، SKILL آن را کامل بخوان.

## مرتبط

[مقایسه‌ی فریم‌ورک‌ها](cross-platform-frameworks.md) · [آزمون اپ](app-testing.md) · [Appllama Skills](../../catalog/appllama-skills.md)
