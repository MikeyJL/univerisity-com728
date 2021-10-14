file_path = "sample.csv"

try:
    with open(file_path, "a") as file:
        file.write("My Song,Unknown Artist,pop,2021\n")
except IOError as e:
    print(e)

"""
Output:

Sample Song,Sample Artist,Sample Category,Sample Year
My Song,Unknown Artist,pop,2021
"""