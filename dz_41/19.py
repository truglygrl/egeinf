def f(a, b, c):
    if a > b:
        return 0
    if c > 9:
        return False
    if a == b:
        return 1
    if c == 9:
        return True
    return f(a + 3, b, c + 1) + f(a*2, b, c + 1)
k = 0
for i in range(1000):
    if f(4, i, 0):
        k += 1
print(k)