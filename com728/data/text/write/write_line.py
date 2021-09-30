file_path = input("\nEnter file path\n>>> ") or "output.txt"

try:
    with open(file_path, "w") as file:
        file.write("data has been overwritten!")
        print("The data has been written to the file.")
except IOError:
    print("Something went wrong...")

"""
Input:

None
"""

"""
Txt output:

data has been overwritten!
"""