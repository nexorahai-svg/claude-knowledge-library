---
name: Void (VoidZero)
slug: void
category: hosting-deploy
domains: [website]
verdict: assess
status: researched
summary: SDK و CLI متن‌باز MIT برای ساخت و استقرار اپ تمام‌پشته‌ی Vite روی Cloudflare Workers (مسیر API فایل‌محور، دیتابیس، AI)؛ مالک: Cloudflare؛ نسخه‌ی ۱٫۳٫۰
use_when: "a Vite site needs a small API and database on Cloudflare without a separate backend ; one-command provision and deploy of a Vite app to Cloudflare Workers"
how: "After deploy verify with curl, a success message can still serve an empty 404; check which Cloudflare account the browser is on before login; Trial first on a small task: try only on a throwaway Vite project with npm install -D void and npx void init, pin the version (1.4.0 latest; our tests were on 1.3.0), read the quickstart at void.cloud first, and check Iran access to the deployed Workers domain"
url: https://github.com/voidzero-dev/void
repo: "https://github.com/voidzero-dev/void"
license: "MIT"
pricing: freemium
risk: medium
sources: [S191]
found_in: [sweep-2026-10-28]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# Void (VoidZero)

## چیست
✅ (جاروی ۲۰۲۶-۱۰-۳۱) نسخه‌ی v1.4.0 (۲۰۲۶-۱۰-۳۰؛ npm 1.4.0، MIT): گزینه‌ی `routing.alwaysUseHttps`، رفع از دست رفتن Set-Cookie در dev، نشت توکن `void auth` به پلتفرم دیگر، نادیده گرفته شدن `maxRetries` صف و شکست نخستین deploy کلادفلر وقتی secret از قبل تنظیم شده. چیز شکننده‌ای دیده نشد. تجربه‌های 🔬 این کارت روی 1.3.0 است: https://github.com/voidzero-dev/void/releases/tag/v1.4.0
- ✅ مخزن MIT، حدود ۶۱۰ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۸. release فعال: `v1.3.0` در ۲۰۲۶-۱۰-۲۷ (قبلی‌ها ۱٫۲٫۱ و ۱٫۲٫۰ در ۲۰۲۶-۱۰-۲۲)؛ بسته‌ی npm با نام `void` نسخه‌ی ۱٫۳٫۰، مجوز MIT و بدون postinstall (رجیستری npm): https://github.com/voidzero-dev/void
- ✅ فایل LICENSE: «Copyright 2026-present, Cloudflare, Inc.» و پست رسمی Cloudflare (۲۰۲۶-۱۰-۱۵) آن را معرفی کرده است: https://blog.cloudflare.com/deploy-with-void/ . (قبلاً در کارت «هنوز release ندارد» بود؛ اکنون اشتباه است.)
- ✅ سه بخش (README): Void SDK (مسیرهای API فایل‌محور، صفحه‌ی سمت سرور، API تایپ‌شده برای دیتابیس، ذخیره‌سازی و AI)، Void CLI (build، ساخت منابع Cloudflare، migration، استقرار، لاگ، برگشت) و Void Platform (محیط استقرار مشترک در حساب Cloudflare خودت). با React، Vue، Svelte یا Solid کار می‌کند.
- ✅ شروع سریع: Node 24.21 یا بالاتر؛ `npm install -D void` سپس `npx void init`، `npm run dev` و `npx void deploy`. `void init` فایل `AGENTS.md` می‌افزاید و skillهای همراه را به عامل‌های شناخته‌شده پیوند می‌دهد.
- ❓ پایداری بلندمدت و کیفیت مستندات؛ آزموده نشد.

## کی استفاده کنیم
- 🧭 حکم ۲۰۲۶-۱۰-۲۸ با تأیید کاربر به 🧪 آزمایش کن رسید؛ دامنه‌ی آزمون: one throwaway Vite project pinned to 1.3.0. تا نتیجه‌ی واقعی در projects/README.md ثبت نشده، 🔬 نیست.
- 🧭 وب‌سایتی با Vite که API و دیتابیس کوچک روی Cloudflare می‌خواهد. مقایسه با [Cloudflare Pages](cloudflare-pages.md) و [Vite](vite.md) در [تمام‌پشته‌ی Cloudflare](../domains/website/04-tech/cloudflare-full-stack.md). برای اپ موبایل یا محتوا مناسب نیست.

## قیمت و مجوز
- ✅ SDK و CLI رایگان و MIT: https://github.com/voidzero-dev/void/blob/main/LICENSE
- ✅ هزینه‌ی واقعی از Cloudflare است: Workers رایگان تا ۱۰۰٬۰۰۰ درخواست در روز و ۱۰ میلی‌ثانیه CPU هر فراخوانی؛ طرح پولی از ۵ دلار در ماه: https://developers.cloudflare.com/workers/platform/pricing/

## ریسک و هشدار
- ✅ استقرار منابع را در حساب Cloudflare خودت می‌سازد؛ با حساب آزمایشی شروع کن. توکن‌ها را در مخزن نگذار.
- 🧭 خیلی نو (چند هفته)؛ نسخه را پین کن. دسترسی از ایران به دامنه‌های Workers جدا سنجیده شود.

## پیشنهاد ارتقا
- 🧭 trial: رسمی (Cloudflare)، MIT، release منظم؛ پیشنهاد آزمون روی یک پروژه‌ی Vite آزمایشی.

## آزمون دست‌اول (۲۰۲۶-۱۰-۲۹) 🔬
- 🔬 روی پروژه‌ی دورریختنی React + Vite: `npm install -D void@1.3.0` سپس `npx void init --deploy none --no-git`؛ `voidPlugin()` به vite.config.ts و `void.config.ts` و `.void/tsconfig.json` افزوده شد؛ بیرون از پوشه چیزی تغییر نکرد.
- 🔬 `npm run dev` (Node 24.22.1) صفحه را با ۲۰۰ داد؛ API محلی Cloudflare (`/cdn-cgi/local/explorer/api`) هم بالا آمد.
- ⚠️ npm 11 اسکریپت‌های postinstall `esbuild` و `workerd` را مسدود کرد؛ dev بی آن‌ها کار کرد.
- ⚠️ `void init` بی پرچم دیتابیس یک پرسش تعاملی (D1، PostgreSQL، MySQL، بدون دیتابیس) می‌دهد؛ برای اجرای بی‌پرسش `--starter` را بدهید.
- ❓ آزموده نشد: مسیر API فایل‌محور، دیتابیس، `void deploy` و باز شدن دامنه‌ی Workers از ایران (استقرار بدون تأیید کاربر انجام نشد).

## آزمون استقرار ۲۰۲۶-۱۰-۳۰ 🔬
- 🔬 روی Debian 13 (Node 24.22.1، npm 11، create-vite 9.3.3، void 1.3.0، cf 1.0.0-beta.18): `npx void init --deploy cloudflare --no-git` پیکربندی را نوشت، ولی `npx void deploy --platform cloudflare` با «Cloudflare authentication is required» ایستاد (۰ از ۱) و `npx void cloudflare login` ۲ از ۲ بار شکست: روی لینوکس برای ذخیره در keyring به `secret-tool` (بسته‌ی `libsecret-tools`، نیاز به `sudo apt-get install`) نیاز دارد که نصب نبود.
- 🔬 `CLOUDFLARE_AUTH_USE_KEYRING=false` و `env -u` تغییری نداد؛ `npx cf auth login --no-use-keyring` را `cf` با «Unknown arguments» رد کرد، هرچند پیام خطا همین پرچم را پیشنهاد می‌کند. ❓ راه جایگزین (متغیر محیطی API token با دسترسی Workers) آزموده نشد؛ مخزن هم موردی درباره‌ی این خطا در جست‌وجوی issueها نشان نداد.
- 🔬 (۲۰۲۶-۱۰-۳۰، void 1.3.0، cf 1.0.0-beta.18، wrangler 4.154.0) با `secret-tool` 0.21.7 ورود درست شد و راه‌حل قفل کلید همین است. ولی ⚠️ **deploy «موفق» سایت کارگر نداد:** `npx void deploy --platform cloudflare` دو بار از دو نسخه Successfully deployed گفت و لاگ `ok=true` بود، اما نشانی workers.dev حدود ۸ دقیقه روی ریشه، `/index.html`، `/__void`، فایل واقعی و favicon جواب ۴۰۴ با ۰ بایت داد. علت معلوم نیست ❓. پس بعد از هر deploy با `curl` خود صفحه را بسنج و به پیام موفقیت اعتماد نکن.
- ⚠️ `npx void cloudflare login` به همان حسابی وصل می‌شود که در مرورگر باز است و این را فقط در یک خط نشان می‌دهد. پیش از ورود حساب مرورگر را چک کن. کد دستگاه ۵ دقیقه اعتبار دارد.
- ✅ راهنمای `void deploy` گزینه‌ی `--project` را دارد؛ گفته‌ی قبلی که این گزینه نیست درست نبود.
- 🔬 `void init` روی پروژه‌ی **موجود** `--starter` را نادیده می‌گیرد و پس از نوشتن فایل‌ها در پرسش دیتابیس می‌ایستد. استقرار Workers و دسترسی از ایران هنوز آزموده نشده (❓).

## پیگیری ۲۰۲۶-۱۰-۳۱ 🔬

- حکم از trial به assess پایین آمد، چون استقرار «موفق» بعد از ۲۴ ساعت هم صفحه نداد.

- 🔬 بیش از ۲۴ ساعت بعد از دو استقرار «موفق»، نشانی هنوز 404 با ۰ بایت می‌دهد؛ پس علت انتشار تدریجی نیست. ❓ علت واقعی معلوم نیست.
- 🔬 پوشه‌ی آزمایشی در `/tmp` با restart از بین رفت، ولی Worker روی حساب Cloudflare ماند. پروژه‌ی آزمایشی را در پوشه‌ی ماندگار بساز و پس از آزمون Worker را پاک کن. لاگ‌ها در `~/.void/logs` می‌مانند.

## مرتبط
[S191](../sources/README.md#s191) · [Vite](vite.md) · [Cloudflare Pages](cloudflare-pages.md)
