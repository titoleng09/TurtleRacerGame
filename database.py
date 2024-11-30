import sqlite3

def connect_db():
    connection = sqlite3.connect('turtle_race.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            time REAL NOT NULL
        )
    ''')
    connection.commit()
    return connection

def add_to_leaderboard(username, time):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO leaderboard (username, time) VALUES (?, ?)
    ''', (username, time))
    connection.commit()
    connection.close()

def fetch_leaderboard():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        SELECT username, time FROM leaderboard ORDER BY time ASC LIMIT 5
    ''')
    results = cursor.fetchall()
    connection.close()
    return results