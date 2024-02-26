from functools import lru_cache
@lru_cache(None)

def f(a, b, c):
    if (a+b) >= 98:
        return 0
    if c > 10:
        return 1000000
    n = [f(a+2, b, c+1), f(a+3, b, c+1), f(a+b, b, c+1), f(a, b+2, c+1), f(a, b+3, c+1), f(a, b+a,c+1)]

    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)

for i in range(1, 79):
    if f(10, i, 0) == -1:
        print(i)