from common import read_data, run

mine, carts = read_data()

print("{},{}".format(*run(mine, carts)))
