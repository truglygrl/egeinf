def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 4
    return f(n-1)*(n-1) + f(n-2)*(n-2)
print(f(5))