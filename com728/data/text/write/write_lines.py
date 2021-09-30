file_path = input("\nEnter file path\n>>> ") or "output.txt"
lines = ["This is the first line.\n", "This is the second.\n", "This is the third line.\n"]

try:
    with open(file_path, "w") as file:
        file.writelines(lines)
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