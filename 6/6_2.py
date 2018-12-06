import sys
from collections import defaultdict

xcoords, ycoords = [], []
lines = sys.stdin.readlines()
for line in lines:
    x,y = [int(c) for c in line.split(',')]
    xcoords.append(x)
    ycoords.append(y)

coords = [(xcoords[h], ycoords[h]) for h in range(len(xcoords))]

min_x, min_y = min(xcoords), min(ycoords)
max_x, max_y = max(xcoords), max(ycoords)

point_to_sum = defaultdict(int)

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def distances(coord, coords):
    return [distance(c, coord) for c in coords]

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        ls = distances((i,j), coords)
        point_to_sum[(i,j)] = sum(ls)
                
print(len([s for s in point_to_sum.values() if s < 10000]))