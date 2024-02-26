from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 111:
        return 0
    t = [f(a+5, b), f(a*4, b), f(a, b + 5), f(a, b*4)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)
for i in range(1, 98):
    if f(12, i) == -2:
        print(i, f(12, i))