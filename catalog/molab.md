---
name: molab (marimo)
slug: molab
category: research-tools
domains: [claude-code, social-media, apps]
verdict: adopt
status: researched
summary: نوت‌بوک ابری رایگان marimo با ۴ CPU، ۳۲ گیگابایت RAM و GPU قوی (RTX Pro 6000)، که Claude Code می‌تواند به آن وصل شود
use_when: "need a strong GPU for a short job such as a local image, video or speech model without owning one ; batch Persian transcription of public audio with faster-whisper ; data analysis or a quick Python experiment in the cloud ; letting Claude Code drive a cloud notebook"
how: "Read domains/claude-code/cloud-gpu-molab.md first (jobs, tools, steps). Open molab.marimo.io, attach the GPU from the specs button, then Pair with an agent: install marimo-pair once (claude plugin marketplace add marimo-team/marimo-pair, then claude plugin install marimo-pair@marimo-pair); in an existing Claude session give it the notebook URL and save the token to a 600-mode file read into MARIMO_TOKEN; add packages in their own call before long cells; notebooks are public-but-unlisted, so no client data or secrets; idle 90 min stops it"
url: https://molab.marimo.io
repo: https://github.com/marimo-team/marimo-pair
license: Apache-2.0 (marimo و marimo-pair)؛ خود سرویس: شرایط سایت
pricing: free
risk: medium
sources: [S182, S185]
found_in: [user]
last_checked: 2026-10-28
next_check: 2026-11-27
---

# molab (marimo)

## چیست
✅ (مستندات رسمی https://docs.marimo.io/guides/molab/، ۲۰۲۶-۱۰-۲۸) نسخه‌ی میزبانی‌شده‌ی نوت‌بوک متن‌باز marimo (Python، جایگزین Jupyter). طبق پرسش‌های متداول رایگان است. هر نوت‌بوک ۴ CPU و ۳۲ گیگابایت RAM دارد و می‌شود از دکمه‌ی مشخصات بالای صفحه یک **NVIDIA RTX Pro 6000 Blackwell با ۹۶ گیگابایت VRAM** به آن وصل کرد. اجرا حداکثر ۱۲ ساعت؛ بعد از ۹۰ دقیقه بی‌کاری خاموش می‌شود. هوش مصنوعی داخلی با مدل‌های متن‌باز، بدون کلید API.
✅ «Pair with an agent»: Claude Code، Codex یا OpenCode روی رایانه‌ی خودت به نوت‌بوک ابری وصل می‌شود و کد می‌نویسد، بسته نصب می‌کند و ویجت‌ها را تغییر می‌دهد. یک بار skill را نصب کن (`npx skills add marimo-team/marimo-pair`)، بعد فرمان `claude "$(uvx marimo@latest pair prompt --url <آدرس نوت‌بوک> --with-token --claude)"` را که صفحه نشان می‌دهد اجرا کن و توکن را وقتی خواست بچسبان. مخزن marimo-pair: Apache-2.0، فعال.
🧭 یک کاربر گزارش داد که اتصال Claude Code کار می‌کند (۲۰۲۶-۱۰-۲۸).

## آزمون واقعی 🔬 (۲۰۲۶-۱۰-۲۸، از لینوکس اصلی)
- 🔬 **GPU همان است که گفته‌اند:** `nvidia-smi` در نوت‌بوک نشان داد NVIDIA RTX PRO 6000 Blackwell Server Edition با ۹۷٬۸۸۷ مگابایت حافظه، درایور 595.71. محیط: Python 3.13، marimo 0.25.2، torch 2.11 با CUDA 13، هسته‌ی gVisor. (`os.cpu_count()` عدد ۲۰ و `/proc/meminfo` حدود ۱۶۰ گیگ نشان داد؛ این‌ها چیزی است که sandbox نشان می‌دهد، نه لزوماً سهم ما.)
- 🔬 **marimo-pair از یک جلسه‌ی موجود Claude جواب داد:** لازم نیست فرمان `claude "$(uvx marimo@latest pair prompt ...)"` صفحه را اجرا کنی، که جلسه‌ی تازه باز می‌کند. با پلاگین نصب‌شده کافی است آدرس نوت‌بوک (`https://sb-….sb.molab.run/`) و توکن را به `execute-code.sh --url …` بدهی. توکن را در فایلی با دسترسی ۶۰۰ بگذار و با `MARIMO_TOKEN` بخوان؛ در چت نفرست. ⚠️ فرمان `read` در حالت `!` گفتگوی اپ دسکتاپ ورودی نمی‌گیرد؛ برای چسباندن پنهان توکن یک تب ترمینال واقعی لازم است.
- 🔬 **دام زمان:** اولین اجرای یک سلول طولانی (نصب ۱.۳ گیگ بسته‌ی CUDA و بعد مدل) با «Execution did not complete: the server ended the stream» تمام شد و سلول `interrupted` ماند. همان سلول بعد از نصب بسته‌ها در یک دقیقه کامل شد. بسته‌ها را در یک فراخوانی جدا اضافه کن (`ctx.packages.add`)، بعد سلول سنگین را اجرا کن.
- 🔬 **نتیجه:** faster-whisper فارسی ۲۶.۵ دقیقه صدا را با large-v3-turbo در ۱۸ ثانیه پیاده کرد، حدود ۱۵۰ برابر CPU رایانه‌ی آزمون؛ جزئیات و دام CUDA 13 در کارت [faster-whisper](faster-whisper.md). [S185](../sources/README.md#s185)
- ردیف آزمون در دفتر پروژه‌ها.
- 🧭 حکم «آزمایشی» می‌ماند تا سقف استفاده‌ی GPU و شرایط سرویس روشن شود؛ از نظر فنی کار کرد.

## کی استفاده کنیم
🧭 برای کار کوتاه GPU که رایانه‌ی خودمان ندارد یا کند است: اجرای مدل تصویر، ویدیو یا گفتار متن‌باز، آزمایش داده، تبدیل فایل سنگین. برای کار طولانی‌تر از ۱۲ ساعت یا داده‌ی محرمانه نه.

## قیمت و مجوز
✅ رایگان طبق مستندات. ❓ سقف استفاده از GPU، صف و شرایط سرویس در مستندات نیامده (صفحه‌ی قیمت پیدا نشد)؛ ممکن است بی‌خبر عوض شود. marimo و marimo-pair هر دو Apache-2.0.

## ریسک و هشدار
متوسط:
- نوت‌بوک‌ها به‌طور پیش‌فرض **عمومی ولی فهرست‌نشده‌اند**؛ هر کس لینک را داشته باشد می‌بیند و می‌تواند کپی کند. داده‌ی مشتری، رمز و کلید API آنجا نگذار.
- توکن اتصال را مثل رمز نگه دار و در چت یا اسکرین‌شات نفرست.
- فرمان اتصال، متن دستور را از سرور نوت‌بوک می‌گیرد و به Claude می‌دهد؛ فقط به نوت‌بوک خودت وصل شو.
- فضای ذخیره محدود است؛ فایل فقط با آپلود از نوار کناری یا `mo.persistent_cache` می‌ماند.

## مرتبط
[راهنمای کارها و روش کار با molab](../domains/claude-code/cloud-gpu-molab.md) · [S182](../sources/README.md#s182) · [colibri](colibri.md)
