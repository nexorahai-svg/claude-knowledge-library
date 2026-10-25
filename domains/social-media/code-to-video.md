# ویدیو و موشن با کد

> **نوع سند:** دستورالعمل
> **هدف این سند:** ساختن ویدیوی لانچ، دموی محصول، ویدیوی هیرو و کلیپ شبکه‌های اجتماعی با Claude Code: Claude برنامه می‌نویسد، مرورگر فریم می‌گیرد، FFmpeg ویدیو می‌سازد.
> **موضوع تحقیق:** روشی که پشت ویدیوهای «یک‌پرامپتی» منتشرشده در X بود، ابزارهای آن (Remotion، HyperFrames، Playwright، FFmpeg) و مجوزهایشان.
> **منابع:** [S30 Remotion و کتابخانه‌ها](../../sources/README.md#s30) · [S31 روش، Playwright، FFmpeg و مخزن‌های نمونه](../../sources/README.md#s31) · [S32 ابزارهای هوش مصنوعی ویدیو](../../sources/README.md#s32) · [S56 راهنماهای PDF ویدیو و عامل](../../sources/README.md#s56) · [S58 واقعیت‌های ابزار](../../sources/README.md#s58) · [S100 ده مخزن موج Opus 5.5](../../sources/README.md#s100)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۴
> **دفعه‌ی بعد چک شود:** مجوز Remotion (نسخه‌ی ۵ تغییراتی دارد)؛ نسخه‌ی ۱.۰ HyperFrames؛ وضعیت Claude Motion؛ قیمت و شرایط Seedance.

---

## اصل اول: Claude ویدیو نمی‌سازد، برنامه می‌سازد

✅ (مقاله‌های P04 و P12، و مخزن‌های نمونه) Claude فایل MP4 تولید نمی‌کند. هر ویدیوی «ساخته‌شده با Claude» در واقع **برنامه‌ای است که هر فریم را بر اساس زمان می‌کشد**؛ یک مرورگر بدون رابط هر فریم را عکس می‌گیرد و FFmpeg عکس‌ها را به ویدیو تبدیل می‌کند.

✅ «یک پرامپت» افسانه است: بهترین نمونه‌ها بریف چند هزار کاراکتری، پوشه‌ی skill، و اجرای چندساعته با چند دور بازبینی داشتند. (مخزن PDoomVideo: دو نسل کار؛ ClaudeAnimationBase: تست‌شده روی effort بالا.)

**کجا کد برنده است** 🧭: ویدیوی محصول، حرکت رابط کاربری، تایپوگرافی متحرک، داستان با داده، توضیح‌دهنده‌ی لانچ.
**کجا کد کم می‌آورد** 🧭: صحنه‌ی واقع‌گرایانه، کاراکتر پیچیده، حرکت ارگانیک → فیلم واقعی یا مدل ویدیو.

---

## سه مسیر

🧭 مسیر کامل کار، از آماده‌سازی تا تحویل، با ترکیب پیشنهادی ابزارها: [ساخت کلیپ با Claude](claude-clip-pipeline.md).

| مسیر | کی | مجوز | حکم |
|---|---|---|---|
| **HTML خالص + Playwright + FFmpeg** | ساده‌ترین؛ بدون فریم‌ورک؛ پیش‌فرض خود Claude اگر چیزی مشخص نکنی | همه آزاد | ✅ [Playwright](../../catalog/playwright.md)، [FFmpeg](../../catalog/ffmpeg.md) |
| **[HyperFrames](../../catalog/hyperframes.md)** (HeyGen) | HTML به MP4 قطعی، بدون React، افزونه‌ی Claude Code | Apache-2.0 | 🧪 (اول اسکریپت‌ها را بخوان) |
| **[Remotion](../../catalog/remotion.md)** | پروژه‌ی React؛ ویدیوهای تکراری با داده‌ی متغیر؛ رندر ابری | رایگان برای فرد و شرکت تا ۳ نفر | ✅ |

✅ طبق مقاله‌ی P04 (از قول یک کاربر): اگر فریم‌ورک را نام نبری، Claude معمولاً مسیر بدون وابستگی (یک فایل HTML، Playwright، FFmpeg) را انتخاب می‌کند، حتی اگر Remotion نصب باشد. ❓ این مشاهده‌ی یک نفر است، نه مستند رسمی.

**ابزار رسمی Anthropic:** ✅ «Claude Motion» (بتا، فقط Team و Enterprise) انیمیشن را با کد می‌سازد و MP4 خروجی می‌دهد: https://support.claude.com/en/articles/17454997-get-started-with-claude-motion. ❓ در دسترس بودنش در Claude Code گفته نشده.

---

## قانون‌های فنی

| # | قانون | چرا |
|---|---|---|
| ۱ | **هر فریم تابع خالص زمان است** (`draw(t)`) | فریم ۲۴۰ بدون اجرای فریم‌های قبلی کشیده شود؛ فریم‌ها موازی و بی‌ترتیب رندر شوند ✅ (راهنمای PDoomVideo) |
| ۲ | **بدون عدد تصادفی؛ به‌جایش hash ثابت** | هر بار همان نتیجه ✅ |
| ۳ | **بدون تایمر، `setTimeout` و transition خود CSS** | این‌ها به ساعت واقعی وابسته‌اند، نه به `t` ✅ (مقاله‌ی P09 درباره‌ی Remotion: فقط `useCurrentFrame()`) |
| ۴ | **کد قدیمی با requestAnimationFrame؟** Clock API | ✅ `page.clock.install()` و `runFor(1000/60)` در Playwright زمان را قدم‌به‌قدم جلو می‌برد |
| ۵ | **اسکرین‌شات، نه ضبط ویدیو** | ✅ `recordVideo` در Playwright فریم‌به‌فریم دقیق نیست |
| ۶ | **حرکت فنری بسته (closed-form)** | حس طبیعی و باز هم تابع خالص زمان 🧭 |
| ۷ | **صدا روی همان ساعت تصویر** | تغییر حالت روی ضرب، لحظه‌ی مهم روی ضرب قوی 🧭 |
| ۸ | **همه‌ی نسبت‌ها از یک تایم‌لاین** | عمودی، مربعی و افقی هر کدام چیدمان خودشان؛ نه برش 🧭 |
| ۹ | **فقط دارایی واقعی محصول** | Claude می‌تواند حرکت دوربین بسازد، ولی هرگز نباید داشبورد یا محصول تو را از خودش اختراع کند 🧭 |

🔬 (Sun Shade DXB، دفتر پروژه‌ها، [S108](../../sources/README.md#s108)) انیمیشن سه‌بعدی ورود لوگو: صفحه‌ی Three.js با `window.renderAt(t)` که هندسه را در هر فریم از نو می‌سازد، Chromium headless روی کارت گرافیک (پرچم‌ها در [لوگو و برند](../website/02-design/logo-and-brand.md))، اسکرین‌شات هر فریم: ۳۳۱ فریم ۱۹۲۰×۱۰۸۰ در حدود ۵۸ ثانیه، MP4 حدود ۱٫۵ مگابایت. برگه‌ی فریم‌ها پیش از تحویل چهار ایراد واقعی نشان داد (دایره‌ی تیره‌ی خورشید پیش از طلوع، دو جرقه‌ی هم‌زمان، هم‌پوشانی نام با لوگو، بیرون زدن خورشید از کنار بادبان).

**«حالت ضبط» در خود صفحه** ✅ (الگو از دموی Code and Chill، [S121](../../sources/README.md#s121)): صفحه‌ای که قرار است از آن ریل ساخته شود، با یک پارامتر آدرس (مثل `?record`) به حالت ضبط می‌رود. در این حالت تم و تنظیمات ذخیره‌شده‌ی بیننده نادیده گرفته می‌شوند، صفحه تا آماده شدن ابزار ضبط صبر می‌کند و همیشه از یک حالت ثابت شروع می‌شود. 🧭 همین الگو را با قانون‌های بالا (`draw(t)` و اسکرین‌شات هر فریم) ترکیب کن؛ ابزار ضبط خود آن سازنده دیده نشد ❓.

**دستور FFmpeg** ✅:
```bash
ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -pix_fmt yuv420p out.mp4
```

---

## روش کار (از مقاله‌های P04، P09، P12، بازنویسی ما)

1. **بریف تولید، نه «یک ویدیوی خفن»:** هدف، مخاطب، طول، نسبت تصویر، دارایی‌های واقعی، صدا، حس، و نمونه‌ی مرجع. پرامپت کوتاه یعنی Claude هر جای خالی را با پیش‌فرض امن پر می‌کند (همان تیتر گرادیانت وسط‌چین).
2. **مرجع برای «دستور زبان بصری»، نه برای کپی:** یک فریم یا کلیپ کوتاه از سبکی که دوست داری، یا کارهای قبلی خودت.
3. **فهرست حالت‌ها:** هر نما یک حالت ورود، یک حالت خروج و یک دلیل برای بودن. اگر Claude نتواند بگوید نمای چهارم چرا هست، حذفش کن.
4. **تایم‌لاین با شماره‌ی فریم قبل از رندر** (P09).
5. **بازبینی با تصویر ثابت قبل از رندر کامل:** ۳ فریم کلیدی، بعد برگه‌ی فریم‌ها (contact sheet) با FFmpeg. ✅ Claude از تصویر متحرک فقط فریم اول را می‌بیند؛ همیشه عکس ثابت بده.
6. **منتقد:** Claude برگه‌ی فریم‌های خودش را نمره می‌دهد و ۳ ایراد بدتر را درست می‌کند (متن روی هم، لغزش به‌جای نرمی، تایپوگرافی تار، لحظه‌ی مرده، پرش در نقطه‌ی حلقه).
7. **اصلاح دقیق:** کجا، چه ایرادی، چه تغییری، چه چیزی ثابت بماند (P09).
8. **نظر دوم از یک جلسه‌ی تازه** (P09).
9. **بسته‌بندی در skill:** بریف، رندرکننده و چک‌لیست بازبینی در فایل بمانند تا ویدیوی دهم بهتر از اول باشد.
10. **کار طولانی با «دروازه»:** اجرای چندساعته بدون حضور تو فقط با توقف در نقاط مشخص (دارایی گم‌شده → توقف و سؤال، نه جعل).

🧭 **تقسیم کار بین زیرعامل‌ها** (درس PDoomVideo): Claude یک ANIMATION_GUIDE.md و STORYBOARD.md می‌نویسد؛ هر فصل مال یک زیرعامل است و فایل‌های مشترک فقط‌خواندنی‌اند. هزینه را در نظر بگیر ([هزینه و کارایی](../claude-code/cost-efficiency.md)).

---

## ویدیوی توضیحی سه‌بعدی با صدای فارسی

الگوهایی از یک راهنمای PDF فارسی ([S56](../../sources/README.md#s56)) که با منبع اصلی چک شد و با روش بالا ترکیب شد. متن آن راهنما کپی نشده است.

**ترتیب کار:** صدا اول، تصویر بعد. 🧭 اول متن روایت تأیید می‌شود و صدا ساخته می‌شود؛ بعد هر ضرب تصویر و هر زیرنویس روی زمان واقعی صدا قفل می‌شود.

| قدم | روش | برچسب |
|---|---|---|
| راهنمای سبک | ویدیوی مرجع را فریم‌به‌فریم (مثلاً هر نیم ثانیه) در برگه‌ی فریم ببین و یک «راهنمای سبک» بنویس: ساختار داستان با ثانیه، سرعت گفتار، نماها، نور، معنای رنگ‌ها، سبک متن، صدا، و اینکه چرا بیننده می‌ماند. آن را **در فایل پروژه ذخیره کن** تا هر ویدیوی بعدی در یک گفت‌وگوی تازه از همان شروع شود | 🧭 |
| متن روایت | فارسی محاوره‌ای؛ حدود ۲.۳ تا ۲.۶ کلمه در ثانیه برای فارسی (۶۰ ثانیه حدود ۱۴۰ تا ۱۵۵ کلمه)؛ **عدد را با حروف بنویس** تا گوینده درست بخواند؛ نام برند با حروف لاتین؛ هر واقعیت با منبع | 🧭 (عدد سرعت از نویسنده‌ی راهنما، آزموده نشد) |
| صدا | ElevenLabs فقط در مدل‌های v3 و v4 فارسی دارد؛ Multilingual v2 و Flash v2.5 ندارند ([صداگذاری](ai-voice.md#elevenlabs)) | ✅ |
| زمان کلمه‌ها | Whisper یا [faster-whisper](../../catalog/faster-whisper.md) برای زمان، ولی **متن زیرنویس همیشه متن خودمان است**: زمان‌ها کلمه‌به‌کلمه با متن تأییدشده هم‌تراز شود، نه املای Whisper ([زیرنویس](captions-and-copy.md)) | 🧭 |
| صحنه‌ی سه‌بعدی | یک صفحه‌ی HTML با WebGL2 یا [Three.js](../../catalog/threejs.md) ([سه‌بعدی](../../domains/website/03-motion-3d/3d-webgl.md))؛ پیش از رندر کامل ۶ تا ۸ تصویر ثابت با زیرنویس فارسی برای تأیید | 🧭 |
| رندر روی کارت گرافیک | «صفحه‌ی رندر» در Chrome که با WebCodecs فریم‌ها را رمزگذاری و MP4 ذخیره می‌کند؛ خیلی سریع‌تر از اسکرین‌شات تک‌تک فریم‌ها. ✅ VideoEncoder در Chrome و Edge از ۹۴، Safari از ۱۶.۴، Firefox دسکتاپ از ۱۳۰. ⚠️ کتابخانه‌ی mp4-muxer منسوخ است (5.2.2، «جایش Mediabunny»)؛ به‌جایش [Mediabunny](../../catalog/mediabunny.md) | ✅ |
| لایه‌ی متن جدا | زیرنویس، برچسب و کارت پایانی جدا به‌صورت فریم PNG شفاف با Playwright ساخته و روی ویدیو گذاشته شود. شکل‌دهی فارسی کار مرورگر است و برای زبان دیگر فقط این لایه عوض می‌شود | 🧭 |
| صدا و افکت | افکت آرام روی ضرب‌ها و موسیقی که زیر صدای گوینده پایین می‌رود. ❓ عدد −۱۴ LUFS رایج است ولی YouTube آن را رسماً اعلام نکرده | 🧭 |
| تحویل | ترکیب با [FFmpeg](../../catalog/ffmpeg.md) (H.264، AAC)؛ برگه‌ی فریم برای هماهنگی، متن راست‌به‌چپ، حروف چسبیده، رقم‌ها و فریم اول | 🧭 |

**قانون‌های سبک قابل‌استفاده** 🧭: فریم اول همان صحنه است (نه سیاهی یا محو شدن)؛ هر رنگ یک معنای ثابت دارد (مثلاً مشکل، فناوری، موفقیت، هشدار)؛ زیرنویس کارائوکه حدود ۴ کلمه با برجسته شدن کل کلمه؛ برچسب به شیء سه‌بعدی چسبیده؛ ۳ تا ۴ کارت عدد بزرگ برای واقعیت‌های کلیدی؛ در متن فارسی فاصله‌ی حروف صفر، هیچ‌وقت حرف تکی را متحرک نکن، نیم‌فاصله و رقم فارسی حفظ شود.

**قالب‌گذاری درخواست** (از الگوی قالب موشن‌گرافیک در [S56](../../sources/README.md#s56)) 🧭: مرجع فقط برای کیفیت و دستور زبان بصری، نه کپی؛ مدت، نسبت، رزولوشن، زبان، فونت، موسیقی و افکت صریح؛ و **تنوع** در سرعت، اندازه، ترکیب، حرکت دوربین، تایپوگرافی و نوع گذار تا انیمیشن تکراری نشود.

**درباره‌ی ادعاهای آن راهنما** ✅: «فقط در Claude دسکتاپ با حالت Cowork» درست نیست. Cowork در طرح‌های پولی هست ([S58](../../sources/README.md#s58))، ولی همین کار در [Claude Code](../claude-code/README.md) هم انجام می‌شود. ادعای «گفت‌وگوی معمولی Claude کد اجرا نمی‌کند و فایل نمی‌سازد» هم غلط است: اجرای کد و ساخت فایل برای همه‌ی کاربران، حتی رایگان، هست. رندر ویدیوی کامل و دسترسی به پوشه‌ی پروژه ولی محیطی مثل Claude Code یا Cowork می‌خواهد.

⚠️ **فونت:** فونت یکان‌بخ که آن راهنما پیشنهاد می‌کند پولی است (فونت‌ایران). خرید آن خروجی گرافیکی و ویدیو را پوشش می‌دهد، ولی گذاشتنش روی سایت مجوز جدا لازم دارد ([کارت](../../catalog/yekan-bakh.md)). فونت رایگان: [فارسی و RTL](../website/02-design/persian-rtl.md).

---

## پرامپت‌ها

### شروع ویدیو
```text
Make a [length]-second [aspect ratio] video for [product/site]. Use plain HTML + Canvas/SVG
with no framework unless I say otherwise. Every frame must be a pure function of time
draw(t): no Math.random (use a seeded hash), no timers, no CSS transitions. Use only the
real assets in [folder]; if something is missing, stop and ask instead of inventing it.

Before writing code: give me a production brief, a shot list where each shot has an entry
state, an exit state and a reason, and a frame-numbered timeline. Wait for my approval.
Then render three key stills and show them to me before rendering the full video.
Encode with: ffmpeg -framerate 60 -i frame_%05d.png -c:v libx264 -pix_fmt yuv420p out.mp4
```

### بازبینی
```text
Build a contact sheet of every 15th frame with ffmpeg and look at it. Score the video out of
10 on readability, motion quality, pacing and loop seam. List the three worst problems
(overlapping text, sliding instead of easing, blurry type, dead beats, a jump at the loop
point) and fix only those. Show me the new contact sheet.
```

### ویدیوی توضیحی سه‌بعدی (صدا اول)
```text
We are making a [length]-second [9:16 or 16:9] 3D explainer in Persian about [topic], in the
style described in our saved style-guide.md. Work one stage at a time and wait for my
approval after each: (1) a spoken-Persian script at about 2.5 words per second, numbers
written as words, brand names in Latin letters, every fact with its source; (2) after I
give you the voice-over file, word timings from faster-whisper aligned word by word to MY
script (show my words, never the transcription's spelling); (3) a WebGL scene and 6-8
preview stills with the Persian captions in our font; (4) a Chrome render page that encodes
the 3D layer with WebCodecs + Mediabunny on my GPU; (5) captions and labels as a separate
transparent PNG layer rendered with Playwright (dir="rtl", letter-spacing 0, keep ZWNJ,
Persian digits); (6) the ffmpeg composite and a contact sheet checking sync, RTL shaping,
digits and the first frame. Vary speed, scale, composition, camera and transitions.
```

---

## مجوزها در یک نگاه

| ابزار | مجوز | نکته |
|---|---|---|
| Remotion | ✅ منبع‌باز، رایگان برای فرد و شرکت تا ۳ نفر | تحویل فایل نهایی به مشتری کارمندان مشتری را حساب نمی‌کند |
| HyperFrames | ✅ Apache-2.0 | پیش از ۱.۰ |
| Playwright | ✅ Apache-2.0 | |
| FFmpeg | ✅ LGPL (بخش‌هایی GPL) | فقط برای توزیع نرم‌افزار مهم است |
| ClaudeAnimationBase | ✅ MIT | کاراکتر Clawd: برند را بررسی کن |
| PDoomVideo | ⛔ بدون مجوز | فقط مطالعه |
| Seedance 2.5 | ❓ شرایط BytePlus | خروجی رسمی با واترمارک |
| VoiceStudio | ⛔ مدل پیش‌فرض غیرتجاری | برای صدا: [صداگذاری](ai-voice.md) |
| mp4-muxer | ⛔ منسوخ | جایش Mediabunny (MPL-2.0) |
| یکان‌بخ | ✅ پولی | ویدیو با خرید فونت؛ سایت مجوز جدا |

---

## فاصله‌ی ادعای پست‌ها با واقعیت

- ✅ پست «۱۰ مخزن موج Opus 5.5» از @yarad_ai (غربال ۰۹) نگفت که سه مخزن **مجوز ندارند** (PDoomVideo، claude-opus-5-5-demo، shipvideo)، [shipvideo](../../catalog/shipvideo.md) فقط روی سکوی پولی سازنده (OpenComputer) کار می‌کند، و [Awesome Opus 5.5 Videos](../../catalog/awesome-opus5-5-videos.md) قیف ترافیک سایت Skillry است. قابل‌استفاده: [Lemo Opuscar](../../catalog/lemo-opuscar.md) 🧪 (MIT، فیلم‌ها CC BY 4.0).

- ✅ «PDoomVideo حدود ۱.۱ هزار ستاره»: الان ۲٬۱۶۶؛ ولی **بدون مجوز**، پس فقط برای مطالعه.
- ✅ پلاگین Scenario برای Blender «تیم سه‌بعدی متن‌باز» نیست؛ افزونه‌ی GPL برای **سرویس پولی** Scenario است ([کارت](../../catalog/scenario-blender.md)).
- ✅ anatomy-reveal «مدل سه‌بعدی واقعی از عکس» نمی‌سازد؛ تصویر ایزومتریک سبک‌دار ساخته‌شده با کد است ([کارت](../../catalog/anatomy-reveal.md)).
- ✅ VoiceStudio «جایگزین رایگان ElevenLabs» برای کار تجاری نیست؛ وزن‌های موتور پیش‌فرض غیرتجاری‌اند ([کارت](../../catalog/voicestudio.md)).
- ✅ ادعای «ویدیو با یک پرامپت» با خود مخزن‌ها و مقاله‌ها رد می‌شود: بریف بلند، چند نسل و بازبینی.

## تجربه‌ی دست‌اول: رندرهای بلند HyperFrames و زیرنویس نستعلیق 🔬

- رندر ۹۰ ثانیه تا ۵ دقیقه با کلیپ‌های ۱۰۸۰ زیاد: `/tmp` (tmpfs ۱۶ گیگ) پر می‌شود ← `TMPDIR` و `--frames-cache-dir` روی `/data`؛ کمبود heap ← `NODE_OPTIONS=--max-old-space-size=12288` و `--workers 3`؛ فریم jpg شکست می‌خورد، png کار می‌کند؛ پردازش‌های یتیم Chrome را بکُش؛ در نگهبان RAM از الگوی `'[h]yperframes render'` استفاده کن. جزئیات: [HyperFrames](../../catalog/hyperframes.md).
- 🔬 کلیپ استوک را پیش از چیدن با ffmpeg بُرش بده و کند کن ([FFmpeg](../../catalog/ffmpeg.md)).
- 🔬 فونت نستعلیق: [IranNastaliq](../../catalog/irannastaliq.md) نه Noto Nastaliq Urdu. تصویرهای کوچک تاریخی ([Wikimedia Commons](../../catalog/wikimedia-commons.md)) را به‌شکل چاپِ قاب‌دار روی نسخه‌ی تار و با Ken-Burns بگذار؛ ویدیوی استوک از [Mixkit](../../catalog/mixkit.md).
- 🔬 هم‌ترازی زیرنویس: [روش نویسه‌به‌نویسه در faster-whisper](../../catalog/faster-whisper.md).
- 🔬 موسیقی با کد (numpy، مالکیت کامل): ambient مراقبه‌ای (درون، پدهای کند، پیانوی کم‌نت، هوا) و موسیقی احساسی که با بخش‌های متن عوض می‌شود (پیانو، ویولن‌سل، زهی). میکس و loudnorm در [FFmpeg](../../catalog/ffmpeg.md).
- 🔬 انیمیشن شخصیت با SVG کد رد شد؛ [Google Flow](../../catalog/google-flow.md). [S151](../../sources/README.md#s151)
