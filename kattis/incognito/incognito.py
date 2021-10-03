import math
import sys

"""
Extacts the data.
"""
lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

"""
Processes the data to a 3d array.
"""
data_arr = []
for index, line in enumerate(lines):
    if index == 0:
        no_of_set = line
    elif line in "1234567890":
        set_builder = []
        for i in range(1, int(line) + 1):
            set_builder.append(lines[index + i].split())
        data_arr.append(set_builder)

"""
Calculates the disguises.
"""
def combos (n, r):
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))

for instance in data_arr:
    no_of_gear = len(set([item[0] for item in instance]))
    no_of_type = len(set([item[1] for item in instance]))

    print(combos(no_of_gear + 1, no_of_type) - 1)