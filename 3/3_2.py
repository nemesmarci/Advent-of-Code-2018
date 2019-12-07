from common import read_data, process, parse_line

lines = read_data()
_, squares = process(lines)


def find_fabric(lines, squares):
    for line in lines:
        num, xcoord, ycoord, width, height = parse_line(line)
        overlap = False

        def overlap():
            for i in range(xcoord, xcoord + width):
                for j in range(ycoord, ycoord + height):
                    if squares[(i, j)] != 1:
                        return True
            return False

        if not overlap():
            return num


print(find_fabric(lines, squares))
