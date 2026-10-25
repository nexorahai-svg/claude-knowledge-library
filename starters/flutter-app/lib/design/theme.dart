import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'styles.dart';
import 'tokens.dart';

/// Builds the whole ThemeData from a style + mode + language, so components
/// (buttons, fields, bars, sheets) follow the tokens without per-screen styling.
ThemeData buildAppTheme(AppStyle style, Brightness requested, {required bool rtlScript}) {
  final t = style.tokens(requested);
  final brightness = style.darkOnly ? Brightness.dark : requested;
  // Persian/Arabic need a font with those glyphs; Latin keeps the brand font.
  final family = rtlScript ? 'Vazirmatn' : 'PlusJakartaSans';
  // Mixed text (an English brand inside Persian, or a Persian name in English)
  // falls back to the other bundled font instead of the device's.
  final fallback = [rtlScript ? 'PlusJakartaSans' : 'Vazirmatn'];
  TextStyle f(TextStyle s) => s.copyWith(fontFamily: family, fontFamilyFallback: fallback);

  final scheme = ColorScheme(
    brightness: brightness,
    primary: t.accent,
    onPrimary: t.onAccent,
    secondary: t.accent,
    onSecondary: t.onAccent,
    error: t.danger,
    onError: Colors.white,
    surface: t.surface,
    onSurface: t.ink,
    onSurfaceVariant: t.muted,
    outline: t.line,
    outlineVariant: t.line,
    surfaceContainerLowest: t.canvas,
    surfaceContainerLow: t.surface,
    surfaceContainer: t.surfaceAlt,
    surfaceContainerHigh: t.surfaceAlt,
    surfaceContainerHighest: t.surfaceAlt,
  );

  final base = ThemeData(
    useMaterial3: true,
    brightness: brightness,
    colorScheme: scheme,
    fontFamily: family,
    fontFamilyFallback: fallback,
    scaffoldBackgroundColor: t.canvas,
    // Cupertino widgets (iOS tab bar, adaptive switches/dialogs) use the same fonts.
    cupertinoOverrideTheme: CupertinoThemeData(
      brightness: brightness,
      primaryColor: t.accent,
      textTheme: CupertinoTextThemeData(
        primaryColor: t.accent,
        textStyle: TextStyle(fontFamily: family, fontFamilyFallback: fallback, color: t.ink, fontSize: 17),
        tabLabelTextStyle: TextStyle(fontFamily: family, fontFamilyFallback: fallback, fontSize: 11, fontWeight: FontWeight.w700),
        navTitleTextStyle: TextStyle(fontFamily: family, fontFamilyFallback: fallback, color: t.ink, fontSize: 17, fontWeight: FontWeight.w700),
        actionTextStyle: TextStyle(fontFamily: family, fontFamilyFallback: fallback, color: t.accent, fontSize: 17),
      ),
    ),
    extensions: [t],
  );

  final text = base.textTheme.apply(fontFamily: family, fontFamilyFallback: fallback, bodyColor: t.ink, displayColor: t.ink);
  RoundedRectangleBorder shape(double r) => RoundedRectangleBorder(borderRadius: BorderRadius.circular(r));

  return base.copyWith(
    textTheme: text.copyWith(
      headlineMedium: text.headlineMedium?.copyWith(fontWeight: FontWeight.w800, letterSpacing: -0.5),
      titleLarge: text.titleLarge?.copyWith(fontWeight: FontWeight.w800, letterSpacing: -0.3),
      titleMedium: text.titleMedium?.copyWith(fontWeight: FontWeight.w700),
      bodyMedium: text.bodyMedium?.copyWith(height: rtlScript ? 1.6 : 1.4),
      bodySmall: text.bodySmall?.copyWith(color: t.muted),
    ),
    appBarTheme: AppBarTheme(
      backgroundColor: t.canvas,
      foregroundColor: t.ink,
      surfaceTintColor: Colors.transparent,
      elevation: 0,
      centerTitle: false,
    ),
    cardTheme: CardThemeData(
      color: t.surface,
      elevation: 0,
      margin: EdgeInsets.zero,
      shape: shape(t.radiusLg).copyWith(side: BorderSide(color: t.line)),
    ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        backgroundColor: t.accent,
        foregroundColor: t.onAccent,
        minimumSize: const Size(AppTokens.minTap, 52),
        shape: shape(t.radiusMd),
        textStyle: f(const TextStyle(fontWeight: FontWeight.w700, fontSize: 15)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: t.ink,
        minimumSize: const Size(AppTokens.minTap, 52),
        side: BorderSide(color: t.line, width: 1.4),
        shape: shape(t.radiusMd),
        textStyle: f(const TextStyle(fontWeight: FontWeight.w700, fontSize: 15)),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        textStyle: f(const TextStyle(fontWeight: FontWeight.w600)),
        foregroundColor: t.accent,
        minimumSize: const Size(AppTokens.minTap, AppTokens.minTap),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: t.surfaceAlt,
      hintStyle: TextStyle(color: t.muted),
      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(t.radiusMd), borderSide: BorderSide.none),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(t.radiusMd),
        borderSide: BorderSide(color: t.accent, width: 1.6),
      ),
      errorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(t.radiusMd),
        borderSide: BorderSide(color: t.danger, width: 1.4),
      ),
    ),
    navigationBarTheme: NavigationBarThemeData(
      backgroundColor: t.surface,
      indicatorColor: t.accent.withValues(alpha: 0.16),
      surfaceTintColor: Colors.transparent,
      iconTheme: WidgetStateProperty.resolveWith(
        (s) => IconThemeData(color: s.contains(WidgetState.selected) ? t.accent : t.muted),
      ),
      labelTextStyle: WidgetStateProperty.resolveWith(
        (s) => TextStyle(
          fontFamily: family,
          fontFamilyFallback: fallback,
          fontSize: 12,
          fontWeight: s.contains(WidgetState.selected) ? FontWeight.w700 : FontWeight.w500,
          color: s.contains(WidgetState.selected) ? t.ink : t.muted,
        ),
      ),
    ),
    navigationRailTheme: NavigationRailThemeData(
      backgroundColor: t.surface,
      indicatorColor: t.accent.withValues(alpha: 0.16),
      selectedIconTheme: IconThemeData(color: t.accent),
      unselectedIconTheme: IconThemeData(color: t.muted),
    ),
    bottomSheetTheme: BottomSheetThemeData(
      backgroundColor: t.surface,
      surfaceTintColor: Colors.transparent,
      showDragHandle: true,
      dragHandleColor: t.line,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(t.radiusXl))),
    ),
    segmentedButtonTheme: SegmentedButtonThemeData(
      style: ButtonStyle(textStyle: WidgetStatePropertyAll(f(const TextStyle(fontWeight: FontWeight.w600)))),
    ),
    dividerTheme: DividerThemeData(color: t.line, thickness: 1, space: 1),
    chipTheme: ChipThemeData(
      backgroundColor: t.surfaceAlt,
      selectedColor: t.accent.withValues(alpha: 0.16),
      side: BorderSide.none,
      shape: shape(999),
      labelStyle: f(TextStyle(color: t.ink, fontWeight: FontWeight.w600)),
    ),
    snackBarTheme: SnackBarThemeData(
      behavior: SnackBarBehavior.floating,
      backgroundColor: t.ink,
      contentTextStyle: f(TextStyle(color: t.canvas)),
      shape: shape(t.radiusMd),
    ),
  );
}
