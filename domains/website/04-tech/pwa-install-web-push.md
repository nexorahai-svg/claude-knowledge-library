# نصب پنل روی گوشی (PWA) و اعلان Web Push بدون کتابخانه

> **نوع سند:** دستورالعمل
> **هدف این سند:** یک سایت بتواند چند «اپ» نصب‌شدنی (مثلاً پنل مشتری و پنل تیم) داشته باشد، کارت راهنمای نصب برای اندروید و آیفون نشان دهد و اعلان گوشی بفرستد، بدون وابستگی به بسته‌ی قدیمی.
> **موضوع تحقیق:** معیارهای نصب Chrome، رفتار iOS 26 و Safari، Web Push روی iOS، استاندارد VAPID و رمزنگاری پیام.
> **منابع:** [S201 نصب PWA و Web Push](../../../sources/README.md#s201)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۳۰
> **دفعه‌ی بعد چک شود:** رفتار «Open as Web App» در iOS 26 و نسخه‌های بعد؛ پشتیبانی Chrome از payload اعلام‌شده؛ نسخه‌ی تازه‌ی بسته‌ی `web-push`.

🔬 الگو در یک پروژه‌ی واقعی ساخته و ۲۰۲۶-۱۰-۲۹ آزموده شد.

## ۱. چند اپ نصب‌شدنی روی یک سایت
- 🔬 هر پنل manifest جدا و `id` پایدار دارد (پنل مشتری `/app`، پنل تیم `/admin`).
- 🔬 مسیر manifest باید نقطه داشته باشد (مثلاً `/manifest-app.webmanifest?lang=xx`)؛ وگرنه middleware زبان با استثنای `.*\..*` آن را ریدایرکت می‌کند.
- 🔬 `screenshots` (form_factor باریک، ۷۸۰×۱۶۸۸) و `description` برگه‌ی نصب بزرگ Chrome را می‌دهند.

## ۲. کارت نصب
- ✅ اندروید و Chrome/Edge دسکتاپ: رویداد `beforeinstallprompt` را نگه دار و `prompt()` را فقط از یک لمس صدا بزن (web.dev، آموزش installation-prompt). کارت را با `appinstalled` و `display-mode: standalone` پنهان کن.
- ✅ آیفون و آیپد API نصب ندارند: راهنمای Share ← Add to Home Screen ← Add را نشان بده. iOS 26: هر سایت افزوده‌شده پیش‌فرض اپ وب باز می‌شود (کلید «Open as Web App»، heise)؛ iOS 16.4 تا 18 هنوز `display: standalone` یا `apple-mobile-web-app-capable` می‌خواهند. 🧭 دقت جزئیات نسخه‌ها را روی دستگاه واقعی چک کن.
- ✅ اپ نصب‌شده‌ی iOS ذخیره‌ی جدا از Safari دارد؛ کاربر باید داخل اپ دوباره وارد شود.
- 🔬 مرورگرهای درون‌برنامه‌ای (UA شامل `Instagram|FBAN|FBAV|Line/|WhatsApp|Telegram|; wv)`) نصب نمی‌کنند: «باز کردن در مرورگر» و کپی لینک بده.
- 🔬 «بعداً» = ۱۴ روز در localStorage.

## ۳. Web Push با node:crypto (حدود ۱۵۰ خط)
- 🔬 بسته‌ی npm `web-push` نسخه‌ی ۳٫۶٫۷ است و آخرین انتشارش ۲۰۲۴-۰۱-۱۶ (`npm view`، ۲۰۲۶-۱۰-۲۹). نوشتن مستقیم شدنی است.
- 🔬 VAPID (RFC 8292): JWT با ES256 از `crypto.sign` با `dsaEncoding: "ieee-p1363"`، کلید به‌صورت JWK.
- 🔬 رمزنگاری پیام RFC 8291/8188 (aes128gcm): ECDH روی P-256، HKDF با `crypto.hkdfSync`، اندازه‌ی رکورد ۴۰۹۶، جداکننده‌ی padding برابر 0x02. آزمون: پیام را با کلیدهای سمت مرورگر رمزگشایی کن.
- 🔬 اشتراک را روی پاسخ 401/403/404/410 حذف کن.
- ✅ iOS اشتراک را بعد از سه push بی‌اعلان رها می‌کند (وب‌کیت)؛ پس `showNotification` همیشه داخل `event.waitUntil`.
- ✅ payload اعلامی `{"web_push":8030,"notification":{title,body,navigate,lang,dir}}` را Safari 18.4+ حتی بدون service worker نشان می‌دهد (وب‌کیت، declarative web push)؛ 🔬 Chrome نادیده می‌گیرد.
- 🔬 `Notification.requestPermission()` را اول از همه در handler لمس صدا بزن (`await` قبلش حرکت کاربر را در iOS از دست می‌دهد).
- 🔬 در آزمون `"PushManager" in window` وقتی stub بشود هم true است؛ با `typeof window.PushManager === "function"` بسنج.

## ۴. آزمون passkey و PWA نصب‌شده روی گوشی واقعی در شبکه‌ی محلی 🔬
(یک پروژه‌ی Next.js، ۲۰۲۶-۱۰-۳۰)
- 🔬 WebAuthn به **نام دامنه** (rpId) نیاز دارد نه IP. راه: سرور برنامه فقط روی `127.0.0.1:3101` (کدهای دمو فقط برای loopback مجازند؛ حالت `--lan` آن‌ها را برای همه با `demo_local_only` رد می‌کند)، پراکسی HTTPS ۴۰ خطی node روی `0.0.0.0:3443` با گواهی mkcert برای `192-168-70-152.nip.io` (DNS عمومی که به IP شبکه‌ی محلی می‌رسد)، CA ریشه روی http ساده (پورت ۳۴۴۴) فقط برای نصب یک‌باره روی گوشی. پراکسی `x-forwarded-proto: https` می‌گذارد و `Host` را عوض نمی‌کند.
- 🔬 متغیرهای برنامه: `MARIO_ALLOWED_HOSTS`، `MARIO_ALLOWED_ORIGINS=https://…nip.io:3443`، `MARIO_RP_ID`، `COOKIE_SECURE=1`. نتیجه: `/fa/login` از راه پراکسی ۲۰۰، `/api/auth/otp` کد دمو داد (با `--lan` مستقیم ۴۰۳)، گواهی mkcert تا ۲۰۲۹-۰۱-۳۰ معتبر؛ ۸۴ عکس صفحه‌ی گوشی با Playwright روی loopback گرفته شد. گوشی واقعی در این گزارش نصب نشد؛ آن بخش ❓.
- 🔬 **شیت پایین با ورودی تاریخچه (۲۰۲۶-۱۰-۳۱):** اگر شیتی که دکمه‌ی Back اندروید را می‌گیرد درست پیش از `router.push` بسته شود، پاک‌سازی آن با `history.back()` ناوبری را برمی‌گرداند و صفحه روی همان کارت می‌ماند. شیت را باز بگذار و `router.replace` بزن. در اپ next-intl هم از مسیریاب زبان‌دار پروژه استفاده کن، نه `useRouter` از `next/navigation`.
- 🔬 **دکمه‌ی ارسال کنار کادر متن روی گوشی (۲۰۲۶-۱۰-۳۱):** فشردن دکمه کادر را از فوکوس درمی‌آورد، نوار پایین که هنگام فوکوس پنهان بود برمی‌گردد، چیدمان جابه‌جا می‌شود و `mousedown` و `mouseup` روی دو عنصر می‌افتند؛ پس `click` اصلاً اجرا نمی‌شود و پیام نمی‌رود. راه‌حل: `preventDefault` در `onMouseDown` دکمه‌های کنار کادر، که صفحه‌کلید را هم باز نگه می‌دارد. با کلیک واقعی بیازما، نه `requestSubmit()`. برای جدا کردن منطق از رسیدن رویداد، `click` را با `requestSubmit()` مقایسه کن و `elementFromPoint` را ببین.
- 🔬 **آزمون خودکار کامل passkey با Playwright:** احراز هویت مجازی CDP (`WebAuthn.enable` و `addVirtualAuthenticator` با ctap2/internal، کلید مقیم، UV و `automaticPresenceSimulation`) ثبت، ورود، فهرست و حذف را بدون دستگاه واقعی اجرا کرد (۳ از ۳ در ۶٫۷ ثانیه). سه دام:
  - rpId اجباری برای آزمون گوشی (مثلاً نشانی nip.io) مبدأ `localhost` را بیرون می‌اندازد. در حالت توسعه، rpId را از روی مبدأ هر درخواست انتخاب کن.
  - `locator.isVisible({timeout})` صبر نمی‌کند و همان لحظه برمی‌گردد؛ `waitFor({state:'visible'})` را به‌کار ببر.
  - بعد از حذف کلید، `signalUnknownCredential` آن را از احراز هویت مجازی هم پاک می‌کند، پس ورود بعدی با `NotAllowedError` تمام می‌شود نه پیام سرور. آزمون باید هر دو را بپذیرد.

## ۵. تصحیح‌های پژوهش اپ موبایل (۲۰۲۶-۱۰-۳۰)
- ✅ **vaul نگهداری نمی‌شود:** README خودش می‌گوید «This repo is unmaintained» ([مخزن](https://github.com/emilkowalski/vaul)). جایگزین: `Drawer` در `@base-ui/react` (نسخه‌ی ۱٫۹٫۰ در صفحه‌ی رسمی؛ بستن با کشیدن، `snapPoints`، `Drawer.SwipeArea`؛ پشتیبانی RTL در صفحه نیامده ← ❓ جداگانه بیازما): https://base-ui.com/react/components/drawer
- ✅ **WebOTP** فقط انتقال `sms` را مستند کرده، آزمایشی است، فقط HTTPS؛ Chrome پشتیبان است و Safari کامل نه (با `autocomplete="one-time-code"` پیشنهاد پر کردن می‌دهد): https://developer.mozilla.org/en-US/docs/Web/API/WebOTP_API . پس پروژه‌ی بی‌پیامک از آن سودی نمی‌برد.
- ✅ iOS 26 (وب‌کیت): هر سایت افزوده به Home Screen به‌طور پیش‌فرض اپ وب باز می‌شود، کاربر می‌تواند «Open as Web App» را خاموش کند: https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/
- ❓ (گزارش پژوهشگر پروژه، منبع رسمی در این بازبینی بازخوانی نشد): کد یک‌ضرب/بدون‌لمس واتساپ فقط برای اپ بومی اندروید؛ push از iOS 16.4 ولی بدون اعلان نصب، Background Sync، Share Target و ارتعاش؛ `<ViewTransition>` در React 19.3 پایدار ولی پرچم Next.js هنوز آزمایشی؛ راهنمای TDRA (ناوبری پایین ۳ تا ۵ مورد، آفلاین بی‌صفحه‌ی خالی و بی‌واژه‌ی Error، نظرسنجی پس از هر خدمت)؛ رد Apple 4.2 برای وب‌سایت بسته‌بندی‌شده؛ Bubblewrap 1.27 برای TWA در Play (۱ تا ۳ روز). فهرست منبع‌ها در `docs/mobile-app/research-market-and-pwa-tech.md` پروژه است.

## مرتبط## مرتبط
[بررسی خودکار](../../claude-code/verification.md) · [ورود مشتری](customer-auth.md)
