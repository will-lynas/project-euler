from math import floor, sqrt, ceil

def get_factors(n):
    out = set()
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            out.add(i)
            out.add(n//i)
    out.add(1) # can't include in loop, else n gets included too
    return out

def is_abundant(n):
    return sum(get_factors(n)) > n

upper = 28123
abundants = set(filter(is_abundant, range(1, upper)))

out = []
for n in range(upper):
    found = False
    for m in abundants:
        if n-m in abundants:
            found = True
            break
    if not found:
        out.append(n)

print(sum(out))
