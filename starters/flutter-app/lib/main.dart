import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'design/styles.dart';
import 'design/theme.dart';
import 'screens/gallery.dart';
import 'strings.dart';

void main() => runApp(StarterApp(controller: AppController()));

/// App-wide choices the user (or a test) can change at runtime.
class AppController extends ChangeNotifier {
  AppController({this._style = AppStyle.cleanMarket, this._mode = ThemeMode.light, this._locale = const Locale('en')});

  AppStyle _style;
  ThemeMode _mode;
  Locale _locale;

  AppStyle get style => _style;
  ThemeMode get mode => _mode;
  Locale get locale => _locale;

  set style(AppStyle v) => _set(() => _style = v);
  set mode(ThemeMode v) => _set(() => _mode = v);
  set locale(Locale v) => _set(() => _locale = v);

  void _set(VoidCallback f) {
    f();
    notifyListeners();
  }

  static AppController of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<_ControllerScope>()!.notifier!;
}

class _ControllerScope extends InheritedNotifier<AppController> {
  const _ControllerScope({required AppController controller, required super.child}) : super(notifier: controller);
}

class StarterApp extends StatelessWidget {
  const StarterApp({super.key, required this.controller, this.home});

  final AppController controller;

  /// Tests can mount a single screen; the app shows the gallery.
  final Widget? home;

  @override
  Widget build(BuildContext context) {
    return _ControllerScope(
      controller: controller,
      child: ListenableBuilder(
        listenable: controller,
        builder: (context, _) {
          final rtlScript = S(controller.locale).rtl;
          return MaterialApp(
            title: 'App starter',
            debugShowCheckedModeBanner: false,
            locale: controller.locale,
            supportedLocales: S.supported,
            localizationsDelegates: GlobalMaterialLocalizations.delegates,
            themeMode: controller.mode,
            theme: buildAppTheme(controller.style, Brightness.light, rtlScript: rtlScript),
            darkTheme: buildAppTheme(controller.style, Brightness.dark, rtlScript: rtlScript),
            home: home ?? const GalleryShell(),
          );
        },
      ),
    );
  }
}
