from functools import lru_cache
@lru_cache(None)

def f(a):
    if a >= 180:
        return 0
    n = []

    if (a+3) % 2 != 0:
        n.append(f(a+3))
    if (a+4) % 2 != 0:
        n.append(f(a+4))
    if (a*4) % 2 != 0:
        n.append(f(a*4))
    if n:
        t = [i for i in n if i <= 0]
        if t:
            return -max(t) + 1
        else:
            return -max(n)


for i in range(1, 200, 2):
    if f(i) == -2:
        print(f(i), i)