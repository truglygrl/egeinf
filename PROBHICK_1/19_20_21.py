import re
from functools import lru_cache
@lru_cache(None)
def f(a):
    if a >= 96:
        return 0

    if a % 2 == 0:
        t = [f(a + 1), f(a + (a // 2))]
    if a % 3 == 0:
        t = [f(a + 1), f(a + (a // 3))]
    t = [f(a + 1), f(a*2)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)


for i in range(1, 96):
    if f(i) == -2:
        print(f(i), i)
