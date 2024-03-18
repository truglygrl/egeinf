def f(a, b, c):
    if a <= c <= b:
        return True
    return False

l = []
for a1 in range(1, 100):
    for a2 in range(a1+1, 100+2):
        fl = 0
        for i in range(1, 1000):
            if ((f(a1, a2, i) <= f(5, 17, i)) or f(13, 23, i)) == False:
                fl = 1
                break
        if fl == 0:
            l.append(a2-a1)

print(max(l))