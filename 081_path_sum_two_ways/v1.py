from functools import cache

with open("matrix") as f:
    data = [[int(n) for n in row.strip().split(",")] for row in f.read().strip().split("\n")]

@cache
def min_path(x, y):
    if x == y == 79:
        return data[x][y]
    if x == 79:
        return data[x][y] + min_path(x, y+1)
    if y == 79:
        return data[x][y] + min_path(x+1, y)
    return data[x][y] + min(min_path(x+1, y), min_path(x, y+1))

print(min_path(0,0))
