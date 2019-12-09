from copy import deepcopy
from common import read_data, Map, run

powerup = 0
victory = False
origin = Map(*read_data())

while not victory:
    powerup += 1
    bg = deepcopy(origin)
    victory, rounds = run(bg, powerup, return_early=True)
    if victory:
        break

print((rounds - 1) * sum(bg.units))
