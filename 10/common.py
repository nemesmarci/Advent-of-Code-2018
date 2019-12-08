import re
import numpy as np
import matplotlib.pyplot as plt


def read_data():
    points = []
    velocities = []
    regex = re.compile(
        r"^position=<\s?([-0-9]+),\s{1,2}([-0-9]+)> "
        r"velocity=<\s?([-0-9]+),\s{1,2}([-0-9]+)>$")

    with open('input.txt') as data:
        for line in data.readlines():
            x, y, vx, vy = regex.match(line).groups()
            points.append((int(x), int(y)))
            velocities.append((int(vx), int(vy)))
    return points, velocities


def get_boundaries(points):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    return min_x, max_x, min_y, max_y


def display(points):
    min_x, max_x, min_y, max_y = get_boundaries(points)
    pixels = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=int)
    for p in points:
        pixels[p[1] - min_y][p[0] - min_x] = 1
    plt.axis('off')
    plt.imshow(pixels, cmap='Greys')
    plt.show()


def run(points, velocities):
    prev = points
    time_passed = 1
    min_area = None

    while(True):
        new = []
        for i, point in enumerate(prev):
            x, y = point[0] + velocities[i][0], point[1] + velocities[i][1]
            new.append((x, y))
        min_x, max_x, min_y, max_y = get_boundaries(new)
        area = (max_y - min_y + 1) * (max_x - min_x + 1)
        if min_area is None or area <= min_area:
            min_area = area
        elif area > min_area:
            return prev, time_passed - 1
        prev = new
        time_passed += 1
