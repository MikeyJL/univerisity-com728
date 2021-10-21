import sqlite3 as sq

file_path = input("File name: ") or "./users.csv"

with open(file_path) as file:
    lines = file.readlines()
    users = [line.split((",")) for line in lines]

db = sq.connect('./users_db.db')
cur = db.cursor()

sql = "INSERT INTO users (name, height, weight, date_of_birth) VALUES (?, ?, ?, ?)"
print("Inserting data into the database...")
for user in users:
    cur.execute(sql, [user[0], float(user[1]), float(user[2]), user[3].strip()])
db.commit()
db.close()

print(f"Done! {len(lines)} records inserted.")


"""
Input:

File name:

Output:

Inserting data into the database...
Done! 3 records inserted.
"""