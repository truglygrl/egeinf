def f(a, b):
    if (a > b) or (a == 14):
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b) + f(a + 3, b)

print(f(1, 9)*f(9, 20))