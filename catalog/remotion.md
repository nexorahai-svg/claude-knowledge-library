---
name: Remotion
slug: remotion
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: ساخت ویدیو با React؛ رایگان برای فرد، شرکت تا ۳ نفر و غیرانتفاعی
use_when: "making launch, product demo or social videos in a React project ; repeated videos with variable data"
how: "claude plugin marketplace add remotion-dev/claude-code-plugin then claude plugin install remotion@remotion; each frame is a function of useCurrentFrame(); free only for individuals and companies up to 3 employees, re-read licence; Persian captions need a multilingual model"
url: https://www.remotion.dev
repo: "https://github.com/remotion-dev/remotion"
license: "مجوز Remotion (منبع‌باز، نه متن‌باز OSI)"
pricing: freemium
risk: low
sources: [S30, S85]
found_in: [batch-01/P08, batch-01/P09, batch-01/P24]
last_checked: 2026-10-31
next_check: "2026-11-29"
---

# Remotion

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۲۸) نسخه‌ی 4.0.539 (۲۰۲۶-۱۰-۲۶؛ npm latest همان)؛ مجوز Remotion بی‌تغییر (کپی‌رایت ۲۰۲۶)؛ Remotion 5 هنوز منتشر نشده (PR #3750 باز؛ npm alpha 4.1.0-alpha12)؛ پیش از ارتقا به ۵ مجوز را دوباره بخوان.
✅ فریم‌ورک React برای ساخت ویدیو با کد؛ هر صحنه یک کامپوننت و هر فریم تابع `useCurrentFrame()`. رندر با CLI یا Lambda. نسخه‌ی 4.0.538 (۲۰۲۶-۱۰-۲۲)، حدود ۶۴.۶ هزار ستاره.

## دستور سریع

**نصب** (✅ README مخزن و [مستند ارتقا](https://www.remotion.dev/docs/upgrading): `^` را بردار تا نسخه‌ی همه‌ی بسته‌های `@remotion/*` یکی بماند؛ آخرین `4.0.539`):
```bash
npx create-video@latest                                   # ساخت پروژه
npm install --save-exact remotion@4.0.539 @remotion/cli@4.0.539
claude plugin marketplace add remotion-dev/claude-code-plugin && claude plugin install remotion@remotion   # ✅ افزونه‌ی رسمی (در کارت)
```
**حداقل اجرا** (✅ [مستند render](https://www.remotion.dev/docs/cli/render)):
```bash
npx remotion render src/index.ts MyComp out/video.mp4 --concurrency 2
```
**تنظیم‌های مهم**
- ✅ `--concurrency` عدد یا درصد است (`50%`)؛ `npx remotion benchmark` بهترین مقدار را پیدا می‌کند. 🧭 روی رایانه‌ی تحت فشار swap با `2` شروع کن و با محافظ منابع (`scripts/resource_guard.py run --mem 8G --`) اجرا کن.
- ✅ `--crf` (کمتر = کیفیت بیشتر، هر کدک بازه‌ی خودش را دارد؛ ۲۳ برای H264 خوب است ولی برای WebM بد)، `--codec h264` پیش‌فرض است.
- ✅ `--scale` وضوح را کم می‌کند و رندر را سریع‌تر؛ `--image-format=png` کندتر از jpeg است ولی برای ویدیوی شفاف لازم.

**خطاهای رایج**
- ✅ مجوز: رایگان تا ۳ کارمند؛ بالاتر مجوز شرکتی می‌خواهد (بخش «قیمت و مجوز» همین کارت). ⚠️ ورژن ۵ مجوز را عوض می‌کند.
- ✅ WebGL و CSS سنگین (`blur`، سایه‌ی بزرگ) روی رندر کند هستند؛ `--gl=swiftshader` گزینه‌ی رندر نرم‌افزاری است.
- ✅ برای ویدیو `<Video>` از `@remotion/media` را بگیر؛ `<OffthreadVideo>` و `<Html5Video>` بهینه نیستند.
- ✅ زیرنویس فارسی: مدل رونویسی چندزبانه لازم است، `medium.en` فقط انگلیسی است.

## کی استفاده کنیم
🧭 ویدیوی لانچ، دموی محصول، ویدیوی شبکه‌های اجتماعی، وقتی پروژه React است یا ویدیوهای تکراری با داده‌ی متغیر لازم داری. مهارت‌های رسمی: [Remotion Skills](remotion-skills.md).

## قیمت و مجوز
✅ (LICENSE.md و صفحه‌ی FAQ) **رایگان، حتی تجاری** برای: فرد، شرکت انتفاعی **تا ۳ کارمند**، سازمان غیرانتفاعی. ✅ اگر مشتری فقط **فایل ویدیوی نهایی** را می‌گیرد، کارمندان مشتری حساب نمی‌شوند؛ اگر مشتری پروژه‌ی Remotion را مالک یا اداره کند، تعداد هر دو جمع می‌شود. ✅ فروش ویدیوهای ساخته‌شده مجاز است؛ فروش خود Remotion (یا نسخه‌ی تغییریافته) ممنوع. ✅ مجوز شرکتی (۴ نفر به بالا): Creators ۲۵ دلار برای هر نفر در ماه؛ Automators ۰.۰۱ دلار برای هر رندر با حداقل ۱۰۰ دلار در ماه؛ Enterprise از ۵۰۰ دلار.

## ریسک و هشدار
کم برای فرد. ⚠️ اگر کسی را استخدام کردی یا با استودیوی دیگری روی همان پروژه کار کردی، تعداد نفرات جمع می‌شود؛ مجوز را دوباره بخوان. نسخه‌ی ۵ تغییراتی در مجوز دارد.

## بازبینی ۲۰۲۶-۱۰-۱۸
✅ (در این بازبینی نسخه 4.0.538 بود؛ نسخه‌ی فعلی بالای کارت است) مجوز رایگان: فرد، شرکت انتفاعی تا ۳ نفر (کل کارکنان شرکت، نه فقط کاربران Remotion)، غیرانتفاعی. بیشتر: Creators ۲۵ دلار برای هر نفر در ماه یا Automators یک سنت برای هر رندر با حداقل ۱۰۰ دلار در ماه. ⚠️ Remotion 5.0 (PR #3750، هنوز باز) پیمانکارها را هم می‌شمارد.
✅ افزونه‌ی رسمی Claude Code: `claude plugin marketplace add remotion-dev/claude-code-plugin` و `claude plugin install remotion@remotion`. FFmpeg 7.1 همراه است (GPLv2+). زیرنویس `@remotion/captions` (MIT)؛ ⚠️ مثال رونویسی `medium.en` فقط انگلیسی است؛ برای فارسی مدل چندزبانه.

## مرتبط
[ویدیو با کد](../domains/social-media/code-to-video.md) · [S30](../sources/README.md#s30) · [ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S85](../sources/README.md#s85)
