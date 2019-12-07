import re
from collections import defaultdict, Counter
from datetime import datetime


def read_data():
    with open('input.txt') as data:
        return data.readlines()


def get_guards(lines):
    pattern = re.compile(
        r"^\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})\] (.*)$")
    guard_regex = re.compile(r"^Guard #([0-9]+) .*$")

    records = dict()
    for line in lines:
        timestamp, msg = pattern.match(line).groups()
        records[timestamp] = msg

    guards = defaultdict(Counter)
    for key in sorted(records.keys()):
        guard = guard_regex.match(records[key])
        if guard:
            guard_id = int(guard.group(1))
        elif "falls" in records[key]:
            start = datetime.strptime(key, "%Y-%m-%d %H:%M").minute
        elif "wakes" in records[key]:
            end = datetime.strptime(key, "%Y-%m-%d %H:%M").minute
            for i in range(start, end):
                guards[guard_id][i] += 1

    return guards


def answer(guards, max_sleep):
    return guards[max_sleep].most_common()[0][0] * max_sleep
