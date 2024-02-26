from functools import lru_cache
@lru_cache(None)
def f(a):
    if a >= 45:
        return 0
    t = [f(a+1), f(a+3)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n)+1
    else:
        return -max(t)
for i in range(1, 50):
    if f(i) == -2:
        print(i, f(i))