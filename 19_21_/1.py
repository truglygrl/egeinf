from functools import lru_cache
@lru_cache(None)

def f(a):
    if a >= 59:
        return 0
    n = [f(a+2), f(a+7), f(a*3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)

for i in range(1, 100):
    if f(i) == -2:
        print(i, f(i))