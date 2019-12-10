import re

BEFORE = re.compile(r"^Before: \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
AFTER = re.compile(r"^After:  \[([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\]$")
INSTR = re.compile(r"^([a-z]+) ([0-9]+) ([0-9]+) ([0-9]+)$")

INSTRUCTIONS = ["adrr", "adri", "murr", "muri", "barr", "bari", "borr", "bori",
                "ser_", "sei_", "gtrr", "gtri", "gtir", "eqrr", "eqri", "eqir"]


INSTR_MAP = {"addr": "adrr", "addi": "adri", "mulr": "murr", "muli": "muri",
             "banr": "barr", "bani": "bari", "setr": "ser_", "seti": "sei_"}


class Processor:
    def __init__(self):
        self.registers = [0, 0, 0, 0, 0, 0]
        with open('input.txt') as data:
            lines = data.readlines()

        self.program = lines[1:]
        self.ip_reg = int(lines[0].split()[1])

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

    def run(self, return_early=False):
        ip = self.registers[self.ip_reg]
        while ip < len(self.program):
            instr, lhs, rhs, out = INSTR.match(self.program[ip]).groups()
            lhs, rhs, out = [int(x) for x in (lhs, rhs, out)]
            if instr in INSTR_MAP:
                instr = INSTR_MAP[instr]
            self.registers[self.ip_reg] = ip
            self.execute(instr, lhs, rhs, out)
            ip = self.registers[self.ip_reg]
            if ip == 0 and return_early:
                return
            ip += 1

        return self.registers[0]
