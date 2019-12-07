from collections import defaultdict
from common import read_data, make_map, distances

borders, coords = read_data()
point_to_coord, coord_to_points = make_map(borders, coords)

point_to_sum = defaultdict(int)
min_x, max_x, min_y, max_y = borders

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        ls = distances((x, y), coords)
        point_to_sum[(x, y)] = sum(ls)

print(len([dist for dist in point_to_sum.values() if dist < 10000]))
