"""1.
Прибавить 1

2.
Прибавить 2

3.
Умножить
на 2

4.
Умножить
на 4"""
def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    if c < 3:
        return f(a+1, b, c) + f(a+2, b, c) + f(a*2, b, c+1) + f(a*4, b, c+1)

print(f(1, 13, 0))