def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-5, b) + f(a-7, b)

print(f(101, 37)*f(37, 20))