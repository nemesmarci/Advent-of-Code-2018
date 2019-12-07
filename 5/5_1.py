from common import react
from functools import reduce

with open('input.txt') as data:
    print(len(reduce(react, data.read().strip())))
