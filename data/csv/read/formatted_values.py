import csv
file_path = "../songs.csv"

with open(file_path, "r") as file:
    csv_list = list(csv.reader(file))
    [print ("[{}]".format(line[3]), line[0], "(by {})".format(line[1])) for idx, line in enumerate(csv_list) if idx > 0]

"""
Output:

[2020] Blinding Lights (by The Weeknd)
[2019] Watermelon Sugar (by Harry Styles)
[2021] Mood (by 24kGoldn)
[2019] Someone You Loved (by Lewis Capaldi)
[2017] Perfect (by Ed Sheeran)
[2017] Believer (by Imagine Dragons)
[2018] Lovely (by Billie Eilish)
[2019] Circles (by Post Malone)
[2017] Shape of You (by Ed Sheeran)
[2021] Memories (by Maroon 5)
[2016] Closer (by The Chainsmokers)
[2019] Bad Guy (by Billie Eilish)
[2016] Say You Won't Let Go (by James Arthur)
"""