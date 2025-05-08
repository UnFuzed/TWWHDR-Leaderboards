import 'package:twwhdr_leaderboard/models/emuns/user_role.dart';

class User {
  final int? userId;
  final String userName;
  final String password;
  final UserRole role;

  User({
    this.userId,
    required this.userName,
    required this.password,
    required this.role
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User
    (
      userId: json['userId'],
      userName: json['user_name'], 
      password: json['password'], 
      role: json['role']
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'user_name' : userName,
      'password' : password,
      'role' : role.name
    };
  }
}