file_path = input("\nEnter file path\n>>> ") or "output.txt"
lines = ["This is the first line.", "This is the second.", "This is the third line."]

try:
    with open(file_path, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print("The data has been written to the file.")
except IOError:
    print("Something went wrong...")

"""
Input:

None
"""

"""
Txt output:

This is the first line.
This is the second.
This is the third line.

"""