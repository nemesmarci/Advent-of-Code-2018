from collections import defaultdict


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return up, left, right, down


def find_matching(string):
    opening = 0
    closing = 0
    for i, c in enumerate(string):
        if c == '(':
            opening += 1
        elif c == ')':
            closing += 1
        if opening == closing:
            return i


class Rooms:
    def __init__(self):
        with open('input.txt') as data:
            routes = data.read().strip()[1:-1]

        self.cave = defaultdict(lambda: '#')
        self.rooms = set()

        start = (0, 0)
        self.cave[start] = '.'
        self.rooms.add(start)

        self.parse(routes, *start)
        self.distances = self.BFS()

    def parse(self, string, x, y):
        x0, y0 = x, y
        i = 0

        while i < len(string):
            c = string[i]

            if c == '(':
                closing = i + find_matching(string[i:])
                sub = string[i:closing + 1]
                self.parse(sub[1:-1], x, y)
                i += len(sub)

            elif c in 'NWSE':
                if c in 'WE':
                    x_step = 1 if c == 'E' else -1
                    x += x_step
                    self.cave[(x, y)] = '|'
                    x += x_step
                    self.cave[(x, y)] = '.'

                else:
                    y_step = 1 if c == 'S' else -1
                    y += y_step
                    self.cave[(x, y)] = '-'
                    y += y_step
                    self.cave[(x, y)] = '.'

                self.rooms.add((x, y))
                i += 1

            elif c == '|':
                x, y = x0, y0
                i += 1

            else:
                i += 1

    def BFS(self):
        distances = dict()
        distances[(0, 0)] = 0
        queue = [(0, 0)]

        while queue:
            current = queue.pop(0)
            current_distance = distances[current]

            for p in get_neighbours(current):
                tile = self.cave[p]

                if tile == '#':
                    continue

                step = 0 if tile in '-|' else 1

                if p in distances and distances[p] < current_distance + 1:
                    continue

                distances[p] = current_distance + step
                queue.append(p)

        return distances
