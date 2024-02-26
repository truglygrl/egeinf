from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if (a + b) >= 259:
        return 0
    n = [f(a+1, b), f(a*2, b), f(a, b+1), f(a, b*2)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)
for i in range(1, 242):
    if f(17, i) == 1:
        print(i, f(17, i))