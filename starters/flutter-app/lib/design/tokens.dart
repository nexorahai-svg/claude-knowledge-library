import 'dart:ui' show lerpDouble;

import 'package:flutter/material.dart';

/// Every visual decision of an app lives here, once. Screens read tokens
/// through `context.tokens`; they never hard-code colours, radii or durations.
///
/// Colour roles (not raw colours) so a style preset or dark mode can swap them:
///   accent      – the one brand colour: primary buttons, selected state, key numbers
///   onAccent    – text/icons placed on [accent]
///   ink         – primary text
///   muted       – secondary text, inactive icons
///   line        – dividers, outlines
///   canvas      – page background
///   surface     – cards, sheets
///   surfaceAlt  – grouped sections, chips, skeleton base
///   success / warning / danger – status only, never decoration
@immutable
class AppTokens extends ThemeExtension<AppTokens> {
  const AppTokens({
    required this.accent,
    required this.onAccent,
    required this.ink,
    required this.muted,
    required this.line,
    required this.canvas,
    required this.surface,
    required this.surfaceAlt,
    required this.success,
    required this.warning,
    required this.danger,
    this.radiusSm = 8,
    this.radiusMd = 14,
    this.radiusLg = 20,
    this.radiusXl = 28,
    this.fast = const Duration(milliseconds: 150),
    this.base = const Duration(milliseconds: 250),
    this.slow = const Duration(milliseconds: 400),
    this.easeOut = Curves.easeOutCubic,
    this.easeInOut = Curves.easeInOutCubic,
    this.cardShadow = const [
      BoxShadow(color: Color(0x14000000), blurRadius: 18, offset: Offset(0, 6)),
    ],
    this.glow,
  });

  final Color accent, onAccent, ink, muted, line, canvas, surface, surfaceAlt;
  final Color success, warning, danger;
  final double radiusSm, radiusMd, radiusLg, radiusXl;
  final Duration fast, base, slow;
  final Curve easeOut, easeInOut;
  final List<BoxShadow> cardShadow;

  /// Optional coloured halo for styles that use light (neon, glow accents).
  final Color? glow;

  /// 4-point spacing scale. Use these, not ad-hoc numbers.
  static const double s1 = 4, s2 = 8, s3 = 12, s4 = 16, s5 = 20, s6 = 24, s8 = 32, s10 = 40, s12 = 48;

  /// Smallest tap target. Android asks for 48×48 dp, iOS for 44×44 pt; 48 satisfies both.
  static const double minTap = 48;

  @override
  AppTokens copyWith({
    Color? accent,
    Color? onAccent,
    Color? ink,
    Color? muted,
    Color? line,
    Color? canvas,
    Color? surface,
    Color? surfaceAlt,
    Color? success,
    Color? warning,
    Color? danger,
    double? radiusSm,
    double? radiusMd,
    double? radiusLg,
    double? radiusXl,
    List<BoxShadow>? cardShadow,
    Color? glow,
  }) {
    return AppTokens(
      accent: accent ?? this.accent,
      onAccent: onAccent ?? this.onAccent,
      ink: ink ?? this.ink,
      muted: muted ?? this.muted,
      line: line ?? this.line,
      canvas: canvas ?? this.canvas,
      surface: surface ?? this.surface,
      surfaceAlt: surfaceAlt ?? this.surfaceAlt,
      success: success ?? this.success,
      warning: warning ?? this.warning,
      danger: danger ?? this.danger,
      radiusSm: radiusSm ?? this.radiusSm,
      radiusMd: radiusMd ?? this.radiusMd,
      radiusLg: radiusLg ?? this.radiusLg,
      radiusXl: radiusXl ?? this.radiusXl,
      fast: fast,
      base: base,
      slow: slow,
      easeOut: easeOut,
      easeInOut: easeInOut,
      cardShadow: cardShadow ?? this.cardShadow,
      glow: glow ?? this.glow,
    );
  }

  @override
  AppTokens lerp(AppTokens? other, double t) {
    if (other == null) return this;
    Color c(Color a, Color b) => Color.lerp(a, b, t)!;
    double d(double a, double b) => lerpDouble(a, b, t)!;
    return AppTokens(
      accent: c(accent, other.accent),
      onAccent: c(onAccent, other.onAccent),
      ink: c(ink, other.ink),
      muted: c(muted, other.muted),
      line: c(line, other.line),
      canvas: c(canvas, other.canvas),
      surface: c(surface, other.surface),
      surfaceAlt: c(surfaceAlt, other.surfaceAlt),
      success: c(success, other.success),
      warning: c(warning, other.warning),
      danger: c(danger, other.danger),
      radiusSm: d(radiusSm, other.radiusSm),
      radiusMd: d(radiusMd, other.radiusMd),
      radiusLg: d(radiusLg, other.radiusLg),
      radiusXl: d(radiusXl, other.radiusXl),
      fast: t < 0.5 ? fast : other.fast,
      base: t < 0.5 ? base : other.base,
      slow: t < 0.5 ? slow : other.slow,
      easeOut: t < 0.5 ? easeOut : other.easeOut,
      easeInOut: t < 0.5 ? easeInOut : other.easeInOut,
      cardShadow: BoxShadow.lerpList(cardShadow, other.cardShadow, t) ?? cardShadow,
      glow: Color.lerp(glow, other.glow, t),
    );
  }

  /// Text/background pairs that must stay readable. The token test checks
  /// each against WCAG: 4.5:1 for body text, 3:1 for large text and icons.
  Map<String, (Color, Color, double)> get contrastPairs => {
        'ink on canvas': (ink, canvas, 4.5),
        'ink on surface': (ink, surface, 4.5),
        'muted on canvas': (muted, canvas, 4.5),
        'muted on surface': (muted, surface, 4.5),
        'onAccent on accent': (onAccent, accent, 4.5),
        'accent on canvas (icons, large text)': (accent, canvas, 3),
        'danger on surface': (danger, surface, 3),
      };
}

extension AppTokensX on BuildContext {
  AppTokens get tokens => Theme.of(this).extension<AppTokens>()!;
}

/// WCAG 2.x contrast ratio between two opaque colours.
double contrastRatio(Color a, Color b) {
  final la = a.computeLuminance(), lb = b.computeLuminance();
  final hi = la > lb ? la : lb, lo = la > lb ? lb : la;
  return (hi + 0.05) / (lo + 0.05);
}
