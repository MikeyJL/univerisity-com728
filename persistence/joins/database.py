import sqlite3 as sq

def display_products_with_stock_levels ():
    db = sq.connect('./catalogue.db')
    cur = db.cursor()
    sql = "SELECT name, description, quantity FROM product NATURAL JOIN stock;"
    cur.execute(sql)
    records = cur.fetchall()

    for record in records:
        product, description, stock = record
        print("\nProduct:", product, "\nDescription:", description, "\nStock:", stock)