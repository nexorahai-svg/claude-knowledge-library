# قانون منابع: رم، پردازنده، کارت گرافیک و دیسک در هر جلسه

> **نوع سند:** دستورالعمل
> **هدف این سند:** هیچ جلسه‌ی Claude، هیچ build، رندر، مدل محلی یا گروه زیرعامل، رایانه را به هنگ کردن نرساند؛ کار سنگین وقتی دستگاه شلوغ است **صبر کند** نه اینکه خراب شود؛ و این قانون کار عادی را هم متوقف نکند.
> **موضوع تحقیق:** هنگ کامل رایانه‌ی اصلی در ۲۰۲۶-۱۰-۲۴ که به ری‌استارت و کار نیمه‌تمام رسید؛ مستندات رسمی Claude Code درباره‌ی حافظه؛ گزارش‌های کاربران (issueهای GitHub)؛ مستندات earlyoom، systemd-oomd، nohang، PSI هسته، cgroup و systemd؛ حد ابزارهای build و رندر.
> **منابع:** [S152 قانون منابع](../../sources/README.md#s152) · [S102 بسته شدن اپ از کمبود حافظه](../../sources/README.md#s102) · [S107 سقف حافظه با MemorySwapMax](../../sources/README.md#s107)
> **آخرین بررسی:** ۲۰۲۶-۱۰-۲۴
> **دفعه‌ی بعد چک شود:** آستانه‌ها بعد از دو هفته کار واقعی (`resource_guard.py check` در لاگ‌ها)؛ نسخه‌ی تازه‌ی Claude Code برای متغیرهای حافظه؛ آیا issueهای نشت حافظه بسته شده‌اند؛ آیا earlyoom در عمل چیزی بسته و دسکتاپ سالم ماند (`journalctl -u earlyoom`).

---

## ۱. قانون (کوتاه)

**اول بسنج، بعد اقدام کن.** فقط کار سنگین سنجیده می‌شود؛ خواندن، ویرایش و فرمان کوچک هرگز.

| وضعیت | یعنی | چه کند |
|---|---|---|
| 🟢 سبز | رم آزاد بالای ۲۵٪، swap زیر ۲۵٪، فشار حافظه کم | کار عادی؛ کار سنگین یکی‌دوتا هم‌زمان؛ تا ۴ زیرعامل |
| 🟡 زرد | رم ۱۲ تا ۲۵٪، یا swap ۲۵ تا ۶۰٪، یا پردازنده‌ی پر، یا VRAM بالای ۸۵٪، یا دمای بالا | **ادامه بده، ولی کم کن:** یک کار سنگین در هر لحظه، پرچم‌های موازی کمتر، حداکثر ۲ زیرعامل، کار بلند با `resource_guard.py run` |
| 🔴 قرمز | رم زیر ۱۲٪ یا زیر ۳ گیگ، یا swap بالای ۶۰٪، یا فشار حافظه بالا (thrash)، یا دیسک زیر ۳ گیگ، یا دمای خطر، یا VRAM کافی برای کار نیست | **صبر کن:** کار سنگین شروع نشود؛ `resource_guard.py wait` تا آزاد شدن (حداکثر ۲۰ دقیقه)؛ در این مدت فقط کار سبک؛ اگر طول کشید به کاربر بگو چه چیزی دستگاه را گرفته و بپرس |

- **هرگز** برنامه‌های کاربر را نبند. فقط پروسه‌هایی که خود همین جلسه ساخته (مثلاً سرور یا زیرعامل رهاشده).
- **هرگز** از ترس هنگ، کار را رد نکن: سبز و زرد یعنی کار انجام می‌شود.
- کار طولانی را در مرحله‌های کوچک با commit و `STATE.md` جلو ببر تا اگر چیزی قطع شد، کار نیمه‌تمام از دست نرود.

## ۲. ابزارها (خودکار)

- **`scripts/resource_guard.py`** (کتابخانه، فقط کتابخانه‌ی استاندارد پایتون، حدود ۳۰ میلی‌ثانیه):
  ```bash
  python3 scripts/resource_guard.py check                    # 🟢/🟡/🔴 با دلیل
  python3 scripts/resource_guard.py check --need-vram 3      # برای کار گرافیکی
  python3 scripts/resource_guard.py wait                     # صبر تا آزاد شدن
  python3 scripts/resource_guard.py run --mem 8G -- <فرمان>  # صبر + اجرا با سقف حافظه و پردازنده
  ```
  می‌سنجد: رم آزاد، swap، فشار حافظه و پردازنده (PSI هسته)، بار پردازنده، فضای دیسک خانه، دمای پردازنده، VRAM و دمای کارت NVIDIA.
- **هوک پیش از ابزار** (پلاگین کتابخانه، در هر جلسه): پیش از هر فرمان سنگین (build، رندر، مدل محلی، تست، نصب، شبیه‌ساز، `claude -p`) و پیش از هر زیرعامل تازه می‌سنجد. قرمز: فرمان اجرا نمی‌شود و Claude دستور صبر را می‌گیرد. زرد: اجرا می‌شود با یادآوری «یکی‌یکی». سبز: ساکت. 🔬 آزموده: `ls` ساکت؛ build روی دستگاه سبز ساکت؛ رم ۸٪ شبیه‌سازی‌شده: رد با دستور صبر.
- **حدهای رسمی Claude Code** (`setup_machine.py` در `settings.json` → `env` می‌گذارد؛ ✅ [مستندات env-vars](https://code.claude.com/docs/en/env-vars)):
  | متغیر | مقدار ما | چه می‌کند |
  |---|---|---|
  | `CLAUDE_CODE_TOOL_MEMORY_LIMIT` | `8G` | یک cgroup حافظه‌ی مشترک برای همه‌ی فرمان‌های Bash و Monitor یک جلسه (لینوکس، v2.1.233+)؛ build فراری فقط خودش کشته می‌شود |
  | `CLAUDE_CODE_WARN_MEMORY_FREE_GIB` | `4` | وقتی رم آزاد زیر ۴ گیگ برود، Claude یادآوری می‌گیرد |
  | `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | `4` | پیش‌فرض ۲۰ |
  | `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` | `4` | پیش‌فرض ۱۶؛ هر عامل در حال اجرا متن خودش را در حافظه نگه می‌دارد |

  ⚠️ این‌ها بعد از باز کردن دوباره‌ی Claude اثر می‌کنند. ❓ اینکه cgroup فرمان‌ها زیر scope اپ دسکتاپ ساخته شود هنوز با `claude --debug` آزموده نشده.

## ۳. چرا هنگ می‌شود (یافته‌ها)

- 🔬 (این رایانه، ۲۰۲۶-۱۰-۲۴) هیچ نگهبان زودهنگام حافظه (earlyoom یا systemd-oomd) نصب نبود. لینوکس بدون آن تا ته swap صبر می‌کند و دستگاه دقیقه‌ها **thrash** می‌کند (کند و بی‌پاسخ) پیش از اینکه هسته پروسه‌ای را ببندد؛ برای کاربر یعنی هنگ و ری‌استارت. لاگ هسته‌ی بوت قبلی برای کاربر قابل خواندن نبود، پس علت دقیق ❓.
- 🔬 (۲۰۲۶-۱۰-۱۹، [S102](../../sources/README.md#s102)) اپ دسکتاپ و همه‌ی جلسه‌ها و فرمان‌هایشان در **یک scope** هستند؛ یک کمبود حافظه همه را با هم می‌بندد (اوج ۲۷٫۶ گیگ رم + ۱۸٫۷ گیگ swap).
- 🔬 (۲۰۲۶-۱۰-۲۴) سقف `MemoryMax` بدون `MemorySwapMax` کار نمی‌کند: کار ۶۰۰ مگابایتی از سقف ۲۰۰ مگ گذشت و به swap رفت. با `MemorySwapMax` فقط همان کار کشته شد (کد ۱۳۷) و دسکتاپ دست نخورد.
- 🔬 (۲۰۲۶-۱۰-۲۴) سقف نرم `MemoryHigh` همراه سقف swap، کار را **دقیقه‌ها گیر انداخت** (نه کشته شد، نه تمام شد) و فشار حافظه‌ی کل دستگاه را به ۴۳٪ رساند؛ از ابزار برداشته شد.
- 🧭 گزارش‌های کاربران در مخزن Claude Code (از آینه‌ی issueها؛ وضعیت فعلی ❓):
  - [#23717](https://claudeissues.com/issue/23717-bug-agent-teams-causes-system-freeze-and-chrome-crash-due-to-excessive-resource): نزدیک‌ترین به ما، با ۳۰ گیگ رم، لینوکس و Chrome باز. دو تا سه هم‌تیمی عامل دستگاه را هنگ کردند. ✅ خوانده شد.
  - [#70523](https://claudeissues.com/issue/70523-bug-kernel-oom-not-v8-heap-from-parallel-subagent-per-agent-mcp-fan-out-exhausts): ۶ زیرعامل موازی حدود ۷۰ پروسه‌ی node و ۴۳٫۵ گیگ حافظه ساختند.
  - [#86643](https://claudeissues.com/issue/86643-bug-runaway-memory-growth-in-claude-code-child-process-causes-full-system-freeze): پروسه‌ی فرزند فراری که دستگاه را کامل هنگ کرد.
  - [#18859](https://github.com/anthropics/claude-code/issues/18859): جلسه‌ی بیکار در ۱۸ ساعت تا ۱۵ گیگ رشد کرد.
  - [#26658](https://claudeissues.com/issue/26658-mcp-server-processes-are-never-cleaned-up-when-sessions-end-orphan-accumulation): پروسه‌های MCP بعد از پایان جلسه می‌مانند.
  - جمع‌بندی: راه‌حل همه‌ی این‌ها دور زدن مشکل بوده، نه اصلاح رسمی. یعنی عامل موازی کمتر، سقف حافظه برای هر فرمان، و بستن پروسه‌های رهاشده.
- ✅ [#60488](https://claudeissues.com/issue/60488-bug-claude-code-escapes-systemd-transient-scope-at-startup-defeating-user-impose): خود `claude` را در `systemd-run --scope` نپیچ؛ حدود ۲ ثانیه بعد از شروع از آن بیرون می‌رود. فرمان‌ها را بپیچ، یا از `CLAUDE_CODE_TOOL_MEMORY_LIMIT` استفاده کن.
- 🔬 (۲۰۲۶-۱۰-۲۴) نمایشگر روی کارت NVIDIA وصل بود؛ کار CUDA و صفحه‌نمایش یک کارت را شریک بودند. کاربر کابل را به خروجی مادربورد زد: حالا صفحه روی کارت داخلی AMD است (`card0-HDMI-A-1: connected`، NVIDIA `display_active: Disabled`) و کل ۸ گیگ کارت NVIDIA برای مدل و رندر آزاد است. ❓ اینکه زیر بار سنگین CUDA صفحه روان می‌ماند هنوز در کار واقعی دیده نشده. بررسی: `cat /sys/class/drm/card*-*/status` و `nvidia-smi --query-gpu=display_active --format=csv`.
- 🔬 دیسک ریشه ۹۳٪ پر (۳۹ گیگ آزاد): build و مدل و swap فایل‌های بزرگ می‌سازند؛ زیر ۱۰ گیگ زرد، زیر ۳ گیگ قرمز.

## ۴. محافظت یک‌باره‌ی سیستم (با sudo، کار کاربر)

۱. **earlyoom** (✅ [README](https://github.com/rfjakob/earlyoom)، [راهنما](https://raw.githubusercontent.com/rfjakob/earlyoom/master/MANPAGE.md)؛ بسته‌ی Debian 13: `earlyoom` 1.8.2). یک پروسه، سنگین‌ترین را، **پیش از** thrash می‌بندد، نه کل جلسه را. `-s 100` یعنی منتظر تمام شدن swap نماند. systemd-oomd کل cgroup را می‌بندد؛ اینجا یعنی **کل اپ Claude با همه‌ی جلسه‌ها**، پس انتخاب نشد. nohang خوب است ولی نسخه‌ی Debian عقب است. هم‌زمان دوتا نصب نشود.
   ```bash
   sudo apt install earlyoom
   sudo tee /etc/default/earlyoom >/dev/null <<'EOF'
   EARLYOOM_ARGS="-r 60 -m 8 -s 100 -p -n --avoid '(^|/)(gnome-shell|gnome-session|gdm|Xwayland|mutter|pipewire|wireplumber|systemd|systemd-logind|NetworkManager|dbus-daemon)$' --prefer '(^|/)(chrome|node|ollama|llama-server|python3?|ffmpeg|java|dart|gradle)$'"
   EOF
   sudo systemctl enable --now earlyoom
   ```
   `-m 8` یعنی در ۸٪ رم آزاد (حدود ۲٫۴ گیگ) پیام پایان، و در ۴٪ کشتن.
   🔬 روی رایانه‌ی اصلی نصب و فعال شد (۲۰۲۶-۱۰-۲۴، earlyoom 1.8.2-1؛ `systemctl is-active earlyoom` → active، آرگومان‌ها همین).
۲. **خواندن لاگ هنگ بعدی:** `sudo usermod -aG adm,systemd-journal $USER` (یک بار خروج و ورود). با این، علت هنگ بعدی دیده می‌شود. 🔬 روی رایانه‌ی اصلی انجام شد (۲۰۲۶-۱۰-۲۴، عضو `adm` و `systemd-journal`).
۳. 🧭 **تنظیم حافظه‌ی هسته** (اختیاری؛ swap فشرده‌ی zram ۸ گیگ از قبل فعال و در اولویت است):
   ```bash
   sudo tee /etc/sysctl.d/99-desktop-memory.conf >/dev/null <<'EOF'
   vm.swappiness=100
   vm.page-cluster=0
   vm.watermark_scale_factor=125
   EOF
   sudo sysctl --system
   ```
   (✅ معنی هر مقدار: [vm.html هسته](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html)؛ مقدارها 🧭 تجربه‌ی جامعه برای zram).
۴. **فضای دیسک** را به بالای ۲۰٪ آزاد برسان.

⛔ سقف حافظه برای کل `user-1000.slice` پیشنهاد نشد: سقف نرم روی کل کاربر می‌تواند همان گیر کردنی را بسازد که در آزمون دیدیم.

## ۵. حد هر ابزار (وقتی زرد است یا کار سنگین است)

| ابزار | حد | منبع |
|---|---|---|
| Gradle (اندروید) | `org.gradle.workers.max=6`، `org.gradle.jvmargs=-Xmx3g`، `org.gradle.daemon.idletimeout=900000` (۱۵ دقیقه، پیش‌فرض ۳ ساعت) | ✅ [Gradle](https://docs.gradle.org/current/userguide/build_environment.html) |
| Playwright | `--workers=2` (هر worker یک مرورگر جدا) | ✅ [Playwright](https://playwright.dev/docs/test-parallel) |
| Remotion | `--concurrency 4` (پیش‌فرض نصف رشته‌ها) | ✅ [Remotion](https://www.remotion.dev/docs/performance) |
| PyTorch | `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`؛ کسر کارت با `per_process_memory_fraction` | ✅ [PyTorch](https://docs.pytorch.org/docs/2.14/notes/cuda.html) |
| Ollama | `OLLAMA_MAX_LOADED_MODELS=1`، `OLLAMA_KEEP_ALIVE=2m`، `OLLAMA_NUM_PARALLEL=1` (پیش‌فرض‌ها ۳، ۵ دقیقه، ۱) | ✅ [Ollama](https://docs.ollama.com/faq) |
| Node/Next/Astro build | `NODE_OPTIONS=--max-old-space-size=4096` | 🧭 |
| ffmpeg | `-threads 8` | ❓ |
| مدل محلی گرافیکی | `check --need-vram <گیگ>`؛ حدود ۱٫۵ گیگ VRAM آزاد بماند | 🔬 |

## مرتبط
[کار موازی](parallel-agents.md) · [جعبه‌ابزار Claude](claude-toolkit.md) · [هزینه](cost-efficiency.md) · پروفایل کاربر
