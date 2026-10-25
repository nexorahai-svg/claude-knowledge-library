import 'package:flutter/widgets.dart';

/// Tiny string table for the gallery. A real app uses `flutter gen-l10n` with
/// ARB files; this keeps the starter dependency-free while proving RTL works.
class S {
  S(this.locale);

  final Locale locale;

  static S of(BuildContext context) => S(Localizations.localeOf(context));

  static const supported = [Locale('en'), Locale('fa'), Locale('ar')];

  bool get rtl => locale.languageCode == 'fa' || locale.languageCode == 'ar';

  String _t(String en, String fa, String ar) => switch (locale.languageCode) {
        'fa' => fa,
        'ar' => ar,
        _ => en,
      };

  String get home => _t('Home', 'خانه', 'الرئيسية');
  String get search => _t('Search', 'جستجو', 'بحث');
  String get states => _t('States', 'حالت‌ها', 'الحالات');
  String get settings => _t('Settings', 'تنظیمات', 'الإعدادات');
  String get greeting => _t('Good evening', 'عصر بخیر', 'مساء الخير');
  String get featured => _t('Featured for you', 'پیشنهاد برای شما', 'مختارات لك');
  String get seeAll => _t('See all', 'همه', 'عرض الكل');
  String get searchHint => _t('Search places, food, services', 'جستجوی مکان، غذا، خدمات', 'ابحث عن أماكن وخدمات');
  String get noResultsTitle => _t('No results yet', 'هنوز نتیجه‌ای نیست', 'لا توجد نتائج بعد');
  String get noResultsBody =>
      _t('Try another word or clear the filters.', 'کلمه‌ی دیگری امتحان کنید یا فیلترها را پاک کنید.', 'جرّب كلمة أخرى أو امسح عوامل التصفية.');
  String get clearFilters => _t('Clear filters', 'پاک کردن فیلترها', 'مسح عوامل التصفية');
  String get errorTitle => _t("We couldn't load this", 'بارگذاری نشد', 'تعذّر التحميل');
  String get errorBody => _t('Check your connection and try again.', 'اتصال را بررسی کنید و دوباره امتحان کنید.', 'تحقق من الاتصال وحاول مرة أخرى.');
  String get retry => _t('Try again', 'دوباره', 'إعادة المحاولة');
  String get offline => _t("You're offline. Showing saved data.", 'آفلاین هستید. داده‌ی ذخیره‌شده نمایش داده می‌شود.', 'أنت غير متصل. نعرض البيانات المحفوظة.');
  String get openSheet => _t('Open sheet', 'باز کردن برگه', 'فتح الورقة');
  String get sheetTitle => _t('Choose a time', 'یک زمان انتخاب کنید', 'اختر وقتًا');
  String get confirm => _t('Confirm', 'تأیید', 'تأكيد');
  String get email => _t('Email', 'ایمیل', 'البريد الإلكتروني');
  String get emailError => _t('Enter a valid email, like name@example.com', 'یک ایمیل درست وارد کنید، مثل name@example.com', 'أدخل بريدًا صحيحًا مثل name@example.com');
  String get style => _t('Style', 'سبک', 'النمط');
  String get dark => _t('Dark mode', 'حالت تیره', 'الوضع الداكن');
  String get language => _t('Language', 'زبان', 'اللغة');
  String get notifications => _t('Notifications', 'اعلان‌ها', 'الإشعارات');
  String get loading => _t('Loading', 'در حال بارگذاری', 'جارٍ التحميل');
  String price(int n) => _t('AED $n', '$n درهم', '$n درهم');
}
