def f(n, m):
    if n <= 2 or m <= 5:
        return 2
    return f(n-3, m) + f(n, m-2)*m + f(n-5, m-5)*n
print(f(11, 16))