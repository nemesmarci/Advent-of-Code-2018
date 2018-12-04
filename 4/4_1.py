import re
import sys
from collections import defaultdict, Counter
from datetime import datetime

pattern = re.compile(
    r"^\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})\] (.*)$")

guard_regex = re.compile(r"^Guard #([0-9]+) .*$")

records = dict()
for line in sys.stdin.readlines():
    timestamp, msg = pattern.match(line).groups()
    records[timestamp] = msg
guards = defaultdict(Counter)
for key in sorted(records.keys()):
    guard = guard_regex.match(records[key])
    if guard:
        guard_id = guard.group(1)
    elif "falls" in records[key]:
        start = datetime.strptime(key, "%Y-%m-%d %H:%M").minute
    elif "wakes" in records[key]:
        end = datetime.strptime(key, "%Y-%m-%d %H:%M").minute
        for i in range(start, end):
            guards[guard_id][i] += 1

max_sleep = max(guards, key=lambda g: sum(guards[g].values()))
print(guards[max_sleep].most_common()[0][0] * int(max_sleep))