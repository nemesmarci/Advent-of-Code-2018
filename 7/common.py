import re
from collections import defaultdict


class Worker:
    def __init__(self, completed):
        self.free = True
        self.time = -1
        self.task = None
        self.completed = completed

    def tick(self):
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.free = True
            self.completed.append(self.task)
            self.task = None
            self.time = -1

    def start(self, task, time):
        self.time = time
        self.task = task
        self.free = False


def read_data():
    pat = re.compile(
            r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$")
    rules = defaultdict(list)
    steps = set()

    with open('input.txt') as data:
        for line in data:
            a, b = pat.match(line).groups()
            steps.add((a, 61 + ord(a) - ord('A')))
            steps.add((b, 61 + ord(b) - ord('A')))
            rules[b] += a
    return rules, steps


def run(steps, rules, completed, n_workers):
    started, time = [], 0
    workers = [Worker(completed) for i in range(n_workers)]

    while len(completed) < len(steps):
        for step in sorted(steps):
            name, duration = step
            if name not in completed and name not in started:
                valid = True
                for r in rules[name]:
                    if r not in completed:
                        valid = False
                        break
                if valid:
                    for w in workers:
                        if w.free:
                            w.start(name, duration)
                            started.append(name)
                            break
        for w in workers:
            w.tick()
        time += 1

    return time
