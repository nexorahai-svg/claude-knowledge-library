---
name: Data Dubai
slug: data-dubai
category: data-documents
domains: [website, apps]
verdict: trial
status: researched
summary: درگاه داده‌ی باز دولت دبی؛ فهرست رسمی فعالیت‌های تجاری DET از آن با خواندن عادی سرور در یک پروژه‌ی واقعی گرفته شد.
use_when: "need the official Dubai business activity list ; refreshing a licence or activity catalogue monthly ; need Dubai government open data instead of scraping a protected site"
how: "Dataset 460355 at https://data.dubai/en/l/460355; read metadata from the server with plain fetch, validate every row, accept odd codes with a flag and apply nothing when validation blocks; read the licence first; never bypass Akamai on Invest in Dubai."
url: https://data.dubai/
repo: ""
license: "Open Data License of Data Dubai"
pricing: free
risk: low
sources: [S219]
found_in: [project-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Data Dubai

## چیست
✅ صفحه‌ی [مجموعه‌ی Business Activities](https://data.dubai/en/l/460355) روی درگاه داده‌ی دبی باز می‌شود و متن مجوز و بخش API دارد. 🔬 یک پروژه آن را از سرور با fetch عادی خواند: ۷٬۷۷۸ ردیف، ۲٬۶۱۶ کد یکتا، حدود ۱۵ ثانیه.

## کی استفاده کنیم
برای فهرست رسمی فعالیت‌های تجاری و داده‌ی باز دبی، به‌جای خواندن سایت‌های محافظت‌شده.

## قیمت و مجوز
🔬 خواندن همین مجموعه کلید نخواست؛ API رسمی بدون کلید 401 داد. ✅ مجوز باز صفحه: جهانی، رایگان و غیرانحصاری، برای استفاده‌ی تجاری و غیرتجاری. شامل حق شخص ثالث، نشان تجاری، تصویر و داده‌ی شخصی نیست؛ ارائه‌ی گمراه‌کننده ممنوع است و نقض مجوز حق استفاده را لغو می‌کند. ✅ بند ۳ (https://data.dubai/en/l/460355، ۲۰۲۶-۱۱-۰۱): منبع را نام ببر، اعلان حق نشر را نگه دار و در صورت امکان لینک بده؛ نام دولت دبی را به کار نبر و کار را دولتی جلوه نده؛ داده‌ی ترجمه یا تغییریافته (Adapted Material) باید با همین مجوز در دسترس باشد، ولی محصول مستقل نه؛ فروش محصول و داده‌ی تغییریافته مجاز است، فروش خود داده‌ی اصلی نه؛ شرط تازه بر استفاده‌کننده‌ی بعدی نگذار.

## ریسک و هشدار
- 🔬 نشانی متادیتایی که پروژه گزارش کرد در آزمون بدون پارامتر ما 404 داد؛ مسیر و پارامتر را از مستند پروژه یا خود صفحه بگیر.
- 🔬 سه کد هفت‌رقمی نبودند (`311003`، `20001.1`، `20002.2`) و regex سخت کل خواندن را متوقف کرد. آن‌ها را بپذیر، علامت بزن و هرگز تعمیر نکن.
- 🔬 اختلاف اول ۱٬۴۸۴ مورد بود، ولی ۱٬۰۰۳ تای آن فقط فهرست‌شدن اضافه زیر گروه «CDA activities» بود. خلاصه‌ی هوش مصنوعی آن را جابجایی گمراه‌کننده نشان داد؛ این موارد را جدا کن.
- 🔬 Invest in Dubai پشت Akamai است و fetch و Chrome بدون رابط پاسخ Access Denied گرفتند. دور نزن؛ داده‌ی باز را بخوان و جزئیات را مسدود علامت بزن.

## مرتبط
[داده‌ی فروشگاه](../domains/website/04-tech/online-store-data.md) · [ارسال و قانون امارات](../domains/website/04-tech/uae-shipping-and-rules.md)
