from functools import *
@lru_cache(None)






def f(a, b):
    if (a + b) >= 77:
        return 0
    t = [f(a+2, b), f(a*2, b), f(a, b+2), f(a, b*2)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    return -max(t)


for i in range(1, 70):
    if f(7, i) == 2:
        print(i, f(7, i))