import sqlite3 as sq

id = input("\nID of user to index: ")

db = sq.connect('./users_db.db')
cur = db.cursor()

sql = f"SELECT * FROM users WHERE id = {id}"
record = cur.execute(sql).fetchone()

print("\nCurrent user details are as follows:")
print("name:", record[1], "height:", record[2], "weight:", record[3], "date_of_birth:", record[4], "\n")

target = input("What would you like to change? ")
value = input(f"What is the new value for {target}? ")

sql = f"UPDATE users SET {target} = \"{value}\" WHERE id = {id};"
cur.execute(sql)
db.commit()

print("\nThe record has been updated.")
db.close()

"""
Input:

1
name
Jack

Output:

The record has been updated.
(Bob -> Jack)
"""