from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a + b >= 91:
        return 0
    if a<b:
        t = [f(a+2, b), f(a+5, b), f(a+15, b)]
        n = [i for i in t if i <= 0]
        if n:
            return -max(n)+1#win
        else:
            return -max(t)
    else:
        t = [f(a, b+2), f(a, b+5), f(a, b+15)]
        n = [i for i in t if i <= 0]
        if n:
            return -max(n) + 1  # win
        else:
            return -max(t)

for i in range(1, 100):
    if f(15, i) == -3:
        print(i, f(15, i))
