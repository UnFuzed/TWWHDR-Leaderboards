enum UserRole {
  admin,
  player,
  owner,
}

extension UserRoleExtension on UserRole {
  String get value {
    switch (this) {
      case UserRole.admin:
        return 'admin';
      case UserRole.player:
        return 'player';
      case UserRole.owner:
        return 'owner';
    }
  }
}