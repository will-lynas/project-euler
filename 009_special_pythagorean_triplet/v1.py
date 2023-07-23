from math import sqrt

def is_square(n):
    return int(sqrt(n)) == sqrt(n)

for b in range(1000):
    for a in range(1,b):
        c_squared = a**2 + b**2
        if is_square(c_squared):
            c = int(sqrt(c_squared))
            if a + b + c == 1000:
                print(a*b*c)
                break
