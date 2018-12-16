import re
import sys
from copy import deepcopy
from collections import defaultdict

before_regex = re.compile(r"^Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
after_regex = re.compile(r"^After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
instr_regex = re.compile(r"^([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)$")

instructions = ["adrr", "adri", "murr", "muri", "barr", "bari", "borr", "bori",
                "ser_", "sei_", "gtrr", "gtri", "gtir", "eqrr", "eqri", "eqir"]


def execute(instr, lhs, rhs, out):
    op = instr[0:2]
    a = instr[2]
    b = instr[3]

    if a == 'r':
        lhs = int(registers[lhs])
    if b == 'r':
        rhs = int(registers[rhs])

    if op == 'ad':
        registers[out] = lhs + rhs
    elif op == 'mu':
        registers[out] = lhs * rhs
    elif op == 'ba':
        registers[out] = lhs & rhs
    elif op == 'bo':
        registers[out] = lhs | rhs
    elif op == 'se':
        registers[out] = lhs
    elif op == 'gt':
        registers[out] = 1 if lhs > rhs else 0
    elif op == 'eq':
        registers[out] = 1 if lhs == rhs else 0

lines = sys.stdin.readlines()
instr_map = defaultdict(set)
at_code = False
i = 0

while not at_code:
    match = before_regex.match(lines[i])
    if match:
        inputs = [int(c) for c in match.groups()]
        instr, lhs, rhs, out = [int(c) for c in instr_regex.match(lines[i + 1]).groups()]
        outputs = [int(c) for c in after_regex.match(lines[i + 2]).groups()]

        for my_instr in instructions:
            registers = deepcopy(inputs)
            execute(my_instr, lhs, rhs, out)
            if registers == outputs:
                instr_map[my_instr].add(instr)

        i += 4
    else:
        at_code = True
        i += 2

code_map = dict()

while len(instr_map) > 0:
    instr = sorted(instr_map, key=lambda i: len(instr_map[i]))[0]
    code = list(instr_map[instr])[0]
    code_map[code] = instr
    del instr_map[instr]
    for instr in instr_map:
        instr_map[instr].discard(code)

registers = [0, 0, 0, 0]
for i in range(i, len(lines)):
    instr, lhs, rhs, out = [int(c) for c in instr_regex.match(lines[i]).groups()]
    execute(code_map[instr], lhs, rhs, out)

print(registers[0])