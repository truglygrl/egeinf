def f(a, b):
    if (a> b) or (a == 10):
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a*2, b) + f(a+1, b)
print(f(2, 16))