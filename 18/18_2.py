from common import read_data, iterate, value

size, tiles = read_data()

last_sequence = []
sequence = []

for i in range(1, 1000000000 + 1):

    current = value(size, tiles)
    if current not in sequence:
        sequence.append(current)
    elif sequence == last_sequence:
        break
    else:
        last_sequence = sequence[sequence.index(current):]
        sequence = [current]

    tiles = iterate(tiles)

for j in range(len(sequence)):
    if (1000000000 - (i + j)) % len(sequence) == 0:
        print(sequence[j + 1])
        break
