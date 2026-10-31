import 'package:flutter/material.dart';

import 'tokens.dart';

/// Named visual styles. Pick one in the design brief, then tune the accent to
/// the brand. Descriptions mirror domains/apps/app-styles.md in the library.
enum AppStyle {
  cleanMarket(
    'Clean marketplace',
    'Bookings, rentals, shops, listings: big photos, white space, one warm accent.',
  ),
  freshGreen(
    'Fresh dashboard',
    'Inventory, sales, admin on mobile: light, one glowing green, gauges, product cut-outs.',
  ),
  glassDash(
    'Night glass',
    'Analytics and control apps that live on screen: deep navy, frosted cards, coral accent.',
  ),
  neonNight(
    'Neon night',
    'Gaming, nightlife, music, launches: near-black, pink/cyan light, glitch and glow motion.',
  ),
  luxuryGold(
    'Luxury noir',
    'Perfume, jewellery, hotels, premium services: black, warm gold, wide-tracked serif titles.',
  ),
  fintechMinimal(
    'Minimal fintech',
    'Banking, wallets, B2B tools: white, ink, one cool blue, numbers first, very little motion.',
  ),
  calmHealth(
    'Calm care',
    'Health, clinics, wellbeing, government services: soft mint, teal, generous spacing, no urgency.',
  ),
  playful(
    'Playful',
    'Kids, education, social, habits: warm cream, violet, big radii, bouncy motion.',
  );

  const AppStyle(this.label, this.bestFor);

  final String label;
  final String bestFor;

  /// Only some styles are designed for both modes; dark-only styles ignore [Brightness.light].
  bool get darkOnly => this == neonNight || this == glassDash || this == luxuryGold;

  AppTokens tokens(Brightness brightness) {
    final dark = brightness == Brightness.dark || darkOnly;
    switch (this) {
      case cleanMarket:
        return dark
            ? _darkNeutral(accent: const Color(0xFFFF6B75), onAccent: const Color(0xFF1B0507))
            : const AppTokens(
                accent: Color(0xFFD63B4A),
                onAccent: Colors.white,
                ink: Color(0xFF16161A),
                muted: Color(0xFF6A6A72),
                line: Color(0xFFE6E6EB),
                canvas: Colors.white,
                surface: Colors.white,
                surfaceAlt: Color(0xFFF5F5F7),
                success: Color(0xFF16834F),
                warning: Color(0xFFB45309),
                danger: Color(0xFFC62828),
              );
      case freshGreen:
        return dark
            ? _darkNeutral(accent: const Color(0xFF34D27B), onAccent: const Color(0xFF04140B), glow: const Color(0xFF34D27B))
            : const AppTokens(
                accent: Color(0xFF12804A),
                onAccent: Colors.white,
                ink: Color(0xFF111418),
                muted: Color(0xFF5F6670),
                line: Color(0xFFDDE7E1),
                canvas: Color(0xFFF2F5F8),
                surface: Colors.white,
                surfaceAlt: Color(0xFFEAF6EF),
                success: Color(0xFF12804A),
                warning: Color(0xFFB45309),
                danger: Color(0xFFC62828),
                radiusLg: 22,
                glow: Color(0x5534D27B),
                cardShadow: [BoxShadow(color: Color(0x1A12804A), blurRadius: 24, offset: Offset(0, 8))],
              );
      case glassDash:
        return const AppTokens(
          accent: Color(0xFFFF8A5B),
          onAccent: Color(0xFF1C0E07),
          ink: Color(0xFFF2F4FA),
          muted: Color(0xFFA3ABC2),
          line: Color(0x29FFFFFF),
          canvas: Color(0xFF0D1120),
          surface: Color(0xFF181E33),
          surfaceAlt: Color(0xFF222A44),
          success: Color(0xFF4ADE80),
          warning: Color(0xFFFBBF24),
          danger: Color(0xFFFF6B6B),
          radiusLg: 24,
          cardShadow: [BoxShadow(color: Color(0x66000000), blurRadius: 30, offset: Offset(0, 12))],
        );
      case neonNight:
        return const AppTokens(
          accent: Color(0xFF2EF2FF),
          onAccent: Color(0xFF05060C),
          ink: Color(0xFFF5F5FA),
          muted: Color(0xFFA7A7B8),
          line: Color(0x26FFFFFF),
          canvas: Color(0xFF07070F),
          surface: Color(0xFF12121C),
          surfaceAlt: Color(0xFF1C1C2A),
          success: Color(0xFF3CF29B),
          warning: Color(0xFFFFD166),
          danger: Color(0xFFFF4D8D),
          glow: Color(0xFFFF3DCB),
          cardShadow: [BoxShadow(color: Color(0x552EF2FF), blurRadius: 24)],
        );
      case luxuryGold:
        return const AppTokens(
          accent: Color(0xFFCDAA63),
          onAccent: Color(0xFF15120D),
          ink: Color(0xFFF4EFE6),
          muted: Color(0xFFADA393),
          line: Color(0x33CDAA63),
          canvas: Color(0xFF0B0A08),
          surface: Color(0xFF17140F),
          surfaceAlt: Color(0xFF221D16),
          success: Color(0xFF7BC47F),
          warning: Color(0xFFE0B354),
          danger: Color(0xFFE57373),
          radiusSm: 2,
          radiusMd: 4,
          radiusLg: 6,
          radiusXl: 10,
          cardShadow: [],
        );
      case fintechMinimal:
        return dark
            ? _darkNeutral(accent: const Color(0xFF7C9CFF), onAccent: const Color(0xFF070B1A))
            : const AppTokens(
                accent: Color(0xFF2F4BD6),
                onAccent: Colors.white,
                ink: Color(0xFF0B0F19),
                muted: Color(0xFF5B6272),
                line: Color(0xFFE5E8EF),
                canvas: Colors.white,
                surface: Color(0xFFFAFBFD),
                surfaceAlt: Color(0xFFF1F3F8),
                success: Color(0xFF15803D),
                warning: Color(0xFFB45309),
                danger: Color(0xFFB91C1C),
                radiusLg: 16,
                cardShadow: [],
              );
      case calmHealth:
        return dark
            ? _darkNeutral(accent: const Color(0xFF5EEAD4), onAccent: const Color(0xFF042521))
            : const AppTokens(
                accent: Color(0xFF0F766E),
                onAccent: Colors.white,
                ink: Color(0xFF12201E),
                muted: Color(0xFF55615F),
                line: Color(0xFFDCE8E6),
                canvas: Color(0xFFF5FAF9),
                surface: Colors.white,
                surfaceAlt: Color(0xFFE8F4F2),
                success: Color(0xFF15803D),
                warning: Color(0xFFB45309),
                danger: Color(0xFFB91C1C),
                radiusLg: 22,
                radiusXl: 32,
              );
      case playful:
        return dark
            ? _darkNeutral(accent: const Color(0xFFB794FF), onAccent: const Color(0xFF14082B))
            : const AppTokens(
                accent: Color(0xFF6D28D9),
                onAccent: Colors.white,
                ink: Color(0xFF1E1530),
                muted: Color(0xFF625A70),
                line: Color(0xFFEFE3D3),
                canvas: Color(0xFFFFF8EF),
                surface: Colors.white,
                surfaceAlt: Color(0xFFFFEFD9),
                success: Color(0xFF15803D),
                warning: Color(0xFFB45309),
                danger: Color(0xFFC62828),
                radiusMd: 18,
                radiusLg: 26,
                radiusXl: 36,
              );
    }
  }
}

AppTokens _darkNeutral({required Color accent, required Color onAccent, Color? glow}) => AppTokens(
      accent: accent,
      onAccent: onAccent,
      ink: const Color(0xFFF2F2F5),
      muted: const Color(0xFFA2A2AD),
      line: const Color(0xFF2C2C33),
      canvas: const Color(0xFF0F0F12),
      surface: const Color(0xFF18181D),
      surfaceAlt: const Color(0xFF222228),
      success: const Color(0xFF4ADE80),
      warning: const Color(0xFFFBBF24),
      danger: const Color(0xFFFF6B6B),
      glow: glow,
      cardShadow: const [BoxShadow(color: Color(0x66000000), blurRadius: 20, offset: Offset(0, 8))],
    );
