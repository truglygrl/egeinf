from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 68:
        return 0
    t = [f(a+2, b), f(a*3, b), f(a, b+2), f(a, b*3)]#2 el for a and b
    n = [i for i in t if i <= 0]#negative
    if n:
        return -max(n) + 1#win
    else:
        return -max(t)#lose

for i in range(1, 60):
    print(8, i, f(8, i))