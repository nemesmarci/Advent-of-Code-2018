import re
from collections import defaultdict, namedtuple


Coordinate = namedtuple('Coordinate', 'x y')
TILES = defaultdict(lambda: '.')


def read_map():
    min_y = max_y = None
    min_x = max_x = None
    TILES[500, 0] = '+'
    with open('input.txt') as coordinates:
        regex = re.compile(r"^(x|y)=([0-9]+), (x|y)=([0-9]+)\.\.([0-9]+)$")
        for line in coordinates:
            first_coord, a, second_coord, b, c = regex.match(line).groups()
            a, b, c = [int(i) for i in [a, b, c]]
            if first_coord == 'x':
                if min_x is None or a < min_x:
                    min_x = a
                if max_x is None or a > max_x:
                    max_x = a
                if min_y is None or b < min_y:
                    min_y = b
                if max_y is None or c > max_y:
                    max_y = c
                for i in range(b, c + 1):
                    TILES[a, i] = '#'
            else:
                if min_y is None or a < min_y:
                    min_y = a
                if max_y is None or a > max_y:
                    max_y = a
                if min_x is None or b < min_x:
                    min_x = b
                if max_x is None or c > max_x:
                    max_x = c
                for i in range(b, c + 1):
                    TILES[i, a] = '#'
    return min_x, max_x, min_y, max_y


MIN_X, MAX_X, MIN_Y, MAX_Y = read_map()


def up(current):
    return Coordinate(x=current.x, y=current.y - 1)


def down(current):
    return Coordinate(x=current.x, y=current.y + 1)


def left(current):
    return Coordinate(x=current.x - 1, y=current.y)


def right(current):
    return Coordinate(x=current.x + 1, y=current.y)


def make_dry(direction, origin):
    current = origin
    while TILES[current] == '~':
        TILES[current] = '|'
        current = left(current) if direction == 'left' else right(current)


def flow_left(current):
    wall = False
    while not wall and TILES[down(current)] not in '.|':
        if TILES[left(current)] in '.|':
            current = left(current)
            TILES[current] = '~'
        else:
            wall = True
    if TILES[down(current)] in '.|':
        make_dry('right', current)
        flow_down(current)
        return False
    else:
        return True


def flow_right(current):
    wall = False
    while not wall and TILES[down(current)] not in '.|':
        if TILES[right(current)] in '.|':
            current = right(current)
            TILES[current] = '~'
        else:
            wall = True
    if TILES[down(current)] in '.|':
        make_dry('left', current)
        flow_down(current)
        return False
    else:
        return True


def flow_down(current):
    wall = False
    while not wall:
        if current.y >= MAX_Y:
            return
        if TILES[down(current)] == '.':
            current = down(current)
            TILES[current] = '|'
        else:
            wall = True
    if full(down(current)):
        TILES[current] = '~'
        left_side = flow_left(current)
        right_side = flow_right(current)
    else:
        return
    while left_side and right_side:
        current = up(current)
        TILES[current] = '~'
        left_side = flow_left(current)
        right_side = flow_right(current)
        if TILES[current] == '|':
            make_dry('right', right(current))


def full(origin):
    if TILES[origin] == '#':
        return True
    current = origin
    while True:
        current = left(current)
        if TILES[current] == '#':
            break
        if TILES[current] in '.|':
            return False
    current = origin
    while True:
        current = right(current)
        if TILES[current] == '#':
            break
        if TILES[current] in '.|':
            return False
    return True


def solve(include_dried):
    spring = Coordinate(500, 0)
    flow_down(spring)

    water = 0
    for y in range(MIN_Y, MAX_Y + 1):
        for x in range(MIN_X - 1, MAX_X + 2):
            current = TILES[x, y]
            if current == '~' or include_dried and current == '|':
                water += 1
    return water
