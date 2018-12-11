import sys
import numpy as np
from collections import defaultdict

serial = int(sys.stdin.readline().strip())

cells = np.zeros((300, 300), dtype=int)

for i in range(1, 300 + 1):
    for j in range(1, 300 + 1):
        rack_id = i + 10
        power = rack_id * j
        power += serial
        power *= rack_id
        power = str(power)
        power = int(power[-3]) if len(power) > 2 else 0
        power -= 5
        cells[i - 1][j - 1] = power

cache = defaultdict(dict)
row_cache = defaultdict(dict)
col_cache = defaultdict(dict)

def stack(x, y, size):
    if size - 1 in cache[(x, y)]:
        total = cache[(x, y)][size - 1]
        y_total = 0
        x_total = 0
        if size - 1 in col_cache[(x + size - 1, y)]:
            y_total += col_cache[(x + size - 1, y)][size - 1]
        else:
            for j in range(size - 1):
                y_total += cells[x + size - 1][y + j]
        if size - 1 in row_cache[(x, y + size - 1)]:
            x_total += row_cache[(x, y + size - 1)][size - 1]
        else:
            for i in range(size - 1):
                x_total += cells[x + i][y + size - 1]
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

max_total = None
max_size = None
for size in range(1, 300 + 1):
    for i in range(1, 300 - size + 1):
        for j in range(1, 300 - size + 1):
            total = stack(i - 1, j - 1, size)
            if max_total is None or total > max_total:
                max_total = total
                max_size = size
                square = (str(i), str(j), str(size))
print(",".join(square))