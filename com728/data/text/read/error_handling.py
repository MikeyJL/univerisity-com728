try:
    with open("bad_file.txt") as file:
        print(file.readlines())
except IOError:
    print("Something went wrong")

"""
Output:

Something went wrong
"""