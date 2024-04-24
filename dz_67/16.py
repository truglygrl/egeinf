def f(a, b):
    if (a > b) or (a == 21):
        return 0
    if a == b:
        return 1
    return f(a+2, b) + f(a*3, b) + f(a*2-1, b)

print(f(5, 17)*f(17, 37))