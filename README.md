# TurtleRacerGame
The ‘TurtleRacers’ Game is a fun and interactive Python-based game built using tkinter for the graphical user interface (GUI) and turtle for visualizing the race. Players can enjoy the game in single-player or multiplayer modes. The project also includes a leaderboard to record and display the best race times.

1. Project Issue/Problem to Be Solved
The primary goal of this project is to create an engaging and interactive turtle racing game where players can compete in single-player or multiplayer modes. The system aims to:
•	Foster competitiveness with a leaderboard system.
•	Allow flexibility with single and multiplayer game modes.
•	Save race outcomes for replay ability and historical analysis.
________________________________________
2. Current Progress (PDLC Stages)
 Problem Analysis
-	Users need a fun and competitive racing game.
-	Requirements include a leaderboard system, multiplayer functionality, and interactive game controls.
 Design
-	Game interface created using Tkinter for menu navigation and user inputs.
-	Turtle Graphics used for the racing visuals.
-	Designed a database to store race results and leaderboard information.
Development
-	Implemented single-player and multiplayer modes with customizable user controls.
-	Added a leaderboard system that saves and fetches race results.
Testing
-	Game mechanics, database interactions, and UI navigation tested for errors.
-	Both game modes verified for functionality and user experience.
________________________________________
3. Project Functions/Features
Game Modes: Single-player and multiplayer modes with custom usernames
Race Mechanism: Dynamic race progress with countdown and winner announcement.
Leaderboard System: Save race results to the database, fetch and display top racers based on performance.
Replay Option: Option to replay the game or exit after a race.
Keyboard Controls; Single-player: Arrow keys for navigation, Multiplayer: Separate keys for each player.
Customizable Turtles: Players can set unique usernames for identification.
________________________________________
5. Pages/Modules
Home Page: Game Mode Selection (Single or Multiplayer) , View Leaderboard Option
Single-Player Setup: Username input for single-player mode.
Multiplayer Setup: Username input for both players.
Game Screen: Turtle racing visuals and race results.
Leaderboard Page: Displays top 5 race results sorted by race time.
________________________________________
6. Database Applied
Database Type: SQLite
Tables: leaderboard: Stores usernames and race times.
Records: Columns: Username (Text), Time (Real)
________________________________________
7. Project References/Sources
•	Python Turtle Graphics Documentation
•	Tkinter Documentation and Tutorials
•	SQLite Official Documentation
•	https://www.youtube.com/results?search_query=turtle+racing+game+
•	https://www.youtube.com/watch?v=lyoyTlltFVU
________________________________________

-	How to Play
Single Player Mode
1.	Launch the game.
2.	Select the Single Player option.
3.	Enter your username when prompted.
4.	Control your turtle using:
o	Right arrow key to move forward.
o	Left arrow key to move backward.
Multiplayer Mode
1.	Launch the game.
2.	Select the Multiplayer option.
3.	Enter usernames for both players.
4.	Control your turtles:
o	Player 1:
	W to move forward.
	S to move backward.
o	Player 2:
	Right arrow key to move forward, Left arrow key to move backward

