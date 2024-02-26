def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-3, b) + f(a - 5, b) + f(a // 3, b)

print(f(68, 35)*f(35, 14)*f(14, 4))