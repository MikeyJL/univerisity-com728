import csv
file_path = "../songs.csv"

with open(file_path, "r") as file:
    csv_list = list(csv.reader(file))
    for idx, line in enumerate(csv_list):
        print(", ".join(line) if idx > 0 else ", ".join(line) + "\n")

"""
Output:

Song, Artist, Category, Year

Blinding Lights, The Weeknd, r&b, 2020
Watermelon Sugar, Harry Styles, pop, 2019
Mood, 24kGoldn, rap, 2021
Someone You Loved, Lewis Capaldi, pop, 2019
Perfect, Ed Sheeran, pop, 2017
Believer, Imagine Dragons, rock, 2017
Lovely, Billie Eilish, electropop, 2018
Circles, Post Malone, rap, 2019
Shape of You, Ed Sheeran, pop, 2017
Memories, Maroon 5, pop, 2021
Closer, The Chainsmokers, pop, 2016
Bad Guy, Billie Eilish, electropop, 2019
Say You Won't Let Go, James Arthur, pop, 2016
"""