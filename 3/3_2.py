import sys
import re
from collections import defaultdict

squares = defaultdict(int)
conflicts = 0
pattern = re.compile(r"^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$")
lines = sys.stdin.readlines()
for line in lines:
    num, xcoord, ycoord, width, height = [
        int(x) for x in pattern.match(line).groups()]
    for i in range(xcoord, xcoord + width):
        for j in range(ycoord, ycoord + height):
            squares[(i, j)] += 1
            if squares[(i, j)] == 2:
                conflicts += 1

for line in lines:
    num, xcoord, ycoord, width, height = [
        int(x) for x in pattern.match(line).groups()]
    overlap = False
    for i in range(xcoord, xcoord + width):
        for j in range(ycoord, ycoord + height):
            if squares[(i, j)] != 1:
                overlap = True
                break
        if overlap:
            break
    if not overlap:
        print(num)
        break