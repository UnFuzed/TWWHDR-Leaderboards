enum WeekType {
  normal,
  spoiler
}

extension WeekTypeExtension on WeekType {
  String get value {
    switch (this) {
      case WeekType.normal:
        return 'normal';
      case WeekType.spoiler:
        return 'spoiler';
    }
  }
}