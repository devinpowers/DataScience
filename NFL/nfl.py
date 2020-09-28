'''NFL'''


import csv
with open("nfl_rosters_2019.csv", "r") as f:
     reader = csv.reader(f, delimiter=',')
     nfl = list(reader)
    

class Player():
    def __init__(self, data_row):
        self.player_name = data_row[2]
        self.position = data_row[5]
        self.team = data_row[4]
        
# skipping the first row which is the column titles and such
first_player = Player(nfl[1])
print("first_player.player_name:", first_player.player_name)
print("first_player.position:", first_player.position)
print("first_player.team:", first_player.team)




