import re
from collections import defaultdict

BEFORE = re.compile(r"^Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
AFTER = re.compile(r"^After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
INSTR = re.compile(r"^([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)$")

INSTRUCTIONS = ["adrr", "adri", "murr", "muri", "barr", "bari", "borr", "bori",
                "ser_", "sei_", "gtrr", "gtri", "gtir", "eqrr", "eqri", "eqir"]


class Processor:
    def __init__(self):
        self.registers = [0, 0, 0, 0]
        with open('input.txt') as data:
            lines = data.readlines()

        i = 0
        test_data = []
        at_code = False

        while not at_code:
            if BEFORE.match(lines[i]):
                test_data.extend(lines[i:i + 4])
                i += 4

            else:
                at_code = True
                i += 2

        self.program = lines[i:]
        self.parse_test_data(test_data)
        self.instructions_parsed = False

    def parse_test_data(self, test_data):
        self.instr_map = defaultdict(set)
        self.three_or_more = 0

        i = 0
        while i < len(test_data):
            match = BEFORE.match(test_data[i])
            inputs = [int(c) for c in match.groups()]
            instr, lhs, rhs, out = (
                int(c) for c in INSTR.match(test_data[i + 1]).groups()
            )
            outputs = [
                int(c) for c in AFTER.match(test_data[i + 2]).groups()
            ]

            possible_instructions = 0
            for my_instr in INSTRUCTIONS:
                if self.test(my_instr, inputs, outputs, lhs, rhs, out):
                    self.instr_map[my_instr].add(instr)
                    possible_instructions += 1

            if possible_instructions >= 3:
                self.three_or_more += 1

            i += 4

    def determine_instructions(self):
        self.code_map = dict()

        while len(self.instr_map) > 0:
            instr = sorted(self.instr_map,
                           key=lambda i: len(self.instr_map[i]))[0]
            code = list(self.instr_map[instr])[0]
            self.code_map[code] = instr
            del self.instr_map[instr]
            for instr in self.instr_map:
                self.instr_map[instr].discard(code)

        self.instructions_parsed = True

    def execute(self, instr, lhs, rhs, out):
        op = instr[:2]
        a = instr[2]
        b = instr[3]

        if a == 'r':
            lhs = int(self.registers[lhs])
        if b == 'r':
            rhs = int(self.registers[rhs])

        if op == 'ad':
            self.registers[out] = lhs + rhs
        elif op == 'mu':
            self.registers[out] = lhs * rhs
        elif op == 'ba':
            self.registers[out] = lhs & rhs
        elif op == 'bo':
            self.registers[out] = lhs | rhs
        elif op == 'se':
            self.registers[out] = lhs
        elif op == 'gt':
            self.registers[out] = 1 if lhs > rhs else 0
        elif op == 'eq':
            self.registers[out] = 1 if lhs == rhs else 0

    def load(self, values):
        self.registers = list(values)

    def test(self, instr, inputs, outputs, lhs, rhs, out):
        self.registers = list(inputs)
        self.execute(instr, lhs, rhs, out)
        return self.registers == outputs

    def run(self):
        if not self.instructions_parsed:
            self.determine_instructions()

        for line in self.program:
            instr, lhs, rhs, out = (int(c) for c in INSTR.match(line).groups())
            self.execute(self.code_map[instr], lhs, rhs, out)

        return self.registers[0]
