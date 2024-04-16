from functools import lru_cache
@lru_cache(None)

def f(a, b, m):
    if (a + b) >= 95:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+2, b, m-1), f(a*3, b, m-1), f(a, b+2, m-1), f(a, b*3, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)

for s in range(1, 89):
    if not f(6, s, 2) and f(6, s, 4):
        print(s)