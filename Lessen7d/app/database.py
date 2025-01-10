
import sqlite3

def init_db():
    connect = sqlite3.connect("schedule.db")
    cursor = connect.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task TEXT,
        time TEXT
    )
    """)
    
    connect.commit()
    return connect, cursor

def add_user(cursor, user_id):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    
def add_task(cursor, user_id, task):
    cursor.execute("INSERT INTO schedules (user_id, task) VALUES (?, ?)", (user_id, task))

def add_schedule_time(cursor, user_id, time):
    cursor.execute("INSERT INTO schedules (user_id, time) VALUES (?, ?)", (user_id, time))

def get_user_schedule(cursor, user_id):
    return cursor.execute("SELECT time, task FROM schedules WHERE user_id = ?", (user_id,)).fetchall()

def delete_schedule(cursor, user_id, time):
    cursor.execute("DELETE FROM schedules WHERE user_id = ? AND time = ?", (user_id, time))

def update_schedule_time(cursor, user_id, old_time, new_time):
    cursor.execute("UPDATE schedules SET time = ? WHERE user_id = ? AND time = ?", (new_time, user_id, old_time))
