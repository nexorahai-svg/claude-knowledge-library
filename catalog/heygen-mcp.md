---
name: HeyGen MCP
slug: heygen-mcp
category: video
domains: [social-media]
verdict: adopt
status: researched
summary: ساخت ویدیوی آواتار سخن‌گو از داخل Claude
use_when: "talking-avatar video from inside Claude ; a spokesperson clip without filming"
how: "claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/ then /mcp for OAuth; spends plan credits; a private avatar needs the face owner consent; Persian is not named, test first"
url: https://developers.heygen.com/mcp/overview
repo: ""
license: "شرایط HeyGen"
pricing: paid
risk: medium
sources: [S86]
found_in: [batch-05]
last_checked: 2026-10-31
next_check: "2026-11-30"
---

# HeyGen MCP

## چیست
✅ اتصال: `claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/` و بعد `/mcp` برای OAuth. از اعتبار طرح HeyGen کم می‌کند؛ درخواست‌های MCP به واحد کامل گرد می‌شوند و ممکن است گران‌تر از کلید API باشند.

## کی استفاده کنیم
🧭 فقط ویدیوی سخن‌گو با آواتار؛ برای تصویر پس‌زمینه نه.

## قیمت و مجوز
✅ در همه‌ی طرح‌ها.

## ریسک و هشدار
⚠️ آواتار خصوصی رضایت صاحب چهره می‌خواهد (`create_avatar_consent`). ❓ فارسی در «۱۷۵ زبان» نام برده نشده.

## Avatar IV (اکتبر ۲۰۲۶) 🧭
عکس + صدا یا متن ← ویدیو؛ رایگان: ۳ ویدیو در ماه با واترمارک؛ Creator ۲۹ دلار در ماه بدون واترمارک (تا 1080p)؛ API حدود ۰٫۰۵ دلار در ثانیه (قیمت میزبان ثالث). مقایسه با Hedra و Kling در [مدل‌های ویدیو](../domains/social-media/ai-video-models.md).

## مرتبط
[ساخت کلیپ با Claude](../domains/social-media/claude-clip-pipeline.md) · [S86](../sources/README.md#s86)

🧭 (۲۰۲۶-۱۰-۳۱: 👀 به ✅) تصمیم مالک: در کار واقعی جوابگوست.
