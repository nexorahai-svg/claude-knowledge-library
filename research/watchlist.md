# فهرست پایش: کجا ابزارهای تازه را پیدا کنیم

> **هدف این سند:** منابع ثابتی که مرتب چک می‌شوند تا قابلیت‌های تازه‌ی Claude، افزونه‌ها، مهارت‌ها، سرورهای MCP، عامل‌ها و ابزارهای طراحی و ساخت سایت، **از منبع اصلی** و قبل از رسیدن به پست‌های X، وارد کتابخانه شوند.
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۱
> **اجرای خودکار (از ۲۰۲۶-۱۰-۲۲):** هر روز ساعت ۱۰ به وقت دبی با تایمر systemd کاربر (`scripts/run_routine.py`، پرامپت در `research/routines/daily-watch.md`)؛ برنامه‌ی Claude لازم نیست باز باشد. تغییرهای کم‌خطر (نسخه‌ی تازه‌ی کارت موجود، لینک مرده، تاریخ بررسی، هشدار مجوز) مستقیم اعمال می‌شوند؛ بقیه پیشنهاد در `research/inbox/<تاریخ>-watch.md`؛ دوشنبه‌ها خلاصه‌ی هفتگی برای `/kl-review`. شکست با پیام دسکتاپ و هشدار شروع جلسه.
> **جاروی دو‌روزه:** به‌روز کردن کل کتابخانه و جستجوی گسترده‌تر جدا انجام می‌شود: [جاروی دو‌روزه](deep-sweep.md).
> **روش:** [برنامه‌ی تحقیق X](x-research-plan.md) برای پست‌ها؛ این فهرست برای منابع اصلی. هر یافته طبق [CLAUDE.md](../CLAUDE.md) ثبت می‌شود.

---

## سطح ۱: رسمی Anthropic (هر روز)

| منبع | چه چیزی | لینک | آخرین مورد دیده‌شده |
|---|---|---|---|
| تغییرات Claude Code | هر نسخه‌ی تازه، تنظیم، دستور، متغیر محیطی | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | نسخه‌ی **2.1.316** (`CLAUDE_CODE_SUBAGENT_EFFORT`، `CLAUDE_CODE_DISABLE_ULTRATHINK`، منسوخ شدن فست‌مود Opus 4.8 تا ۳۰ نوامبر، رفع `--restricted` و `autoMode.allow`، شکست صریح کار زمان‌بندی‌شده‌ی ابری بی‌حکم ایمنی؛ 2.1.315 منتشر نشد؛ قبلی 2.1.314؛ چک: ۲۰۲۶-۱۰-۳۱) |
| تغییرات مستندات Claude Code | صفحه‌ی changelog مستندات | https://code.claude.com/docs/en/changelog | 2.1.316 (۲۰۲۶-۱۰-۳۱؛ چک: ۲۰۲۶-۱۰-۳۱) |
| نسخه‌ی npm Claude Code | شماره‌ی آخرین نسخه | https://registry.npmjs.org/@anthropic-ai/claude-code/latest | 2.1.316 (چک: ۲۰۲۶-۱۰-۳۱؛ Agent SDK 0.3.316) |
| یادداشت‌های انتشار API | مدل تازه، قابلیت API، قیمت | https://platform.claude.com/docs/en/release-notes/overview | ۲۰۲۶-۱۰-۳۰ (فست‌مود Opus 4.8 منسوخ، حذف ۲۰۲۶-۱۱-۳۰؛ ۱۰-۲۹ Usage and Cost Analytics API بتا؛ ۱۰-۲۸ سقف درخواست ۱۲۸ مگابایت؛ چک: ۲۰۲۶-۱۰-۳۱) |
| یادداشت‌های انتشار اپ‌ها | Claude.ai، دسکتاپ، موبایل | https://support.claude.com/en/articles/12138966-release-notes | ۲۰۲۶-۱۰-۲۱ (Claude Duet پیش‌نمایش پژوهشی، Pro/Max آمریکا؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اخبار Anthropic | اعلام مدل و محصول | https://www.anthropic.com/news | ۲۰۲۶-۱۰-۲۸ (گسترش AI for Science؛ ۱۰-۲۷ دارو و GSA؛ ۱۰-۲۶ ثبت S-1؛ چک: ۲۰۲۶-۱۰-۳۱) |
| وبلاگ Claude | راهنما و قابلیت‌ها | https://claude.com/blog | ۲۰۲۶-۱۰-۲۸ (سه پست Enterprise: گزارش هوشمند و بودجه‌ی گروهی، IDC/Quanta، آرتیفکت حقوقی؛ ۱۰-۲۷ هزینه‌ی Claude Code روی Google Cloud؛ چک: ۲۰۲۶-۱۰-۳۱) |


## سطح ۱ب: اپلیکیشن و شبکه‌های اجتماعی (هر روز، فقط عنوان نسخه‌ها و اعلان‌ها)

| حوزه | منبع | لینک |
|---|---|---|
| اپ | Flutter (یادداشت انتشار) | https://docs.flutter.dev/release/release-notes — آخرین دیده‌شده: 3.47.9 پایدار (۲۰۲۶-۱۰-۲۹، از JSON انتشارها؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | React Native (وبلاگ) | https://reactnative.dev/blog — آخرین دیده‌شده: RN 0.88 (۲۰۲۶-۱۰-۱۹؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | Expo (تغییرات) | https://expo.dev/changelog — آخرین دیده‌شده: SDK 58 (۲۰۲۶-۱۰-۱۵؛ npm 58.0.21؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | Compose Multiplatform (تازه‌ها) | https://kotlinlang.org/docs/multiplatform/whats-new-compose.html — آخرین دیده‌شده: پایدار 1.12.2؛ 1.13.0-beta01 (۲۰۲۶-۱۰-۲۳، از GitHub releases؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | Tauri (نسخه‌ها) | https://github.com/tauri-apps/tauri/releases — آخرین دیده‌شده: 2.12.5 (۲۰۲۶-۱۰-۲۱؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | Electron (وبلاگ) | https://www.electronjs.org/blog — آخرین دیده‌شده: پست «Electron 45» (۲۰۲۶-۱۰-۲۱)؛ npm 45.2.1 (چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | اخبار توسعه‌دهندگان Apple | https://developer.apple.com/news/ — آخرین دیده‌شده: ۲۰۲۶-۱۰-۲۹ (کارمزد ۲۶٪ فروشگاه تایوان از ۳۱ اکتبر؛ ۱۰-۲۸ Touch on Mac؛ چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | قوانین بررسی App Store | https://developer.apple.com/app-store/review/guidelines/ — «Last Updated: October 16, 2026» (چک: ۲۰۲۶-۱۰-۳۱) |
| اپ | وبلاگ توسعه‌دهندگان Android | https://developer.android.com/blog (خوراک: https://developer.android.com/static/blog/atom.xml؛ از ۲۰۲۶-۱۰ جای Blogspot قدیمی https://android-developers.googleblog.com/) — آخرین دیده‌شده: ۲۰۲۶-۱۰-۲۹ (پست API مخاطبین؛ ۱۰-۲۸ سه پست Android Dev Summit 26: Android Studio Rabbit 2، BYOA/ACP، Android CLI؛ چک: ۲۰۲۶-۱۰-۳۱) |
| شبکه | مستندات Instagram Platform | https://developers.facebook.com/docs/instagram-platform — آخرین دیده‌شده در changelog: ۲۰۲۶-۱۰-۲۸ (webhook واگذاری Meta Business Agent: `message.admin_text`؛ ۱۰-۲۰ کپشن استوری و `ordered_comments` هم مستقیم دیده شد ✅؛ چک: ۲۰۲۶-۱۰-۳۱ با curl فقط ورودی ژوئیه را داد، صفحه دینامیک است ❓) |
| شبکه | TikTok Content Posting API | https://developers.tiktok.com/doc/content-posting-api-get-started — آخرین دیده‌شده: ۲۰۲۶-۰۸-۰۴ (چک: ۲۰۲۶-۱۰-۳۱؛ تاریخ با curl خوانده نمی‌شود، مرورگر لازم است) |
| شبکه | YouTube Data API | https://developers.google.com/youtube/v3/docs (تاریخچه: https://developers.google.com/youtube/v3/revision_history) — آخرین دیده‌شده: ۲۰۲۶-۱۰-۱۵ (چک: ۲۰۲۶-۱۰-۳۱؛ قدیمی‌تر: ۰۹-۳۰ `snippet.imageUrl` کامنت، ۰۹-۱۴ بندانگشتی ۵۰ مگابایت) |
| شبکه | X API | https://developer.x.com/en/docs (changelog: https://docs.x.com/changelog) — آخرین دیده‌شده: ۲۰۲۶-۱۰-۲۹ (Conversion API رویداد اپ در Ads API؛ چک: ۲۰۲۶-۱۰-۳۱) |
| شبکه | LinkedIn Posts API | https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api (نسخه‌ها: https://learn.microsoft.com/en-us/linkedin/marketing/versioning؛ صفحه‌ی `recent-changes` بی‌پارامتر ۳۰۱ می‌دهد و فقط با `?view=li-lms-2026-10` ۲۰۰ است) — آخرین دیده‌شده: نسخه‌ی 202610؛ 202511 در ۲۰۲۶-۱۱-۱۶ بازنشسته می‌شود؛ لینک کارآمد changelog: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes?view=li-lms-2026-10 (چک: ۲۰۲۶-۱۰-۳۱) |

## سطح ۲: افزونه، مهارت و MCP (هر هفته)

| منبع | چه چیزی | لینک |
|---|---|---|
| فهرست افزونه‌های Claude | افزونه‌ها و اتصال‌دهنده‌های تأییدشده | https://claude.com/plugins |
| بازار رسمی افزونه‌ها | مخزن افزونه‌های رسمی Anthropic | https://github.com/anthropics/claude-plugins-official |
| مهارت‌های رسمی | مخزن skillهای Anthropic | https://github.com/anthropics/skills |
| بنیاد Agentic AI (AAIF، زیر Linux Foundation) 🟢 | مالک استاندارد Agent Skills از ۲۰۲۶-۱۰-۲۲ و MCP؛ ببین نسخه‌گذاری، فرایند پیشنهاد تغییر و راهنمای امنیتی skill منتشر شد یا نه | https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation (خبر اهدا؛ سایت agentskills.io) |
| ثبت رسمی MCP | سرورهای MCP منتشرشده | https://registry.modelcontextprotocol.io — ✅ (۲۰۲۶-۱۰-۳۰) `/v0/servers?limit=20` الفبایی برمی‌گرداند نه تازه‌ترین؛ برای پایش دوشنبه پارامتر مرتب‌سازی یا `updated_since` لازم است (در مستندات API ثبت بخوان ❓). دو نام در حوزه‌ی ما که باید خوانده شوند ❓: `ac.inference.sh/mcp` (تصویر، ویدیو، صدا، سه‌بعدی؛ پرداخت به ازای اجرا) و `ac.snag/snag` (شواهد کنسول و شبکه برای عامل کدنویس) |
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
| پیج اینستاگرام پارس‌پک (S158) | فقط ریلزهای **فنی** (امنیت، سرور، دیتابیس، طراحی سیستم، ابزار متن‌باز)؛ سرگرمی، تبلیغ و کاورهای عکس آدم کنار گذاشته شود. فقط با مرورگر داخلی (حساب جدای مخصوص خواندن، که کاربر در آن وارد شده؛ فقط خواندن، بدون لایک/فالو/کامنت/پیام، پیمایش آرام) و `scripts/fetch_post.py`؛ اسلاید کاروسل از صفحه‌ی `/p/<code>/embed/captioned/`؛ **هرگز با Chrome حساب کاربر** (ریسک بسته شدن حساب توسعه‌دهنده‌ی Meta). هر ادعا با منبع رسمی؛ ابزارهای «کامنت بگذار» را از GitHub پیدا کن. | https://www.instagram.com/parspackcom/reels/ — آخرین دیده‌شده: `De4aJOQoYOw` (pgvector، ۲۰۲۶-۱۰-۲۴) |
| پیج اینستاگرام رسانه ابرها (S159) | همان قواعد ردیف پارس‌پک؛ خبر مدل و ابزار هوش مصنوعی را فقط با صفحه‌ی رسمی ثبت کن؛ «رایگان/نامحدود» را همیشه چک کن | https://www.instagram.com/abrhamedia/ — آخرین دیده‌شده: De9KrVmsogu (۲۰۲۶-۱۰-۲۶) |
| پیج اینستاگرام SelfhostLab (S160) | همان قواعد؛ لینک GitHub در کپشن هست؛ مجوز را از LICENSE مخزن بخوان، نه از متن پست | https://www.instagram.com/selfhost_lab/ — آخرین دیده‌شده: `De33srTCqPH` (heretix-api، ۲۰۲۶-۱۰-۲۴) |
| پیج اینستاگرام Textura Agency (S179) | ریل روزانه‌ی سایت سینمایی ساخته‌شده با Claude؛ فقط ایده‌ی ترکیب‌بندی و حرکت؛ پرامپت پولی است، کپی نکن | https://www.instagram.com/textura.eu/ — آخرین دیده‌شده: De-MnEduyHF (۲۰۲۶-۱۰-۲۶) |
| پیج اینستاگرام مسیر AI (S224) | تبلیغ خدمات و آموزش فارسی؛ فقط ایده‌ی تیزر محصول؛ ترفند دور زدن منطقه را اجرا نکن | https://www.instagram.com/masiraii/ — آخرین دیده‌شده: DezMH8MxthP (۲۰۲۶-۱۰-۲۲) |
| پیج اینستاگرام میلاد ابراهیم‌پور (S161) | همان قواعد؛ ادعای قابلیت Claude/ChatGPT را با راهنمای رسمی چک کن؛ ورکشاپ و دوره را نادیده بگیر | https://www.instagram.com/miladxaitalks/ — آخرین دیده‌شده: `De1_X9ZAl-C` (۲۰۲۶-۱۰-۲۴) |
| پیج اینستاگرام محبود (S162) | همان قواعد؛ خبر محصول را با newsroom یا مستندات رسمی چک کن | https://www.instagram.com/mahbodpour/ — آخرین دیده‌شده: `Demj0dQslvD` (۲۰۲۶-۱۰) |
| پیج اینستاگرام code.xr (S170) | فقط ایده‌ی ریزتعامل و داشبورد تازه؛ کپی ممنوع | https://www.instagram.com/code.xr/ — آخرین دیده‌شده: `De5-GaEz96s` (۲۰۲۶-۱۰) |
| پیج اینستاگرام Numan (S171) | ممیزی و بازطراحی سایت کسب‌وکار خدماتی محلی؛ فقط اصول تبدیل | https://www.instagram.com/numanwebs/ — آخرین دیده‌شده: `DdjTVOio051` (۲۰۲۶-۰۹) |
| پیج اینستاگرام uiux.build (S174) | کاروسل‌های آموزشی طراحی؛ فقط اصول را بردار؛ برچسب «AI content» دارد | https://www.instagram.com/uiux.build/ — آخرین دیده‌شده: DdtcfHOt20t (۲۰۲۶-۰۹-۲۵) |
| پیج اینستاگرام Enkis Web Studio (S176) | سایت‌های روایت اسکرولی محصول؛ فقط اصول | https://www.instagram.com/enkywebstudio/ — آخرین دیده‌شده: `De6Xe_doNuA` (۲۰۲۶-۱۰) |

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
