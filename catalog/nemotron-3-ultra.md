---
name: NVIDIA Nemotron 3 Ultra
slug: nemotron-3-ultra
category: local-ai
domains: [claude-code]
verdict: assess
status: researched
summary: مدل زبانی باز انویدیا (۵۵۰ میلیارد پارامتر MoE، زمینه‌ی تا یک میلیون توکن)؛ ادعای «بهتر از Claude Code» در جدول خود انویدیا نیست
use_when: "comparing open-weight models for an agent or coding tool ; needing very long context (up to 1M tokens) through a hosted open model"
how: "Do not replace Claude Code with it: NVIDIA's own table shows lower SWE-Bench Verified (70.7) than other open models and no Claude comparison; running it needs 8 datacenter GPUs; try only through a hosted API with OpenCode, read the provider terms first"
url: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16
repo: ""
license: OpenMDW-1.1
pricing: free
risk: low
sources: [S183]
found_in: [instagram]
last_checked: 2026-10-30
next_check: "2027-01-28"
---

# NVIDIA Nemotron 3 Ultra

## چیست
✅ (کارت مدل در Hugging Face، ۲۰۲۶-۱۰-۲۸) مدل زبانی باز انویدیا: ۵۵۰ میلیارد پارامتر که هر بار ۵۵ میلیارد فعال است (MoE ترکیبی Mamba و Transformer)، زمینه‌ی تا ۱ میلیون توکن، برای استدلال، کار عامل‌محور، ابزار و متن بلند. منتشر شده در ۲۰۲۶-۰۶-۰۳ (تازه نیست). حداقل سخت‌افزار برای اجرا: ۸ کارت GB200/B200 یا ۱۶ کارت H100؛ یعنی روی رایانه‌ی شخصی اجرا نمی‌شود.
✅ جدول سنجش خود کارت مدل: SWE-Bench Verified برابر 70.7، کمتر از GLM-5.1 (76.2)، Kimi-K2.6 (75.7) و DeepSeek V4 Pro (74.5)؛ Terminal Bench 2.1 برابر 56.4. هیچ مقایسه‌ای با Claude یا Codex در جدول نیست.
✅ ادعای ریل (@mojavad_ai، ۲۰۲۶-۱۰-۲۷) که «Claude Code و Codex را کنار زده» نادرست و گمراه‌کننده است: Claude Code ابزار است نه مدل، و خود انویدیا آن را حتی بالاتر از مدل‌های باز دیگر هم نشان نمی‌دهد. «۵ برابر سریع‌تر» در این بررسی دیده نشد ❓.

## کی استفاده کنیم
🧭 فقط اگر متن خیلی بلند (بیش از چند صد هزار توکن) با مدل باز لازم باشد، از راه یک سرویس میزبان. برای کدنویسی روزمره جای Claude Code را نمی‌گیرد.

## قیمت و مجوز
✅ وزن‌ها با مجوز OpenMDW-1.1 (https://openmdw.ai/license/1-1/)؛ ✅ متن کامل OpenMDW-1.1 خوانده شد (https://openmdw.ai/license/1-1/): استفاده بدون محدودیت و رایگان؛ هنگام بازتوزیع باید نسخه‌ی مجوز و اعلان‌های حق نشر بماند؛ شکایت حق ثبت یا کپی‌رایت علیه مدل مجوز را پایان می‌دهد؛ هیچ محدودیتی روی خروجی‌ها نمی‌گذارد. ❓ «کلید رایگان» ریل احتمالاً اعتبار آزمایشی build.nvidia.com است؛ سقف و شرایطش در این بررسی خوانده نشد.

## ریسک و هشدار
کم برای خود مدل. هشدار: ریل راهنمای نصب را فقط با «کامنت بده» می‌فرستد؛ آدرس رسمی همین کارت مدل است. کد یا داده‌ی مشتری را به کلید آزمایشی سرویس رایگان نده.

## مرتبط
- [Nemotron 3.5 Transcribe](nemotron-3-5-transcribe.md): گفتار به متن هم‌خانواده؛ فارسی ندارد
[S183](../sources/README.md#s183) · [OpenCode](opencode.md) · [colibri](colibri.md)
