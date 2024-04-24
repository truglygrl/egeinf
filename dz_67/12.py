def f(n):
    if n < 4:
        return 2 ** n
    if (n > 3) and (n % 2 == 0):
        return 2*f(n-1) + f(n // 2)
    return f(n-2) + 2*n + f(n // 3) + 1


print(f(128))