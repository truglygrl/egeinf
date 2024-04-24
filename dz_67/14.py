def f(n):
    if n == 0:
        return 2
    if n == 1:
        return 5
    return f(n-1) * f(n-2)
def g(n):
    if n < 5:
        return 0
    if n == 5:
        return 1
    return g(n - 1) + f(n - 2)


print(f(5) + g(8))