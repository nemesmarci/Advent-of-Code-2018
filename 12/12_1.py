import re
import sys
import copy

initial = sys.stdin.readline().strip().split(': ')[1]
lines = sys.stdin.readlines()

regex = re.compile(r"^(.{5}) => (.){1}$")

rules = dict()
for line in lines:
    match = regex.match(line)
    if match:
        a, b = regex.match(line).groups()
        if a[2] != b:
            rules[a] = b

initial = list(initial)
num_of_prepends = 0

if initial[0:4] != list(4 * '.'):
    num_of_prepends += 4
    initial = list(4 * '.') + initial

if initial[-4:] != list(4 * '.'):
    initial += list(4 * '.')

next_step = copy.deepcopy(initial)

for generation in range(20):
    for i in range(2, len(initial) - 3):
        local = "".join(initial[i - 2: i + 3])
        if local in rules:
            next_step[i] = rules[local]

    if next_step[0:4] != list(4 * '.'):
        num_of_prepends += 4
        next_step = list(4 * '.') + next_step
    elif next_step[0:8] == list(8 * '.'):
        num_of_prepends -= 4
        next_step = next_step[4:]
    if next_step[-4:] != list(4 * '.'):
        next_step += list(4 * '.')
    elif next_step[-8:] == list(8 * '.'):
        next_step = next_step[-4]
    initial = copy.deepcopy(next_step) 

sum_of_ids = 0
for i in range(len(initial)):
    if initial[i] == '#':
        sum_of_ids += i - num_of_prepends
print(sum_of_ids)