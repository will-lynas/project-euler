from functools import cache

n = 20

@cache
def how_many(x, y):

    if x == y == 0:
        return 1

    if x == 0:
        return how_many(x, y-1)
    if y == 0:
        return how_many(x-1, y)

    return how_many(x, y-1) + how_many(x-1, y)

print(how_many(n,n))
