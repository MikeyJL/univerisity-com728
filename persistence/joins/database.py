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
    
    db.close()

def display_product_supplier():
    db = sq.connect('./catalogue.db')
    cur = db.cursor()
    sql = "SELECT product.name, supplier.name FROM product INNER JOIN supplier ON product.supplier_id == supplier.id ;"
    cur.execute(sql)
    records = cur.fetchall()

    for record in records:
        product, supplier = record
        print("\nProduct:", product, "\nSupplier:", supplier)
    
    db.close()