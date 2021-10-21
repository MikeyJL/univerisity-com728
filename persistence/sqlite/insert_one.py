import sqlite3

name = input("\nUser's name: ")
height = input("\nUser's height: ")
weight = input("\nUser's weight: ")
dob = input("\nUser's DOB: ")

db = sqlite3.connect("./users_db.db")
cursor = db.cursor()
sql = f"INSERT INTO users (name, height, weight, date_of_birth) Values (?, ?, ?, ?);"
id = cursor.execute(sql, [name, float(height), float(weight), dob])
db.commit()
db.close()

print(f"The id of the new user is: {cursor.lastrowid}")

"""
Input:

John
1.7
83
2020-01-01

Output:

[(1, "Bob", 1.6, 85, "2021-01-01"),
(3, "Mikey", 1.83, 100, "1999-10-28"),
(6, "John", 1.7, 83, 2020-01-01"")]
"""