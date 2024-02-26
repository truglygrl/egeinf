from functools import lru_cache
@lru_cache(None)

def f(n):
    if n == 0:
        return 0
    if (n > 0) and (n % 2 == 0):
        return f(n//10) + n % 10
    return f(n // 10)
c = 0
for k in range(10**9, 2*10**9+1):
    if f(k) == 0:
        c += 1
print(c)