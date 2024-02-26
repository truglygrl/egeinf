def f(a):
    s = ''
    while a>0:
        s = str(a % 3) + s
        a //= 3
    return s
n = 27**400 - 9**300 - 3**100 + 3**50
print(f(n).count('0'))
print(f(n))