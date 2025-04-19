import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:twwhdr_leaderboard/pages/home_page.dart';
import 'package:twwhdr_leaderboard/routes.dart' as routes;

void main() async {
  await dotenv.load(fileName: 'assets/.env');
  runApp(MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp
    (
      title: 'TWWHDR Leaderboards',
      theme: ThemeData.dark(),
      initialRoute: '/',
      onGenerateRoute: (settings) 
      {
        switch (settings.name)
        {
          case routes.homePage:
            return MaterialPageRoute(builder: (_) => const HomePage());
          default:
            return MaterialPageRoute
            (
              builder: (_) => Scaffold
              (
                body: Center(child: Text('Page not found'))
              )
          );
        }
      },
    );   
  }
}
