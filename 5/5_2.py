import sys
from functools import reduce

def react(a, b):
    lhs, ret = (a[-1], a[:-1]) if len(a) > 1 else (a, "")
    return ret if lhs != b and lhs.lower() == b.lower() else a + b  

line = sys.stdin.read().strip()
results = dict()
chars = set(line.lower())
for c in chars:
    removed = list(filter(lambda x: x.lower() != c, line))
    results[c] = len(reduce(react, removed))
    
print(min(results.values()))