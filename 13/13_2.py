import sys

turns = {'<':'v^', '>':'^v', '^': '<>', 'v':'><'}
next_turns = {'left': 'straight', 'straight': 'right', 'right': 'left'}

class Cart:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x, self.y = x, y
        self.next_turn = 'left'

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def tick(self):
        if self.direction in '<>':
            self.x += 1 if self.direction == '>' else -1
        else:
            self.y += 1 if self.direction == 'v' else -1

        for other in (cart for cart in carts if cart != self):
            if (other.x, other.y) == (self.x, self.y):
                return other

        track = mine[(self.x, self.y)]

        if track == '/' and self.direction in '<>' or \
           track == '\\' and self.direction in '^v' or \
           track == '+' and self.next_turn == 'left':
               self.direction = turns[self.direction][0]

        elif track == '/' and self.direction in '^v' or \
           track == '\\' and self.direction in '<>' or \
           track == '+' and self.next_turn == 'right':
               self.direction = turns[self.direction][1]

        if track == '+':
            self.next_turn = next_turns[self.next_turn]

        return False

mine = dict()
carts = list()

lines = sys.stdin.readlines()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ' ':
            continue
        if c in '<>^v':
            mine[(x, y)] = '-' if c in '<>' else '|'
            carts.append(Cart(c, x, y))
        else:
            mine[(x, y)] = c

while len(carts) > 1:
    sorted_carts = sorted(carts)
    for cart in sorted_carts:
        if cart not in carts:
            continue
        collided_with = cart.tick()
        if collided_with:
            carts.remove(cart)
            carts.remove(collided_with)

print("{},{}".format(carts[0].x, carts[0].y))