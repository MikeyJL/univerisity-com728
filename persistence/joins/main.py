from database import display_products_with_stock_levels, display_product_supplier

def display_menu():
    menu = """\nPlease select one of the following options:
[1] Display stock levels
[2] Display suppliers"""
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
        display_products_with_stock_levels()
    elif option == 2:
        display_product_supplier()

if __name__ == "__main__":
    run()