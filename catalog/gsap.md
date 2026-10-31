---
name: GSAP
slug: gsap
category: animation
domains: [website, social-media]
verdict: adopt
status: researched
summary: کتابخانه‌ی انیمیشن وب: تایم‌لاین، اسکرول (ScrollTrigger)، تیتر خط‌به‌خط (SplitText)
use_when: "scroll-driven animation, element entrances, pinned sections or complex timelines ; per-line heading animation with SplitText"
how: "npm install gsap (all plugins incl. ScrollTrigger and SplitText are free, commercial use ok) or load a pinned version from the official CDN; pair with Lenis for smooth scroll; also install gsap-skills"
url: https://gsap.com/
repo: "https://github.com/greensock/GSAP"
license: "Standard No Charge License (رایگان، تجاری مجاز)"
pricing: free
risk: low
sources: [S04]
found_in: [batch-01/P24]
last_checked: 2026-10-31
next_check: "2027-01-14"
---

# GSAP

## چیست
✅ استانداردترین کتابخانه‌ی انیمیشن وب. از وقتی Webflow پشتیبانش شد، **کل کتابخانه و همه‌ی پلاگین‌ها** (ScrollTrigger، SplitText، MorphSVG، ScrollSmoother، DrawSVG…) رایگان است، حتی تجاری.

## دستور سریع
✅ ([gsap.com/docs/v3/Installation](https://gsap.com/docs/v3/Installation/)، npm: gsap 3.15.0؛ از 3.13 به بعد همه‌ی پلاگین‌ها از npm رایگان‌اند، مجوز Standard No Charge):
```bash
npm install gsap          # در React: npm install @gsap/react
```
```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
gsap.from(".card", { y: 40, opacity: 0, stagger: 0.1, scrollTrigger: { trigger: ".card", start: "top 80%" } });
```
✅ تنظیم‌های مهم: همیشه `gsap.registerPlugin(...)` (وگرنه ابزار build ممکن است پلاگین را حذف کند)؛ برای کاهش حرکت و موبایل/دسکتاپ `gsap.matchMedia()` که انیمیشن‌ها را هنگام عوض شدن شرط خودکار برمی‌گرداند؛ `scrub`، `pin`، `markers: true` در توسعه؛ نسخه را قفل کن یا از CDN رسمی با نسخه‌ی مشخص بخوان.
خطاهای رایج: در React از `useGSAP()` (`@gsap/react`) با `{ scope: ref }` استفاده کن تا انیمیشن‌ها و ScrollTriggerها هنگام unmount برگردند. 🧭 پس از تغییری که چیدمان را عوض می‌کند (مثل بارگذاری فونت یا تصویر) `ScrollTrigger.refresh()` موقعیت‌ها را دوباره حساب می‌کند ([docs](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)). برای پلاگین‌های رایگان (SplitText، ScrollSmoother و ...) نسخه‌ی 3.13 یا بالاتر لازم است (مستندات نصب). مهارت‌های رسمی: [GSAP Skills](gsap-skills.md).
💲 رایگان برای همه، شامل تجاری ([gsap.com/pricing](https://gsap.com/pricing/)).

## کی استفاده کنیم
انیمیشن وابسته به اسکرول، ورود عناصر، سکشن چسبان، صحنه‌های پیچیده. با Lenis برای اسکرول نرم.

## قیمت و مجوز
✅ رایگان برای همه، شامل پروژه‌ی تجاری. منبع: https://gsap.com/pricing/

## ریسک و هشدار
کم. فقط از npm یا CDN رسمی با نسخه‌ی مشخص بارگذاری کن.

✅ مهارت‌های رسمی GSAP برای Claude: [GSAP Skills](gsap-skills.md).

## مرتبط
[حرکت و انیمیشن](../domains/website/03-motion-3d/motion-animation.md) · [S04](../sources/README.md#s04)
