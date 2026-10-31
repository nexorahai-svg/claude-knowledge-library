---
name: Impeccable (لایه‌ی طراحی برای عامل‌ها)
slug: impeccable
category: design-inspiration
domains: [website, security]
verdict: assess
status: researched
summary: skill طراحی Apache-2.0 با ۲۴ فرمان، ۶۲ قاعده‌ی تشخیص طراحی هوش‌مصنوعی‌زده، CLI و hook؛ شامل مرجع iOS/Android؛ تله‌متری و دانلود باینری دارد
use_when: "scanning a generated frontend for typical AI-design tells with the deterministic detector (no LLM needed) ; polishing or critiquing a web UI, including iOS and Android guidance, next to the official frontend-design skill"
how: "Do not install without the user's yes; npx impeccable install downloads an engine binary and adds an edit hook, so pin the version, run npx impeccable telemetry off first, use --no-hooks, and prefer npx impeccable detect on one sample page"
url: https://github.com/pbakaus/impeccable
repo: "https://github.com/pbakaus/impeccable"
license: "Apache-2.0"
pricing: free
risk: high
sources: [S190]
found_in: [watch-2026-10-28]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Impeccable (لایه‌ی طراحی برای عامل‌ها)

## چیست
- ✅ مخزن Apache-2.0، حدود ۹۲٬۳۰۰ ستاره، بایگانی نشده، آخرین push در ۲۰۲۶-۱۰-۲۸. آخرین release: `cli-v4.8.0` در ۲۰۲۶-۱۰-۲۶ (GitHub API): https://github.com/pbakaus/impeccable
- ✅ README: یک skill (`/impeccable <فرمان>`) با ۲۴ فرمان (polish، audit، critique، distill، animate، bolder، quieter...)، تکرار زنده‌ی طرح در مرورگر، ۶۲ قاعده‌ی قطعی تشخیص (بدون LLM و کلید API) و یک افزونه‌ی مرورگر. `/impeccable init` فایل `PRODUCT.md` را می‌سازد.
- ✅ پوشه‌ی مرجع شامل `ios.md` و `android.md` است (برگرفته از `ehmo/platform-design-skills`، MIT، طبق NOTICE.md)، پس برای اپ هم کمی کاربرد دارد: https://github.com/pbakaus/impeccable/blob/main/NOTICE.md
- ✅ CLI مستقل: `npx impeccable detect <پوشه|فایل|URL>` بدون عامل کار می‌کند؛ پشتیبان‌های Claude Code، Cursor، Codex، Copilot، Gemini و دیگران.
- ❓ کیفیت واقعی نسبت به `frontend-design` آزموده نشده.

## کی استفاده کنیم
- 🧭 فقط پس از بازبینی: اجرای تشخیص‌دهنده روی یک صفحه‌ی نمونه یا خروجی تولیدشده، کنار [frontend-design](frontend-design.md). نصب کامل با hook برای ما زود است.

## قیمت و مجوز
- ✅ رایگان، Apache-2.0 (تجاری آزاد با حفظ مجوز و NOTICE): https://github.com/pbakaus/impeccable/blob/main/LICENSE

## ریسک و هشدار
- ✅ تله‌متری: هنگام شروع طرح جدید، skill از `impeccable.style` یک «دست» دنیای دیداری می‌گیرد (آن درخواست جزو کار است) و مگر خاموش کنی رکورد ناشناس انتخاب را می‌فرستد. فرستاده نمی‌شود: نام پروژه، فایل‌ها، کد، PRODUCT.md. خاموش‌کردن: `npx impeccable telemetry off` یا `DO_NOT_TRACK=1` یا `IMPECCABLE_NO_TELEMETRY=1`. (بخش Telemetry در README)
- ✅ موتور یک باینری است که کنار launcher یا در `~/.impeccable/bin/` یک‌بار دانلود می‌شود (بخش Install در README).
- ✅ نصب با `npx impeccable install` به‌طور پیش‌فرض hook بومی هر ابزار را هم می‌نویسد؛ برای Claude Code در `.claude/settings.local.json`. README هشدار می‌دهد hookهای نصب‌شده مستقل از تأیید ابزار اجرا می‌شوند و اولین ویرایش می‌تواند موتور را دانلود کند. گزینه‌ی `--no-hooks` آن را رد می‌کند.
- 🧭 بزرگ‌ترین سطح خطر میان skillهای طراحی؛ نسخه را پین کن و `scripts/` را بخوان (قانون ۴).

## مرتبط
[سبک‌های طراحی](../domains/website/02-design/design-styles.md) · [S190](../sources/README.md#s190) · https://impeccable.style/privacy
