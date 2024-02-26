n = 36**15 + 6**38 - 11
def f(a):
    s = ''
    while a > 0:
        s = str(a % 6) + s
        a //= 6
    return s
print(f(n).count('0'))