---
name: prompts.chat (Awesome ChatGPT Prompts)
slug: prompts-chat
category: claude-code-tooling
domains: [claude-code, social-media, website]
verdict: trial
status: researched
summary: کتابخانه‌ی باز و جمعی پرامپت (کد، نوشتن، تصویر، ویدیو) با سایت، سرور MCP و پلاگین رسمی Claude Code؛ کد MIT و متن پرامپت‌ها CC0
use_when: "looking for a starting idea for an image, video or caption prompt ; checking how others phrase a role or task prompt before writing our own ; searching prompts from inside Claude Code"
how: "Trial first on a small task: claude mcp add --transport http prompts-chat https://prompts.chat/api/mcp and use search_prompts only; never send client text to improve_prompt and never paste a prompt verbatim into the library, write our own"
url: https://prompts.chat
repo: "https://github.com/f/prompts.chat"
license: "MIT (code) + CC0 1.0 (prompt data)"
pricing: free
risk: medium
sources: [S195]
found_in: [batch-22]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# prompts.chat (Awesome ChatGPT Prompts)

## چیست
✅ مخزن `f/prompts.chat` (نام قبلی Awesome ChatGPT Prompts)، ساخت ۲۰۲۲-۱۲-۰۵، حدود ۱۷۵ هزار ستاره، فعال (آخرین push ۲۰۲۶-۱۰-۲۸)، بایگانی نشده (GitHub API، ۲۰۲۶-۱۰-۲۸).
✅ سایت برای جستجو و اشتراک پرامپت، «skill» و workflow؛ قابل نصب روی سرور خودمان (Next.js، Prisma، Docker).
✅ فایل `prompts.csv` مخزن (https://github.com/f/prompts.chat، ۲۰۲۶-۱۰-۳۰) ۲٬۷۷۲ ردیف پرامپت دارد. ❓ ادعای «بیش از ۱۰ هزار» در پست‌ها تأیید نشد.
✅ سرور MCP: راه دور `https://prompts.chat/api/mcp` یا محلی `npx -y prompts.chat mcp`. ابزارها: `search_prompts`، `get_prompt` (با پر کردن متغیر)، `save_prompt` (کلید API لازم)، `improve_prompt`. همه‌ی پرامپت‌های عمومی به‌صورت MCP prompt هم عرضه می‌شوند.
✅ پلاگین رسمی Claude Code: `/plugin marketplace add f/prompts.chat` و بعد `/plugin install prompts.chat@prompts.chat`؛ فرمان‌های `/prompts.chat:prompts` و `/prompts.chat:skills`.

## کی استفاده کنیم
🧪 برای ایده‌ی اول: پرامپت تصویر و ویدیو برای محتوای شبکه‌های اجتماعی، نقش‌نامه برای متن، یا دیدن شیوه‌ی نوشتن دیگران. پرامپت نهایی را همیشه خودمان می‌نویسیم و با سبک پروژه تطبیق می‌دهیم.
🧭 فقط سرور MCP راه دور را اضافه کن؛ پلاگین کامل عامل و skill خودکار هم می‌آورد و متن جلسه را سنگین می‌کند.

## حسن و عیب
- حسن: رایگان، بسیار شناخته‌شده، مجوز روشن، MCP بدون ثبت‌نام برای جستجو، جستجو بر اساس نوع، دسته و برچسب.
- عیب: کیفیت پرامپت‌ها جمعی و نابرابر است؛ بیشتر انگلیسی و قدیمی‌ها برای ChatGPT نوشته شده‌اند؛ پرامپت فارسی کم است. جستجو کلیدواژه‌ای است، نه «انتخاب بهترین پرامپت».

## قیمت و مجوز
✅ رایگان. کد و محتوای سایت MIT؛ متن پرامپت‌ها CC0 1.0 (مالکیت عمومی) طبق فایل LICENSE. با این حال قانون کتابخانه پابرجاست: متن دیگران را در سندها نمی‌گذاریم.

## ریسک و هشدار
⚠️ MCP راه دور هر جستجو را به سرور prompts.chat می‌فرستد؛ `improve_prompt` متن پرامپت را برای بازنویسی به آنجا می‌فرستد. نام مشتری، متن خصوصی یا کلید را هرگز به آن نده. کلید `pchat_` فقط برای `save_prompt` لازم است؛ لازم نیست بسازی. پرامپت جمعی ممکن است دستور پنهان داشته باشد؛ پیش از اجرا بخوان.
⚠️ پست‌ها با قیف «کامنت کن تا لینک بگیری» تبلیغش می‌کنند؛ آدرس درست همین `prompts.chat` است.

## مرتبط
[S195](../sources/README.md#s195) · غربال ۲۲ · [کتابخانه‌ی پرامپت سایت](../domains/website/08-prompts/prompt-library.md)
