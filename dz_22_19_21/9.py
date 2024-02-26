from functools import lru_cache
@lru_cache(None)

def f(a, b, c):
    if (a+b) >= 210:
        return 0
    if c > 10:
        return 100000
    n = [f(a+5, b, c + 1), f(a, b + 5, c + 1), f(a*a, b, c + 1), f(a, b*b, c+1)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)
for i in range(1, 205):
    if f(3, i, 0) == -2:
        print(i)