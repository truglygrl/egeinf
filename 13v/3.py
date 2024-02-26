from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if a + b >= 109:
        return 0
    t = [f(a+7, b), f(a*3, b), f(a, b+7), f(a, b*3)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)

for i in range(1, 120):
    if f(12, i) == -2:
        print(i, f(12, i))