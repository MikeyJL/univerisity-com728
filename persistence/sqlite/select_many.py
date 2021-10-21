import sqlite3

num = input("\nNumber of records to get: ")
print('')

db = sqlite3.connect('./users_db.db')
cursor = db.cursor()
sql = "SELECT * FROM users;"
cursor.execute(sql)
records = cursor.fetchmany(int(num))
db.close()

for record in records:
    print(list(record))

"""
Input: 2

Output:

[1, 'Bob', 1.6, 85, '2021-01-01']
[3, 'Mikey', 1.83, 100, '1999-10-28']
"""