import csv
file_path = "../songs.csv"

with open(file_path, "r") as file:
    csv_list = list(csv.reader(file))
    [print (line[0]) for idx, line in enumerate(csv_list) if idx > 0]

"""
Output:

Blinding Lights
Watermelon Sugar
Mood
Someone You Loved
Perfect
Believer
Lovely
Circles
Shape of You
Memories
Closer
Bad Guy
Say You Won't Let Go
"""