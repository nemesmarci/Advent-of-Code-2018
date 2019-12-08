from common import iterate, INITIAL

with open('input.txt') as data:
    iterations = int(data.read())

recipes, elf1, elf2 = INITIAL

for i in range(iterations + 10):
    elf1, elf2 = iterate(recipes, elf1, elf2)

print("".join((str(r) for r in recipes[iterations: iterations + 10])))
