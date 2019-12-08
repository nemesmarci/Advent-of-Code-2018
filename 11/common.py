import numpy as np
from collections import defaultdict


def read_data():
    with open('input.txt') as data:
        serial = int(data.read())

    cells = np.zeros((300, 300), dtype=int)

    for x in range(1, 300 + 1):
        for y in range(1, 300 + 1):
            rack_id = x + 10
            power = (rack_id * y + serial) * rack_id
            power = int(('00' + str(power))[-3]) - 5
            cells[x - 1][y - 1] = power

    return cells


def stack(x, y, size, cells, cache, row_cache, col_cache):
    if size - 1 in cache[(x, y)]:
        total = cache[(x, y)][size - 1]
        if size - 1 in col_cache[(x + size - 1, y)]:
            y_total = col_cache[(x + size - 1, y)][size - 1]
        else:
            for j in range(size - 1):
                y_total = cells[x + size - 1][y + j]
        if size - 1 in row_cache[(x, y + size - 1)]:
            x_total = row_cache[(x, y + size - 1)][size - 1]
        else:
            for i in range(size - 1):
                x_total = cells[x + i][y + size - 1]
        total += x_total + y_total
        corner = cells[x + size - 1][y + size - 1]
        col_cache[(x + size - 1, y)][size] = y_total + corner
        row_cache[(x, y + size - 1)][size] = x_total + corner
        total += corner
    else:
        total = 0
        for i in range(size):
            for j in range(size):
                total += cells[x + i][y + j]
    cache[(x, y)][size] = total
    return total


def find_max_power(cells, sizes):
    cache, row_cache, col_cache = (defaultdict(dict) for i in range(3))
    max_total = None
    for size in sizes:
        for x in range(1, 300 - size + 1):
            for y in range(1, 300 - size + 1):
                total = stack(x - 1, y - 1,
                              size, cells, cache, row_cache, col_cache)
                if max_total is None or total > max_total:
                    max_total = total
                    square = (str(x), str(y), str(size))

    return square
