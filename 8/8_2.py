from common import read_data, parse


def value(node):
    v = 0
    if len(node.childs) == 0:
        return sum(node.meta)
    for i in node.meta:
        if i == 0 or i > len(node.childs):
            continue
        v += value(node.childs[i-1])
    return v


root = parse(0, read_data())[1]
print(value(root))
