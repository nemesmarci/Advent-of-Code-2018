from common import read_data, run

rules, steps = read_data()

completed = []
run(steps, rules, completed=completed, n_workers=1)
print("".join(completed))
