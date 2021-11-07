import database as db

db.setup()

menu = """
Please select one of the following options:

[1] Display presenters
[2] Display events
[3] Display presenters for event
[4] Display events for presenter

>>> """
option = None
while not option:
    try:
        option = int(input(menu))
    except ValueError as e:
        print(f"\n--------------------\n\nERROR: Please enter a number: {e}")

print(f"\nYou've selected option {option}")