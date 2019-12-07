with open('input.txt') as data:
    lines = data.readlines()

frequency = 0
frequencies = set()

found = False
while not found:
    for line in lines:
        frequencies.add(frequency)
        frequency += int(line)
        if frequency in frequencies:
            found = True
            break

print(frequency)
