import csv
file_path = "../songs.csv"

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    print(list(csv_reader)[0])

"""
Output:

['Song', 'Artist', 'Category', 'Year']
"""