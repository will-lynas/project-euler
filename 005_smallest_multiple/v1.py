from functools import reduce

n = 20

def gcd(a,b):
    assert a >= b
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    assert a >= b
    return a * b // gcd(a,b)

print(reduce(lcm, reversed(range(1,n+1)), 20))
