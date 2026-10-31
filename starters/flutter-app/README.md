# Flutter app starter

Starting point for every new Flutter app (Android + iOS). It carries the library's
design system so a new app begins with tokens, a chosen style, platform-correct
navigation, the five data states, RTL, and the design QA tests already green.

Persian guide: `domains/apps/app-design-system.md` in the knowledge library.

## Start a new app

```bash
cp -r <library>/starters/flutter-app ~/Desktop/<my_app>
cd ~/Desktop/<my_app>
# rename the package in pubspec.yaml (name: my_app) and in test imports, then:
flutter create --org com.<company> --project-name my_app --platforms android,ios .
flutter pub get
flutter analyze && flutter test
```

`flutter create .` only adds the missing platform folders; it does not overwrite `lib/`.

## What is inside

| File | What it gives you |
|---|---|
| `lib/design/tokens.dart` | `AppTokens` theme extension: colour roles, radii, 4-pt spacing, motion, shadows, glow; `contrastRatio()` |
| `lib/design/styles.dart` | 8 named styles (`AppStyle`), light/dark where the style allows |
| `lib/design/theme.dart` | One `ThemeData` from style + mode + script: buttons, fields, bars, sheets, chips; Cupertino fonts; Latin/Persian font fallback |
| `lib/design/adaptive.dart` | Window size classes (600 / 840 dp), `AdaptiveScaffold` (Material bar on Android, Cupertino tab bar on iOS, rail on tablets), `showAppSheet` |
| `lib/widgets/states.dart` | `EmptyState`, `ErrorState`, `OfflineBanner`, `Skeleton` (respects reduce motion) |
| `lib/widgets/primary_button.dart` | Prominent action with pressed, loading and disabled states plus haptic |
| `lib/strings.dart` | Tiny EN/FA/AR table for the gallery; real apps use `flutter gen-l10n` |
| `lib/screens/gallery.dart` | Living style guide: home, search, states, settings (switch style, mode, language live) |
| `test/tokens_test.dart` | Every style's text/background pairs meet WCAG contrast |
| `test/a11y_test.dart` | Flutter's 4 accessibility guidelines on all tabs, Android + iOS, light + dark, LTR + RTL |
| `test/golden_test.dart` | Snapshots of every style plus RTL and iOS (`--tags golden`) |
| `assets/fonts/` | Plus Jakarta Sans 400–800 and Vazirmatn 400/600/800 (OFL, licences included) |

## Rules this starter enforces

- Screens read `context.tokens`; no raw colours, radii or durations in screens.
- One prominent button per view; every icon-only button has a `tooltip` (its accessible name).
- Every data screen implements loading, content, empty, error and offline.
- Layout decisions use window size, not "phone or tablet".
- Platform choice comes from `Theme.of(context).platform`, so tests can force iOS.

## Checks

```bash
flutter analyze
flutter test --exclude-tags golden   # tokens + accessibility
flutter test --tags golden           # visual snapshots
flutter test --tags golden --update-goldens   # after an intended visual change
```

Goldens are rendered by the test engine with the bundled fonts; regenerate them on the
machine that runs CI if pixels differ between operating systems.
