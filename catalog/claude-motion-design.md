---
name: Claude Motion Design (Howseen)
slug: claude-motion-design
category: video
domains: [social-media]
verdict: assess
status: researched
summary: اسکیل ساخت ویدیوی موشن فقط با HTML، Playwright و ffmpeg، با تاری حرکت و هماهنگی با ضرب موسیقی، بدون مجوز Remotion
use_when: "a launch or promo video in pure code with beat-synced cuts ; deterministic frame-by-frame rendering without Remotion licensing"
how: "Copy skill/motion-design under a different folder name: it collides with the LottieFiles motion-design skill already installed; needs playwright, imageio-ffmpeg, numpy, pillow; an optional 21st.dev client reads API_KEY_21ST"
url: https://github.com/howseen-ai/claude-motion-design
repo: "https://github.com/howseen-ai/claude-motion-design"
license: "MIT"
pricing: free
risk: low
sources: [S214]
found_in: [x-yarad-ai-2026-10-30]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# Claude Motion Design (Howseen)

## چیست
- ✅ مخزن MIT، حدود ۷۳۷ ستاره، ساخت ۲۰۲۶-۰۹-۲۷، آخرین push در ۲۰۲۶-۱۰-۰۴. کل فیلم یک تابع `seek(t)` است، فریم‌به‌فریم رندر می‌شود، و برش‌ها روی نقشه‌ی ضرب موسیقی می‌نشینند.
- ✅ در کد یک کلاینت اختیاری 21st.dev هست که کلید را از محیط یا `~/.config/21st.key` می‌خواند. کد کامل خوانده نشد ❓.
- 👀 آزموده نشده. ما برای همین کار [HyperFrames](hyperframes.md) را داریم، پس بیشتر برای روش تاری حرکت و هماهنگی ضرب مفید است.

## ریسک و هشدار
- ⚠️ نام اسکیل `motion-design` با اسکیل LottieFiles که نصب است یکی است؛ با نام دیگری کپی کن.
- مخزن تبلیغ محصول سازنده است و ادعاها از خود اوست.

## مرتبط
[سبک‌های موشن](../domains/social-media/motion-design-styles.md) · [S214](../sources/README.md#s214)
