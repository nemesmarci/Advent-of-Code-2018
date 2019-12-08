INITIAL = [3, 7], 0, 1


def iterate(recipes=[3, 7], elf1=0, elf2=1):
    s = recipes[elf1] + recipes[elf2]
    for c in str(s):
        recipes.append(int(c))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    return elf1, elf2
