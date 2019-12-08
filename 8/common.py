class Node:
    def __init__(self, childs, meta):
        self.childs = childs
        self.meta = meta


def read_data():
    with open('input.txt') as data:
        return [int(c) for c in data.readline().split()]


def parse(n, line):
    n_childs = line[n]
    n += 1
    n_meta = line[n]
    childs = []
    meta = []
    for i in range(n_childs):
        n += 1
        n, child = parse(n, line)
        childs.append(child)
    for i in range(n_meta):
        n += 1
        meta.append(line[n])
    return n, Node(childs, meta)
