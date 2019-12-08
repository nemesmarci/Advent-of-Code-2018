TURNS = {'<': 'v^', '>': '^v', '^':  '<>', 'v': '><'}
NEXT_TURNS = {'left': 'straight', 'straight': 'right', 'right': 'left'}


def read_data():
    mine = {}
    carts = []

    with open('input.txt') as data:
        lines = data.readlines()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ' ':
                continue
            if c in '<>^v':
                mine[(x, y)] = '-' if c in '<>' else '|'
                carts.append(Cart(c, x, y, carts, mine))
            else:
                mine[(x, y)] = c

    return mine, carts


class Cart:
    def __init__(self, direction, x, y, carts, mine):
        self.direction = direction
        self.x, self.y = x, y
        self.next_turn = 'left'
        self.carts = carts
        self.mine = mine

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def tick(self):
        if self.direction in '<>':
            self.x += 1 if self.direction == '>' else -1
        else:
            self.y += 1 if self.direction == 'v' else -1

        for other in (cart for cart in self.carts if cart != self):
            if (other.x, other.y) == (self.x, self.y):
                return other

        track = self.mine[(self.x, self.y)]

        if track == '/' and self.direction in '<>' or \
            track == '\\' and self.direction in '^v' or \
                track == '+' and self.next_turn == 'left':
                    self.direction = TURNS[self.direction][0]

        elif track == '/' and self.direction in '^v' or \
            track == '\\' and self.direction in '<>' or \
                track == '+' and self.next_turn == 'right':
                    self.direction = TURNS[self.direction][1]

        if track == '+':
            self.next_turn = NEXT_TURNS[self.next_turn]

        return False


def run(mine, carts, return_early=False):
    while len(carts) > 1:
        sorted_carts = sorted(carts)
        for cart in sorted_carts:
            if cart not in carts:
                continue
            collided_with = cart.tick()
            if collided_with:
                if return_early:
                    return cart.x, cart.y
                carts.remove(cart)
                carts.remove(collided_with)
    return carts[0].x, carts[0].y
