import sys
from copy import deepcopy
from collections import defaultdict

lines = sys.stdin.readlines()
size = len(lines)
original_cave = defaultdict(lambda: '.')


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


original_goblins = 0
original_elves = 0
original_units = []

for y, line in enumerate(lines):
    for x, c in enumerate(line.strip()):
        if c in 'GE':
            unit = Unit(x, y, c)
            original_units.append(unit)
            original_cave[(x, y)] = unit
            if c == 'G':
                original_goblins += 1
            else:
                original_elves += 1
        else:
            original_cave[(x, y)] = c


def path(begin, end):
    counters = dict()
    visited = [end]
    counters[end] = 0
    i = 0
    found = False
    while i < len(visited) and not found:
        current = visited[i]
        value = counters[current]
        for neighbour in get_neighbours(current):
            if ((cave[neighbour] == '.' or neighbour == begin) and
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

    next_step = min([n for n in get_neighbours(begin) if n in counters],
                    key=lambda n: counters[n])

    return counters[begin], next_step


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return up, left, right, down


def open_squares_around(unit):
    return [n for n in get_neighbours(unit.location()) if cave[n] == '.']


def can_attack(attacker):
    neighbours = get_neighbours(attacker.location())
    local_enemies = []
    for n in neighbours:
        if type(cave[n]) is Unit and cave[n].species != attacker.species:
            local_enemies.append(cave[n])
    if len(local_enemies) > 0:
        return min(local_enemies, key=lambda e: e.hp)
    return None


def attack(unit, target):
    target.hp -= unit.ap
    if target.hp < 0:
        cave[target.location()] = '.'
        units.remove(target)
        if target.species == 'G':
            global goblins
            goblins -= 1
        else:
            global elves
            elves -= 1
            global victory
            victory = False

elves_ap = 3
victory = False

while not victory:
    elves_ap += 1
    rounds = 0
    victory = True
    cave = deepcopy(original_cave)
    units = deepcopy(original_units)
    for unit in units:
        cave[unit.location()] = unit
        if unit.species == 'E':
            unit.ap = elves_ap        
    elves = original_elves
    goblins = original_goblins

    while elves > 0 and goblins > 0:
        if not victory:
            break
        units_in_round = sorted(units)
        for unit in units_in_round:
            if unit not in units:
                continue
            target = can_attack(unit)
            if target is not None:
                attack(unit, target)
                if not victory:
                    break
                continue
            targets = set()
            enemies = [u for u in units if u.species != unit.species]

            for enemy in enemies:
                targets.update(open_squares_around(enemy))

            targets = sorted(targets, key=lambda t: (t[1], t[0]))
            if len(targets) == 0:
                continue
            steps = [path(unit.location(), t) for t in targets]
            steps = [s for s in steps if s is not None]
            if len(steps) == 0:
                continue
            next_step = min(steps, key=lambda s: s[0])[1]
            cave[unit.location()] = '.'
            cave[next_step] = unit
            unit.x = next_step[0]
            unit.y = next_step[1]
            target = can_attack(unit)
            if target is not None:
                attack(unit, target)
        rounds += 1

print((rounds - 1) * sum(units))