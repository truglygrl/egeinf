from functools import lru_cache
@lru_cache(None)

def f(a, b, m):
    if (a+b) >= 73:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

for s in range(1, 62):
    if not f(11, s, 2) and f(11, s, 4):
        print(s)