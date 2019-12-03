from common import read_data, iterate, value

size, tiles = read_data()

for i in range(10):
    tiles = iterate(tiles)

print(value(size, tiles))
