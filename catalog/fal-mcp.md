---
name: fal MCP
slug: fal-mcp
category: video
domains: [social-media]
verdict: assess
status: researched
summary: دسترسی به مدل‌های ویدیو و تصویر (Veo، Kling، …) از داخل Claude با OAuth
url: https://fal.ai/docs/model-apis/mcp
repo: ""
license: "شرایط fal"
pricing: paid
risk: medium
sources: [S86]
found_in: [batch-05]
last_checked: 2026-10-18
next_check: "2026-11-17"
---

# fal MCP

## چیست
✅ اتصال: `claude mcp add --transport http --scope user fal https://mcp.fal.ai/mcp-relay`؛ فقط OAuth، بدون کلید در چت. ابزارها: `get_pricing`، `run_model`، `submit_job`.

## کی استفاده کنیم
🧭 ارزان‌ترین Veo 3.1 Lite بی‌صدا، فقط بعد از روشن شدن شرایط انتشار.

## قیمت و مجوز
✅ Veo 3.1 Lite ۷۲۰p: بی‌صدا ۰.۰۳، با صدا ۰.۰۵ دلار در ثانیه. Kling v3 Pro: ۰.۱۱۲ و ۰.۱۶۸.

## ریسک و هشدار
⚠️ شرایط fal دسترسی را «برای استفاده‌ی شخصی یا داخلی کسب‌وکار» می‌دهد و مالکیت خروجی را صریح نمی‌گوید؛ ❓ پست عمومی. شرایط هر مدل هم جداگانه اعمال می‌شود.

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S86](../sources/README.md#s86)
