from collections import Counter
from common import read_data, make_map

borders, coords = read_data()
point_to_coord, coord_to_points = make_map(borders, coords)

infinites = set()
min_x, max_x, min_y, max_y = borders

for c in range(len(coords)):
    for p in coord_to_points[c]:
        if p[0] == min_x or p[1] == min_y or p[0] == max_x or p[1] == max_y:
            infinites.add(c)
            break

finite_coords = [c for c in point_to_coord.values() if c not in infinites]
print(max(Counter(finite_coords).values()))
