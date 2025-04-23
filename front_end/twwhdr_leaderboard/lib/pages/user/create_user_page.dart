import 'package:flutter/material.dart';

class CreateUserPage extends StatefulWidget {
  const CreateUserPage({super.key});

  @override
  State<CreateUserPage> createState() => _CreateUserPageState();
}

class _CreateUserPageState extends State<CreateUserPage> {

  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _comfirmPasswordController = TextEditingController();

  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    _comfirmPasswordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold
    (
      appBar: AppBar
      (
        flexibleSpace: Center
        (
          child: Text
          (
            'Create User',
            style: TextStyle
            (
              fontSize: 20,
              fontWeight: FontWeight.bold
            ),
          ),
        ),
      ),
      body: Center
      (
        child: SizedBox(
          child: Column
          (
            children: 
            [
              TextFormField
              (
                controller: _usernameController,
              ),
              TextFormField
              (
                controller: _passwordController,
              ),
              TextFormField
              (
                controller: _comfirmPasswordController,
              )
            ],
          ),
        ),
      ),
    );
  }
}