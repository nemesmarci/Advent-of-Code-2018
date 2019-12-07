from common import read_data, get_guards, answer

guards = get_guards(read_data())
max_sleep = max(guards, key=lambda g: guards[g].most_common()[0][1])
print(answer(guards, max_sleep))
