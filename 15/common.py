from collections import defaultdict


def read_data():
    cave = defaultdict(lambda: '.')
    goblins, elves, units = [0, 0, []]

    with open('input.txt') as data:
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                if c in 'GE':
                    unit = Unit(x, y, c)
                    units.append(unit)
                    cave[(x, y)] = unit
                    if c == 'G':
                        goblins += 1
                    else:
                        elves += 1
                else:
                    cave[(x, y)] = c

    return goblins, elves, units, cave


class Unit:
    def __init__(self, x, y, species):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
        self.species = species

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def location(self):
        return (self.x, self.y)

    def __radd__(self, other):
        return self.hp + other


class Map:
    def __init__(self, goblins, elves, units, cave):
        self.goblins = goblins
        self.elves = elves
        self.units = units
        self.cave = cave
        self.lost = False

    def path(self, begin, end):
        counters = dict()
        visited = [end]
        counters[end] = 0
        i = 0
        found = False
        while i < len(visited) and not found:
            current = visited[i]
            value = counters[current]
            for neighbour in self.get_neighbours(current):
                if ((self.cave[neighbour] == '.' or neighbour == begin) and
                   (neighbour not in counters or neighbour in counters and
                        value + 1 < counters[neighbour])):
                    visited.append(neighbour)
                    counters[neighbour] = value + 1
                    if neighbour == begin:
                        found = True
                        break
            i += 1

        if not found:
            return None

        next_step = min([
            n for n in self.get_neighbours(begin) if n in counters],
                        key=lambda n: counters[n])

        return counters[begin], next_step

    def get_neighbours(self, current):
        up = (current[0], current[1] - 1)
        left = (current[0] - 1, current[1])
        right = (current[0] + 1, current[1])
        down = (current[0], current[1] + 1)
        return up, left, right, down

    def open_squares_around(self, unit):
        return [n for n in self.get_neighbours(unit.location())
                if self.cave[n] == '.']

    def can_attack(self, attacker):
        neighbours = self.get_neighbours(attacker.location())
        local_enemies = []
        for n in neighbours:
            if type(self.cave[n]) is Unit \
                    and self.cave[n].species != attacker.species:
                local_enemies.append(self.cave[n])
        if len(local_enemies) > 0:
            return min(local_enemies, key=lambda e: e.hp)
        return None

    def attack(self, unit, target):
        target.hp -= unit.ap
        if target.hp < 0:
            self.cave[target.location()] = '.'
            self.units.remove(target)
            if target.species == 'G':
                self.goblins -= 1
            else:
                self.elves -= 1
                self.lost = True


def run(bg, powerup=0, return_early=False):
    for unit in bg.units:
        if unit.species == 'E':
            unit.ap += powerup

    rounds = 0
    while bg.elves > 0 and bg.goblins > 0:
        units_in_round = sorted(bg.units)

        for unit in units_in_round:
            if unit not in bg.units:
                continue

            target = bg.can_attack(unit)
            if target is not None:
                bg.attack(unit, target)
                if return_early and bg.lost:
                    return False, None
                continue

            enemies = [u for u in bg.units if u.species != unit.species]
            targets = set()
            for enemy in enemies:
                targets.update(bg.open_squares_around(enemy))
            if len(targets) == 0:
                continue

            targets = sorted(targets, key=lambda t: (t[1], t[0]))
            steps = [s for s in (bg.path(unit.location(), t) for t in targets)
                     if s is not None]
            if len(steps) == 0:
                continue

            next_step = min(steps, key=lambda s: s[0])[1]
            bg.cave[unit.location()] = '.'
            bg.cave[next_step] = unit
            unit.x = next_step[0]
            unit.y = next_step[1]
            target = bg.can_attack(unit)
            if target is not None:
                bg.attack(unit, target)
                if return_early and bg.lost:
                    return False, None

        rounds += 1

    return True, rounds
