from functools import lru_cache
@lru_cache(None)
def f(a):
    if a >= 46:
        return 0
    n = [f(a+3), f(a*2)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)
for i in range(1, 49):
    if f(i) == -2:
        print(f(i), i)