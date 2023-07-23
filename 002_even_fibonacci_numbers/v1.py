n = 4_000_000

s = 0

a, b =  1, 2

while a < n:
    if a % 2 == 0:
        s += a
    a, b = b, a+b

print(s)
