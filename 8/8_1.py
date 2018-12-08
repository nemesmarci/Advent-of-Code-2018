import sys

class Node:
    def __init__(self, childs, meta):
        self.childs = childs
        self.meta = meta

def parse_node(n):
    n_childs = int(line[n])
    n += 1
    n_meta = int(line[n])
    childs = []
    meta = []
    for i in range(n_childs):
        n += 1
        j, child = parse_node(n)
        childs.append(child)
        n += (j - n)
    for i in range(n_meta):
        n += 1
        m = int(line[n])
        meta.append(m)
    return (n, Node(childs, meta))

def value(node):
    v = sum(node.meta)
    for child in node.childs:
        v += value(child)
    return v

line = sys.stdin.readline().split()

root = parse_node(0)[1]
print(value(root))