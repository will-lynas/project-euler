from itertools import permutations

digits = "0123456789"
p = permutations(digits)

print("".join(next(x for i,x in enumerate(p) if i==1_000_000-1)))
