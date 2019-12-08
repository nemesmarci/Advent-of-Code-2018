import re
import copy


def read_data():
    with open('input.txt') as data:
        initial = data.readline().strip().split(': ')[1]
        lines = data.readlines()

    regex = re.compile(r"^(.{5}) => (.){1}$")

    rules = dict()
    for line in lines:
        match = regex.match(line)
        if match:
            a, b = regex.match(line).groups()
            if a[2] != b:
                rules[a] = b

    initial = list(initial)

    if initial[0:4] != list(4 * '.'):
        n_prepends = 4
        initial = list(4 * '.') + initial

    if initial[-4:] != list(4 * '.'):
        initial += list(4 * '.')

    return list(initial), rules, n_prepends


def run(generations):
    initial, rules, n_prepends = read_data()
    prev_sum = 0
    prev_diff = 0
    next_step = copy.deepcopy(initial)

    for generation in range(generations):
        for i in range(2, len(initial) - 3):
            local = "".join(initial[i - 2: i + 3])
            if local in rules:
                next_step[i] = rules[local]

        current_sum = sum(i - n_prepends for i in range(len(next_step))
                          if next_step[i] == '#')

        diff = current_sum - prev_sum
        if diff == prev_diff:
            break

        prev_sum = current_sum
        prev_diff = diff

        if next_step[0:4] != list(4 * '.'):
            n_prepends += 4
            next_step = list(4 * '.') + next_step
        elif next_step[0:8] == list(8 * '.'):
            n_prepends -= 4
            next_step = next_step[4:]
        if next_step[-4:] != list(4 * '.'):
            next_step += list(4 * '.')
        elif next_step[-8:] == list(8 * '.'):
            next_step = next_step[-4]

        initial = copy.deepcopy(next_step)

    return current_sum + (generations - generation - 1) * diff
