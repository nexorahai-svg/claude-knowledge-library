import 'package:flutter/material.dart';

import '../design/adaptive.dart';
import '../design/styles.dart';
import '../design/tokens.dart';
import '../main.dart';
import '../strings.dart';
import '../widgets/primary_button.dart';
import '../widgets/states.dart';

/// Living style guide: every pattern of the library's screen catalogue in the
/// active style, mode and language. Start a new app by replacing these pages.
class GalleryShell extends StatefulWidget {
  const GalleryShell({super.key, this.initialIndex = 0});

  final int initialIndex;

  @override
  State<GalleryShell> createState() => _GalleryShellState();
}

class _GalleryShellState extends State<GalleryShell> {
  late int _index = widget.initialIndex;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return AdaptiveScaffold(
      selectedIndex: _index,
      onSelect: (i) => setState(() => _index = i),
      destinations: [
        Destination(s.home, Icons.home_outlined, Icons.home_rounded),
        Destination(s.search, Icons.search_rounded, Icons.saved_search_rounded),
        Destination(s.states, Icons.layers_outlined, Icons.layers_rounded),
        Destination(s.settings, Icons.tune_outlined, Icons.tune_rounded),
      ],
      body: IndexedStack(
        index: _index,
        children: const [HomePage(), SearchPage(), StatesPage(), SettingsPage()],
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key, this.loadDelay = const Duration(milliseconds: 900)});

  final Duration loadDelay;

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    if (widget.loadDelay == Duration.zero) {
      _loading = false;
    } else {
      Future.delayed(widget.loadDelay, () {
        if (mounted) setState(() => _loading = false);
      });
    }
  }

  static const _items = [
    (Icons.villa_rounded, 'Marina suite', 640, 4.92),
    (Icons.restaurant_rounded, 'Rooftop dinner', 210, 4.81),
    (Icons.spa_rounded, 'Desert spa day', 480, 4.88),
    (Icons.directions_boat_rounded, 'Sunset cruise', 350, 4.95),
  ];

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    final s = S.of(context);
    final text = Theme.of(context).textTheme;
    return SafeArea(
      bottom: false,
      child: ListView(
        padding: const EdgeInsets.symmetric(vertical: AppTokens.s4),
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: AppTokens.s5),
            child: Row(
              children: [
                Expanded(child: Text(s.greeting, style: text.headlineMedium)),
                // Icon-only buttons need a tooltip: it is also their accessible name.
                IconButton.filledTonal(
                  tooltip: s.notifications,
                  onPressed: () {},
                  icon: const Icon(Icons.notifications_none_rounded),
                ),
              ],
            ),
          ),
          const SizedBox(height: AppTokens.s5),
          Padding(
            padding: const EdgeInsetsDirectional.only(start: AppTokens.s5, end: AppTokens.s2),
            child: Row(
              children: [
                Expanded(child: Text(s.featured, style: text.titleLarge)),
                TextButton(onPressed: () {}, child: Text(s.seeAll)),
              ],
            ),
          ),
          SizedBox(
            height: 236,
            child: ListView.separated(
              padding: const EdgeInsets.symmetric(horizontal: AppTokens.s5),
              scrollDirection: Axis.horizontal,
              itemCount: _items.length,
              separatorBuilder: (_, _) => const SizedBox(width: AppTokens.s4),
              itemBuilder: (context, i) {
                final (icon, title, price, rating) = _items[i];
                return AnimatedSwitcher(
                  duration: t.slow,
                  child: _loading
                      ? Semantics(
                          key: const ValueKey('sk'),
                          label: s.loading,
                          child: const SizedBox(
                            width: 200,
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Skeleton(height: 150),
                                SizedBox(height: 12),
                                Skeleton(width: 150, height: 14),
                                SizedBox(height: 8),
                                Skeleton(width: 90, height: 12),
                              ],
                            ),
                          ),
                        )
                      : _FeatureCard(key: ValueKey(title), icon: icon, title: title, price: s.price(price), rating: rating),
                );
              },
            ),
          ),
          const SizedBox(height: AppTokens.s4),
          for (final (icon, title, price, rating) in _items)
            ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: AppTokens.s5, vertical: AppTokens.s1),
              leading: Container(
                width: 48,
                height: 48,
                decoration: BoxDecoration(color: t.surfaceAlt, borderRadius: BorderRadius.circular(t.radiusMd)),
                child: Icon(icon, color: t.accent),
              ),
              title: Text(title, style: const TextStyle(fontWeight: FontWeight.w700)),
              subtitle: Text('★ $rating'),
              trailing: Text(s.price(price), style: const TextStyle(fontWeight: FontWeight.w800)),
              onTap: () {},
            ),
        ],
      ),
    );
  }
}

class _FeatureCard extends StatelessWidget {
  const _FeatureCard({super.key, required this.icon, required this.title, required this.price, required this.rating});

  final IconData icon;
  final String title;
  final String price;
  final double rating;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    return SizedBox(
      width: 200,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            height: 150,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(t.radiusLg),
              boxShadow: [...t.cardShadow, if (t.glow != null) BoxShadow(color: t.glow!.withValues(alpha: 0.35), blurRadius: 22)],
              gradient: LinearGradient(
                begin: AlignmentDirectional.topStart,
                end: AlignmentDirectional.bottomEnd,
                colors: [t.accent, Color.lerp(t.accent, t.canvas, 0.55)!],
              ),
            ),
            child: Icon(icon, size: 48, color: t.onAccent),
          ),
          const SizedBox(height: AppTokens.s3),
          Text(title, maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontWeight: FontWeight.w700)),
          const SizedBox(height: AppTokens.s1),
          Text('$price · ★ $rating', style: TextStyle(color: t.muted)),
        ],
      ),
    );
  }
}

class SearchPage extends StatefulWidget {
  const SearchPage({super.key});

  @override
  State<SearchPage> createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  final _selected = <int>{1};

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    const chips = ['Nearby', 'Top rated', 'Under 300', 'Open now'];
    return SafeArea(
      bottom: false,
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(AppTokens.s5, AppTokens.s4, AppTokens.s5, AppTokens.s3),
            child: TextField(
              decoration: InputDecoration(prefixIcon: const Icon(Icons.search_rounded), hintText: s.searchHint),
            ),
          ),
          SizedBox(
            height: AppTokens.minTap,
            child: ListView.separated(
              padding: const EdgeInsets.symmetric(horizontal: AppTokens.s5),
              scrollDirection: Axis.horizontal,
              itemCount: chips.length,
              separatorBuilder: (_, _) => const SizedBox(width: AppTokens.s2),
              itemBuilder: (context, i) => FilterChip(
                label: Text(chips[i]),
                selected: _selected.contains(i),
                onSelected: (v) => setState(() => v ? _selected.add(i) : _selected.remove(i)),
              ),
            ),
          ),
          Expanded(
            child: EmptyState(
              icon: Icons.travel_explore_rounded,
              title: s.noResultsTitle,
              message: s.noResultsBody,
              action: OutlinedButton(onPressed: () => setState(_selected.clear), child: Text(s.clearFilters)),
            ),
          ),
        ],
      ),
    );
  }
}

class StatesPage extends StatefulWidget {
  const StatesPage({super.key});

  @override
  State<StatesPage> createState() => _StatesPageState();
}

class _StatesPageState extends State<StatesPage> {
  final _form = GlobalKey<FormState>();
  bool _busy = false;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    final s = S.of(context);
    return SafeArea(
      bottom: false,
      child: ListView(
        children: [
          OfflineBanner(text: s.offline),
          Padding(
            padding: const EdgeInsets.all(AppTokens.s5),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Card(
                  child: ErrorState(title: s.errorTitle, message: s.errorBody, retryLabel: s.retry, onRetry: () {}),
                ),
                const SizedBox(height: AppTokens.s5),
                Form(
                  key: _form,
                  child: TextFormField(
                    keyboardType: TextInputType.emailAddress,
                    autofillHints: const [AutofillHints.email],
                    decoration: InputDecoration(labelText: s.email, prefixIcon: const Icon(Icons.mail_outline_rounded)),
                    validator: (v) => (v ?? '').contains('@') ? null : s.emailError,
                  ),
                ),
                const SizedBox(height: AppTokens.s4),
                PrimaryButton(
                  label: s.confirm,
                  loading: _busy,
                  onPressed: () async {
                    if (!_form.currentState!.validate()) return;
                    setState(() => _busy = true);
                    await Future.delayed(const Duration(seconds: 1));
                    if (mounted) setState(() => _busy = false);
                  },
                ),
                const SizedBox(height: AppTokens.s3),
                OutlinedButton(
                  onPressed: () => showAppSheet(
                    context,
                    builder: (ctx) => Column(
                      mainAxisSize: MainAxisSize.min,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        Text(s.sheetTitle, style: Theme.of(ctx).textTheme.titleLarge),
                        const SizedBox(height: AppTokens.s4),
                        for (final slot in ['10:00', '12:30', '17:00'])
                          ListTile(
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(t.radiusMd)),
                            leading: const Icon(Icons.schedule_rounded),
                            title: Text(slot),
                            onTap: () => Navigator.pop(ctx),
                          ),
                      ],
                    ),
                  ),
                  child: Text(s.openSheet),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = AppController.of(context);
    final s = S.of(context);
    final t = context.tokens;
    final text = Theme.of(context).textTheme;
    return SafeArea(
      bottom: false,
      child: ListView(
        padding: const EdgeInsets.symmetric(vertical: AppTokens.s4),
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: AppTokens.s5),
            child: Text(s.settings, style: text.headlineMedium),
          ),
          SwitchListTile.adaptive(
            title: Text(s.dark),
            value: c.mode == ThemeMode.dark || c.style.darkOnly,
            onChanged: c.style.darkOnly ? null : (v) => c.mode = v ? ThemeMode.dark : ThemeMode.light,
          ),
          ListTile(
            title: Text(s.language),
            trailing: SegmentedButton<String>(
              showSelectedIcon: false,
              segments: const [
                ButtonSegment(value: 'en', label: Text('EN')),
                ButtonSegment(value: 'fa', label: Text('فا')),
                ButtonSegment(value: 'ar', label: Text('ع')),
              ],
              selected: {c.locale.languageCode},
              onSelectionChanged: (v) => c.locale = Locale(v.first),
            ),
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(AppTokens.s5, AppTokens.s5, AppTokens.s5, AppTokens.s2),
            child: Text(s.style, style: text.titleLarge),
          ),
          RadioGroup<AppStyle>(
            groupValue: c.style,
            onChanged: (v) => c.style = v!,
            child: Column(
              children: [
                for (final style in AppStyle.values)
                  RadioListTile<AppStyle>.adaptive(
                    value: style,
                    title: Text(style.label, style: const TextStyle(fontWeight: FontWeight.w700)),
                    subtitle: Text(style.bestFor, style: TextStyle(color: t.muted)),
                    secondary: _Swatch(style: style),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _Swatch extends StatelessWidget {
  const _Swatch({required this.style});

  final AppStyle style;

  @override
  Widget build(BuildContext context) {
    final t = style.tokens(Theme.of(context).brightness);
    return ExcludeSemantics(
      child: Container(
        width: 40,
        height: 40,
        decoration: BoxDecoration(
          color: t.canvas,
          shape: BoxShape.circle,
          border: Border.all(color: context.tokens.line),
        ),
        alignment: Alignment.center,
        child: CircleAvatar(radius: 11, backgroundColor: t.accent),
      ),
    );
  }
}
