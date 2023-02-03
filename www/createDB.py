import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
cursor.execute(query)

conn.commit()
conn.close()