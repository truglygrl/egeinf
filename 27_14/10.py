def f(a, b, c):
    if a <= c <= b:
        return True
    return False
l = []
for a1 in range(1, 500-1):
    for a2 in range(a1+1, 500):
        fl = 0
        for i in range(700):
            if (f(10, 32, i) or (not f(a1, a2, i)) <= (not f(18, 45, i))) == False:
                fl = 1
                break
        if fl == 0:
            l.append(a2-a1)
print(min(l))