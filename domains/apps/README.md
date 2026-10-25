# حوزه‌ی اپلیکیشن: موبایل و دسکتاپ، چندسکویی

> **هدف این حوزه:** ساختن اپلیکیشن برای iOS، Android، Windows، macOS و Linux با Claude Code: انتخاب فریم‌ورک، طراحی رابط، تست، امضا و انتشار در فروشگاه‌ها.
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۲
> **ابزارهای این حوزه:** [کاتالوگ](../../catalog/README.md) (ستون حوزه = apps)

---

## سندهای آماده

| سند | نوع | برای چه کاری |
|---|---|---|
| [mobile-launch-playbook.md](mobile-launch-playbook.md) | راهنمای قدم‌به‌قدم | **از اینجا شروع کن:** اولین اپ موبایل تا فروشگاه؛ زمان‌بندی واقعی، تصمیم پشته و بک‌اند، برنامه‌ی هفت روز، قانون‌های پروژه |
| [app-backend.md](app-backend.md) | توضیح | محل داده (امارات)، ورود، اعلان، پرداخت، امنیت فایل مدارک |
| [app-operations.md](app-operations.md) | مرجع | گزارش خطا، تحلیل، فرم‌های حریم خصوصی، به‌روزرسانی بدون فروشگاه، امنیت |
| [app-protection.md](app-protection.md) | دستورالعمل | محافظت در برابر مهندسی معکوس (سرور، مبهم‌سازی، Play Integrity) و آزمون مهاجم روی خروجی خودمان |
| [cross-platform-frameworks.md](cross-platform-frameworks.md) | توضیح | انتخاب فریم‌ورک: Flutter، Expo، Compose Multiplatform، MAUI؛ کی بومی بسازیم |
| [desktop-apps.md](desktop-apps.md) | توضیح | Tauri، Electron، Flutter Desktop: امنیت، به‌روزرسانی، امضا |
| [app-design-system.md](app-design-system.md) | دستورالعمل | **طراحی هر اپ:** پرسش‌نامه، توکن، فونت، فرق iOS و Android، اندازه‌ی پنجره، دروازه‌ی کیفیت طراحی، [قالب شروع](../../starters/flutter-app/README.md) |
| [app-styles.md](app-styles.md) | مرجع | هشت سبک نام‌دار با دستور دقیق و عکس، و سلیقه‌ی ثبت‌شده‌ی کاربر |
| [app-screen-patterns.md](app-screen-patterns.md) | مرجع | کاتالوگ صفحه‌ها: پنج حالت، اجزا و فرق دو سکو برای هر صفحه |
| [app-design.md](app-design.md) | مرجع | اندازه‌ی لمس، کنتراست، متن، قرینه‌سازی فارسی |
| [app-testing.md](app-testing.md) | دستورالعمل | Maestro و MCPهای شبیه‌ساز؛ قانون «تمام نیست تا تست سبز شود» |
| [publishing-apps.md](publishing-apps.md) | راهنمای قدم‌به‌قدم | حساب، شرط بررسی، آزمون بسته، CI، فروشگاه‌های دسکتاپ |
| [licensing-and-sales.md](licensing-and-sales.md) | توضیح | مجوز و کلید، ابطال با lease، سرور مجوز روی Cloudflare، پرداخت ایرانی/اماراتی و محدودیت‌های ایران |
| [local-network-app.md](local-network-app.md) | توضیح | اپ کسب‌وکار روی یک رایانه در محل: کارمند یا مهمان، تونل، همگام‌سازی، قیمت در سرور، حریم خصوصی، چاپ برگه |

## مشترک با حوزه‌های دیگر

- [روش کار با Claude](../website/01-method/claude-workflow.md) و [Vibe Coding](../website/01-method/vibe-coding.md): چرخه‌ی مرحله‌ای، Git، امنیت
- [هزینه و کارایی Claude Code](../claude-code/cost-efficiency.md) · [کار موازی](../claude-code/parallel-agents.md) · [بررسی خودکار](../claude-code/verification.md) · [امنیت MCP](../claude-code/mcp-safety.md)
- [فارسی و RTL](../website/02-design/persian-rtl.md) (اصول جهت و فونت برای اپ هم صدق می‌کند)
- [Supabase](../../catalog/supabase.md) برای بک‌اند و ورود کاربر

---

## در صف تحقیق

| موضوع | سؤال‌های اصلی |
|---|---|
| **Material 3** | خواندن صفحه‌های دسترسی‌پذیری و دوجهته با مرورگر |

🧭 قانون این حوزه: هر توصیه از مستندات رسمی فریم‌ورک و فروشگاه، با تاریخ؛ قوانین فروشگاه‌ها مرتب عوض می‌شوند.
