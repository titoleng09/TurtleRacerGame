import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import time
import turtle
from database import add_to_leaderboard, fetch_leaderboard

username = None
game_mode = None


def start_single_player():
    """Starts the single-player mode."""
    global game_mode
    game_mode = "single"
    root.withdraw()  
    launch_race_game()


def start_multiplayer():
    """Starts the multiplayer mode."""
    global game_mode
    game_mode = "multi"
    root.withdraw()  
    launch_race_game()

def display_username_above_turtle(turtle_obj, username, y_offset=20):
    turtle_obj.penup()
    turtle_obj.goto(turtle_obj.xcor(), turtle_obj.ycor() + y_offset)
    turtle_obj.write(username, align="center", font=("Arial", 10, "bold"))
    turtle_obj.goto(turtle_obj.xcor(), turtle_obj.ycor() - y_offset)

def launch_race_game():
    """Turtle racing game logic."""
    screen = turtle.Screen()
    screen.title("Turtle Racing Game")
    screen.setup(800, 600)
    screen.bgcolor("lightblue")
    screen.bgpic('road.gif') 

    track = turtle.Turtle()
    track.hideturtle()
    track.penup()
    track.speed(0)
    track.goto(-350, 300)
    track.pendown()
    for _ in range(2):
        track.forward(700)
        track.right(90)
        track.forward(600)
        track.right(90)

    colors = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
    user_turtle = turtle.Turtle()
    user_turtle.shape('turtle')
    user_turtle.shapesize(2)
    user_turtle.color("black")
    user_turtle.penup()
    user_turtle.goto(-330, 260)

    y_positions = [-260, -172, -85, 2, 85, 172, 260]
    opponent_turtles = []

    for i in range(6):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(colors[i])
        t.penup()
        t.goto(-330, y_positions[i])
        t.shapesize(2)
        opponent_turtles.append(t)

    def get_username():
        """Prompt user for their username in single-player mode."""
        username = turtle.textinput("Single Player", "Enter your username:")  
        if username:  
            return username
        return "Player"  

    if game_mode == "single":
        username = get_username() 
        display_username_above_turtle(user_turtle, username)

    elif game_mode == "multi":
        usernames = [player1_username.get(), player2_username.get()]  
        display_username_above_turtle(user_turtle, usernames[0])  
        display_username_above_turtle(opponent_turtles[0], usernames[1])  
        opponent_turtles = opponent_turtles[0:]  
        
    if game_mode == "single":

        def move_up():
            user_turtle.forward(10)

        def move_down():
            user_turtle.backward(10)

        screen.listen()
        screen.onkey(move_up, "Right")
        screen.onkey(move_down, "Left")


    elif game_mode == "multi":

        player_controls = {
            "Player1": {"turtle": user_turtle, "up": "w", "down": "s"},
            "Player2": {"turtle": opponent_turtles[0], "up": "Right", "down": "Left"}
        }
        manual_turtle = [user_turtle, opponent_turtles[0]]
        opponent_turtles = opponent_turtles[1:]

        def move_turtle(player, direction):
            if direction == "up":
                player_controls[player]["turtle"].forward(100)
            elif direction == "down":
                player_controls[player]["turtle"].backward(100)


        screen.listen()
        screen.onkey(lambda: move_turtle("Player1", "up"), player_controls["Player1"]["up"])
        screen.onkey(lambda: move_turtle("Player1", "down"), player_controls["Player1"]["down"])
        screen.onkey(lambda: move_turtle("Player2", "up"), player_controls["Player2"]["up"])
        screen.onkey(lambda: move_turtle("Player2", "down"), player_controls["Player2"]["down"])

    def start_race():
        countdown_turtle = turtle.Turtle()
        countdown_turtle.hideturtle()
        countdown_turtle.penup()
        countdown_turtle.goto(0, 200)

        for i in range(3, 0, -1):
            countdown_turtle.clear()
            countdown_turtle.write(f"{i}", align="center", font=("Arial", 30, "bold"))
            time.sleep(1)
        countdown_turtle.clear()
        countdown_turtle.write("Go!", align="center", font=("Arial", 30, "bold"))
        time.sleep(0.5)
        countdown_turtle.clear()

        #Race Logic
        print("Race starts now!")
        winner = None
        while not winner:
            for turtle_ in opponent_turtles:
                turtle_.forward(random.randint(1, 25))
                if turtle_.xcor() > 330:
                    winner = turtle_
                    break
            if user_turtle.xcor() > 330:
                winner = user_turtle
                break

        announce_turtle = turtle.Turtle()
        announce_turtle.hideturtle()
        announce_turtle.penup()
        announce_turtle.goto(0, 150)

    
        play_again()

    winner = start_race()

    screen.mainloop()

def play_again():
    play_again_window = tk.Toplevel(root)
    play_again_window.title('TurtleRacers!')

    screen_width = play_again_window.winfo_screenwidth()
    screen_height = play_again_window.winfo_screenheight()

    window_width = 300
    window_height = 150

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    play_again_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    play_again_window.resizable(False, False)

    play_again_label = tk.Label(play_again_window, text='Nice Try Racer!', font=("Arial", 20 , 'bold') , fg = 'red', bg = 'black')
    play_again_label.pack(pady=10)

    def restart_game():
        play_again_window.destroy()
        try:
            turtle.clearscreen()
        except turtle.terminator:
            pass
        if game_mode == 'single':
            start_single_player()
        elif game_mode == 'multi':
            start_multiplayer_mode()

    def exit_game():
        play_again_window.destroy()
        try:
            turtle.bye()
        except turtle.Terminator:
            pass
        mode_selection_frame.tkraise()
    play_again_button = tk.Button(play_again_window, text="Play Again", command=restart_game)
    play_again_button.pack(pady=5)

    main_menu_button = tk.Button(play_again_window, text="Exit", command=exit_game)
    main_menu_button.pack(pady=5)

    def end_race(winner):
        messagebox.showinfo("Race Over", f"The winner is {winner}!")
        play_again()
def save_to_leaderboard(username, race_time):
    """Save race results to the leaderboard."""
    cursor.execute("INSERT INTO leaderboard (username, time) VALUES (?, ?)", (username, race_time))
    conn.commit()


def fetch_top_results(limit=5):
    """Fetch top results sorted by race time."""
    cursor.execute("SELECT username, time FROM leaderboard ORDER BY time ASC LIMIT ?", (limit,))
    return cursor.fetchall()

def display_leaderboard():
    """Display the leaderboard in a new window."""
    leaderboard_window = tk.Toplevel(root)
    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("400x300")

    tk.Label(leaderboard_window, text="Top 5 Results", font=("Arial", 16, "bold")).pack(pady=10)

    results = fetch_top_results(limit=5)

    if not results:
        tk.Label(leaderboard_window, text="No results yet!", font=("Arial", 12)).pack(pady=20)
    else:
        for i, (username, race_time) in enumerate(results, start=1):
            tk.Label(leaderboard_window, text=f"{i}. {username} - {race_time:.2f} seconds").pack(pady=5)


root = tk.Tk()
root.geometry("500x400")
root.title("Turtle Racing Game")
label = Label(root, text = 'Welcome Turtle Racers!!!', font = ('Arial',30, 'bold')  , fg = 'Red', bg = 'black')
label.place(x = 10,y = 90)

mode_selection_frame = tk.Frame(root)
mode_selection_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(mode_selection_frame, text="Select Game Mode:").pack(pady=10)


def start_single_player_mode():
    mode_selection_frame.place_forget()  # Hide game mode selection frame
    single_player_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show single-player frame


def start_multiplayer_mode():
    mode_selection_frame.place_forget()  # Hide game mode selection frame
    multiplayer_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show multiplayer frame


single_player_button = tk.Button(mode_selection_frame, text="Single Player", fg = 'blue', command=start_single_player_mode)
single_player_button.pack(pady=5)

multiplayer_button = tk.Button(mode_selection_frame, text="Multiplayer",fg = 'red' , command=start_multiplayer_mode)
multiplayer_button.pack(pady=5)

leaderboard_button = tk.Button(root, text="View Leaderboard", command=display_leaderboard)
leaderboard_button.place(x=195, y=270)  # Adjust position as needed

single_player_frame = tk.Frame(root)


single_player_proceed = tk.Button(single_player_frame,text = "By yourself? let's go", command=start_single_player)
single_player_proceed.grid(row=1, column=0, columnspan=2, pady=10)

# Frame for multiplayer usernames input
multiplayer_frame = tk.Frame(root)
tk.Label(multiplayer_frame, text="Enter Player1's Username:").grid(row=0, column=0, padx=5, pady=5)
player1_username = tk.Entry(multiplayer_frame)
player1_username.grid(row=0, column=1, padx=5, pady=5)

tk.Label(multiplayer_frame, text="Enter Player2's Username:").grid(row=1, column=0, padx=5, pady=5)
player2_username = tk.Entry(multiplayer_frame)
player2_username.grid(row=1, column=1, padx=5, pady=5)


def proceed_to_multiplayer_game():
    username1 = player1_username.get()
    username2 = player2_username.get()
    if not username1.strip() or not username2.strip():
        messagebox.showerror("Error", "Both usernames must be entered.")
        return
    multiplayer_frame.place_forget()
    start_game([username1, username2])  # Start the game with both usernames


multiplayer_proceed = tk.Button(multiplayer_frame, text="Proceed", command=start_multiplayer)
multiplayer_proceed.grid(row=2, column=0, columnspan=2, pady=10)


# Placeholder function for starting the game
def start_game(usernames):
    # Replace this with the game logic
    game_frame = tk.Frame(root)
    game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(game_frame, text="Game Screen").pack(pady=10)

    for i, username in enumerate(usernames, start=1):
        tk.Label(game_frame, text=f"Turtle {i}: {username}").pack(pady=5)



root.mainloop()


def main():

    add_to_leaderboard(player1_username,race_time)

    # Example: Fetching leaderboard
    leaderboard = fetch_leaderboard()
    print("\nLeaderboard:")
    for rank, (username, time) in enumerate(leaderboard, start=1):
        print(f"{rank}. {username} - {time:.2f} seconds")


if __name__ == "__main__":
    main()
