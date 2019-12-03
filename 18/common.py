from copy import deepcopy


def read_data():
    with open('input.txt') as area:
        lines = area.readlines()
        size = len(lines)
        tiles = dict()

        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                tiles[x + 1, y + 1] = c

        for x in [0, size + 1]:
            for y in range(0, size + 2):
                tiles[x, y] = ' '

        for y in [0, size + 1]:
            for x in range(0, size + 2):
                tiles[x, y] = ' '

    return size, tiles


def around(location):
    lx, ly = location
    return [(x, y) for x in range(lx - 1, lx + 2)
            for y in range(ly - 1, ly + 2)
            if (x, y) != (lx, ly)]


def sum_neighbours(location, tiles):
    trees = lumberyards = 0
    for l in around(location):
        if tiles[l] == '|':
            trees += 1
        elif tiles[l] == '#':
            lumberyards += 1
    return trees, lumberyards


def iterate(tiles):
    new_tiles = deepcopy(tiles)

    for location in tiles:
        typ = tiles[location]
        if typ == ' ':
            continue
        trees, lumberyards = sum_neighbours(location, tiles)
        if typ == '.':
            if trees >= 3:
                new_tiles[location] = '|'
        elif typ == '|':
            if lumberyards >= 3:
                new_tiles[location] = '#'
        elif typ == '#':
            if trees < 1 or lumberyards < 1:
                new_tiles[location] = '.'

    return new_tiles


def value(size, tiles):
    trees = lumberyards = 0
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            if tiles[x, y] == '|':
                trees += 1
            elif tiles[x, y] == '#':
                lumberyards += 1
    return trees * lumberyards
