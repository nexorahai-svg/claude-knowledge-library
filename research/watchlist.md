# فهرست پایش: کجا ابزارهای تازه را پیدا کنیم

> **هدف این سند:** منابع ثابتی که مرتب چک می‌شوند تا قابلیت‌های تازه‌ی Claude، افزونه‌ها، مهارت‌ها، سرورهای MCP، عامل‌ها و ابزارهای طراحی و ساخت سایت، **از منبع اصلی** و قبل از رسیدن به پست‌های X، وارد کتابخانه شوند.
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۴ (لینک‌ها ۲۰۲۶-۱۰-۱۷ باز شدند)
> **اجرای خودکار (از ۲۰۲۶-۱۰-۲۲):** هر روز ساعت ۱۰ به وقت دبی با تایمر systemd کاربر (`scripts/run_routine.py`، پرامپت در `research/routines/daily-watch.md`)؛ برنامه‌ی Claude لازم نیست باز باشد. تغییرهای کم‌خطر (نسخه‌ی تازه‌ی کارت موجود، لینک مرده، تاریخ بررسی، هشدار مجوز) مستقیم اعمال می‌شوند؛ بقیه پیشنهاد در `research/inbox/<تاریخ>-watch.md`؛ دوشنبه‌ها خلاصه‌ی هفتگی برای `/kl-review`. شکست با پیام دسکتاپ و هشدار شروع جلسه.
> **جاروی دو‌روزه:** به‌روز کردن کل کتابخانه و جستجوی گسترده‌تر جدا انجام می‌شود: [جاروی دو‌روزه](deep-sweep.md).
> **روش:** [برنامه‌ی تحقیق X](x-research-plan.md) برای پست‌ها؛ این فهرست برای منابع اصلی. هر یافته طبق [CLAUDE.md](../CLAUDE.md) ثبت می‌شود.

---

## سطح ۱: رسمی Anthropic (هر روز)

| منبع | چه چیزی | لینک | آخرین مورد دیده‌شده |
|---|---|---|---|
| تغییرات Claude Code | هر نسخه‌ی تازه، تنظیم، دستور، متغیر محیطی | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | نسخه‌ی **2.1.310** (Monitor روی Bedrock/Vertex/Foundry، رفع compaction و cleanup؛ قبلی 2.1.309؛ چک: ۲۰۲۶-۱۰-۲۴) |
| تغییرات مستندات Claude Code | صفحه‌ی changelog مستندات | https://code.claude.com/docs/en/changelog | 2.1.310 (چک: ۲۰۲۶-۱۰-۲۴) |
| نسخه‌ی npm Claude Code | شماره‌ی آخرین نسخه | https://registry.npmjs.org/@anthropic-ai/claude-code/latest | 2.1.310 (چک: ۲۰۲۶-۱۰-۲۴) |
| یادداشت‌های انتشار API | مدل تازه، قابلیت API، قیمت | https://platform.claude.com/docs/en/release-notes/overview | ۲۰۲۶-۱۰-۲۱ (API نسخه‌ی 2026-10-21 و SDKهای Python 2.0 / TS 1.0 با مجوز Apache-2.0؛ چک: ۲۰۲۶-۱۰-۲۲) |
| یادداشت‌های انتشار اپ‌ها | Claude.ai، دسکتاپ، موبایل | https://support.claude.com/en/articles/12138966-release-notes | ۲۰۲۶-۱۰-۰۷ (Haiku 5.5؛ چک: ۲۰۲۶-۱۰-۲۰) |
| اخبار Anthropic | اعلام مدل و محصول | https://www.anthropic.com/news | ۲۰۲۶-۱۰-۱۸ (public benefit fund؛ چک: ۲۰۲۶-۱۰-۲۲) |
| وبلاگ Claude | راهنما و قابلیت‌ها | https://claude.com/blog | ۲۰۲۶-۱۰-۱۹ (بازطراحی کنترل نسخه، وبلاگ مهندسی؛ چک: ۲۰۲۶-۱۰-۲۲) |

## سطح ۱ب: اپلیکیشن و شبکه‌های اجتماعی (هر روز، فقط عنوان نسخه‌ها و اعلان‌ها)

| حوزه | منبع | لینک |
|---|---|---|
| اپ | Flutter (یادداشت انتشار) | https://docs.flutter.dev/release/release-notes |
| اپ | React Native (وبلاگ) | https://reactnative.dev/blog |
| اپ | Expo (تغییرات) | https://expo.dev/changelog |
| اپ | Compose Multiplatform (تازه‌ها) | https://kotlinlang.org/docs/multiplatform/whats-new-compose.html |
| اپ | Tauri (نسخه‌ها) | https://github.com/tauri-apps/tauri/releases |
| اپ | Electron (وبلاگ) | https://www.electronjs.org/blog |
| اپ | اخبار توسعه‌دهندگان Apple | https://developer.apple.com/news/ |
| اپ | قوانین بررسی App Store | https://developer.apple.com/app-store/review/guidelines/ |
| اپ | وبلاگ توسعه‌دهندگان Android | https://android-developers.googleblog.com/ |
| شبکه | مستندات Instagram Platform | https://developers.facebook.com/docs/instagram-platform |
| شبکه | TikTok Content Posting API | https://developers.tiktok.com/doc/content-posting-api-get-started |
| شبکه | YouTube Data API | https://developers.google.com/youtube/v3/docs |
| شبکه | X API | https://developer.x.com/en/docs |
| شبکه | LinkedIn Posts API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api |

## سطح ۲: افزونه، مهارت و MCP (هر هفته)

| منبع | چه چیزی | لینک |
|---|---|---|
| فهرست افزونه‌های Claude | افزونه‌ها و اتصال‌دهنده‌های تأییدشده | https://claude.com/plugins |
| بازار رسمی افزونه‌ها | مخزن افزونه‌های رسمی Anthropic | https://github.com/anthropics/claude-plugins-official |
| مهارت‌های رسمی | مخزن skillهای Anthropic | https://github.com/anthropics/skills |
| ثبت رسمی MCP | سرورهای MCP منتشرشده | https://registry.modelcontextprotocol.io |
| سرورهای مرجع MCP | پیاده‌سازی‌های مرجع | https://github.com/modelcontextprotocol/servers |

## سطح ۳: جامعه (هر هفته، با احتیاط)

| منبع | چه چیزی | لینک |
|---|---|---|
| موضوع claude-code در گیت‌هاب | مخزن‌های تازه‌ی جامعه | https://github.com/topics/claude-code |
| ترندهای گیت‌هاب | پروژه‌های پرطرفدار روز | https://github.com/trending |
| حساب‌های X | **فقط حساب‌های 🟢 و 🟡**؛ حساب‌های 🔴 پیگیری نمی‌شوند | [x-accounts.md](x-accounts.md) |
| فهرست عامل‌ها | دسته‌بندی‌شده | https://github.com/slavakurilyak/awesome-ai-agents |
| Trendshift | مخزن‌های پرطرفدار گیت‌هاب به تفکیک روز، هفته، ماه، سال و موضوع؛ تبلیغ دارد ([کارت](../catalog/trendshift.md)) | https://trendshift.io |
| Star History | نمودار رشد ستاره‌ها برای سنجیدن اینکه رشد یک مخزن واقعی و پیوسته است ([کارت](../catalog/star-history.md)) | https://star-history.com |
| Agent Skills Hub | فهرست خودکار مخزن‌های skill و MCP از گیت‌هاب؛ یک‌نفره و غیررسمی؛ **فقط برای کشف، نه اعتماد** ([کارت](../catalog/agent-skills-hub.md)) | https://agentskillshub.top |

🧭 ترتیب اعتماد برای افزونه، skill و MCP: اول منبع‌های رسمی سطح ۲، بعد فهرست‌های جامعه. «ستاره‌ی زیاد» یا «نمره‌ی امنیت خودکار» جای خواندن کد را نمی‌گیرد (قانون ۴ [CLAUDE.md](../CLAUDE.md)).

## سطح ۴: طراحی و حرکت (هر هفته)

| منبع | لینک |
|---|---|
| Recent (Godly) | https://recent.design |
| Awwwards | https://www.awwwards.com |
| ویدیوهای لانچ | https://whatships.com |
| تغییرات GSAP، Motion، Three.js | صفحه‌ی releases مخزن هر کدام (لینک در کارت‌ها) |

---

## قانون‌های پایش

1. **منبع رسمی قبل از پست:** اگر قابلیتی در changelog رسمی آمده، کارت یا سند را از همان‌جا به‌روز کن، نه از پست X.
2. **ستاره و هیاهو معیار نیست:** هر ابزار جامعه کارت `queued` می‌گیرد تا مجوز، کد و جریان داده‌اش بررسی شود (قانون ۴ در [CLAUDE.md](../CLAUDE.md)).
3. **ستون «آخرین مورد دیده‌شده» را به‌روز نگه دار** تا دفعه‌ی بعد فقط موارد تازه بررسی شوند.
4. **قابلیت تازه‌ی Claude Code که سندی را عوض می‌کند** (مثلاً تنظیم هزینه یا حالت مجوز)، همان سند را با برچسب ✅ و شماره‌ی نسخه به‌روز کند.

## پرامپت پایش

```text
Run the knowledge-library watch: open every Tier 1 source in research/watchlist.md and list
what is new since the "last seen" entries. For each new Claude Code version, read the
changelog lines and decide which library documents or cards they affect. Then check Tier 2
for new official plugins, skills and MCP servers. Verify each item against its primary
source, file results per CLAUDE.md (cards, documents, sources, CHANGELOG), update the
"last seen" column, commit, and give me a short Persian summary.
```
