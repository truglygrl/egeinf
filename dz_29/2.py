def f(n):
    if n <= 2:
        return n
    return g(n//2) + f(n-2)
def g(n):
    if n <= 2:
        return n-1
    return f(n-2) - g(n//5) + 11

for i in range(10000):
    if g(i) == 7693:
        print(i)