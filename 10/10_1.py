from common import read_data, display, run

points, velocities = read_data()
display(run(points, velocities)[0])
