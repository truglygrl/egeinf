"""1.
Прибавить1

2.
Прибавить4

3.
Прибавить6

4.
Умножить
на3"""
def f(a, b, c):
    if a > b:
        return 0
    if a == b:
        return 1
    if c >= 1:
        return f(a + 1, b, c) + f(a + 4, b, c) + f(a + 6, b, c)
    return f(a+1, b, c) + f(a+4, b, c) + f(a+6, b, c) + f(a*3, b, c+1)




print(f(3, 26, 0))