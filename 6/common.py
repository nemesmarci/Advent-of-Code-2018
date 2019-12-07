from collections import defaultdict


def read_data():
    xcoords, ycoords = [], []
    with open('input.txt') as data:
        for line in data:
            x, y = [int(c) for c in line.split(',')]
            xcoords.append(x)
            ycoords.append(y)
        coords = [(xcoords[h], ycoords[h]) for h in range(len(xcoords))]
        min_x, min_y = min(xcoords), min(ycoords)
        max_x, max_y = max(xcoords), max(ycoords)
        return (min_x, max_x, min_y, max_y), coords


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def distances(coord, coords):
    return [distance(c, coord) for c in coords]


def make_map(borders, coords):
    min_x, max_x, min_y, max_y = borders
    point_to_coord = defaultdict(int)
    coord_to_points = defaultdict(list)
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            ls = distances((i, j), coords)
            minl = min(ls)
            coord = ls.index(minl)
            coord_to_points[coord].append((i, j))
            if ls.count(minl) == 1:
                point_to_coord[(i, j)] = coord
    return point_to_coord, coord_to_points
