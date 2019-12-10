from common import Rooms

r = Rooms()
print(sum([1 for room in r.rooms if r.distances[room] >= 1000]))
