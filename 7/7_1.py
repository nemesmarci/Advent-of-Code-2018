import sys
import re
from collections import defaultdict

pat = re.compile(r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$")
rules = defaultdict(list)
steps = set()

for line in sys.stdin.readlines():
    a, b = pat.match(line).groups()
    steps.add(a)
    steps.add(b)
    rules[b] += a

completed = []

while len(completed) < len(steps):
    for c in sorted(steps):
        found = False
        if c not in completed:
            valid = True
            for r in rules[c]:
                if r not in completed:
                    valid = False
                    break
            if valid:
                completed.append(c)
                found = True
        if found:
            break

print("".join(completed))