# سئوی فنی و دیده شدن در جستجوی هوش مصنوعی

> **نوع سند:** دستورالعمل
> **هدف این سند:** هر سایت تازه از روز اول در گوگل، بینگ و دستیارهای هوش مصنوعی (ChatGPT، Gemini، Copilot، Perplexity، Claude) پیدا و نقل شود؛ با تنظیم‌های فنی درست و بدون ترفندهای بی‌اثر.
> **موضوع تحقیق:** robots.txt و ربات‌های هوش مصنوعی، sitemap و lastmod، IndexNow، hreflang، داده‌ی ساختاریافته، llms.txt، کنترل ویژگی‌های هوش مصنوعی، اندازه‌گیری، سایتی که هنوز آدرس واقعی ندارد، IndexNow روی سایت پویا.
> **منابع:** [S51 سئوی فنی و جستجوی هوش مصنوعی](../../../sources/README.md#s51) · [S13 Core Web Vitals](../../../sources/README.md#s13) · [S62 DNS، ایمیل و سئو برای سرور خودمان](../../../sources/README.md#s62) · [S139 انتشار یک پروژه‌ی واقعی](../../../sources/README.md#s139) · [S190 WebMCP](../../../sources/README.md#s190)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۰
> **دفعه‌ی بعد چک شود:** نام ربات‌های تازه‌ی OpenAI، Anthropic، Perplexity، Apple و Google؛ تغییر نتایج ویژه‌ی گوگل (FAQ در مه ۲۰۲۶ حذف شد)؛ اینکه موتور بزرگی خواندن llms.txt را اعلام کند؛ گزارش‌های هوش مصنوعی Search Console و Bing.

این سند حاصل اجرای واقعی روی سایت یک پروژه‌ی واقعی است (دفتر پروژه‌ها): SEO ۱۰۰ در Lighthouse، ۶۰ صفحه شناخته‌شده در Search Console، ۳ نتیجه‌ی معتبر در Rich Results Test. 🔬

---

## هر موتور جوابش را از کجا می‌آورد

| موتور | ربات جستجو | منبع جواب زنده | راه معرفی سایت |
|---|---|---|---|
| ChatGPT | ✅ `OAI-SearchBot` (بستنش سایت را از جستجوی ChatGPT بیرون می‌برد)؛ `ChatGPT-User`؛ `GPTBot` فقط آموزش | ✅ نمایه‌ی خودش + Bing | ندارد؛ در Bing بودن مهم است 🧭 |
| Google AI Overviews / AI Mode / Gemini | ✅ `Googlebot`؛ `Google-Extended` فقط آموزش Gemini و روی Search اثری ندارد | ✅ نمایه‌ی گوگل + Business Profile | Google Search Console |
| Microsoft Copilot | ✅ `Bingbot` | ✅ نمایه‌ی Bing | Bing Webmaster Tools + IndexNow |
| Claude | ✅ `Claude-SearchBot`، `Claude-User`؛ `ClaudeBot` فقط آموزش. نام‌های قدیمی `Claude-Web` و `anthropic-ai` در فهرست فعلی نیستند | ❓ شواهد غیررسمی می‌گوید Brave Search | ندارد |
| Perplexity | ✅ `PerplexityBot`، `Perplexity-User` | نمایه‌ی خودش | ندارد |
| Apple (Siri، Spotlight) | ✅ `Applebot`؛ `Applebot-Extended` فقط آموزش مدل. داده‌ی `Applebot` برای جواب هوش مصنوعی Siri هم استفاده می‌شود؛ برای جلوگیری از آن `nosnippet` لازم است (https://support.apple.com/en-us/119829) | نمایه‌ی اپل + Apple Business Connect | Apple Business Connect |

🧭 نتیجه: برای دیده شدن در همه، **Search Console + Bing Webmaster Tools + IndexNow + Google Business Profile** کافی است. هیچ «نشانه‌گذاری ویژه‌ی هوش مصنوعی» لازم نیست؛ ✅ گوگل صریح می‌گوید همان اصول عادی سئو کافی است.

---

## ۱. robots.txt

✅ قانون‌های مهم (مشخصات گوگل):
- هر ربات **فقط دقیق‌ترین گروهی** را که اسمش را آورده اجرا می‌کند؛ گروه نام‌دار با گروه `*` جمع نمی‌شود. پس `Disallow`های مشترک (مثل `/admin/` و `/api/`) را **در هر گروه نام‌دار تکرار کن**.
- طولانی‌ترین مسیر برنده است؛ در تساوی، کم‌محدودیت‌تر.
- حداکثر ۵۰۰ کیلوبایت؛ تا ۲۴ ساعت کش می‌شود؛ `crawl-delay` نادیده گرفته می‌شود.

✅ **Content-Signal** (پیشنهاد Cloudflare) داخل گروه `*`، مثلاً `Content-Signal: search=yes, ai-input=yes, ai-train=no`. فقط توصیه است؛ هیچ شرکتی متعهد به رعایتش نشده.
🔬 LHCI 0.15.1 این خط را «دستور ناشناخته» می‌داند و امتیاز SEO را از ۱۰۰ به ۹۲ می‌رساند. ✅ علتش این است که LHCI 0.15.1 (آخرین نسخه) هنوز Lighthouse 12.6.1 را همراه دارد؛ خود Lighthouse از نسخه‌ی 13.1.0 `content-signal` را در فهرست مجاز گذاشته (https://github.com/GoogleChrome/lighthouse/blob/main/core/audits/seo/robots-txt.js). پس PageSpeed Insights و Lighthouse تازه خطا نمی‌گیرند و فقط LHCI می‌گیرد. اگر همه‌ی مقدارها `yes` است (همان پیش‌فرض)، خط را نگذار؛ فقط وقتی می‌خواهی چیزی را `no` کنی ارزش دارد.

⚠️ ✅ اگر در Cloudflare «Managed robots.txt» یا AI Crawl Control روشن باشد، قانون‌های خود Cloudflare **قبل از** قانون‌های تو می‌نشیند. چک کن ربات‌های جستجوی هوش مصنوعی را نبسته باشد.

🧭 الگوی پیشنهادی: ربات‌های جستجو و جواب هوش مصنوعی همه باز؛ ربات‌های آموزش طبق تصمیم صاحب سایت (باز یا `Disallow: /`).

## ۲. sitemap و lastmod

- ✅ گوگل `<lastmod>` را فقط وقتی استفاده می‌کند که «پیوسته و قابل‌تأیید دقیق» باشد؛ `priority` و `changefreq` را نادیده می‌گیرد. سقف: ۵۰ مگابایت یا ۵۰٬۰۰۰ آدرس.
- ✅ Bing می‌گوید lastmod نشانه‌ی کلیدی تازگی برای جواب‌های هوش مصنوعی است؛ تاریخ و ساعت ISO 8601، **زمان واقعی تغییر، نه زمان build**.
- 🔬 روش ما در یک پروژه‌ی واقعی: هنگام build از محتوای هر صفحه اثر انگشت گرفته می‌شود و فقط وقتی محتوا عوض شد تاریخ جلو می‌رود (فایل `lastmod.json` در Git). همین تاریخ در `dateModified` داده‌ی ساختاریافته هم می‌نشیند.

## ۳. IndexNow

- ✅ کلید ۸ تا ۱۲۸ کاراکتر (`a-z A-Z 0-9 -`) در فایل `https://دامنه/{key}.txt`. ارسال: `POST https://api.indexnow.org/indexnow` با JSON شامل `host`، `key`، `keyLocation`، `urlList` (تا ۱۰٬۰۰۰ آدرس). پاسخ ۲۰۰ یعنی قبول؛ ۲۰۲ یعنی «بررسی کلید در انتظار» و هنوز قبول کامل نیست (https://www.indexnow.org/documentation). ✅ گوگل در فهرست موتورهای عضو نیست (https://www.indexnow.org/searchengines.json).
- ✅ به Bing، Yandex، Naver، Seznam و Yep می‌رسد (گوگل عضو نیست).
- 🔬 (یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۲) اولین ارسال **چند ثانیه بعد از انتشار** فایل کلید، از `api.indexnow.org` جواب ۴۰۳ (کلید نامعتبر) گرفت؛ همان لحظه `GET https://www.bing.com/indexnow?url=…&key=…` جواب ۲۰۰ داد و ارسال دوباره‌ی همان ۱۰۶۳ آدرس هم ۲۰۰ شد. پس ۴۰۳ بلافاصله بعد از انتشار را «دوباره بفرست» بدان، نه «کلید خراب است». در همان پروژه lastmod با اثر انگشت محتوا (بدون نام فایل‌های هش‌دار Astro) در ساخت دوم «۰ تغییر» داد.
- ✅ فقط آدرس‌های **تغییرکرده** را بفرست.
- ✅ Cloudflare **Crawler Hints** خودکار IndexNow می‌فرستد ([کارت Cloudflare Pages](../../../catalog/cloudflare-pages.md)).
- 🔬 در یک پروژه‌ی واقعی: یک اسکریپت کوچک بعد از هر انتشار آدرس‌هایی را می‌فرستد که lastmod آن‌ها از دفعه‌ی قبل عوض شده؛ بار اول همه‌ی ۶۰ آدرس با پاسخ ۲۰۲.
- **سایت پویا (محتوا از پنل مدیریت، نه از build):** ✅ فایل کلید می‌تواند نام دیگری داشته باشد، به شرط اینکه در هر ارسال با `keyLocation` اعلام شود؛ ولی آن فایل فقط آدرس‌های **زیر پوشه‌ی خودش** را پوشش می‌دهد و مستندات ریشه‌ی سایت را توصیه می‌کند. ✅ ۲۰۰ فقط یعنی «رسید»، نه «نمایه شد»؛ ۴۰۳ کلید نامعتبر، ۴۲۲ آدرس مال این میزبان نیست، ۴۲۹ ارسال زیاد (شاید اسپم). 🧭 کار زمان‌بندی‌شده (مثلاً هر ۶ ساعت) از sitemap آدرس‌هایی را بفرستد که تازه‌اند یا تاریخشان عوض شده، فهرست ارسال‌شده را با تاریخ نگه دارد، ۲۰۰ و ۲۰۲ را «رسیده» بداند و بقیه را دفعه‌ی بعد دوباره بفرستد. 🔬 یک فروشگاه واقعی همین را ساخت و با آزمون واحد سنجید (دفتر پروژه‌ها). ❓ هنوز از دامنه‌ی زنده ارسال نشده.

## ۴. سایت چندزبانه (hreflang)

✅ در sitemap، در HTML یا در هدر HTTP؛ هر سه معادل‌اند. اگر بیش از یکی استفاده شد باید **دقیقاً یکسان** باشند. هر صفحه به خودش و همه‌ی نسخه‌های دیگر لینک بدهد (دوطرفه) و `x-default` داشته باشد.

🔬 در Next.js 16، `alternates` گذاشته‌شده در layout به همه‌ی صفحه‌ها ارث می‌رسد؛ hreflang و canonical را در هر صفحه بساز ([Next.js](../../../catalog/nextjs.md#csp-و-metadata-در-nextjs-16)).

## ۵. داده‌ی ساختاریافته (JSON-LD)

| نوع | چه بگذاریم | نکته |
|---|---|---|
| LocalBusiness (یا زیرنوع مثل HomeAndConstructionBusiness) | ✅ لازم: `name`، `address` با `addressCountry`. پیشنهادی: `geo`، `telephone`، `url`، `openingHoursSpecification`، `priceRange` (کمتر از ۱۰۰ کاراکتر)، `image`؛ برای Organization: `logo` حداقل ۱۱۲ پیکسل، `sameAs` | `sameAs` فقط به پروفایل‌هایی که **واقعاً وجود دارند** |
| Service + Offer / UnitPriceSpecification | ✅ معتبر در schema.org (`minPrice`، `maxPrice`، `priceCurrency` مثل AED، `unitCode` مثل `MTK` برای متر مربع) | ✅ نتیجه‌ی ویژه‌ی گوگل ندارد؛ ارزشش شفافیت برای Bing و مدل‌های زبانی است. خدمت را **Product** علامت نزن |
| FAQPage | ✅ هنوز معتبر، فقط برای پرسش و پاسخِ **دیده‌شدنی** در صفحه | ✅ نتیجه‌ی ویژه‌ی FAQ را گوگل در مه ۲۰۲۶ حذف کرد؛ HowTo در ۲۰۲۳ |
| Review / AggregateRating | ⛔ برای کسب‌وکاری که نظرهای خودش را کنترل می‌کند | ✅ گوگل این را «خودستایی» می‌داند؛ نظرها را در Business Profile جمع کن |
| GovernmentService | ⛔ برای مرکز **خصوصی** که کار دولتی را برای مشتری انجام می‌دهد | ✅ schema.org آن را «خدمتی که یک سازمان دولتی ارائه می‌دهد» تعریف می‌کند. 🧭 به‌جایش LocalBusiness (یا ProfessionalService) + Service؛ نام اداره را در متن بیاور، نه به‌عنوان ارائه‌دهنده |
| WebPage با `dateModified` | 🧭 تاریخ واقعی تغییر، هماهنگ با lastmod | |

✅ گوگل: داده‌ی ساختاریافته باید با متن دیده‌شدنی صفحه یکی باشد.

🔬 روش ما: قیمت‌ها از پنل مدیریت در یک جا نگه داشته می‌شوند و هم در جدول دیده‌شدنی صفحه، هم در Offer داده‌ی ساختاریافته و هم در llms.txt از همان منبع ساخته می‌شوند؛ پس هرگز با هم اختلاف ندارند.

## ۶. محتوایی که نقل می‌شود 🧭

- هر صفحه‌ی خدمت با **یک پاراگراف جواب مستقیم** شروع شود: چه کسی، چه چیزی، کجا، حدود قیمت
- جدول قیمت، مشخصات، ضمانت و مناطق خدمت به‌صورت **متن و جدول دیده‌شدنی**، نه داخل تب، تصویر یا PDF (✅ توصیه‌ی مایکروسافت برای Copilot)
- پرسش‌های متداول واقعی، به زبان بومی هر بازار
- صفحه‌ی «درباره‌ی ما»، مجوز، پروژه‌های واقعی با نام محل
- ذکر نام کسب‌وکار در جاهای دیگر: دایرکتوری‌ها، شبکه‌های اجتماعی، مطبوعات

## ۶٫۵. «AEO» و «GEO» در برابر منبع اصلی
✅ (Google، https://developers.google.com/search/docs/appearance/ai-features، به‌روز ۲۰۲۵-۱۲-۱۰) برای AI Overviews و AI Mode «نه شرط اضافه‌ای هست و نه بهینه‌سازی ویژه‌ای لازم است». شرط فنی فقط این است که صفحه نمایه شود و بتواند با snippet نمایش داده شود. فایل متنی هوش مصنوعی، markup یا داده‌ی ساختاریافته‌ی خاص لازم نیست. 🧭 پس «AEO و GEO» نام تازه‌ی همین سئوی خوب است؛ برای پست‌هایی که چیز دیگری وعده می‌دهند، دسته‌ی ۱۷ را ببین.

## ۷. llms.txt

✅ قالب llmstxt.org: `# نام`، `> خلاصه`، متن اختیاری، بخش‌های `##` با فهرست لینک، بخش `## Optional`. ✅ گوگل: «نه کمک می‌کند نه ضرر». 🧭 ارزان است؛ اگر می‌سازی، خودکار از همان محتوای سایت بساز تا با صفحه‌ها اختلاف پیدا نکند.

## ۸. کنترل ویژگی‌های هوش مصنوعی

- ✅ گوگل: صفحه باید نمایه‌شده و قابل‌نمایش در snippet باشد. `nosnippet`، `max-snippet` و `noindex` ویژگی‌های هوش مصنوعی را هم محدود می‌کنند.
- ✅ Bing: `noarchive` محتوا را از جواب‌های چت Bing بیرون می‌برد؛ `nocache` فقط آدرس، عنوان و خلاصه را نشان می‌دهد؛ اگر هر دو باشد، `nocache` حساب می‌شود. ❓ منبع از ۲۰۲۳ است و نام «Bing Chat» دارد، نه Copilot.
- 🧭 در صفحه‌های عمومی هیچ‌کدام را نگذار.
- ✅ ([S190](../../../sources/README.md#s190)) **WebMCP (آمادگی برای عامل مرورگر):** استاندارد پیشنهادی که سایت با آن ابزارهای خودش (مثل جستجو یا فرم) را به عامل هوش مصنوعی داخل مرورگر عرضه می‌کند. آزمایش مبدأ از Chrome 149؛ برای آزمون محلی پرچم `chrome://flags/#enable-webmcp-testing`. مشخصات: https://github.com/webmachinelearning/webmcp · راهنما: https://developer.chrome.com/docs/ai/webmcp (به‌روزرسانی ۲۰۲۶-۱۰-۰۷). 🧭 هنوز استاندارد نهایی نیست؛ برای سایت مشتری لازم نیست، فقط زیر نظر بماند.

## ۹. ثبت و اندازه‌گیری

1. **Google Search Console** با ویژگی Domain (تأیید با رکورد TXT در DNS) و ارسال sitemap.
2. **Bing Webmaster Tools** (می‌تواند از Search Console وارد کند؛ تأیید با CNAME هم ممکن است) و ارسال sitemap. ✅ گزارش «AI Performance» (پیش‌نمایش عمومی) نقل‌قول‌های Copilot، خلاصه‌های هوش مصنوعی Bing و چند شریک را یکجا نشان می‌دهد، نه جدا (https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview).
3. **IndexNow** و Crawler Hints.
4. **Google Business Profile** برای جستجوی محلی ([سئوی محلی](local-business-profile.md)).
5. در GA4 یک گروه کانال «AI assistants» بالاتر از Referral با الگوی منبع `chatgpt|openai|perplexity|claude|gemini|copilot|…` 🧭
6. در فرم تماس بپرس «از کجا با ما آشنا شدید؟» و گزینه‌ی «ChatGPT یا دستیار هوش مصنوعی» را بگذار؛ منبع اولین بازدید (referrer، utm، صفحه‌ی ورود) را همراه فرم بفرست. 🔬
7. ماهانه همان سؤال‌های مشتری را به زبان‌های بازار از ChatGPT، Gemini، Copilot، Perplexity و Claude بپرس و ببین نام کسب‌وکار می‌آید یا نه. 🧭

## ۹٫۵. ChatGPT و نمایه‌ی بینگ 🔬
(یک پروژه‌ی واقعی، ۲۰۲۶-۱۰-۲۲؛ [S139](../../../sources/README.md#s139))
- یک روز پس از ارسال به Bing، `site:example.com` هیچ صفحه‌ی خودی نشان نداد ← ChatGPT برای سایتی که در Bing نیست جواب نمی‌دهد. IndexNow دوباره ارسال شد (۱٬۰۸۹ آدرس، پاسخ ۲۰۰ = فقط رسید). صبر چند روزه + آدرس را مستقیم به ChatGPT بده.
- ریدایرکت زبان فقط با جاوااسکریپت برای خواننده‌ی بدون اسکریپت (ChatGPT) صفحه‌ی خالی بود ← یک **Pages Function روی `/`** با `302` بر اساس `Accept-Language` و هدر `Vary: Accept-Language`؛ بعدش ChatGPT سایت را خواند.
- ❓ پیش‌فرض Cloudflare برای «block AI bots» در منطقه‌های تازه با توکن Pages-deploy قابل بررسی نبود؛ در داشبورد ببین ([Bing](../../../catalog/bing-webmaster-tools.md)، [IndexNow](../../../catalog/indexnow.md)).

## ۱۰. سایتی که هنوز آدرس واقعی ندارد

وقتی سایت روی سرور آزمایشی، IP یا `localhost` اجرا می‌شود و دامنه‌ی واقعی HTTPS هنوز وصل نیست:

- 🔬 یک تابع (`indexable()`) فقط وقتی «بله» بگوید که آدرس عمومی واقعی `https` تنظیم شده و حالت دمو خاموش است. تا آن روز: همه‌ی صفحه‌ها `noindex`، robots.txt با `Disallow: /`، sitemap خالی، و فایل کلید IndexNow و llms.txt جواب ۴۰۴. پس هیچ نسخه‌ی آزمایشی وارد نمایه نمی‌شود (دفتر پروژه‌ها).
- ⚠️ ✅ گوگل: `noindex` فقط وقتی کار می‌کند که robots.txt صفحه را **نبسته** باشد؛ ربات باید صفحه را بخواند تا `noindex` را ببیند. 🧭 پس `Disallow: /` فقط برای نسخه‌ای است که هیچ لینک بیرونی ندارد؛ روز انتشار **اول** `Disallow` را بردار.
- ✅ هدر `X-Robots-Tag: noindex` برای پاسخ‌های غیر HTML (PDF، تصویر، API) هم کار می‌کند. 🔬 در یک فروشگاه واقعی روی پنل مدیریت، پورتال مشتری، صفحه‌های ورود و ثبت‌نام و همه‌ی `/api` از `headers()` در `next.config` گذاشته شد.
- 🔬 ✅ صفحه‌ی ورود (`/login`) را در robots.txt **نبند**: `noindex` آن باید خوانده شود؛ اگر بسته باشد، آدرسش ممکن است بدون محتوا در نتایج بماند.

---

## پرامپت

```text
Set up technical SEO and AI-search visibility for this site. Follow
~/Desktop/knowledge-library/domains/website/09-seo/seo-and-ai-search.md:
robots.txt with named groups for search, AI-answer and AI-training bots (repeat shared
Disallows in every group); add a Content-Signal line only if one of its values is "no"
(Lighthouse flags it as an unknown directive); sitemap with hreflang and a real
per-page lastmod based on a content fingerprint; an IndexNow key file and a script that
submits only changed URLs; JSON-LD LocalBusiness, Service with Offer prices, FAQPage only
for visible Q&A, BreadcrumbList, WebPage dateModified; no self-serving review markup; an
llms.txt generated from the same content. Keep prices in one source so the page table,
the JSON-LD and llms.txt never disagree. Validate with Rich Results Test and Lighthouse.
```

## Search Console و ردیابی خزنده‌ی AI (۲۰۲۶-۱۰-۲۸)
- 🧭 Search Console (اعلام ۲۰۲۶-۰۹-۲۴) جستجوی متنی را از جستجوی چندوجهی (Lens، Circle to Search) جدا گزارش می‌کند. اگر کالای ما با عکس پیدا می‌شود، گزارش چندوجهی را جدا ببین. فقط پوشش ثانویه خوانده شد (https://developers.google.com/search/blog).
- 👀 [GEOInflow](../../../catalog/geoinflow.md) (MIT) بازدید خزنده‌های AI را ردیابی می‌کند. هنوز آزموده نشده.

منبع: [S191](../../../sources/README.md#s191).
