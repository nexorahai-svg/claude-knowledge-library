---
name: Buffer
slug: buffer
category: social-publishing
domains: [social-media]
verdict: trial
status: researched
summary: ابزار زمان‌بندی پست با API در همه‌ی طرح‌ها
url: https://buffer.com
repo: ""
license: "سرویس تجاری"
pricing: freemium
risk: medium
sources: [S46]
found_in: []
last_checked: 2026-10-17
next_check: "2026-11-16"
---

# Buffer

## چیست
✅ رایگان: ۳ کانال، ۱۰ پست در هر کانال، ۳٬۰۰۰ درخواست API در ماه. Essentials ۵ دلار هر کانال. ۱۲ شبکه از جمله Instagram، TikTok، YouTube، LinkedIn، X.

## کی استفاده کنیم
🧭 ارزان‌ترین راه با API.

## قیمت و مجوز
✅ بالا. ✅ MCP راه‌دور رسمی: `https://mcp.buffer.com/mcp` با هدر `Authorization: Bearer <کلید API>` (developers.buffer.com/guides/integrations/mcp.html). برای Claude و Claude Code راه ساده‌تر ورود OAuth از «Connectors» است، بدون کلید API. ابزارها: create_post، edit_post، delete_post، create_idea، list_posts، get_aggregated_post_metrics، قالب پست و دو ابزار عمومی GraphQL (execute_query و execute_mutation). سقف نرخ: پاسخ 429 با هدر Retry-After؛ فهرست‌ها تا ۱۰۰ مورد در هر صفحه.

## ریسک و هشدار
⚠️ دسترسی انتشار به نام ما؛ با پیش‌نویس شروع کن.

## مرتبط
[انتشار](../domains/social-media/publishing.md) · [S46](../sources/README.md#s46)
