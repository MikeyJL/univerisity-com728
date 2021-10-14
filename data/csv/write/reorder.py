import csv
file_path = "../songs.csv"
output_path = "./output.csv"

with open(file_path, "r") as input:
    csv_list = list(csv.reader(input))
    with open(output_path, "w") as output:
        for w in ([",".join(x) for x in map(lambda line: [y for y in reversed(line)], csv_list)]):
            output.write("{}\n".format(w))

"""
Output:

Year,Category,Artist,Song
2020,r&b,The Weeknd,Blinding Lights
2019,pop,Harry Styles,Watermelon Sugar
2021,rap,24kGoldn,Mood
2019,pop,Lewis Capaldi,Someone You Loved
2017,pop,Ed Sheeran,Perfect
2017,rock,Imagine Dragons,Believer
2018,electropop,Billie Eilish,Lovely
2019,rap,Post Malone,Circles
2017,pop,Ed Sheeran,Shape of You
2021,pop,Maroon 5,Memories
2016,pop,The Chainsmokers,Closer
2019,electropop,Billie Eilish,Bad Guy
2016,pop,James Arthur,Say You Won't Let Go

"""