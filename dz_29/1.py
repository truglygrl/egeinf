def f(n):
    if (n == 1) or (n == 2) or (n == 3):
        return 1
    return f(n-3) + f(n-1)
print(f(12))