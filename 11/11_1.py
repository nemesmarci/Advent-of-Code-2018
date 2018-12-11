import sys
import numpy as np

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

def stack(x, y):
    total = 0
    for i in range(3):
        for j in range(3):
            total += cells[x + i][y + j]
    return total

max_total = None
for i in range(1, 300 - 2):
    for j in range(1, 300 - 2):
        total = stack(i - 1, j - 1)
        if max_total is None or total > max_total:
            max_total = total
            square = (str(i), str(j))
print(",".join(square))