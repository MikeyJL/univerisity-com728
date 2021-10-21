import sqlite3

db = sqlite3.connect('./users_db.db')
cursor = db.cursor()
sql = "SELECT * FROM users;"
cursor.execute(sql)
record = cursor.fetchone()
db.close()
print(record)

"""
Output:

(1, 'Bob', 1.6, 85, '2021-01-01')
"""