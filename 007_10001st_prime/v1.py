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

n = 2
while len(primes) < number_of_primes:
    if is_prime(n):
        primes.append(n)
    n += 1

print(primes[-1])
