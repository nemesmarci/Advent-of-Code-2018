from common import read_data, get_guards, answer

guards = get_guards(read_data())
max_sleep = max(guards, key=lambda g: sum(guards[g].values()))
print(answer(guards, max_sleep))
