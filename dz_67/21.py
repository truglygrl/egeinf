def f(a, b):
    if (a > b) or (a == 10) or (a == 20):
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a + 2, b) + f(a*3, b)

print(f(3, 15)*f(15, 30))