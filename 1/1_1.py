frequency = 0
with open('input.txt') as data:
    for line in data:
        frequency += int(line)
print(frequency)
