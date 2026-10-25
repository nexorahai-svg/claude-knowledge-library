---
name: Dart و Flutter MCP Server
slug: dart-mcp-server
category: app-testing
domains: [apps]
verdict: adopt
status: researched
summary: MCP رسمی تیم Dart که عامل را به اپ Flutter در حال اجرا وصل می‌کند
url: https://docs.flutter.dev/ai/mcp-server
repo: "https://github.com/dart-lang/ai"
license: "BSD-3-Clause"
pricing: free
risk: medium
sources: [S41, S38]
found_in: []
last_checked: 2026-10-17
next_check: "2027-01-15"
---

# Dart و Flutter MCP Server

## چیست
✅ dart_mcp_server 1.2.1، همراه Dart SDK؛ فرمان `dart mcp-server`. اجرا و توقف اپ، hot reload، تست، لاگ، درخت ویجت. برچسب «آزمایشی».

## کی استفاده کنیم
🧭 هر پروژه‌ی Flutter.

## قیمت و مجوز
✅ رایگان.

## ریسک و هشدار
⚠️ پروسه اجرا و متوقف می‌کند و تست اجرا می‌کند. ✅ دستوری که روی رایانه‌ی اصلی کار کرد و `claude mcp list` آن را «Connected» نشان داد (۲۰۲۶-۱۰-۲۱، Dart 3.13.5):
```bash
claude mcp add dart --scope user -- ~/development/flutter/bin/dart mcp-server
```

## مرتبط
[تست اپ](../domains/apps/app-testing.md) · [S41](../sources/README.md#s41) · [S38](../sources/README.md#s38)
