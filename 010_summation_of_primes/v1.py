from math import floor, sqrt

number_of_primes = 10_001 

primes = []

def is_prime(n):
    for prime in primes:
        if prime > floor(sqrt(n)):
            return True
        if n % prime == 0:
            return False
    return True

for n in range(2, 2_000_000):
    if is_prime(n):
        primes.append(n)

print(sum(primes))
