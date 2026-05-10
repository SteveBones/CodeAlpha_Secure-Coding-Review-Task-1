import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, password))

results = cursor.fetchall()

if results:
    print("Login successful")
else:
    print("Invalid credentials")

conn.close()
