import 'package:flutter/material.dart';
import 'package:twwhdr_leaderboard/routes.dart' as routes;

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int? _selectedWeek;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        flexibleSpace: Center(
          child: Text(
            'The Wind Waker HD Randomizer Leaderboards',
            style: TextStyle(
              fontSize: 40,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        actions: [
          const Text('Not Logged in'),
          IconButton(
            onPressed: () {
              Navigator.pushNamed(context, routes.createUserPage);
            },
            icon: const Icon(
              Icons.account_circle_rounded,
              color: Colors.white,
            ),
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Week selection dropdown
            DropdownButtonFormField<int>(
              value: _selectedWeek,
              decoration: const InputDecoration(
                labelText: 'Select Week',
              ),
              items: List.generate(10, (index) {
                return DropdownMenuItem<int>(
                  value: index + 1,
                  child: Text('Week ${index + 1}'),
                );
              }),
              onChanged: (value) {
                setState(() {
                  _selectedWeek = value;
                });
              },
              validator: (value) {
                if (value == null) {
                  return 'Please select a week';
                }
                return null;
              },
            ),
            const SizedBox(height: 20),
            // Additional buttons (optional)
            Row(
              children: [
                TextButton(
                  onPressed: () {
                    // Handle Create Week action
                  },
                  child: const Text('Create Week'),
                ),
                const SizedBox(width: 8),
                TextButton(
                  onPressed: () {
                    // Handle Submit Record action
                  },
                  child: const Text('Submit Record'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
