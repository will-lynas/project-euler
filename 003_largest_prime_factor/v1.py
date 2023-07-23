n = 600851475143

def largest_prime_factor(n):

    for i in range(2,n):
        if n % i == 0:
            print(f"{n}/{i}={n//i}")
            return largest_prime_factor(n//i)
    return n

print(largest_prime_factor(n))
