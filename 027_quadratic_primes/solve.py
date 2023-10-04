#!/usr/bin/env python3
from math import sqrt, ceil
from dataclasses import dataclass

def is_prime(n):
    if n<0:
        return False
    for i in range(2, ceil(sqrt(n))):
        if n%i == 0:
            return False
    return True

@dataclass
class Best:
    a: int
    b: int


best_consecutive = 0
best = Best(0,0)

for a in range(-1000+1,1000):
    for b in range(-1000, 1000+1):
        n = 0
        while True:
#            print(f"{a=} {b=} {n=}")
            if not is_prime(n**2 + a*n + b):
                break
            n += 1
        if n>best_consecutive:
            best_consecutive = n
            best.a = a
            best.b = b

print(f"{best.a=} {best.b=} {best_consecutive=}")
print(best.a*best.b)


