import 'package:flutter/material.dart';
import 'package:twwhdr_leaderboard/models/emuns/user_role.dart';
import 'package:twwhdr_leaderboard/models/user.dart';
import 'package:twwhdr_leaderboard/services/user_service.dart';

class CreateUserPage extends StatefulWidget {
  const CreateUserPage({super.key});

  @override
  State<CreateUserPage> createState() => _CreateUserPageState();
}

class _CreateUserPageState extends State<CreateUserPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _confirmPasswordController = TextEditingController();

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(
          child: Text(
            'Create User',
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
        ),
      ),
      body: Form(
        key: _formKey,
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextFormField(
                decoration: const InputDecoration(labelText: 'Username'),
                controller: _usernameController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Username cannot be empty';
                  }
                  return null;
                },
              ),
              TextFormField(
                decoration: const InputDecoration(labelText: 'Password'),
                controller: _passwordController,
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Password cannot be empty';
                  } else if (value.length < 6) {
                    return 'Password must be at least 6 characters';
                  }
                  return null;
                },
              ),
              TextFormField(
                decoration: const InputDecoration(labelText: 'Confirm Password'),
                controller: _confirmPasswordController,
                obscureText: true,
                validator: (value) {
                  if (value != _passwordController.text) {
                    return 'Passwords do not match';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 20),
              FilledButton(
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    final user = User(
                      userName: _usernameController.text,
                      password: _passwordController.text,
                      role: UserRole.admin,
                    );

                    try {
                      // await createUser(user);

                      if (mounted) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text('User was created successfully! THIS IS A TEST MESSAGE')),
                        );
                        Navigator.pop(context, true);
                      }
                    } catch (e) {
                      if (mounted) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('An error occurred when creating the user: $e')),
                        );
                      }
                    }
                  }
                },
                child: const Text('Create User'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
