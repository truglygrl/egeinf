def f(n):
    if n <= 1:
        return 11
    return f(n-5) + n*g(n // 4)
def g(n):
    if n <= 1:
        return 11
    return f(n // 3) + g(n-1)

print(g(21))