import sys

frequency = 0
lines = sys.stdin.readlines()
for line in lines:
    frequency += int(line)
print(frequency)