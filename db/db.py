import sqlite3

with sqlite3.connect('base.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER)
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS auto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    nodel TEXT,
    year INTEGER)
    """)
    # Пример создания пользователя
    cursor.execute("INSERT INTO user (name, age) VALUES ('BOB', 25)")
    connection.commit()
