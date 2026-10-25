import 'package:app_starter/design/styles.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'helpers.dart';

/// Flutter's official accessibility guidelines on every gallery tab, for both
/// platforms, light and dark, left-to-right and right-to-left.
void main() {
  const cases = [
    (AppStyle.cleanMarket, ThemeMode.light, 'en', TargetPlatform.android),
    (AppStyle.cleanMarket, ThemeMode.dark, 'fa', TargetPlatform.iOS),
    (AppStyle.neonNight, ThemeMode.dark, 'ar', TargetPlatform.android),
    (AppStyle.freshGreen, ThemeMode.light, 'fa', TargetPlatform.iOS),
  ];

  for (final (style, mode, lang, platform) in cases) {
    for (var tab = 0; tab < 4; tab++) {
      testWidgets('a11y ${style.name} ${mode.name} $lang ${platform.name} tab $tab', (tester) async {
        usePhone(tester);
        final handle = tester.ensureSemantics();
        await tester.pumpWidget(app(style: style, mode: mode, lang: lang, tab: tab, platform: platform));
        await tester.pump(const Duration(seconds: 1)); // finish the simulated load
        await tester.pump(const Duration(milliseconds: 500));

        await expectLater(tester, meetsGuideline(androidTapTargetGuideline));
        await expectLater(tester, meetsGuideline(iOSTapTargetGuideline));
        await expectLater(tester, meetsGuideline(labeledTapTargetGuideline));
        await expectLater(tester, meetsGuideline(textContrastGuideline));

        handle.dispose();
        debugDefaultTargetPlatformOverride = null;
      });
    }
  }
}
