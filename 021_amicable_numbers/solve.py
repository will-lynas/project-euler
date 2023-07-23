def proper_divisors(n):
    out = []
    for i in range(1,n):
        if n % i == 0:
            out.append(i)
    return out

def d(n):
    return sum(proper_divisors(n))

amicable_numbers = set()
for a in range(1, 10_000):
    d_a = d(a)
    if d_a != a and d(d_a) == a:
        amicable_numbers.add(a)

print(sum(amicable_numbers))