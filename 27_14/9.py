def f(a, b, c):
    if a <= c <= b:
        return True
    return False
l = []
for a1 in range(1, 500-1):
    for a2 in range(a1+1, 500):
        fl = 0
        for i in range(1, 1000):
            if ((f(a1, a2, i) <= f(15, 39, i)) or f(44, 57, i)) == False:
                fl = 1
                break
        if fl == 0:
            l.append(a2-a1)
print(l)