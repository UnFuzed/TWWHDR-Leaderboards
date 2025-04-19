import 'package:flutter/material.dart';
import 'package:twwhdr_leaderboard/routes.dart' as routes;

class HomePage extends StatelessWidget {
  const HomePage({super.key});

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
            'The Wind Waker HD Randomizer Leaderboards',
            style: TextStyle
            (
              fontSize: 40,
              fontWeight: FontWeight.bold
            ),
          ),
        ),
        actions: 
        [
          Text('Not Logged in'),
          IconButton
          (
            onPressed: () {
              Navigator.pushNamed(context, routes.homePage);
            }, 
            icon: Icon(Icons.account_circle_rounded))
        ],
      ),
      body: Row
      (
        children: 
        [
          // TextButton(onPressed: () {}, child: Text('Create Week')),
          // TextButton(onPressed: () {}, child: Text('Test Button')),
          // TextButton(onPressed: () {}, child: Text('Submit Record')),
        ],
      ),
    );
  }
}