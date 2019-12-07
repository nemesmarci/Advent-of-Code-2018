import re
from collections import defaultdict


PATTERN = re.compile(r"^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$")


def read_data():
    with open('input.txt') as data:
        return data.readlines()


def parse_line(line):
    return [int(x) for x in PATTERN.match(line).groups()]


def process(data):
    conflicts = 0
    squares = defaultdict(int)
    for line in data:
        num, xcoord, ycoord, width, height = parse_line(line)
        for i in range(xcoord, xcoord + width):
            for j in range(ycoord, ycoord + height):
                squares[(i, j)] += 1
                if squares[(i, j)] == 2:
                    conflicts += 1
    return conflicts, squares
