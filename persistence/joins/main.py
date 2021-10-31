from database import display_products_with_stock_levels

menu = """Please select one of the following options:
[1] Display stock levels
"""

option = False
print(menu)
while not option:
    try:
        option = int(input(">>> "))
    except ValueError:
        print("\nPlease enter a number.\n")

print("You've selected option: ", option)
if option == 1:
    display_products_with_stock_levels()