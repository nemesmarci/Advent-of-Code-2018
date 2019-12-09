from common import read_data, Map, run

bg = Map(*read_data())
rounds = run(bg)[1]
print((rounds - 1) * sum(bg.units))
