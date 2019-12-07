from functools import reduce
from common import react

with open('input.txt') as data:
    line = data.read().strip()

results = dict()
chars = set(line.lower())
for c in chars:
    removed = list(filter(lambda x: x.lower() != c, line))
    results[c] = len(reduce(react, removed))

print(min(results.values()))
