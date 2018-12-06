import sys
from collections import defaultdict, Counter

xcoords, ycoords = [], []
lines = sys.stdin.readlines()
for line in lines:
    x,y = [int(c) for c in line.split(',')]
    xcoords.append(x)
    ycoords.append(y)

coords = [(xcoords[h], ycoords[h]) for h in range(len(xcoords))]

min_x, min_y = min(xcoords), min(ycoords)
max_x, max_y = max(xcoords), max(ycoords)

point_to_coord = defaultdict(int)
coord_to_points = defaultdict(list)

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def distances(coord, coords):
    return [distance(c, coord) for c in coords]

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        ls = distances((i,j), coords)
        minl = min(ls)
        coord = ls.index(minl)
        coord_to_points[coord].append((i,j))
        if ls.count(minl) == 1:
            point_to_coord[(i,j)] = coord
                
infinites = set()
for c in range(len(coords)):
    for p in coord_to_points[c]:
        if p[0] == min_x or p[1] == min_y or p[0] == max_x or p[1] == max_y:
            infinites.add(c)
            break

finite_coords = [c for c in point_to_coord.values() if c not in infinites]
print(max(Counter(finite_coords).values()))