from common import Rooms

r = Rooms()
print(max(r.distances[room] for room in r.rooms))
