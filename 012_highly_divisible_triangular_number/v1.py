from math import floor, sqrt

def get_divisors(n):
    divisors = set()
    for i in range(1,floor(sqrt(n))):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors


number_divisors = 500

triangle = 0
for i in range(9999999):
    triangle += i
    if len(get_divisors(triangle)) > number_divisors:
        print(triangle)
        break
