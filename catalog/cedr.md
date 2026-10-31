---
name: cedr
slug: cedr
category: claude-code-tooling
domains: [claude-code, security]
verdict: hold
status: researched
summary: CLI بتای Rust (Apache-2.0) که کار را به عامل و مدل مناسب مسیریابی می‌کند، بازبینی چند فروشنده را در یک دروازه ادغام می‌کند و skill و MCP را با قفل پین می‌کند
use_when: "pinning skills and MCP servers and failing CI when a server's tools change ; measuring token and cost of local coding-agent logs ; comparing with cc-switch and ccusage"
how: "Trial first on a small task: download the release archive for your platform from the GitHub releases page, check its checksum, run cedr monitor or the guard lint on a throwaway project only; beta so formats may change; do not enable monitor push"
url: https://cedr.dev
repo: "https://github.com/Sheernox/cedr"
license: "Apache-2.0"
pricing: free
risk: medium
sources: [S216]
found_in: [watch-2026-10-31]
last_checked: 2026-10-31
next_check: "2027-01-29"
---

# cedr

## چیست
✅ (GitHub API و README، ۲۰۲۶-۱۰-۳۱) مالک سازمان Sheernox؛ ساخته ۲۰۲۶-۱۰-۲۹، push ۲۰۲۶-۱۰-۳۱، ۵۹ ستاره، Apache-2.0، آخرین release نسخه‌ی v0.5.2 (۲۰۲۶-۱۰-۳۱؛ ۹ release در چند روز). README خودش «بتای عمومی» می‌گوید. سه بخش: Route (انتخاب عامل و مدل و effort از `routes.toml`)، Council (یک بازبین از هر فروشنده؛ هر P0 یا P1 دروازه را می‌بندد) و Guard (لینت پیکربندی عامل و قفل `.cedr/guard.lock` برای هر skill و MCP که اگر ابزارها یا میزبان‌های شبکه‌ی سرور عوض شود CI را خراب می‌کند). `cedr monitor` لاگ محلی را می‌خواند و فقط با `push` یا ارسال خودکار شمارش‌ها را می‌فرستد. فایل‌های باینری برای Linux x86_64 و ARM64 و macOS Apple silicon. ❓ کد خوانده نشد.

## کی استفاده کنیم
🧭 بخش Guard (قفل skill و MCP) با نگرانی ما درباره‌ی MCP و skill شخص ثالث ([ایمنی MCP](../domains/claude-code/mcp-safety.md)) می‌خواند؛ monitor با [ccusage](ccusage.md) همپوشانی دارد؛ مسیریابی با [cc-switch](cc-switch.md). هنوز در هیچ پروژه‌ای آزموده نشده.

## قیمت و مجوز
✅ Apache-2.0 و رایگان.

## ریسک و هشدار
⚠️ خیلی نو و بتا؛ باینری بسته‌بندی‌شده می‌خواند لاگ‌های محلی عامل‌ها (شامل نام پروژه‌ها). ارسال خودکار آمار را روشن نکن. Council چند فروشنده را صدا می‌زند و هزینه و ارسال کد به آن‌هاست ❓.

## مرتبط
[S216](../sources/README.md#s216)

🧭 (۲۰۲۶-۱۰-۳۱: 👀 به ⛔) تصمیم مالک: ابزاری که کدش خوانده نشده استفاده نمی‌شود.
