from functools import lru_cache
@lru_cache(None)

def f(a, b, m):
    if a > b + 1:
        return 0
    if a == b:
        return 1
    if m == 1:
        return f(a*2, b, 2) + f(a*3, b, 3)
    else:
        return f(a-1, b, 1) + f(a*2, b, 2) + f(a*3, b, 3)

print(f(3, 20, 0))