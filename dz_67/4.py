def f(n):
    if n <= 9:
        return n
    if n <= 30:
        return f(n-7) + 2*n**2
    return f(n-9)*n + 15
print(f(31))