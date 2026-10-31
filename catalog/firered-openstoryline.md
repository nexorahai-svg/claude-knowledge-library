---
name: FireRed-OpenStoryline
slug: firered-openstoryline
category: video
domains: [social-media]
verdict: assess
status: researched
summary: عامل تدوین ویدیو با فرمان متنی از تیم FireRed (Xiaohongshu)؛ به چند API مدل زبانی و تصویری چینی وابسته
url: https://github.com/FireRedTeam/FireRed-OpenStoryline
repo: "https://github.com/FireRedTeam/FireRed-OpenStoryline"
license: "Apache-2.0"
pricing: freemium
risk: medium
sources: [S130]
found_in: [batch-16]
last_checked: 2026-10-21
next_check: "2027-01-21"
---

# FireRed-OpenStoryline

## چیست
✅ (README) عامل تدوین: فیلم و عکس خودت را می‌گیرد و با فرمان متنی تدوین، زیرنویس و موسیقی می‌گذارد؛ رابط وب، CLI و MCP. حدود ۳٫۵ هزار ستاره، Apache-2.0، آخرین تغییر ۲۰۲۶-۰۷-۳۱.

## کی استفاده کنیم
👀 فعلاً نه. اجرا نشد، چون کلید پولی و فرستادن فیلم به سرویس بیرونی لازم است.

## قیمت و مجوز
✅ کد Apache-2.0. ⚠️ (README) دارایی‌های آزاد پیش‌فرض (فونت و موسیقی) «به‌خاطر محدودیت مجوز» پایه‌ای‌اند؛ نمونه‌های زیبای دمو با کتابخانه‌ی دارایی اپ Xiaohongshu ساخته شده‌اند. ⚠️ گذارهای هوش مصنوعی به سرویس پولی تولید ویدیو وابسته‌اند و خود README می‌گوید «هزینه نسبتاً بالاست».

## ریسک و هشدار
⚠️ (docs/api-key) مدل زبانی (پیش‌فرض DeepSeek) و مدل بینایی (GLM-4.6V از Zhipu یا Qwen3-VL از Alibaba) لازم است؛ فیلم و عکس مشتری به این سرویس‌ها می‌رود. ⚠️ فایل مدل‌ها (`models.zip`) از سرور ابری Tencent در شانگهای دانلود می‌شود.

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S130](../sources/README.md#s130) · دسته‌ی ۱۶
