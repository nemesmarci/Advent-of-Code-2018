import sys

frequency = 0
frequencies = set()
lines = sys.stdin.readlines()
found = False
while not found:
    for line in lines:
        frequencies.add(frequency)
        frequency += int(line)
        if frequency in frequencies:
          found = True
          break
print(frequency)