import re
import sys

import numpy as np
import matplotlib.pyplot as plt

regex = re.compile(r"^position=<\s?([-0-9]+),\s{1,2}([-0-9]+)> velocity=<\s?([-0-9]+),\s{1,2}([-0-9]+)>$")

lines = sys.stdin.readlines()

points = []
velocities = []

for line in lines:
    x, y, vx, vy = regex.match(line).groups()
    points.append((int(x), int(y)))
    velocities.append((int(vx), int(vy)))

def get_boundaries(points):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    return min_x, max_x, min_y, max_y

def display(secs):
    pixels = np.zeros((100, 100), dtype=int)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)
    fig.suptitle(secs)
    for p in points:
        pixels[p[1] - min_y][p[0] - min_x] = 1
    plt.imshow(pixels, cmap='Greys', interpolation='nearest')
    plt.show()

found_small_range = False
time_passed = 1

while(True):
    for pi, p in enumerate(points):
        x, y = p[0] + velocities[pi][0], p[1] + velocities[pi][1]
        points[pi] = (x, y)
    min_x, max_x, min_y, max_y = get_boundaries(points)
    if max_x - min_x < 100 and max_y - min_y < 100:
        if not found_small_range:
            found_small_range = True
            found_at = time_passed
        # check small images to find the message
        # display(time_passed)
        if time_passed == found_at + 4:
            display(time_passed)
            break
    time_passed += 1
print(time_passed)