import sys
import re
from collections import defaultdict

completed = []

class Worker:
    def __init__(self):
        self.free = True
        self.time = -1
        self.task = None
        
    def tick(self):
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.free = True
            completed.append(self.task)
            self.task = None
            self.time = -1
    
    def start(self, task, time):
        self.time = time
        self.task = task
        self.free = False

pat = re.compile(r"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$")
rules = defaultdict(list)
steps = set()

for line in sys.stdin.readlines():
    a, b = pat.match(line).groups()
    steps.add((a, int(ord(a) - 4)))
    steps.add((b, int(ord(b) - 4)))
    rules[b] += a

workers = [Worker() for i in range(5)]
time = 0
started = []
while len(completed) < len(steps):
    for c in sorted(steps):
        if c[0] not in completed and c[0] not in started:
            valid = True
            for r in rules[c[0]]:
                if r not in completed:
                    valid = False
                    break
            if valid:
                for w in workers:
                    if w.free:
                        w.start(c[0], c[1])
                        started.append(c[0])
                        break
    for w in workers:
        w.tick()
    time += 1
print(time)