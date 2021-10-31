import database as db

def display_menu():
    menu = """\nPlease select one of the following options:
[1] Display stock levels
[2] Display suppliers
[3] Display supplier locations
[4] Display missing suppliers"""
    print(menu)

def run():
    display_menu()
    option = False
    while not option:
        try:
            option = int(input(">>> "))
        except ValueError:
            print("\nPlease enter a number.\n")
    
    print("\nYou've selected option: ", option)
    if option == 1:
        db.display_products_with_stock_levels()
    elif option == 2:
        db.display_product_supplier()
    elif option == 3:
        db.display_product_supplier_locations()
    elif option == 4:
        db.display_products_missing_suppliers()

if __name__ == "__main__":
    run()