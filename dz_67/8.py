def f(n):
    if n == 1:
        return 2
    return n**2 + f(n-1)

print(f(7))