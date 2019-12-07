from common import read_data, run

rules, steps = read_data()

print(run(steps, rules, completed=[], n_workers=5))
