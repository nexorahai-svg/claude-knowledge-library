<div align="center">

# Claude Knowledge Library

**A verified, self-updating knowledge library that turns Claude Code into a senior builder for apps, websites and social content.**

308 tool cards · 60 guides · 9 project playbooks · 155 sources checked against primary docs

[![License: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-1f7a4d)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-2f62b0)](LICENSE-CODE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#install-in-30-seconds)
[![Languages](https://img.shields.io/badge/docs-EN%20%C2%B7%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C%20%C2%B7%20%D8%B9%D8%B1%D8%A8%D9%8A-555)](#languages)
[![Updated](https://img.shields.io/badge/updated-2026--10--25-a86a12)](#how-it-stays-current)

Made by **[Nexorah AI](https://github.com/nexorahai-svg)** in Dubai · [Instagram](https://www.instagram.com/nexorahai/) · [Telegram](https://t.me/nexorah_ai)

⭐ **If this saves you a week of research, star the repo — it is how we know to keep going.**

</div>

---

## Why this exists

Every new project starts with the same questions: *which framework, which plugin, which AI model, is it free for commercial use, will it break Persian or Arabic text?* Posts and videos exaggerate; prices and licences change monthly. This library answers those questions once, **with a source for every claim**, and gives the answers to Claude in every session — automatically.

## What you get

| | |
|---|---|
| 🗂️ **308 tool cards** | Each with a verdict — ✅ adopt · 🧪 trial · 👀 assess · ⛔ hold — licence, pricing, risk, and the date it was last checked against the vendor's own docs. |
| 🧭 **9 playbooks** | Step-by-step for a business website, online store, web app, mobile app, desktop app, local-business app, social content, brand identity, AI feature. |
| 📚 **60 guides** | Design systems, RTL, SEO, verification, cost control, paid AI media tools (video, image, voice, music) with prompt templates. |
| 🔌 **Claude Code plugin** | Detects your project type and tells Claude which plugins and connectors to use, guards your RAM/CPU/GPU before heavy work, keeps Claude in the language you chose, and reminds it to file new findings. |
| 🛡️ **Safety first** | Third-party plugins, MCP servers and skills are read file by file before any verdict; risky ones (account bans, scraping, credential access) are flagged ⛔. |

Labels used everywhere: ✅ checked against the primary source · 🧭 strong secondary signal · ❓ unverified · 🔬 tested in a real project.

## Install in 30 seconds

```bash
claude plugin marketplace add https://github.com/nexorahai-svg/claude-knowledge-library.git
claude plugin install knowledge-library@knowledge-library
git clone https://github.com/nexorahai-svg/claude-knowledge-library.git ~/Desktop/knowledge-library
```

Open a new Claude Code session in any project. The first session asks which language you want Claude to use; after that the library works on its own.

## What happens in every session

- **Session start:** recognises the project (Flutter, Cloudflare, Supabase, Shopify, website, video, social content …) and lists the right tools, what to keep off, and what is missing.
- **Before heavy work:** measures free RAM, swap, memory pressure, CPU, disk and GPU; waits instead of freezing the machine (`scripts/resource_guard.py`).
- **End of every reply:** checks that Claude answered in your language (Persian, Arabic, Spanish, French … 30+ languages).

## Start here

- [`llms.txt`](llms.txt) — the short router Claude reads first
- [`playbooks/`](playbooks/) — pick your project type
- [`catalog/README.md`](catalog/README.md) — every tool with its verdict
- [`domains/social-media/paid-ai-tools.md`](domains/social-media/paid-ai-tools.md) — ElevenLabs, Google Flow/Veo, Kling, Seedance, Midjourney … prices, rules and prompts
- [`domains/claude-code/claude-toolkit.md`](domains/claude-code/claude-toolkit.md) — the best Claude plugins, connectors and hidden features
- [`domains/claude-code/resource-safety.md`](domains/claude-code/resource-safety.md) — keep heavy AI work from freezing your computer

## How it stays current

A daily watch and a weekly deep sweep re-check releases, licences and prices against official sources; changes land here automatically after a leak check.

## Languages

Guides are written in **Persian** (prompts and code in English), because the library was built for trilingual (English · Arabic · Persian, RTL-first) work in the UAE. Claude reads them in any language and answers you in yours.

<div dir="rtl">

### فارسی

کتابخانه‌ی دانش تأییدشده برای ساخت اپ، سایت و محتوای شبکه‌های اجتماعی با Claude Code: 308 کارت ابزار با حکم و منبع، 9 پلی‌بوک پروژه، 60 سند راهنما، و پلاگینی که در هر جلسه خودش ابزار درست را انتخاب می‌کند، رایانه را از هنگ کردن حفظ می‌کند و Claude را به زبان شما نگه می‌دارد. اگر به کارتان آمد، ⭐ ستاره بزنید و در [اینستاگرام](https://www.instagram.com/nexorahai/) دنبالمان کنید.

### العربية

مكتبة معرفة موثّقة لبناء التطبيقات والمواقع ومحتوى التواصل الاجتماعي باستخدام Claude Code: 308 بطاقة أداة مع تقييم ومصدر، 9 أدلة مشاريع، 60 دليلًا، وإضافة تختار الأدوات المناسبة في كل جلسة وتحمي جهازك من التجمّد وتُبقي Claude بلغتك. إذا أفادتك، امنحها ⭐ وتابعنا على [إنستغرام](https://www.instagram.com/nexorahai/).

</div>

## License

Content (documents, cards, playbooks): [CC BY 4.0](LICENSE) — use and adapt freely, credit **Nexorah AI** with a link to this repository.
Code (scripts, plugin, starters): [MIT](LICENSE-CODE).
Third-party tools described here keep their own licences; verdicts are our assessment, not legal advice.
