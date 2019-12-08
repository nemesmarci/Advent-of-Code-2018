from common import read_data, play

players, last_points = read_data()
print(play(players, last_points * 100))
