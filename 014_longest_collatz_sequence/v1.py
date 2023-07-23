from functools import cache
from timeit import timeit

def brute_force():

    best_start = None
    best_len = 1

    for start in range(1, 1_000_000):
        seq = [start]
        while (last := seq[-1]) != 1:
            if last % 2 == 0:
                seq.append(last//2)
            else:
                seq.append(last*3 + 1)

        if (seq_len := len(seq)) > best_len:
            best_start = start
            best_len = seq_len

    return best_start


def manual_cache():

    cache = {1: 1}

    for start in range(2, 1_000_000):
        seq = [start]
        while True:
            last = seq[-1]

            if last in cache:
                cache[start] = cache[last] + len(seq) - 1
                break

            if last % 2 == 0:
                seq.append(last/2)
            else:
                seq.append(last*3 + 1)

    return max(cache, key=lambda x: cache[x])


def recursive_cache():

    @cache
    def inner(n):
        if n == 1:
            return 1
        if n%2 == 0:
            return 1 + inner(n//2)
        else:
            return 1 + inner(n*3+1)

    best_start = None
    best_len = 1

    for start in range(1, 1_000_000):
        if (result := inner(start)) > best_len:
            best_start = start
            best_len = result

    return best_start

"""
def time_function(func):
    func = func.__name__
    print(f"{func}: {timeit(func+'()', 'from __main__ import '+func, number=1)}")

time_function(brute_force)
time_function(manual_cache)
time_function(recursive_cache)
"""

print(recursive_cache())
