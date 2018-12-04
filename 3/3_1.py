import sys
import re
from collections import defaultdict

squares = defaultdict(int)
conflicts = 0
for line in sys.stdin.readlines():
    pattern = re.compile(r"^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$")
    num, xcoord, ycoord, width, height = [
        int(x) for x in pattern.match(line).groups()]
    for i in range(xcoord, xcoord + width):
        for j in range(ycoord, ycoord + height):
            squares[(i, j)] += 1
            if squares[(i, j)] == 2:
                conflicts += 1
print(conflicts)