def f(n):
    if n < 2:
        return 3*n + n**2
    if n % 2 == 0:
        return f(n-2) + f(n // 2)
    return f(n-2) + f(n-3)

print(f(77))