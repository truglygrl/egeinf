def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)*n



print(f(10) - f(5))