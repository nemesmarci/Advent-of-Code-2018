import sys

line = int(sys.stdin.readline().strip())

recipes = [3, 7]
elf1 = 0
elf2 = 1

for i in range(line + 10):
    s = recipes[elf1] + recipes[elf2]
    for c in str(s):
        recipes.append(int(c))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print("".join((str(r) for r in recipes[line: line + 10])))