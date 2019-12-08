from common import read_data, find_max_power

cells = read_data()
print(",".join(find_max_power(cells, range(1, 300 + 1))))
