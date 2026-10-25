import 'dart:convert';

import 'package:app_starter/design/styles.dart';
import 'package:app_starter/main.dart';
import 'package:app_starter/screens/gallery.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

/// Loads every font in the asset manifest (brand fonts and Material icons), so
/// goldens show real text instead of the test font's boxes.
Future<void> loadAppFonts() async {
  final manifest = json.decode(await rootBundle.loadString('FontManifest.json')) as List<dynamic>;
  for (final f in manifest.cast<Map<String, dynamic>>()) {
    final loader = FontLoader(f['family'] as String);
    for (final a in (f['fonts'] as List).cast<Map<String, dynamic>>()) {
      loader.addFont(rootBundle.load(a['asset'] as String));
    }
    await loader.load();
  }
}

/// A phone-sized window (iPhone/Pixel class: 390 × 844 logical px).
void usePhone(WidgetTester tester, {Size size = const Size(390, 844)}) {
  tester.view.physicalSize = size * 3;
  tester.view.devicePixelRatio = 3;
  addTearDown(tester.view.reset);
}

Widget app({
  AppStyle style = AppStyle.cleanMarket,
  ThemeMode mode = ThemeMode.light,
  String lang = 'en',
  int tab = 0,
  TargetPlatform platform = TargetPlatform.android,
}) {
  debugDefaultTargetPlatformOverride = platform;
  return StarterApp(
    controller: AppController(style: style, mode: mode, locale: Locale(lang)),
    home: GalleryShell(initialIndex: tab),
  );
}
