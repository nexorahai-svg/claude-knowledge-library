---
name: Expo MCP
slug: expo-mcp
category: app-testing
domains: [apps]
verdict: trial
status: researched
summary: سرور MCP راه دور رسمی Expo: مستندات، ساخت EAS، کنترل شبیه‌ساز
use_when: "working on an Expo app and needing docs, EAS builds or simulator control from Claude ; Expo-only projects"
how: "Trial first on a small task: claude mcp add --transport http expo https://mcp.expo.dev/mcp, then /mcp to sign in with OAuth; for simulator control run npx expo install expo-mcp --dev (SDK 54+) and EXPO_UNSTABLE_MCP_SERVER=1 npx expo start; docs search needs paid EAS"
url: https://docs.expo.dev/mcp/
repo: ""
license: "سرویس Expo"
pricing: freemium
risk: medium
sources: [S41]
found_in: []
last_checked: 2026-10-30
next_check: "2026-11-29"
---

# Expo MCP

## چیست
✅ آدرس `https://mcp.expo.dev/mcp` با OAuth و حساب Expo. برای کنترل محلی شبیه‌ساز بسته‌ی `expo-mcp` را به پروژه اضافه کن.

✅ نصب و اجرا (https://docs.expo.dev/mcp/، ۲۰۲۶-۱۰-۲۷): claude mcp add --transport http expo https://mcp.expo.dev/mcp

## کی استفاده کنیم
🧭 فقط اپ‌های Expo.

## قیمت و مجوز
✅ (https://docs.expo.dev/mcp/، ۲۰۲۶-۱۰-۲۷) حساب Expo لازم است؛ جدول قابلیت‌های رسمی می‌گوید جست‌وجوی مستندات سمت سرور «نیاز به طرح پولی EAS» دارد. قابلیت‌های محلی (شبیه‌ساز) فقط SDK 54 به بعد. ✅ قیمت EAS (https://expo.dev/pricing، ۲۰۲۶-۱۰-۳۰): Free ‏۰ دلار؛ Starter ‏۱۹ دلار در ماه + مصرف؛ Production ‏۱۹۹ دلار در ماه + مصرف؛ Enterprise سفارشی. (صفحه نگفت کدام طرح پولی دقیقاً به جست‌وجوی مستندات سمت سرور دسترسی می‌دهد ❓.)

## ریسک و هشدار
⚠️ OAuth به حساب و ساخت‌های Expo دسترسی می‌دهد.

## مرتبط
- [expo-skills](expo-skills.md): اسکیل‌های رسمی Expo که همین MCP را ثبت می‌کنند (assess)
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41)
