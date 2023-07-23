# Could do this in reverse in some way, but this will run

def is_palindrome(n):
    return str(n) == str(n)[::-1]

best = 0
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            best = max(best, i*j)

print(best)
