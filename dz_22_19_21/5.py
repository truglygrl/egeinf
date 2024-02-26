from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if (a+b) >= 140:
        return 0
    n = [f(a+5, b), f(a, b+5), f(a*2, b), f(a, b*2)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)
s = 0
for i in range(1, 100):
    if f(i, 25) == -1:
        s += i
print(s)