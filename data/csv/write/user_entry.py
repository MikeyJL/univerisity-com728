file_path = "user_entries.csv"

try:
    with open(file_path, "w") as file:
        file.write("Year,Artist,Song Title\n")
        for i in range(1, 4):
            song_name = input("({}) Name of your favourite song: ".format(i))
            song_year = input("({}) Name of your favourite song: ".format(i))
            song_artist = input("({}) Name of your favourite song: ".format(i))
            file.write("{},{},{}\n".format(song_year, song_artist, song_name))
except IOError as e:
    print(e)

"""
Input:

> Blinding light
> 2019
> The Weekend

Output:

Year,Artist,Song Title
2019,The Weekend,Blinding light
...
"""
