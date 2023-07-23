from functools import cache
from enum import Enum

with open("matrix") as f:
    # FYI, (0,0) is top left
    data = [[int(n) for n in row.strip().split(",")] for row in f.read().strip().split("\n")]

class CameFrom(Enum):
    ABOVE = 1
    BELOW = 2 
    SIDE = 3

size = len(data)

@cache
def min_path(x, y, came_from):
    cur = data[y][x]
    possible = []

    # If we reach the end, we can't do better
    if x == size-1:
        return cur

    # We can always go right
    possible.append(min_path(x+1, y, CameFrom.SIDE))
   
    # See if we can go up. Don't backtrack
    if y != 0 and came_from is not CameFrom.ABOVE:
        possible.append(min_path(x, y-1, CameFrom.BELOW))    
    # And go down?
    if y != size-1 and came_from is not CameFrom.BELOW:
        possible.append(min_path(x, y+1, CameFrom.ABOVE))

    return cur + min(possible)



print(min((min_path(0, i, CameFrom.SIDE) for i in range(size-1))))
