@Tags(['golden'])
library;

import 'package:app_starter/design/styles.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'helpers.dart';

/// Visual snapshots: the home screen in every style (the library's style
/// catalogue images come from here), plus RTL and iOS variants.
/// Update after an intended change: flutter test --update-goldens --tags golden
void main() {
  setUpAll(loadAppFonts);

  Future<void> shot(WidgetTester tester, String name, Widget w) async {
    usePhone(tester);
    await tester.pumpWidget(w);
    await tester.pump(const Duration(seconds: 1));
    await tester.pump(const Duration(milliseconds: 500));
    await expectLater(find.byType(MaterialApp), matchesGoldenFile('goldens/$name.png'));
    debugDefaultTargetPlatformOverride = null;
  }

  for (final style in AppStyle.values) {
    testWidgets('home ${style.name}', (t) => shot(t, 'home_${style.name}', app(style: style)));
  }
  testWidgets('home cleanMarket dark fa', (t) => shot(t, 'home_cleanMarket_dark_fa', app(mode: ThemeMode.dark, lang: 'fa')));
  testWidgets('settings ios', (t) => shot(t, 'settings_ios', app(tab: 3, platform: TargetPlatform.iOS)));
  testWidgets('states ar', (t) => shot(t, 'states_ar', app(tab: 2, lang: 'ar', style: AppStyle.calmHealth)));
}
