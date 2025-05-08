import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:twwhdr_leaderboard/models/user.dart';

const String apiBaseUrl = String.fromEnvironment('API_BASE_URL');

Future<dynamic> createUser(User user) async {

  try {
    final response = await http.post
    (
      // Uri.parse('$apiBaseUrl/create_user'),
      Uri.parse('http://127.0.0.1:5000/create_user'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(user.toJson())
    
    );

    if (response.statusCode != 201)
    {
      throw Exception('Failed to create user. Status Code: ${response.statusCode}, Response: ${response.body}');
    }


  }
  catch (e) {
    throw Exception('Error occured while creating the user: $e');
  }
}
