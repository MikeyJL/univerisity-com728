from database import Database
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--generate", action="store_true")
args = parser.parse_args()

db = Database(generate=args.generate)

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

if option == 1:
    db.get_all_presenters_and_org()
elif option == 2:
    db.get_all_events_and_location()
elif option == 3:
    db.get_all_presenters_for_event()