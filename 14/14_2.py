from common import iterate, INITIAL

with open('input.txt') as data:
    scores = [int(c) for c in data.read()]

recipes, elf1, elf2 = INITIAL

while(True):
    elf1, elf2 = iterate(recipes, elf1, elf2)

    if recipes[-len(scores):] == scores \
            or recipes[-len(scores)-1:-1] == scores:
        break

offset = -1 if recipes[-len(scores)-1:-1] == scores else 0
print(len(recipes) - len(scores) + offset)
