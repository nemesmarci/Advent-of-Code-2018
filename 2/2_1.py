from collections import Counter

twos = 0
threes = 0
with open('input.txt') as data:
    for line in data:
        cnt = Counter(line)
        if 2 in cnt.values():
            twos += 1
        if 3 in cnt.values():
            threes += 1

print(twos * threes)
