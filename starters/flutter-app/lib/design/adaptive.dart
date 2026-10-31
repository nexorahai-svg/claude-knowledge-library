import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'tokens.dart';

/// Material window size classes (width, dp). Layout decisions use the window
/// size, never "is this a phone/tablet" (Flutter adaptive best practices).
enum WindowClass { compact, medium, expanded }

WindowClass windowClassOf(BuildContext context) {
  final w = MediaQuery.sizeOf(context).width;
  if (w < 600) return WindowClass.compact;
  if (w < 840) return WindowClass.medium;
  return WindowClass.expanded;
}

/// Uses the Theme's platform (not dart:io) so tests can force iOS or Android.
bool isCupertino(BuildContext context) {
  final p = Theme.of(context).platform;
  return p == TargetPlatform.iOS || p == TargetPlatform.macOS;
}

class Destination {
  const Destination(this.label, this.icon, this.selectedIcon);

  final String label;
  final IconData icon;
  final IconData selectedIcon;
}

/// Top-level navigation that follows each platform:
///   compact  → bottom bar: Material NavigationBar on Android, CupertinoTabBar on iOS
///   medium   → NavigationRail (icons + labels)
///   expanded → extended NavigationRail beside the content
/// 3–5 destinations, labels always visible, never hidden or disabled.
class AdaptiveScaffold extends StatelessWidget {
  const AdaptiveScaffold({
    super.key,
    required this.destinations,
    required this.selectedIndex,
    required this.onSelect,
    required this.body,
  }) : assert(destinations.length >= 2 && destinations.length <= 5);

  final List<Destination> destinations;
  final int selectedIndex;
  final ValueChanged<int> onSelect;
  final Widget body;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    final size = windowClassOf(context);

    if (size == WindowClass.compact) {
      return Scaffold(
        body: body,
        bottomNavigationBar: isCupertino(context)
            ? CupertinoTabBar(
                currentIndex: selectedIndex,
                onTap: onSelect,
                activeColor: t.accent,
                inactiveColor: t.muted,
                backgroundColor: t.surface.withValues(alpha: 0.94),
                border: Border(top: BorderSide(color: t.line, width: 0.5)),
                items: [
                  for (final d in destinations)
                    BottomNavigationBarItem(icon: Icon(d.icon), activeIcon: Icon(d.selectedIcon), label: d.label),
                ],
              )
            : NavigationBar(
                selectedIndex: selectedIndex,
                onDestinationSelected: onSelect,
                destinations: [
                  for (final d in destinations)
                    NavigationDestination(icon: Icon(d.icon), selectedIcon: Icon(d.selectedIcon), label: d.label),
                ],
              ),
      );
    }

    return Scaffold(
      body: SafeArea(
        child: Row(
          children: [
            NavigationRail(
              selectedIndex: selectedIndex,
              onDestinationSelected: onSelect,
              extended: size == WindowClass.expanded,
              labelType: size == WindowClass.expanded ? NavigationRailLabelType.none : NavigationRailLabelType.all,
              destinations: [
                for (final d in destinations)
                  NavigationRailDestination(icon: Icon(d.icon), selectedIcon: Icon(d.selectedIcon), label: Text(d.label)),
              ],
            ),
            VerticalDivider(width: 1, color: t.line),
            // Keep reading width comfortable on big screens.
            Expanded(
              child: Align(
                alignment: AlignmentDirectional.topCenter,
                child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 960), child: body),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Bottom sheet that follows the platform: Material sheet with drag handle on
/// Android, Cupertino modal popup on iOS. One sheet at a time (Apple HIG).
Future<T?> showAppSheet<T>(BuildContext context, {required WidgetBuilder builder}) {
  if (isCupertino(context)) {
    return showCupertinoModalPopup<T>(
      context: context,
      builder: (ctx) {
        final t = ctx.tokens;
        return Container(
          padding: const EdgeInsets.fromLTRB(20, 12, 20, 20),
          decoration: BoxDecoration(
            color: t.surface,
            borderRadius: BorderRadius.vertical(top: Radius.circular(t.radiusXl)),
          ),
          child: SafeArea(top: false, child: Material(type: MaterialType.transparency, child: builder(ctx))),
        );
      },
    );
  }
  return showModalBottomSheet<T>(
    context: context,
    isScrollControlled: true,
    useSafeArea: true,
    builder: (ctx) => Padding(padding: const EdgeInsets.fromLTRB(20, 0, 20, 20), child: builder(ctx)),
  );
}
