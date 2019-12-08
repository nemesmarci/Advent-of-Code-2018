from common import read_data, find_max_power

cells = read_data()
print(",".join(find_max_power(cells, [3])[:-1]))
