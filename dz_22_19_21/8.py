from functools import lru_cache
@lru_cache(None)
def f(a, b, c):
    if (a+b) >= 190:
        return 0
    if c > 10:
        return 100000000000
    if a > b: #За один ход игрок может добавить в меньшую из куч количество камней в другой куче или
# в меньшей из куч возвести количество камней в квадрат.
        n = [f(a, b+a, c+1), f(a, b*b, c + 1)]
    else:
        n = [f(a+b, b, c + 1), f(a*a, b, c + 1)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)

#первой куче было 5 камня

for i in range(1, 89):
    if f(5, i, 0) == -2:
        print(i)
