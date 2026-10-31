import 'package:app_starter/design/styles.dart';
import 'package:app_starter/design/tokens.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Design-token oracle: every style, in every mode it supports, must keep its
/// text/background pairs readable (WCAG 4.5:1 body, 3:1 large text/icons).
void main() {
  for (final style in AppStyle.values) {
    for (final b in style.darkOnly ? [Brightness.dark] : Brightness.values) {
      test('${style.name} ${b.name} contrast', () {
        final failures = <String>[];
        style.tokens(b).contrastPairs.forEach((name, pair) {
          final (fg, bg, min) = pair;
          final r = contrastRatio(fg, bg);
          if (r < min) failures.add('$name ${r.toStringAsFixed(2)} < $min');
        });
        expect(failures, isEmpty);
      });
    }
  }
}
