import sqlite3 as sq

db = sq.connect('./users_db.db')
cur = db.cursor()

id = input("Please enter the user id: ")


sql = f"SELECT * FROM users WHERE id = {id}"
record = cur.execute(sql).fetchone()
print("\nThe following record has been found:")
print("name:", record[1], "height:", record[2], "weight:", record[3], "date_of_birth:", record[4], "\n")

sql = f"DELETE FROM users WHERE id = {id}"
cur.execute(sql)
db.commit()
print("The record has been removed.\n")

db.close()

"""
Input:

3

Output:

The following record has been found:
name: Mikey height: 1.83 weight: 100 date_of_birth: 1999-10-28

The record has been removed.
"""