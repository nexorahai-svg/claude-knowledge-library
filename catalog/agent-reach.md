---
name: Agent-Reach
slug: agent-reach
category: research-tools
domains: [social-media, security]
verdict: assess
status: researched
summary: CLI خواندن و جستجوی X، Reddit، YouTube، GitHub و (آزمایشی) Instagram برای عامل؛ ورود Chrome را در مرورگر خودش کپی می‌کند
url: https://github.com/Panniantong/Agent-Reach
repo: "https://github.com/Panniantong/Agent-Reach"
license: "MIT"
pricing: free
risk: high
use_when: "need an agent to read a public YouTube, GitHub or web page in bulk when the library's fetch_post.py and official APIs do not cover it ; never for Instagram or X with the main account"
how: "Do not install without the user's yes; install only from the repo's docs/install.md (the PyPI package of the same name is fake); log in with a spare account, never let it copy the main Chrome login"
sources: [S159, S199]
last_checked: 2026-10-28
next_check: "2027-01-26"
---

# Agent-Reach

## چیست
✅ (MIT). README خودش هشدار می‌دهد که بسته‌ی هم‌نام در PyPI جعلی است؛ فقط از install.md گیت‌هاب.

- ✅ نسخه‌ی v1.6.0 (۲۰۲۶-۱۰-۲۳) بازسازی کامل است: یک فرمان `agent-reach`، همه‌چیز در `~/.agent-reach/`. یادداشت انتشار: ۲۸ از ۴۰ کار پیش از انتشار آزموده شد؛ Instagram (محدودیت نرخ)، Reddit و LinkedIn آزموده نشدند ([S199](../sources/S199.md)).
- ✅ Instagram در جدول README «آزمایشی» و نیازمند ورود است: جستجوی کاربر، پروفایل و پست‌ها. ادعای ریل‌ها که «لینک عمومی اینستاگرام را می‌خواند» ساده‌شده است.

## ریسک و هشدار
- ✅ برای سایت‌های نیازمند ورود، بار اول ورودِ همان سایت را از Chrome کاربر در مرورگر اختصاصی خودش کپی می‌کند (README می‌گوید رمزها را نمی‌خواند). این معمولاً حساب اصلی است؛ خود README حساب فرعی پیشنهاد می‌کند، چون پلتفرم‌ها حساب‌های خودکار را محدود می‌کنند.
- ✅ README یک حامی تبلیغاتی (سرویس خزش داده) دارد.
- ✅ بسته‌ی هم‌نام در PyPI جعلی است.

## کی استفاده کنیم
🧭 ریسک خزیدن و بسته شدن حساب؛ برای X از روش فقط‌خواندنی کتابخانه (`fetch_post.py`) استفاده کن.
