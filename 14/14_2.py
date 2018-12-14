import sys

line = [int(c) for c in sys.stdin.readline().strip()]

recipes = [3, 7]
elf1 = 0
elf2 = 1

while(True):
    s = recipes[elf1] + recipes[elf2]
    for c in str(s):
        recipes.append(int(c))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

    if recipes[-len(line):] == line or recipes[-len(line)-1:-1] == line:
        break

mod = -1 if recipes[-len(line)-1:-1] == line else 0
print(len(recipes) - len(line) + mod)