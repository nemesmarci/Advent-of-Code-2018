import re


def read_data():
    pattern = re.compile(
            r"^([0-9]+) players; last marble is worth ([0-9]+) points$")
    with open('input.txt') as data:
        line = data.read()
        players, last_points = pattern.match(line).groups()
        return int(players), int(last_points)


class Marble:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None


def play(players, last_points):
    current = Marble(0)
    current.next = current.prev = current
    points = [0 for p in range(int(players))]
    current_player = 0

    for i in range(1, int(last_points) + 1):
        if i % 23 != 0:
            new = Marble(i)
            current = current.next
            old_next = current.next
            current.next = new
            new.next = old_next
            new.prev = current
            old_next.prev = new
            current = new
        else:
            points[current_player] += i
            for j in range(7):
                current = current.prev
            current_next = current.next
            current_prev = current.prev
            current.next = current.prev = None
            current_prev.next = current_next
            current_next.prev = current_prev
            points[current_player] += current.num
            current = current_next
        current_player = (current_player + 1) % int(players)
    return max(points)
