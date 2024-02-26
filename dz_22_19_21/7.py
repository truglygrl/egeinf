from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if (a+b) >= 260:
        return 0
    n = [f(a+10, b), f(a*2, b), f(a*4, b), f(a, b+10), f(a, b*2), f(a, b*4)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)
s = 0
for i in range(1, 189):
    if f(44, i) == 3:
        s += i
        print(i)
print(s)