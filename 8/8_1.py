from common import read_data, parse


def value(node):
    v = sum(node.meta)
    for child in node.childs:
        v += value(child)
    return v


root = parse(0, read_data())[1]
print(value(root))
